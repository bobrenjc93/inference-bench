from __future__ import annotations

import hashlib
import json
import os
import re
import signal
import socket
import subprocess
import sys
import threading
import time
from abc import ABC, abstractmethod
from pathlib import Path
from urllib.parse import quote

import httpx

from ..deployment import (
    DISAGGREGATED_PREFILL_DECODE,
    STANDARD_DEPLOYMENT,
    deployment_mode_for_evaluation,
    normalize_deployment_mode,
    resolve_role_tensor_parallel_sizes,
)


def _env_float(name: str, default: float, *, minimum: float | None = None) -> float:
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    try:
        value = float(raw)
    except ValueError:
        return default
    if minimum is not None:
        value = max(minimum, value)
    return value


def _env_flag(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off"}


def _visible_gpu_tokens() -> list[str] | None:
    raw = os.environ.get("CUDA_VISIBLE_DEVICES")
    if raw is None or raw.strip() == "":
        return None
    tokens = [part.strip() for part in raw.split(",") if part.strip()]
    return tokens or None


def _has_cli_option(args: list[str], option: str) -> bool:
    return any(arg == option or arg.startswith(f"{option}=") for arg in args)


def _verify_mooncake_rdma_logs(
    log_paths: dict[str, Path],
    *,
    provider: str,
) -> dict[str, object]:
    hca_counts: dict[str, int] = {}
    for role, log_path in log_paths.items():
        try:
            text = log_path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            raise RuntimeError(
                f"[{provider}] Mooncake {role} log is unavailable"
            ) from exc
        discovered = [
            int(value)
            for value in re.findall(
                r"Topology discovery complete\. Found (\d+) HCAs\.", text
            )
        ]
        if not discovered or max(discovered) <= 0:
            raise RuntimeError(
                f"[{provider}] Mooncake {role} did not report a discovered HCA"
            )
        if "installTransport, type=rdma" not in text:
            raise RuntimeError(
                f"[{provider}] Mooncake {role} did not confirm RDMA data-plane "
                "transport installation"
            )
        hca_counts[role] = max(discovered)
    return {
        "mooncake_rdma_log_check": "passed",
        "mooncake_protocol": "rdma",
        "mooncake_data_plane_transport": "rdma",
        "mooncake_discovered_hcas": hca_counts,
    }


class Provider(ABC):
    name: str
    repo_url: str
    runtime_import_names: tuple[str, ...] = ()

    def __init__(self, build_dir: str = "./builds"):
        self.build_dir = Path(build_dir).resolve()
        self.repo_dir = self.build_dir / self.name
        self.venv_dir = self.repo_dir / "venv"
        self.verbose: bool = False
        self.hardware: str = ""
        self._server_process: subprocess.Popen | None = None
        self.deployment_mode = STANDARD_DEPLOYMENT
        self.prefill_tensor_parallel_size: int | None = None
        self.decode_tensor_parallel_size: int | None = None
        self._deployment_log_paths: dict[str, str] = {}
        self._deployment_observation: dict[str, object] = {}
        self.model_revision: str | None = None
        self._resolved_server_model: str = ""
        self.evaluation_version = 2

    def configure_deployment(
        self,
        *,
        deployment_mode: str,
        tensor_parallel_size: int,
        prefill_tensor_parallel_size: int | None = None,
        decode_tensor_parallel_size: int | None = None,
        model_revision: str | None = None,
        model: str | None = None,
        evaluation_version: int | None = None,
    ) -> None:
        mode = normalize_deployment_mode(deployment_mode)
        prefill_tp, decode_tp = resolve_role_tensor_parallel_sizes(
            deployment_mode=mode,
            tensor_parallel_size=tensor_parallel_size,
            prefill_tensor_parallel_size=prefill_tensor_parallel_size,
            decode_tensor_parallel_size=decode_tensor_parallel_size,
        )
        self.deployment_mode = mode
        self.prefill_tensor_parallel_size = prefill_tp
        self.decode_tensor_parallel_size = decode_tp
        self.model_revision = model_revision
        self._configured_model = model
        configured_version = (
            evaluation_version
            if evaluation_version is not None
            else (4 if mode == DISAGGREGATED_PREFILL_DECODE else 2)
        )
        if isinstance(configured_version, bool) or not isinstance(
            configured_version,
            int,
        ):
            raise ValueError("evaluation_version must be an integer")
        expected_mode = deployment_mode_for_evaluation(configured_version)
        if mode != expected_mode:
            raise ValueError(
                f"evaluation v{configured_version} requires deployment mode "
                f"{expected_mode}"
            )
        self.evaluation_version = configured_version

    @property
    def is_disaggregated_prefill_decode(self) -> bool:
        return self.deployment_mode == DISAGGREGATED_PREFILL_DECODE

    @property
    def is_scored_evaluation(self) -> bool:
        return self.evaluation_version >= 3

    def _reject_scored_environment_overrides(
        self,
        *,
        names: tuple[str, ...] = (),
        prefixes: tuple[str, ...] = (),
    ) -> None:
        if not self.is_scored_evaluation:
            return
        configured = sorted(
            name
            for name in os.environ
            if name in names or any(name.startswith(prefix) for prefix in prefixes)
        )
        if configured:
            raise ValueError(
                f"[{self.name}] Environment override is prohibited in a scored "
                "evaluation: " + ", ".join(configured)
            )

    def _disaggregated_gpu_envs(self) -> tuple[dict[str, str], dict[str, str]]:
        if not self.is_disaggregated_prefill_decode:
            raise RuntimeError("Provider is not configured for disaggregated serving")
        prefill_tp = int(self.prefill_tensor_parallel_size or 0)
        decode_tp = int(self.decode_tensor_parallel_size or 0)
        required = prefill_tp + decode_tp
        visible = _visible_gpu_tokens()
        gpu_tokens = visible if visible is not None else [str(i) for i in range(required)]
        if len(gpu_tokens) < required:
            raise ValueError(
                f"[{self.name}] Disaggregated deployment needs {required} visible GPUs "
                f"({prefill_tp} prefill + {decode_tp} decode), but found "
                f"{len(gpu_tokens)} in CUDA_VISIBLE_DEVICES"
            )
        selected_tokens = gpu_tokens[:required]
        if len(set(selected_tokens)) != required:
            raise ValueError(
                f"[{self.name}] Disaggregated GPU roles must use {required} "
                "distinct CUDA_VISIBLE_DEVICES entries"
            )
        rows = self._query_gpu_memory()
        if rows:
            by_index = {str(row["index"]): str(row["uuid"]) for row in rows}
            by_uuid = {str(row["uuid"]): str(row["uuid"]) for row in rows}
            resolved = [
                by_index.get(token) or by_uuid.get(token) for token in selected_tokens
            ]
            if any(uuid is None for uuid in resolved):
                unknown = [
                    token
                    for token, uuid in zip(selected_tokens, resolved)
                    if uuid is None
                ]
                raise ValueError(
                    f"[{self.name}] Could not resolve visible GPU identifiers: "
                    + ", ".join(unknown)
                )
            if len(set(resolved)) != required:
                raise ValueError(
                    f"[{self.name}] Prefill and decode roles resolve to fewer than "
                    f"{required} unique physical GPUs"
                )
        prefill_devices = ",".join(selected_tokens[:prefill_tp])
        decode_devices = ",".join(selected_tokens[prefill_tp:required])
        return (
            {"CUDA_VISIBLE_DEVICES": prefill_devices},
            {"CUDA_VISIBLE_DEVICES": decode_devices},
        )

    @staticmethod
    def _reserve_local_ports(count: int, *, excluded: set[int] | None = None) -> list[int]:
        excluded = set(excluded or ())
        sockets: list[socket.socket] = []
        ports: list[int] = []
        try:
            while len(ports) < count:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(("127.0.0.1", 0))
                port = int(sock.getsockname()[1])
                if port in excluded:
                    sock.close()
                    continue
                excluded.add(port)
                sockets.append(sock)
                ports.append(port)
        finally:
            for sock in sockets:
                sock.close()
        return ports

    @staticmethod
    def _reserve_local_port_block(
        count: int, *, excluded: set[int] | None = None
    ) -> int:
        if count < 1:
            raise ValueError("Port block size must be at least 1")
        excluded = set(excluded or ())
        for base_port in range(20000, 65537 - count):
            candidates = range(base_port, base_port + count)
            if any(port in excluded for port in candidates):
                continue
            sockets: list[socket.socket] = []
            try:
                for port in candidates:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    try:
                        sock.bind(("127.0.0.1", port))
                    except OSError:
                        sock.close()
                        raise
                    sockets.append(sock)
            except OSError:
                continue
            finally:
                for sock in sockets:
                    sock.close()
            return base_port
        raise RuntimeError(f"Could not find a free block of {count} local ports")

    def _record_disaggregated_spec(self, spec: dict) -> Path:
        self.build_dir.mkdir(parents=True, exist_ok=True)
        spec_path = self.build_dir / f"{self.name}_disaggregated_spec.json"
        spec_path.write_text(json.dumps(spec, indent=2, sort_keys=True) + "\n")
        self._deployment_log_paths["deployment_spec"] = str(spec_path)
        return spec_path

    def _disaggregated_supervisor_cmd(self, spec: dict) -> list[str]:
        spec_path = self._record_disaggregated_spec(spec)
        for phase in spec.get("phases", []):
            for component in phase.get("components", []):
                name = str(component.get("name", "component"))
                log_path = str(component.get("log_path", ""))
                if log_path:
                    self._deployment_log_paths[f"{name}_server"] = log_path
        launcher = Path(__file__).resolve().parents[1] / "disaggregated_launcher.py"
        return [sys.executable, str(launcher), str(spec_path)]

    def extra_log_paths(self) -> dict[str, str]:
        return dict(self._deployment_log_paths)

    def _log(self, msg: str) -> None:
        if self.verbose:
            print(msg)

    @property
    def venv_python(self) -> str:
        return str(self.venv_dir / "bin" / "python")

    @property
    def server_python(self) -> str:
        override = self._server_python_override()
        if self.is_scored_evaluation and override:
            raise ValueError(
                f"[{self.name}] Server Python overrides are prohibited in a "
                "scored evaluation"
            )
        return override if override else self.venv_python

    def _server_python_override(self) -> str:
        env_name = f"INFERENCE_BENCH_{self.name.upper().replace('-', '_')}_PYTHON"
        return os.environ.get(env_name, "").strip()

    def _server_python_bin_dir(self) -> str:
        override = self._server_python_override()
        if not override:
            return str(self.venv_dir / "bin")
        path = Path(override).expanduser()
        if path.parent == Path("."):
            return ""
        return str(path.parent)

    @property
    def api_base(self) -> str:
        return f"http://localhost:{self._port}/v1"

    def get_commit_hash(self) -> str:
        if not (self.repo_dir / ".git").exists():
            return ""
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo_dir,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return ""
        commit = result.stdout.strip()
        if not commit:
            return ""
        status = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all"],
            cwd=self.repo_dir,
            capture_output=True,
            text=True,
        )
        if status.returncode == 0 and status.stdout.strip():
            return f"{commit}-dirty"
        if status.returncode != 0:
            return f"{commit}-status-unknown"
        return commit

    def prepare_source_provenance(self, *, skip_build: bool) -> dict[str, object]:
        if not self.is_scored_evaluation:
            return {}
        if skip_build:
            raise RuntimeError(
                f"[{self.name}] --skip-build is prohibited for scored "
                "evaluations; use a fresh build"
            )
        if self.venv_dir.exists():
            raise RuntimeError(
                f"[{self.name}] Scored evaluations require a fresh "
                "provider environment; remove the existing venv or use a fresh "
                "build directory"
            )
        if not getattr(self, "_fresh_scored_clone", False):
            raise RuntimeError(
                f"[{self.name}] Scored evaluations require a checkout "
                "freshly cloned during this invocation"
            )
        state = self._source_state()
        self._validate_source_identity(state)
        if state.get("dirty"):
            raise RuntimeError(
                f"[{self.name}] Scored builds must start from a clean origin/main "
                "checkout; use a fresh build directory"
            )
        if state.get("ignored_runtime_artifacts"):
            raise RuntimeError(
                f"[{self.name}] Scored builds must not reuse ignored Python or "
                "native runtime artifacts; use a fresh build directory"
            )
        if state.get("commit") != getattr(self, "_fresh_scored_clone_commit", None):
            raise RuntimeError(
                f"[{self.name}] Fresh checkout commit changed before the scored build"
            )
        self._source_prebuild_state = state
        return {}

    def finalize_source_provenance(self) -> dict[str, object]:
        if not self.is_scored_evaluation:
            return {}
        prebuild = getattr(self, "_source_prebuild_state", None)
        if not isinstance(prebuild, dict):
            raise RuntimeError(f"[{self.name}] Source pre-build state was not recorded")
        post_build = self._source_state()
        self._validate_source_identity(post_build)
        for field in ("commit", "origin_main", "remote"):
            if post_build.get(field) != prebuild.get(field):
                raise RuntimeError(
                    f"[{self.name}] Source {field} changed during the provider build"
                )
        runtime_import_state = self._runtime_import_state()
        runtime_environment_state = self._runtime_environment_state()
        manifest_path = self._source_provenance_manifest_path()
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest = {
            "schema_version": 1,
            "provider": self.name,
            "repo_url": self.repo_url,
            "pre_build_state": prebuild,
            "post_build_state": post_build,
            "runtime_import_state": runtime_import_state,
            "runtime_environment_state": runtime_environment_state,
        }
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        patch_path = self._source_provenance_patch_path()
        diff = self._git_output_bytes(
            ["git", "diff", "--binary", "--no-ext-diff", "HEAD", "--", "."]
        )
        if diff:
            patch_path.write_bytes(diff)
        else:
            try:
                patch_path.unlink()
            except FileNotFoundError:
                pass
        self._finalized_source_state = post_build
        self._finalized_runtime_import_state = runtime_import_state
        self._finalized_runtime_environment_state = runtime_environment_state
        self._finalized_source_manifest_sha256 = _sha256_file(manifest_path)
        self._finalized_source_patch_sha256 = (
            _sha256_file(patch_path) if patch_path.exists() else None
        )
        self._register_source_provenance_logs(manifest_path)
        return self._source_provenance_observation(
            post_build,
            runtime_import_state=runtime_import_state,
            runtime_environment_state=runtime_environment_state,
        )

    def verify_source_provenance(self) -> dict[str, object]:
        if not self.is_scored_evaluation:
            return {}
        expected_source = getattr(self, "_finalized_source_state", None)
        expected_imports = getattr(self, "_finalized_runtime_import_state", None)
        expected_environment = getattr(
            self,
            "_finalized_runtime_environment_state",
            None,
        )
        if not all(
            isinstance(value, dict)
            for value in (expected_source, expected_imports, expected_environment)
        ):
            raise RuntimeError(
                f"[{self.name}] In-process scored build provenance is unavailable"
            )
        current = self._source_state()
        self._validate_source_identity(current)
        if expected_source != current:
            raise RuntimeError(
                f"[{self.name}] Provider source changed after the scored build"
            )
        runtime_import_state = self._runtime_import_state()
        if expected_imports != runtime_import_state:
            raise RuntimeError(
                f"[{self.name}] Provider runtime imports changed after the scored build"
            )
        runtime_environment_state = self._runtime_environment_state()
        if expected_environment != runtime_environment_state:
            raise RuntimeError(
                f"[{self.name}] Provider runtime environment changed after the "
                "scored build"
            )
        manifest_path = self._source_provenance_manifest_path()
        expected_manifest_sha = getattr(
            self,
            "_finalized_source_manifest_sha256",
            None,
        )
        if not manifest_path.is_file() or _sha256_file(manifest_path) != expected_manifest_sha:
            raise RuntimeError(
                f"[{self.name}] Source provenance manifest changed after the scored build"
            )
        patch_path = self._source_provenance_patch_path()
        expected_patch_sha = getattr(self, "_finalized_source_patch_sha256", None)
        if expected_patch_sha is None:
            if patch_path.exists():
                raise RuntimeError(
                    f"[{self.name}] Unexpected source patch appeared after the scored build"
                )
        elif not patch_path.is_file() or _sha256_file(patch_path) != expected_patch_sha:
            raise RuntimeError(
                f"[{self.name}] Source patch changed after the scored build"
            )
        self._register_source_provenance_logs(manifest_path)
        return self._source_provenance_observation(
            current,
            runtime_import_state=runtime_import_state,
            runtime_environment_state=runtime_environment_state,
        )

    def _source_state(self) -> dict[str, object]:
        if not (self.repo_dir / ".git").exists():
            raise RuntimeError(f"[{self.name}] Provider checkout is missing")
        commit = self._git_output(["git", "rev-parse", "HEAD"])
        origin_main = self._git_output(["git", "rev-parse", "origin/main"])
        remote = self._git_output(["git", "remote", "get-url", "origin"])
        diff = self._git_output_bytes(
            ["git", "diff", "--binary", "--no-ext-diff", "HEAD", "--", "."]
        )
        untracked_output = self._git_output_bytes(
            ["git", "ls-files", "--others", "--exclude-standard", "-z"]
        )
        untracked: dict[str, str] = {}
        for raw_path in untracked_output.split(b"\0"):
            if not raw_path:
                continue
            relative = raw_path.decode("utf-8", errors="strict")
            path = self.repo_dir / relative
            if path.is_symlink():
                digest = hashlib.sha256(os.readlink(path).encode()).hexdigest()
            elif path.is_file():
                digest = _sha256_file(path)
            else:
                digest = hashlib.sha256(b"").hexdigest()
            untracked[relative] = digest
        ignored_runtime_artifacts = self._ignored_runtime_artifacts()
        return {
            "commit": commit,
            "origin_main": origin_main,
            "remote": remote,
            "tracked_diff_sha256": hashlib.sha256(diff).hexdigest(),
            "tracked_diff_bytes": len(diff),
            "untracked_files": untracked,
            "ignored_runtime_artifacts": ignored_runtime_artifacts,
            "dirty": bool(diff or untracked),
        }

    def _ignored_runtime_artifacts(self) -> dict[str, dict[str, int | str]]:
        output = self._git_output_bytes(
            ["git", "ls-files", "--others", "--ignored", "--exclude-standard", "-z"]
        )
        artifacts: dict[str, dict[str, int | str]] = {}
        for raw_path in output.split(b"\0"):
            if not raw_path:
                continue
            relative = raw_path.decode("utf-8", errors="strict")
            if relative == "venv" or relative.startswith("venv/"):
                continue
            if not _is_runtime_sensitive_artifact(relative):
                continue
            path = self.repo_dir / relative
            if not path.is_file():
                continue
            artifacts[relative] = {
                "sha256": _sha256_file(path),
                "size": path.stat().st_size,
            }
        return artifacts

    def _validate_source_identity(self, state: dict[str, object]) -> None:
        if state.get("commit") != state.get("origin_main"):
            raise RuntimeError(
                f"[{self.name}] Scored source must be exactly origin/main"
            )
        if _normalize_git_remote(str(state.get("remote", ""))) != _normalize_git_remote(
            self.repo_url
        ):
            raise RuntimeError(
                f"[{self.name}] Scored source remote does not match {self.repo_url}"
            )

    def _source_provenance_observation(
        self,
        state: dict[str, object],
        *,
        runtime_import_state: dict[str, object],
        runtime_environment_state: dict[str, object],
    ) -> dict[str, object]:
        return {
            "source_provenance_check": "passed",
            "source_commit": state["commit"],
            "source_origin_main": state["origin_main"],
            "source_dirty": state["dirty"],
            "source_tracked_diff_sha256": state["tracked_diff_sha256"],
            "source_tracked_diff_bytes": state["tracked_diff_bytes"],
            "source_untracked_files": state["untracked_files"],
            "source_ignored_runtime_artifacts": state[
                "ignored_runtime_artifacts"
            ],
            "runtime_import_provenance_check": "passed",
            "runtime_import_state": runtime_import_state,
            "runtime_environment_provenance_check": "passed",
            "runtime_environment_state": runtime_environment_state,
        }

    def _runtime_import_state(self) -> dict[str, object]:
        import_names = self.runtime_import_names or (self.name,)
        script = """
import importlib.util
import json
import sys

modules = {}
for name in sys.argv[1:]:
    spec = importlib.util.find_spec(name)
    if spec is None:
        raise SystemExit(f"module {name!r} is unavailable")
    locations = []
    if spec.origin and spec.origin not in {"built-in", "frozen"}:
        locations.append(spec.origin)
    if spec.submodule_search_locations:
        locations.extend(spec.submodule_search_locations)
    modules[name] = sorted(set(locations))
print(json.dumps({
    "python_executable": sys.executable,
    "python_prefix": sys.prefix,
    "modules": modules,
}, sort_keys=True))
"""
        env = Provider._server_env(self)
        command = [self.server_python, "-c", script, *import_names]
        result = subprocess.run(
            command,
            cwd=self.repo_dir,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            detail = (result.stderr or result.stdout).strip()
            raise RuntimeError(
                f"[{self.name}] Could not resolve runtime provider imports: {detail}"
            )
        try:
            state = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"[{self.name}] Runtime import probe returned invalid JSON"
            ) from exc
        modules = state.get("modules")
        if not isinstance(modules, dict):
            raise RuntimeError(f"[{self.name}] Runtime import probe omitted modules")
        repo_root = self.repo_dir.resolve()
        for name in import_names:
            raw_locations = modules.get(name)
            if not isinstance(raw_locations, list) or not raw_locations:
                raise RuntimeError(
                    f"[{self.name}] Runtime import {name!r} has no source location"
                )
            for raw_location in raw_locations:
                location = Path(str(raw_location)).resolve()
                try:
                    location.relative_to(repo_root)
                except ValueError as exc:
                    raise RuntimeError(
                        f"[{self.name}] Runtime import {name!r} resolves outside "
                        f"the verified checkout: {location}"
                    ) from exc
        return state

    def _runtime_environment_state(self) -> dict[str, object]:
        env = Provider._server_env(self)
        result = subprocess.run(
            [self.server_python, "-m", "pip", "freeze", "--all"],
            cwd=self.repo_dir,
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"[{self.name}] Could not capture the scored Python environment: "
                f"{result.stderr.strip()}"
            )
        packages = sorted(
            line.strip() for line in result.stdout.splitlines() if line.strip()
        )
        artifact_digest = hashlib.sha256()
        artifact_count = 0
        artifact_bytes = 0
        startup_files: dict[str, str] = {}
        if self.venv_dir.is_dir():
            for path in sorted(self.venv_dir.rglob("*")):
                if not path.is_file() or not _is_venv_runtime_artifact(path):
                    continue
                relative = path.relative_to(self.venv_dir).as_posix()
                digest = _sha256_file(path)
                size = path.stat().st_size
                artifact_digest.update(relative.encode())
                artifact_digest.update(b"\0")
                artifact_digest.update(str(size).encode())
                artifact_digest.update(b"\0")
                artifact_digest.update(digest.encode())
                artifact_digest.update(b"\0")
                artifact_count += 1
                artifact_bytes += size
                if path.suffix.lower() == ".pth" or path.name.lower() in {
                    "sitecustomize.py",
                    "usercustomize.py",
                }:
                    startup_files[relative] = digest
        return {
            "pip_freeze": packages,
            "venv_runtime_artifact_count": artifact_count,
            "venv_runtime_artifact_bytes": artifact_bytes,
            "venv_runtime_artifact_manifest_sha256": artifact_digest.hexdigest(),
            "venv_startup_files": startup_files,
        }

    def _source_provenance_manifest_path(self) -> Path:
        return self.build_dir / f"{self.name}_source_provenance.json"

    def _source_provenance_patch_path(self) -> Path:
        return self.build_dir / f"{self.name}_source.patch"

    def _register_source_provenance_logs(self, manifest_path: Path) -> None:
        self._deployment_log_paths["source_provenance"] = str(manifest_path)
        patch_path = self._source_provenance_patch_path()
        if patch_path.exists():
            self._deployment_log_paths["source_patch"] = str(patch_path)

    def _git_output(self, command: list[str]) -> str:
        return self._git_output_bytes(command).decode().strip()

    def _git_output_bytes(self, command: list[str]) -> bytes:
        if self.is_scored_evaluation and command[0] == "git":
            command = ["/usr/bin/git", *command[1:]]
        result = subprocess.run(
            command,
            cwd=self.repo_dir,
            env=(
                self._scored_git_env()
                if self.is_scored_evaluation
                else None
            ),
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            detail = result.stderr.decode(errors="replace").strip()
            raise RuntimeError(f"[{self.name}] {' '.join(command)} failed: {detail}")
        return result.stdout

    def clone(self) -> None:
        if (self.repo_dir / ".git").exists():
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] Scored evaluations require a fresh "
                    "build directory; refusing to reuse an existing checkout"
                )
            self._log(f"[{self.name}] Repo already cloned at {self.repo_dir}, pulling latest...")
            subprocess.run(
                ["git", "pull"],
                cwd=self.repo_dir,
                check=True,
            )
            return
        self.repo_dir.parent.mkdir(parents=True, exist_ok=True)
        self._log(f"[{self.name}] Cloning {self.repo_url} -> {self.repo_dir}")
        subprocess.run(
            [
                "/usr/bin/git" if self.is_scored_evaluation else "git",
                "clone",
                self.repo_url,
                str(self.repo_dir),
            ],
            env=(
                self._scored_git_env()
                if self.is_scored_evaluation
                else None
            ),
            check=True,
        )
        if self.is_scored_evaluation:
            head = self._git_output(["git", "rev-parse", "HEAD"])
            remote_main = self._remote_main_commit()
            if head != remote_main:
                raise RuntimeError(
                    f"[{self.name}] Fresh clone HEAD does not match the canonical "
                    "remote main branch"
                )
            self._fresh_scored_clone = True
            self._fresh_scored_clone_commit = head

    def _remote_main_commit(self) -> str:
        result = subprocess.run(
            ["/usr/bin/git", "ls-remote", self.repo_url, "refs/heads/main"],
            env=self._scored_git_env(),
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(
                f"[{self.name}] Could not resolve canonical remote main: "
                f"{result.stderr.strip()}"
            )
        fields = result.stdout.strip().split()
        if len(fields) != 2 or fields[1] != "refs/heads/main":
            raise RuntimeError(f"[{self.name}] Canonical remote main is unavailable")
        return fields[0]

    @staticmethod
    def _scored_git_env() -> dict[str, str]:
        env = {
            key: value
            for key, value in os.environ.items()
            if not key.startswith("GIT_")
            and key
            not in {
                "ALL_PROXY",
                "CURL_CA_BUNDLE",
                "HTTPS_PROXY",
                "HTTP_PROXY",
                "NO_PROXY",
                "SSL_CERT_DIR",
                "SSL_CERT_FILE",
                "all_proxy",
                "https_proxy",
                "http_proxy",
                "no_proxy",
            }
        }
        env.update(
            {
                "GIT_ALLOW_PROTOCOL": "https",
                "GIT_CONFIG_GLOBAL": os.devnull,
                "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_CONFIG_SYSTEM": os.devnull,
                "GIT_TERMINAL_PROMPT": "0",
            }
        )
        return env

    def _create_venv(self) -> None:
        if not self.venv_dir.exists():
            self._log(f"[{self.name}] Creating virtualenv at {self.venv_dir}")
            subprocess.run(
                [sys.executable, "-m", "venv", str(self.venv_dir)],
                check=True,
            )

    def _pip_install(self, *args: str, cwd: str | Path | None = None) -> None:
        cmd = [self.venv_python, "-m", "pip", "install", *args]
        self._log(f"[{self.name}] Running: {' '.join(cmd)}")
        subprocess.run(cmd, check=True, cwd=cwd)

    @abstractmethod
    def build(self) -> None:
        ...

    def prepare_model_assets(self, model: str) -> None:
        del model

    @abstractmethod
    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        ...

    def _server_env(self) -> dict[str, str]:
        self._reject_scored_environment_overrides(
            names=(
                "CUDA_LAUNCH_BLOCKING",
                "PYTORCH_CUDA_ALLOC_CONF",
                "USE_BAREX",
            ),
            prefixes=("MC_", "MOONCAKE_", "NCCL_", "TORCH_NCCL_"),
        )
        env = os.environ.copy()
        if self.is_scored_evaluation:
            for name in tuple(env):
                if name.startswith(("SGLANG_", "TORCHINFERNO_", "VLLM_")) or name in {
                    "CMAKE_ARGS",
                    "CMAKE_BUILD_TYPE",
                    "MAX_JOBS",
                    "TORCH_CUDA_ARCH_LIST",
                }:
                    env.pop(name, None)
            for name in tuple(env):
                if name.startswith(
                    ("GOMP_", "KMP_", "MKL_", "NUMEXPR_", "OMP_", "TBB_")
                ):
                    env.pop(name, None)
            for name in tuple(env):
                if name == "USE_BAREX" or name.startswith(
                    ("MC_", "MOONCAKE_", "VLLM_MOONCAKE_", "SGLANG_MOONCAKE_")
                ):
                    env.pop(name, None)
            for name in (
                "DYLD_INSERT_LIBRARIES",
                "DYLD_LIBRARY_PATH",
                "LD_AUDIT",
                "LD_LIBRARY_PATH",
                "LD_PRELOAD",
                "PYTHONHOME",
                "PYTHONINSPECT",
                "PYTHONPATH",
                "PYTHONSTARTUP",
                "PYTHONUSERBASE",
            ):
                env.pop(name, None)
            env["PYTHONNOUSERSITE"] = "1"
            env["PYTHONDONTWRITEBYTECODE"] = "1"
        return env

    @staticmethod
    def _trusted_system_probe_env() -> dict[str, str]:
        env = os.environ.copy()
        for name in (
            "DYLD_INSERT_LIBRARIES",
            "DYLD_LIBRARY_PATH",
            "LD_AUDIT",
            "LD_LIBRARY_PATH",
            "LD_PRELOAD",
            "PYTHONHOME",
            "PYTHONPATH",
            "PYTHONUSERBASE",
        ):
            env.pop(name, None)
        env["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin"
        return env

    def _server_model(self, model: str) -> str:
        if self.is_scored_evaluation:
            if not _env_flag("INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT", True):
                raise ValueError(
                    "INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT=0 is prohibited in "
                    "a scored evaluation"
                )
            if os.environ.get("INFERENCE_BENCH_SERVER_MODEL", "").strip():
                raise ValueError(
                    "INFERENCE_BENCH_SERVER_MODEL is prohibited in a scored "
                    "evaluation"
                )
            if Path(model).expanduser().exists():
                raise ValueError(
                    "Local model paths are prohibited in a scored evaluation"
                )
        resolved = _server_model_path(model, revision=self.model_revision)
        if self.is_scored_evaluation and resolved == model:
            raise RuntimeError(
                f"[{self.name}] Scored evaluations require the complete "
                "pinned checkpoint snapshot before server startup"
            )
        self._resolved_server_model = resolved
        return resolved

    def verify_model_provenance(self, model: str) -> dict[str, object]:
        if not self.is_scored_evaluation:
            return {}
        revision = str(self.model_revision or "")
        snapshot = _cached_hf_snapshot(model, revision=revision)
        if snapshot is None or snapshot.name != revision:
            raise RuntimeError(
                f"[{self.name}] Complete checkpoint revision {revision!r} was not "
                "found in the Hugging Face cache after startup"
            )
        try:
            resolved_server_model = Path(self._resolved_server_model).resolve()
        except (OSError, TypeError) as exc:
            raise RuntimeError(
                f"[{self.name}] Server checkpoint path could not be verified"
            ) from exc
        if resolved_server_model != snapshot.resolve():
            raise RuntimeError(
                f"[{self.name}] Server did not launch from the verified pinned "
                "checkpoint snapshot"
            )
        metadata_hashes: dict[str, str] = {}
        for filename in (
            "config.json",
            "generation_config.json",
            "tokenizer.json",
            "tokenizer_config.json",
            "special_tokens_map.json",
            "model.safetensors.index.json",
            "pytorch_model.bin.index.json",
        ):
            path = snapshot / filename
            if path.is_file():
                metadata_hashes[filename] = _sha256_file(path)
        weight_files = _snapshot_weight_files(snapshot)
        if not weight_files or not all(path.is_file() for path in weight_files):
            raise RuntimeError(
                f"[{self.name}] Checkpoint revision {revision!r} is incomplete"
            )
        official_files = _official_hf_file_metadata(model, revision)
        critical_files = {path.name: path for path in weight_files}
        official_critical_metadata = {
            filename
            for filename in official_files
            if "/" not in filename
            and (
                filename in {
                    "config.json",
                    "generation_config.json",
                    "model.safetensors.index.json",
                    "pytorch_model.bin.index.json",
                    "special_tokens_map.json",
                    "added_tokens.json",
                    "chat_template.jinja",
                }
                or filename.startswith("tokenizer")
                or filename.endswith(".py")
            )
        }
        for filename in official_critical_metadata:
            path = snapshot / filename
            if not path.is_file():
                raise RuntimeError(
                    f"[{self.name}] Pinned checkpoint is missing official file "
                    f"{filename!r}"
                )
            critical_files[filename] = path
        if "config.json" not in critical_files or not any(
            name.startswith("tokenizer") for name in critical_files
        ):
            raise RuntimeError(
                f"[{self.name}] Pinned checkpoint is missing config/tokenizer files"
            )
        verified_files = {
            filename: _verify_official_hf_file(
                path,
                filename=filename,
                official=official_files.get(filename),
            )
            for filename, path in sorted(critical_files.items())
        }
        return {
            "model_provenance_check": "passed",
            "model_id": model,
            "model_revision": revision,
            "resolved_snapshot": str(snapshot),
            "checkpoint_metadata_sha256": metadata_hashes,
            "checkpoint_weight_file_count": len(weight_files),
            "checkpoint_weight_bytes": sum(path.stat().st_size for path in weight_files),
            "checkpoint_official_content_check": "passed",
            "checkpoint_verified_files": verified_files,
        }

    def _gpu_memory_wait_fraction(self) -> float | None:
        return None

    def wait_for_gpu_isolation(self, tp: int) -> None:
        if not _env_flag("INFERENCE_BENCH_GPU_ISOLATION_CHECK", True):
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] GPU isolation checks cannot be disabled for "
                    "a scored evaluation"
                )
            return
        timeout_s = _env_float("INFERENCE_BENCH_GPU_ISOLATION_TIMEOUT_S", 900.0, minimum=0.0)
        poll_s = _env_float("INFERENCE_BENCH_GPU_ISOLATION_POLL_S", 2.0, minimum=0.5)
        clean_wait_s = _env_float("INFERENCE_BENCH_GPU_ISOLATION_CLEAN_WAIT_S", 5.0, minimum=0.0)
        start = time.time()
        clean_since: float | None = None
        printed_wait = False
        last_detail = ""
        while True:
            apps = self._external_gpu_apps(tp)
            now = time.time()
            if not apps:
                if clean_since is None:
                    clean_since = now
                if now - clean_since >= clean_wait_s:
                    if printed_wait:
                        self._log(f"[{self.name}] GPU isolation is ready")
                    return
            else:
                clean_since = None
                last_detail = "\n".join(apps)
            elapsed = now - start
            if elapsed >= timeout_s:
                raise TimeoutError(
                    f"[{self.name}] External GPU processes did not clear "
                    f"within {timeout_s:.0f}s.\n{last_detail}"
                )
            if apps:
                printed_wait = True
                self._log(
                    f"[{self.name}] Waiting for GPU isolation "
                    f"({elapsed:.0f}/{timeout_s:.0f}s): {apps[0]}"
                )
            time.sleep(min(poll_s, max(0.0, timeout_s - elapsed)))

    def gpu_isolation_monitor(self, tp: int) -> "_GpuIsolationMonitor":
        return _GpuIsolationMonitor(self, tp)

    def start_server(self, model: str, tp: int, port: int, timeout: int = 600) -> None:
        self._port = port
        self._wait_for_gpu_memory_ready(tp)
        cmd = self._server_cmd(model, tp, port)
        env = self._server_env()
        python_bin_dir = self._server_python_bin_dir()
        if python_bin_dir:
            env["PATH"] = python_bin_dir + ":" + env.get("PATH", "")

        self._log_path = self.build_dir / f"{self.name}_server.log"
        self._log_path.parent.mkdir(parents=True, exist_ok=True)
        self._log_file = open(self._log_path, "w")

        self._log(f"[{self.name}] Starting server: {' '.join(cmd)}")
        self._log(f"[{self.name}] Server log: {self._log_path}")
        self._server_process = subprocess.Popen(
            cmd,
            cwd=self.repo_dir if self.is_scored_evaluation else None,
            env=env,
            stdout=self._log_file,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )

        self._wait_for_health(timeout)

    def _wait_for_gpu_memory_ready(self, tp: int) -> None:
        fraction = self._gpu_memory_wait_fraction()
        if fraction is None or fraction <= 0.0:
            return
        if not _env_flag("INFERENCE_BENCH_GPU_MEMORY_WAIT", True):
            return
        timeout_s = _env_float("INFERENCE_BENCH_GPU_MEMORY_WAIT_TIMEOUT_S", 900.0, minimum=0.0)
        poll_s = _env_float("INFERENCE_BENCH_GPU_MEMORY_WAIT_POLL_S", 10.0, minimum=1.0)
        start = time.time()
        last_detail = ""
        printed_wait = False
        while True:
            ready, detail = self._gpu_memory_ready_once(tp=tp, required_fraction=fraction)
            if ready:
                if printed_wait:
                    self._log(f"[{self.name}] GPU memory is ready")
                return
            last_detail = detail
            elapsed = time.time() - start
            if elapsed >= timeout_s:
                raise TimeoutError(
                    f"[{self.name}] GPUs did not reach required free memory "
                    f"within {timeout_s:.0f}s.\n{last_detail}"
                )
            printed_wait = True
            self._log(
                f"[{self.name}] Waiting for GPU memory before server start "
                f"({elapsed:.0f}/{timeout_s:.0f}s): {detail.splitlines()[0]}"
            )
            time.sleep(min(poll_s, max(0.0, timeout_s - elapsed)))

    def _gpu_memory_ready_once(self, *, tp: int, required_fraction: float) -> tuple[bool, str]:
        rows = self._query_gpu_memory()
        if not rows:
            return True, "nvidia-smi did not report GPUs; skipping GPU memory wait"
        selected = self._select_gpu_rows(rows, tp)
        if not selected:
            return True, "no selected GPUs; skipping GPU memory wait"
        apps = self._query_gpu_apps()
        failures: list[str] = []
        lines: list[str] = []
        for row in selected:
            required_mib = int(row["total_mib"] * required_fraction)
            ok = row["free_mib"] >= required_mib
            line = (
                f"gpu={row['index']} free={row['free_mib'] / 1024:.1f}GiB "
                f"required={required_mib / 1024:.1f}GiB "
                f"total={row['total_mib'] / 1024:.1f}GiB"
            )
            lines.append(line)
            if not ok:
                failures.append(line)
        if failures and apps:
            lines.append("compute processes:")
            lines.extend(f"  {app}" for app in apps)
        if failures:
            detail_lines = failures + [line for line in lines if line not in failures]
            return False, "\n".join(detail_lines)
        return True, "\n".join(lines)

    def _query_gpu_memory(self) -> list[dict[str, int | str]]:
        cmd = [
            "/usr/bin/nvidia-smi",
            "--query-gpu=index,uuid,name,memory.total,memory.free",
            "--format=csv,noheader,nounits",
        ]
        try:
            result = subprocess.run(
                cmd,
                env=(
                    self._trusted_system_probe_env()
                    if self.is_scored_evaluation
                    else None
                ),
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] nvidia-smi is required for scored "
                    "GPU isolation"
                )
            return []
        if result.returncode != 0:
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] nvidia-smi GPU query failed during scored "
                    f"GPU isolation: {result.stderr.strip()}"
                )
            return []
        rows: list[dict[str, int | str]] = []
        for line in result.stdout.splitlines():
            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 5:
                continue
            try:
                rows.append(
                    {
                        "index": int(parts[0]),
                        "uuid": parts[1],
                        "name": parts[2],
                        "total_mib": int(parts[3]),
                        "free_mib": int(parts[4]),
                    }
                )
            except ValueError:
                continue
        if not rows and self.is_scored_evaluation:
            raise RuntimeError(
                f"[{self.name}] nvidia-smi returned no parseable GPU inventory "
                "for scored GPU isolation"
            )
        return rows

    def _query_gpu_apps(self) -> list[str]:
        return [str(row["raw"]) for row in self._query_gpu_app_rows()]

    def _query_gpu_app_rows(self) -> list[dict[str, int | str]]:
        cmd = [
            "/usr/bin/nvidia-smi",
            "--query-compute-apps=pid,process_name,gpu_uuid,used_memory",
            "--format=csv,noheader,nounits",
        ]
        try:
            result = subprocess.run(
                cmd,
                env=(
                    self._trusted_system_probe_env()
                    if self.is_scored_evaluation
                    else None
                ),
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] nvidia-smi is required for scored "
                    "GPU process monitoring"
                )
            return []
        if result.returncode != 0:
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] nvidia-smi process query failed during scored "
                    f"GPU monitoring: {result.stderr.strip()}"
                )
            return []
        rows: list[dict[str, int | str]] = []
        for line in result.stdout.splitlines():
            raw = line.strip()
            if not raw:
                continue
            parts = [part.strip() for part in raw.split(",", 3)]
            if len(parts) != 4:
                rows.append(
                    {
                        "raw": raw,
                        "pid": -1,
                        "process_name": "",
                        "gpu_uuid": "",
                        "used_memory_mib": -1,
                    }
                )
                continue
            try:
                pid = int(parts[0])
            except ValueError:
                pid = -1
            try:
                used_memory = int(parts[3])
            except ValueError:
                used_memory = -1
            rows.append(
                {
                    "raw": raw,
                    "pid": pid,
                    "process_name": parts[1],
                    "gpu_uuid": parts[2],
                    "used_memory_mib": used_memory,
                }
            )
        return rows

    @staticmethod
    def _select_gpu_rows(rows: list[dict[str, int | str]], tp: int) -> list[dict[str, int | str]]:
        visible = _visible_gpu_tokens()
        if visible is None:
            return rows[: max(1, int(tp))]
        by_index = {str(row["index"]): row for row in rows}
        by_uuid = {str(row["uuid"]): row for row in rows}
        selected: list[dict[str, int | str]] = []
        for token in visible:
            row = by_index.get(token) or by_uuid.get(token)
            if row is not None:
                selected.append(row)
        return selected[: max(1, int(tp))]

    def _external_gpu_apps(self, tp: int) -> list[str]:
        rows = self._query_gpu_memory()
        if not rows:
            return []
        selected = self._select_gpu_rows(rows, tp)
        if not selected:
            return []
        selected_uuids = {str(row["uuid"]) for row in selected}
        allowed_pids = self._server_process_group_pids()
        external: list[str] = []
        for app in self._query_gpu_app_rows():
            if str(app.get("gpu_uuid", "")) not in selected_uuids:
                continue
            pid = int(app.get("pid", -1))
            if pid in allowed_pids:
                continue
            external.append(str(app.get("raw", "")))
        return external

    def verify_gpu_coverage(self, expected_gpu_count: int) -> dict[str, object]:
        if not _env_flag("INFERENCE_BENCH_GPU_COVERAGE_CHECK", True):
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] GPU coverage checks cannot be disabled for "
                    "a scored evaluation"
                )
            self._deployment_observation = {"gpu_coverage_check": "disabled"}
            return dict(self._deployment_observation)
        rows = self._query_gpu_memory()
        if not rows:
            if self.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.name}] nvidia-smi GPU coverage data is required for "
                    "a scored evaluation"
                )
            self._deployment_observation = {"gpu_coverage_check": "unavailable"}
            return dict(self._deployment_observation)
        selected = self._select_gpu_rows(rows, expected_gpu_count)
        selected_uuids = [str(row["uuid"]) for row in selected]
        if len(selected_uuids) != expected_gpu_count:
            raise RuntimeError(
                f"[{self.name}] Expected {expected_gpu_count} visible GPUs, but "
                f"nvidia-smi resolved {len(selected_uuids)}"
            )
        if len(set(selected_uuids)) != expected_gpu_count:
            raise RuntimeError(
                f"[{self.name}] Expected {expected_gpu_count} unique physical GPUs, "
                "but CUDA_VISIBLE_DEVICES contains aliases or duplicates"
            )
        observed_gpu_names = [str(row.get("name", "")) for row in selected]
        if "h100" in self.hardware.lower() and any(
            "h100" not in name.lower() for name in observed_gpu_names
        ):
            raise RuntimeError(
                f"[{self.name}] Configured hardware requires H100 GPUs, but "
                f"nvidia-smi reported: {observed_gpu_names}"
            )
        allowed_pids = self._server_process_group_pids()
        selected_uuid_set = set(selected_uuids)
        apps = [
            app
            for app in self._query_gpu_app_rows()
            if int(app.get("pid", -1)) in allowed_pids
            and str(app.get("gpu_uuid", "")) in selected_uuid_set
        ]
        covered_uuids = {str(app["gpu_uuid"]) for app in apps}
        missing = [
            str(row["index"])
            for row in selected
            if str(row["uuid"]) not in covered_uuids
        ]
        if missing:
            raise RuntimeError(
                f"[{self.name}] Server process tree did not establish CUDA contexts "
                f"on configured GPU indices: {', '.join(missing)}"
            )
        self._deployment_observation = {
            "gpu_coverage_check": "passed",
            "expected_gpu_count": expected_gpu_count,
            "observed_gpu_count": len(covered_uuids),
            "observed_gpu_indices": [int(row["index"]) for row in selected],
            "observed_gpu_uuids": selected_uuids,
            "observed_gpu_names": observed_gpu_names,
            "observed_gpu_total_memory_mib": [
                int(row["total_mib"]) for row in selected
            ],
            "server_compute_process_count": len(
                {int(app.get("pid", -1)) for app in apps}
            ),
        }
        return dict(self._deployment_observation)

    def verify_runtime_integrity(self) -> dict[str, object]:
        return {}

    def _server_process_group_pids(self) -> set[int]:
        process = self._server_process
        if process is None:
            return set()
        try:
            pgid = os.getpgid(process.pid)
        except ProcessLookupError:
            return set()
        pids = {int(process.pid)}
        try:
            result = subprocess.run(
                ["pgrep", "-g", str(pgid)],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            return pids
        if result.returncode not in {0, 1}:
            return pids
        for line in result.stdout.splitlines():
            try:
                pids.add(int(line.strip()))
            except ValueError:
                pass
        pids.update(self._descendant_pids(pids))
        return pids

    @staticmethod
    def _descendant_pids(root_pids: set[int]) -> set[int]:
        if not root_pids:
            return set()
        try:
            result = subprocess.run(
                ["ps", "-eo", "pid=,ppid="],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            return set()
        if result.returncode != 0:
            return set()
        children_by_parent: dict[int, list[int]] = {}
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) != 2:
                continue
            try:
                pid = int(parts[0])
                ppid = int(parts[1])
            except ValueError:
                continue
            children_by_parent.setdefault(ppid, []).append(pid)
        descendants: set[int] = set()
        stack = list(root_pids)
        while stack:
            parent = stack.pop()
            for child in children_by_parent.get(parent, []):
                if child in root_pids or child in descendants:
                    continue
                descendants.add(child)
                stack.append(child)
        return descendants

    def _wait_for_health(self, timeout: int) -> None:
        self._log(f"[{self.name}] Waiting for server to be ready (timeout={timeout}s)...")
        start = time.time()
        last_health_error = ""
        while time.time() - start < timeout:
            ready, health_error = self._check_health_once()
            if ready:
                print(f"[{self.name}] Server ready in {time.time() - start:.1f}s")
                return
            if health_error:
                last_health_error = health_error

            if self._server_process and self._server_process.poll() is not None:
                log_tail = self._server_log_tail()
                raise RuntimeError(
                    f"[{self.name}] Server process exited with code "
                    f"{self._server_process.returncode}.\nLog tail:\n{log_tail}"
                )
            time.sleep(5)
        ready, health_error = self._check_health_once()
        if ready:
            print(f"[{self.name}] Server ready in {time.time() - start:.1f}s")
            return
        if health_error:
            last_health_error = health_error
        log_tail = self._server_log_tail()
        health_detail = f"Last health check: {last_health_error}\n" if last_health_error else ""
        raise TimeoutError(
            f"[{self.name}] Server did not become ready within {timeout}s.\n"
            f"{health_detail}Log tail:\n{log_tail}"
        )

    def _check_health_once(self) -> tuple[bool, str]:
        try:
            resp = httpx.get(f"http://localhost:{self._port}/v1/models", timeout=5)
            if resp.status_code == 200:
                return True, ""
            body = resp.text.replace("\n", " ")[:300]
            return False, f"HTTP {resp.status_code}: {body}"
        except httpx.HTTPError as exc:
            return False, f"{exc.__class__.__name__}: {exc}"

    def _server_log_tail(self, max_chars: int = 12000) -> str:
        try:
            self._log_file.flush()
        except Exception:
            pass
        try:
            with open(self._log_path) as f:
                return f.read()[-max_chars:]
        except Exception:
            return ""

    def stop_server(self) -> None:
        if self._server_process is None:
            return
        port = getattr(self, "_port", None)
        process = self._server_process
        cleanup_pids = self._server_process_group_pids()
        self._log(f"[{self.name}] Stopping server (pid={process.pid})")
        try:
            pgid = os.getpgid(process.pid)
        except ProcessLookupError:
            pgid = None
        try:
            if pgid is not None:
                os.killpg(pgid, signal.SIGTERM)
            else:
                self._signal_processes(cleanup_pids, signal.SIGTERM)
            process.wait(timeout=30)
        except (ProcessLookupError, subprocess.TimeoutExpired):
            try:
                if pgid is not None:
                    os.killpg(pgid, signal.SIGKILL)
                else:
                    self._signal_processes(cleanup_pids, signal.SIGKILL)
                process.wait(timeout=10)
            except (ProcessLookupError, subprocess.TimeoutExpired):
                pass
        self._terminate_surviving_processes(cleanup_pids)
        self._server_process = None
        if hasattr(self, "_log_file") and self._log_file:
            self._log_file.close()
            self._log_file = None
        if isinstance(port, int):
            self._wait_for_port_release(port)
        cleanup_wait_s = float(os.environ.get("INFERENCE_BENCH_PROVIDER_CLEANUP_WAIT_S", "30"))
        if cleanup_wait_s > 0:
            self._log(f"[{self.name}] Waiting {cleanup_wait_s:.1f}s for provider cleanup")
            time.sleep(cleanup_wait_s)

    def _terminate_surviving_processes(self, pids: set[int]) -> None:
        live = self._wait_for_pids_exit(pids, timeout=5.0)
        if not live:
            return
        self._log(
            f"[{self.name}] Terminating surviving server processes: "
            f"{', '.join(str(pid) for pid in sorted(live))}"
        )
        self._signal_processes(live, signal.SIGTERM)
        live = self._wait_for_pids_exit(live, timeout=5.0)
        if not live:
            return
        self._log(
            f"[{self.name}] Killing surviving server processes: "
            f"{', '.join(str(pid) for pid in sorted(live))}"
        )
        self._signal_processes(live, signal.SIGKILL)
        self._wait_for_pids_exit(live, timeout=5.0)

    @classmethod
    def _wait_for_pids_exit(cls, pids: set[int], *, timeout: float) -> set[int]:
        deadline = time.time() + max(0.0, timeout)
        live = cls._live_pids(pids)
        while live and time.time() < deadline:
            time.sleep(min(0.2, max(0.0, deadline - time.time())))
            live = cls._live_pids(live)
        return live

    @staticmethod
    def _live_pids(pids: set[int]) -> set[int]:
        current_pid = os.getpid()
        live: set[int] = set()
        for pid in pids:
            if pid <= 0 or pid == current_pid:
                continue
            try:
                os.kill(pid, 0)
            except ProcessLookupError:
                continue
            except PermissionError:
                live.add(pid)
            else:
                live.add(pid)
        return live

    @staticmethod
    def _signal_processes(pids: set[int], signum: int) -> None:
        current_pid = os.getpid()
        for pid in sorted(pids):
            if pid <= 0 or pid == current_pid:
                continue
            try:
                os.kill(pid, signum)
            except ProcessLookupError:
                pass

    def _wait_for_port_release(self, port: int, timeout: int = 60) -> None:
        start = time.time()
        while time.time() - start < timeout:
            if self._port_can_bind(port):
                return
            time.sleep(1)
        self._log(f"[{self.name}] Port {port} was still busy after {timeout}s")

    @staticmethod
    def _port_can_bind(port: int) -> bool:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("0.0.0.0", port))
            return True
        except OSError:
            return False
        finally:
            sock.close()


def _normalize_git_remote(value: str) -> str:
    normalized = value.strip().removesuffix(".git").rstrip("/")
    if normalized.startswith("git@github.com:"):
        normalized = "https://github.com/" + normalized.removeprefix(
            "git@github.com:"
        )
    return normalized.lower()


def _is_runtime_sensitive_artifact(relative: str) -> bool:
    name = Path(relative).name.lower()
    return (
        Path(name).suffix
        in {".dll", ".dylib", ".pth", ".py", ".pyc", ".pyd", ".pyo", ".so"}
        or re.search(r"\.so(?:\.|$)", name) is not None
    )


def _is_venv_runtime_artifact(path: Path) -> bool:
    name = path.name.lower()
    return (
        path.suffix.lower() in {".dll", ".dylib", ".pth", ".pyd", ".so"}
        or re.search(r"\.so(?:\.|$)", name) is not None
        or name in {"sitecustomize.py", "usercustomize.py"}
    )


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def _git_blob_sha1_file(path: Path) -> str:
    digest = hashlib.sha1()
    size = path.stat().st_size
    digest.update(f"blob {size}\0".encode())
    with path.open("rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


_VERIFIED_FILE_DIGESTS: dict[tuple[str, str, int, int, int, int], str] = {}


def _verified_file_digest(path: Path, algorithm: str) -> str:
    resolved = path.resolve()
    stat = resolved.stat()
    key = (
        str(resolved),
        algorithm,
        stat.st_size,
        stat.st_ino,
        stat.st_mtime_ns,
        stat.st_ctime_ns,
    )
    cached = _VERIFIED_FILE_DIGESTS.get(key)
    if cached is not None:
        return cached
    if algorithm == "sha256":
        digest = _sha256_file(resolved)
    elif algorithm == "git-sha1":
        digest = _git_blob_sha1_file(resolved)
    else:
        raise ValueError(f"unsupported file digest algorithm: {algorithm}")
    _VERIFIED_FILE_DIGESTS[key] = digest
    return digest


def _official_hf_file_metadata(
    model: str,
    revision: str,
) -> dict[str, dict[str, int | str]]:
    token = (
        os.environ.get("HF_TOKEN", "").strip()
        or os.environ.get("HUGGING_FACE_HUB_TOKEN", "").strip()
    )
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    model_path = quote(model, safe="/")
    revision_path = quote(revision, safe="")
    url = (
        f"https://huggingface.co/api/models/{model_path}/revision/{revision_path}"
    )
    try:
        with httpx.Client(follow_redirects=True, timeout=60, trust_env=False) as client:
            response = client.get(
                url,
                params={"blobs": "true"},
                headers=headers,
            )
        response.raise_for_status()
        payload = response.json()
    except (httpx.HTTPError, ValueError) as exc:
        raise RuntimeError(
            f"Could not fetch official Hugging Face metadata for {model}@{revision}"
        ) from exc
    if not isinstance(payload, dict) or payload.get("sha") != revision:
        raise RuntimeError(
            f"Hugging Face did not resolve {model}@{revision} to the pinned commit"
        )
    siblings = payload.get("siblings")
    if not isinstance(siblings, list):
        raise RuntimeError("Hugging Face model metadata omitted the file tree")
    files: dict[str, dict[str, int | str]] = {}
    for sibling in siblings:
        if not isinstance(sibling, dict):
            continue
        filename = sibling.get("rfilename")
        size = sibling.get("size")
        if not isinstance(filename, str) or isinstance(size, bool) or not isinstance(
            size, int
        ):
            continue
        metadata: dict[str, int | str] = {"size": size}
        lfs = sibling.get("lfs")
        if isinstance(lfs, dict) and isinstance(lfs.get("sha256"), str):
            metadata["sha256"] = str(lfs["sha256"])
        elif isinstance(sibling.get("blobId"), str):
            metadata["git_blob_sha1"] = str(sibling["blobId"])
        files[filename] = metadata
    if not files:
        raise RuntimeError("Hugging Face model metadata contained no verifiable files")
    return files


def _verify_official_hf_file(
    path: Path,
    *,
    filename: str,
    official: dict[str, int | str] | None,
) -> dict[str, int | str]:
    if not isinstance(official, dict):
        raise RuntimeError(f"Pinned revision does not contain {filename!r}")
    expected_size = official.get("size")
    if (
        isinstance(expected_size, bool)
        or not isinstance(expected_size, int)
        or path.stat().st_size != expected_size
    ):
        raise RuntimeError(f"Official size check failed for {filename!r}")
    expected_sha256 = official.get("sha256")
    if isinstance(expected_sha256, str):
        actual = _verified_file_digest(path, "sha256")
        if actual != expected_sha256:
            raise RuntimeError(f"Official SHA-256 check failed for {filename!r}")
        return {"size": expected_size, "sha256": actual}
    expected_git_sha1 = official.get("git_blob_sha1")
    if isinstance(expected_git_sha1, str):
        actual = _verified_file_digest(path, "git-sha1")
        if actual != expected_git_sha1:
            raise RuntimeError(f"Official Git blob check failed for {filename!r}")
        return {"size": expected_size, "git_blob_sha1": actual}
    raise RuntimeError(f"Official metadata has no content digest for {filename!r}")


def _server_model_path(model: str, *, revision: str | None = None) -> str:
    override = os.environ.get("INFERENCE_BENCH_SERVER_MODEL", "").strip()
    if override:
        return override
    if not _env_flag("INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT", True):
        return model
    cached = _cached_hf_snapshot(model, revision=revision)
    return str(cached) if cached is not None else model


def _cached_hf_snapshot(model: str, *, revision: str | None = None) -> Path | None:
    candidate = Path(model).expanduser()
    if candidate.exists():
        return None
    repo_cache_name = f"models--{model.replace('/', '--')}"
    for cache_root in _hf_cache_roots():
        repo_cache = cache_root / repo_cache_name
        snapshots = repo_cache / "snapshots"
        if not snapshots.exists():
            continue
        if revision:
            snapshot = snapshots / revision
            if snapshot.is_dir() and _snapshot_has_model_files(snapshot):
                return snapshot
            continue
        for snapshot in _snapshot_candidates(repo_cache):
            if _snapshot_has_model_files(snapshot):
                return snapshot
    return None


def _hf_cache_roots() -> list[Path]:
    roots: list[Path] = []
    for name in ("HUGGINGFACE_HUB_CACHE", "HF_HUB_CACHE"):
        raw = os.environ.get(name, "").strip()
        if raw:
            roots.append(Path(raw).expanduser())
    hf_home = os.environ.get("HF_HOME", "").strip()
    if hf_home:
        roots.append(Path(hf_home).expanduser() / "hub")
    roots.append(Path.home() / ".cache" / "huggingface" / "hub")

    deduped: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        key = root.resolve() if root.exists() else root
        if key in seen:
            continue
        seen.add(key)
        deduped.append(root)
    return deduped


def _snapshot_candidates(repo_cache: Path) -> list[Path]:
    snapshots = repo_cache / "snapshots"
    refs_main = repo_cache / "refs" / "main"
    if refs_main.is_file():
        snapshot = snapshots / refs_main.read_text().strip()
        if snapshot.exists():
            return [snapshot]
    return sorted(
        (path for path in snapshots.iterdir() if path.is_dir()),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )


def _snapshot_has_model_files(snapshot: Path) -> bool:
    if not (snapshot / "config.json").exists():
        return False
    return bool(_snapshot_weight_files(snapshot))


def _snapshot_weight_files(snapshot: Path) -> list[Path]:
    for index_name in ("model.safetensors.index.json", "pytorch_model.bin.index.json"):
        index_path = snapshot / index_name
        if index_path.exists():
            try:
                index = json.loads(index_path.read_text())
            except json.JSONDecodeError:
                return []
            weight_map = index.get("weight_map", {})
            if not isinstance(weight_map, dict):
                return []
            files = {str(filename) for filename in weight_map.values()}
            paths = [snapshot / filename for filename in sorted(files)]
            return paths if paths and all(path.exists() for path in paths) else []
    for filename in ("model.safetensors", "pytorch_model.bin"):
        path = snapshot / filename
        if path.exists():
            return [path]
    return []


class _GpuIsolationMonitor:
    def __init__(self, provider: Provider, tp: int):
        self.provider = provider
        self.tp = tp
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._contaminating_apps: list[str] = []
        self._monitor_error: Exception | None = None

    def __enter__(self) -> "_GpuIsolationMonitor":
        if not _env_flag("INFERENCE_BENCH_GPU_ISOLATION_CHECK", True):
            if self.provider.is_scored_evaluation:
                raise RuntimeError(
                    f"[{self.provider.name}] GPU isolation monitoring cannot be "
                    "disabled for a scored evaluation"
                )
            return self
        poll_s = _env_float("INFERENCE_BENCH_GPU_ISOLATION_MONITOR_POLL_S", 1.0, minimum=0.25)

        def _run() -> None:
            while not self._stop.wait(poll_s):
                try:
                    apps = self.provider._external_gpu_apps(self.tp)
                except Exception as exc:
                    self._monitor_error = exc
                    self.provider._log(
                        f"[{self.provider.name}] GPU isolation monitoring failed: {exc}"
                    )
                    return
                if apps:
                    self._contaminating_apps = apps
                    self.provider._log(
                        f"[{self.provider.name}] GPU isolation violation: {apps[0]}"
                    )
                    return

        self._thread = threading.Thread(target=_run, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=2.0)
        if exc_type is None and self._contaminating_apps:
            detail = "\n".join(self._contaminating_apps)
            raise RuntimeError(f"GPU isolation was violated during benchmark.\n{detail}")
        if exc_type is None and self._monitor_error is not None:
            raise RuntimeError(
                "GPU isolation could not be verified during benchmark: "
                f"{self._monitor_error}"
            ) from self._monitor_error
        return False
