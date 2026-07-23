from __future__ import annotations

import json
import hashlib
import os
import subprocess
import sys
from pathlib import Path
from unittest import mock

import pytest

from inference_bench.deployment import DISAGGREGATED_PREFILL_DECODE
from inference_bench.providers.base import Provider, _git_blob_sha1_file


class _TestProvider(Provider):
    name = "test"
    repo_url = "https://github.com/example/provider.git"
    runtime_import_names = ("provider_pkg",)

    def build(self) -> None:
        pass

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        return []

    @property
    def venv_python(self) -> str:
        return sys.executable


def _git(provider: _TestProvider, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=provider.repo_dir,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _init_scored_provider(tmp_path: Path) -> tuple[_TestProvider, Path]:
    provider = _TestProvider(build_dir=str(tmp_path))
    provider.repo_dir.mkdir(parents=True)
    _git(provider, "init", "-q", "-b", "main")
    _git(provider, "config", "user.email", "inference-bench@example.invalid")
    _git(provider, "config", "user.name", "inference-bench")
    package = provider.repo_dir / "provider_pkg"
    package.mkdir()
    package_file = package / "__init__.py"
    package_file.write_text("VALUE = 1\n")
    (provider.repo_dir / ".gitignore").write_text("*.pyc\n*.so\nignored.py\n")
    _git(provider, "add", ".gitignore", "provider_pkg/__init__.py")
    _git(provider, "commit", "-qm", "initial")
    _git(provider, "remote", "add", "origin", provider.repo_url)
    _git(provider, "update-ref", "refs/remotes/origin/main", "HEAD")
    provider.configure_deployment(
        deployment_mode=DISAGGREGATED_PREFILL_DECODE,
        tensor_parallel_size=1,
        prefill_tensor_parallel_size=1,
        decode_tensor_parallel_size=1,
        model_revision="a" * 40,
    )
    provider._fresh_scored_clone = True
    provider._fresh_scored_clone_commit = _git(provider, "rev-parse", "HEAD")
    return provider, package_file


def test_provider_commit_hash_marks_dirty_worktree(tmp_path) -> None:
    provider = _TestProvider(build_dir=str(tmp_path))
    provider.repo_dir.mkdir(parents=True)
    subprocess.run(["git", "init", "-q"], cwd=provider.repo_dir, check=True)
    subprocess.run(
        ["git", "config", "user.email", "inference-bench@example.invalid"],
        cwd=provider.repo_dir,
        check=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "inference-bench"],
        cwd=provider.repo_dir,
        check=True,
    )
    tracked = provider.repo_dir / "tracked.txt"
    tracked.write_text("clean\n")
    subprocess.run(["git", "add", "tracked.txt"], cwd=provider.repo_dir, check=True)
    subprocess.run(["git", "commit", "-qm", "initial"], cwd=provider.repo_dir, check=True)

    clean_hash = provider.get_commit_hash()
    tracked.write_text("dirty\n")

    assert len(clean_hash) == 40
    assert provider.get_commit_hash() == f"{clean_hash}-dirty"


def test_scored_source_manifest_records_build_patch_and_untracked_files(
    tmp_path: Path,
) -> None:
    provider, package_file = _init_scored_provider(tmp_path)

    provider.prepare_source_provenance(skip_build=False)
    package_file.write_text("VALUE = 2\n")
    generated = provider.repo_dir / "generated.py"
    generated.write_text("BUILD_VALUE = 3\n")
    native_artifact = provider.repo_dir / "kernel.so"
    native_artifact.write_bytes(b"native-build-output")
    serialized_artifact = (
        provider.repo_dir
        / ".inference-bench-artifacts"
        / "deepseek-v4"
        / "tilelang"
        / "params.pkl"
    )
    serialized_artifact.parent.mkdir(parents=True)
    serialized_artifact.write_bytes(b"serialized-kernel-parameters")
    observation = provider.finalize_source_provenance()

    manifest_path = provider._source_provenance_manifest_path()
    manifest = json.loads(manifest_path.read_text())
    assert observation["source_provenance_check"] == "passed"
    assert observation["runtime_import_provenance_check"] == "passed"
    assert observation["source_dirty"] is True
    assert observation["source_tracked_diff_bytes"] > 0
    assert "generated.py" in observation["source_untracked_files"]
    assert observation["source_ignored_runtime_artifacts"]["kernel.so"][
        "sha256"
    ] == hashlib.sha256(native_artifact.read_bytes()).hexdigest()
    assert manifest["post_build_state"]["commit"] == _git(provider, "rev-parse", "HEAD")
    assert manifest["runtime_import_state"]["modules"]["provider_pkg"]
    assert provider._source_provenance_patch_path().read_text().startswith("diff --git")
    assert provider.verify_source_provenance()["source_provenance_check"] == "passed"

    original_manifest = manifest_path.read_text()
    manifest_path.write_text("{}\n")
    with pytest.raises(RuntimeError, match="manifest changed"):
        provider.verify_source_provenance()
    manifest_path.write_text(original_manifest)

    original_parameters = serialized_artifact.read_bytes()
    serialized_artifact.write_bytes(b"mutated-kernel-parameters")
    with pytest.raises(RuntimeError, match="source changed"):
        provider.verify_source_provenance()
    serialized_artifact.write_bytes(original_parameters)

    generated.write_text("changed after build\n")
    with pytest.raises(RuntimeError, match="changed after the scored build"):
        provider.verify_source_provenance()


@pytest.mark.parametrize("dirty_kind", ["tracked", "untracked"])
def test_scored_source_rejects_dirty_prebuild_checkout(
    tmp_path: Path,
    dirty_kind: str,
) -> None:
    provider, package_file = _init_scored_provider(tmp_path)
    if dirty_kind == "tracked":
        package_file.write_text("VALUE = 9\n")
    else:
        (provider.repo_dir / "untracked.txt").write_text("unexpected\n")

    with pytest.raises(RuntimeError, match="must start from a clean origin/main"):
        provider.prepare_source_provenance(skip_build=False)


def test_scored_source_rejects_wrong_remote_and_wrong_head(tmp_path: Path) -> None:
    wrong_remote, _ = _init_scored_provider(tmp_path / "remote")
    _git(wrong_remote, "remote", "set-url", "origin", "https://example.com/wrong.git")
    with pytest.raises(RuntimeError, match="remote does not match"):
        wrong_remote.prepare_source_provenance(skip_build=False)

    wrong_head, package_file = _init_scored_provider(tmp_path / "head")
    package_file.write_text("VALUE = 2\n")
    _git(wrong_head, "add", "provider_pkg/__init__.py")
    _git(wrong_head, "commit", "-qm", "advance local head")
    with pytest.raises(RuntimeError, match="exactly origin/main"):
        wrong_head.prepare_source_provenance(skip_build=False)


def test_scored_disaggregated_run_rejects_skip_build(
    tmp_path: Path,
) -> None:
    provider, _ = _init_scored_provider(tmp_path)
    with pytest.raises(RuntimeError, match="--skip-build is prohibited"):
        provider.prepare_source_provenance(skip_build=True)


def test_scored_source_rejects_preexisting_ignored_runtime_artifact(
    tmp_path: Path,
) -> None:
    provider, _ = _init_scored_provider(tmp_path)
    (provider.repo_dir / "kernel.so").write_bytes(b"stale-native-code")

    with pytest.raises(RuntimeError, match="must not reuse ignored Python or native"):
        provider.prepare_source_provenance(skip_build=False)


def test_scored_source_rejects_preexisting_bytecode_and_venv(tmp_path: Path) -> None:
    bytecode_provider, _ = _init_scored_provider(tmp_path / "bytecode")
    (bytecode_provider.repo_dir / "forged.pyc").write_bytes(b"forged-bytecode")
    with pytest.raises(RuntimeError, match="must not reuse ignored Python or native"):
        bytecode_provider.prepare_source_provenance(skip_build=False)

    venv_provider, _ = _init_scored_provider(tmp_path / "venv")
    venv_provider.venv_dir.mkdir(parents=True)
    with pytest.raises(RuntimeError, match="require a fresh provider environment"):
        venv_provider.prepare_source_provenance(skip_build=False)


def test_scored_runtime_imports_ignore_python_path_and_stay_in_checkout(
    tmp_path: Path,
) -> None:
    provider, _ = _init_scored_provider(tmp_path)
    shadow = tmp_path / "shadow" / "provider_pkg"
    shadow.mkdir(parents=True)
    (shadow / "__init__.py").write_text("VALUE = 'shadow'\n")

    with mock.patch.dict(
        os.environ,
        {
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": "url.file:///tmp/shadow.insteadOf",
            "GIT_CONFIG_VALUE_0": "https://github.com/",
            "LD_AUDIT": "/tmp/audit.so",
            "LD_LIBRARY_PATH": "/tmp/shadow-libs",
            "LD_PRELOAD": "/tmp/preload.so",
            "PYTHONHOME": "/tmp/not-a-python-home",
            "PYTHONPATH": str(shadow.parent),
            "PYTHONUSERBASE": str(shadow.parent),
        },
        clear=False,
    ):
        env = provider._server_env()
        state = provider._runtime_import_state()

    assert "PYTHONHOME" not in env
    assert "PYTHONPATH" not in env
    assert "PYTHONUSERBASE" not in env
    assert env["PYTHONNOUSERSITE"] == "1"
    assert env["PYTHONDONTWRITEBYTECODE"] == "1"
    assert "LD_AUDIT" not in env
    assert "LD_LIBRARY_PATH" not in env
    assert "LD_PRELOAD" not in env
    resolved = Path(state["modules"]["provider_pkg"][0]).resolve()
    assert resolved.is_relative_to(provider.repo_dir.resolve())

    git_env = provider._scored_git_env()
    assert "GIT_CONFIG_COUNT" not in git_env
    assert git_env["GIT_CONFIG_GLOBAL"] == os.devnull
    assert git_env["GIT_CONFIG_NOSYSTEM"] == "1"
    assert git_env["GIT_ALLOW_PROTOCOL"] == "https"


def test_scored_runtime_rejects_python_and_model_overrides(tmp_path: Path) -> None:
    provider, _ = _init_scored_provider(tmp_path)
    with (
        mock.patch.dict(
            os.environ,
            {
                "INFERENCE_BENCH_TEST_PYTHON": sys.executable,
                "INFERENCE_BENCH_SERVER_MODEL": "/tmp/alternate-model",
            },
            clear=False,
        ),
        pytest.raises(ValueError, match="Python overrides are prohibited"),
    ):
        _ = provider.server_python
    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_SERVER_MODEL": "/tmp/alternate-model"},
            clear=False,
        ),
        pytest.raises(ValueError, match="SERVER_MODEL is prohibited"),
    ):
        provider._server_model("model-id")


def test_model_provenance_requires_complete_pinned_snapshot(tmp_path: Path) -> None:
    provider, _ = _init_scored_provider(tmp_path)
    revision = "a" * 40
    snapshot = tmp_path / revision
    snapshot.mkdir()
    (snapshot / "config.json").write_text('{"model_type": "test"}\n')
    (snapshot / "tokenizer.json").write_text('{"version": "1.0"}\n')
    (snapshot / "model.safetensors.index.json").write_text(
        json.dumps(
            {
                "weight_map": {
                    "layer.0": "model-00001-of-00002.safetensors",
                    "layer.1": "model-00002-of-00002.safetensors",
                }
            }
        )
    )
    first_weight = snapshot / "model-00001-of-00002.safetensors"
    second_weight = snapshot / "model-00002-of-00002.safetensors"
    first_weight.write_bytes(b"first")
    second_weight.write_bytes(b"second")
    provider._resolved_server_model = str(snapshot)
    files = {
        "config.json": snapshot / "config.json",
        "tokenizer.json": snapshot / "tokenizer.json",
        "model.safetensors.index.json": snapshot / "model.safetensors.index.json",
        first_weight.name: first_weight,
        second_weight.name: second_weight,
    }
    official = {
        filename: {
            "size": path.stat().st_size,
            **(
                {"sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
                if filename.endswith(".safetensors")
                else {"git_blob_sha1": _git_blob_sha1_file(path)}
            ),
        }
        for filename, path in files.items()
    }

    with (
        mock.patch(
            "inference_bench.providers.base._cached_hf_snapshot",
            return_value=snapshot,
        ),
        mock.patch(
            "inference_bench.providers.base._official_hf_file_metadata",
            return_value=official,
        ),
    ):
        observation = provider.verify_model_provenance("org/model")

    assert observation["model_revision"] == revision
    assert observation["checkpoint_weight_file_count"] == 2
    assert observation["checkpoint_weight_bytes"] == 11
    assert "config.json" in observation["checkpoint_metadata_sha256"]
    assert observation["checkpoint_official_content_check"] == "passed"

    provider._resolved_server_model = str(tmp_path / "different-snapshot")
    with (
        mock.patch(
            "inference_bench.providers.base._cached_hf_snapshot",
            return_value=snapshot,
        ),
        pytest.raises(RuntimeError, match="did not launch from the verified"),
    ):
        provider.verify_model_provenance("org/model")
    provider._resolved_server_model = str(snapshot)

    first_weight.write_bytes(b"wrong")
    with (
        mock.patch(
            "inference_bench.providers.base._cached_hf_snapshot",
            return_value=snapshot,
        ),
        mock.patch(
            "inference_bench.providers.base._official_hf_file_metadata",
            return_value=official,
        ),
        pytest.raises(RuntimeError, match="Official SHA-256 check failed"),
    ):
        provider.verify_model_provenance("org/model")
    first_weight.write_bytes(b"first")

    second_weight.unlink()
    with (
        mock.patch(
            "inference_bench.providers.base._cached_hf_snapshot",
            return_value=snapshot,
        ),
        pytest.raises(RuntimeError, match="is incomplete"),
    ):
        provider.verify_model_provenance("org/model")
