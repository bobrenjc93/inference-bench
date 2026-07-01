from __future__ import annotations

import json
from pathlib import Path

from inference_bench.providers.sglang import SglangProvider
from inference_bench.providers.torchinferno import TorchInfernoProvider
from inference_bench.providers.vllm import VllmProvider


def test_providers_launch_cached_hf_snapshot_with_served_model_alias(
    tmp_path,
    monkeypatch,
) -> None:
    model = "org/model"
    snapshot = _write_hf_snapshot(tmp_path / "hf", model)
    _isolate_hf_cache_env(monkeypatch, tmp_path / "hf")

    torchinferno_cmd = TorchInfernoProvider(build_dir=str(tmp_path))._server_cmd(
        model,
        tp=8,
        port=9000,
    )
    vllm_cmd = VllmProvider(build_dir=str(tmp_path))._server_cmd(model, tp=8, port=9001)
    sglang_cmd = SglangProvider(build_dir=str(tmp_path))._server_cmd(model, tp=8, port=9002)

    assert _arg_value(torchinferno_cmd, "--model") == str(snapshot)
    assert _arg_value(vllm_cmd, "--model") == str(snapshot)
    assert _arg_value(vllm_cmd, "--served-model-name") == model
    assert _arg_value(sglang_cmd, "--model-path") == str(snapshot)
    assert _arg_value(sglang_cmd, "--served-model-name") == model


def test_cached_hf_snapshot_can_be_disabled(tmp_path, monkeypatch) -> None:
    model = "org/model"
    _write_hf_snapshot(tmp_path / "hf", model)
    _isolate_hf_cache_env(monkeypatch, tmp_path / "hf")
    monkeypatch.setenv("INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT", "0")

    cmd = VllmProvider(build_dir=str(tmp_path))._server_cmd(model, tp=8, port=9000)

    assert _arg_value(cmd, "--model") == model
    assert "--served-model-name" not in cmd


def test_provider_python_override_controls_server_command(tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("INFERENCE_BENCH_VLLM_PYTHON", "/opt/vllm/bin/python")
    monkeypatch.setenv("INFERENCE_BENCH_SGLANG_PYTHON", "/opt/sglang/bin/python")
    monkeypatch.setenv("INFERENCE_BENCH_TORCHINFERNO_PYTHON", "/opt/ti/bin/python")
    monkeypatch.setenv("INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT", "0")

    model = "org/model"

    assert VllmProvider(build_dir=str(tmp_path))._server_cmd(model, tp=8, port=9001)[0] == (
        "/opt/vllm/bin/python"
    )
    assert SglangProvider(build_dir=str(tmp_path))._server_cmd(model, tp=8, port=9002)[0] == (
        "/opt/sglang/bin/python"
    )
    assert TorchInfernoProvider(build_dir=str(tmp_path))._server_cmd(
        model,
        tp=8,
        port=9000,
    )[0] == "/opt/ti/bin/python"


def _write_hf_snapshot(hf_home: Path, model: str) -> Path:
    commit = "a" * 40
    repo_cache = hf_home / "hub" / f"models--{model.replace('/', '--')}"
    snapshot = repo_cache / "snapshots" / commit
    shard = "model-00001-of-00001.safetensors"
    snapshot.mkdir(parents=True)
    refs = repo_cache / "refs"
    refs.mkdir()
    (refs / "main").write_text(commit)
    (snapshot / "config.json").write_text("{}\n")
    (snapshot / shard).write_text("")
    (snapshot / "model.safetensors.index.json").write_text(
        json.dumps({"weight_map": {"weight": shard}}) + "\n"
    )
    return snapshot


def _isolate_hf_cache_env(monkeypatch, hf_home: Path) -> None:
    monkeypatch.setenv("HF_HOME", str(hf_home))
    monkeypatch.delenv("HUGGINGFACE_HUB_CACHE", raising=False)
    monkeypatch.delenv("HF_HUB_CACHE", raising=False)
    monkeypatch.delenv("INFERENCE_BENCH_SERVER_MODEL", raising=False)
    monkeypatch.delenv("INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT", raising=False)


def _arg_value(cmd: list[str], name: str) -> str:
    return cmd[cmd.index(name) + 1]
