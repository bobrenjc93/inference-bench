from __future__ import annotations

import asyncio
import json
import os
import signal
import socket
import subprocess
import sys
import time
import types
from pathlib import Path
from unittest import mock

import httpx
import pytest

from inference_bench.config import Config, SCORED_BENCHMARKS, SCORED_PROVIDERS
from inference_bench.deployment import DISAGGREGATED_PREFILL_DECODE
from inference_bench.integrity import REQUIRED_RUNTIME_COUNTERS
from inference_bench.disaggregated_launcher import _Component
from inference_bench.providers.sglang import SglangProvider
from inference_bench.providers.torchinferno import TorchInfernoProvider
from inference_bench.providers.vllm import VllmProvider
from inference_bench.vllm_disagg_protocol import make_prefill_request
from inference_bench.vllm_mooncake_proxy import _decode_body, _prefill_body
from inference_bench import vllm_disagg_proxy


@pytest.fixture(autouse=True)
def _pinned_test_snapshot(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    snapshot = tmp_path / ("a" * 40)
    snapshot.mkdir(exist_ok=True)
    monkeypatch.setattr(
        "inference_bench.providers.base._cached_hf_snapshot",
        lambda _model, *, revision=None: snapshot,
    )


def _configure_disaggregated(provider) -> None:  # noqa: ANN001
    provider.configure_deployment(
        deployment_mode=DISAGGREGATED_PREFILL_DECODE,
        tensor_parallel_size=4,
        prefill_tensor_parallel_size=4,
        decode_tensor_parallel_size=4,
        model_revision="a" * 40,
    )


def _read_spec(command: list[str]) -> dict:
    return json.loads(Path(command[-1]).read_text())


def _free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def _write_mooncake_rdma_logs(
    build_dir: Path,
    *,
    provider: str,
    metrics: str = "",
) -> None:
    common = (
        "Topology discovery complete. Found 4 HCAs.\n"
        "installTransport, type=rdma\n"
    )
    if provider == "sglang":
        common += "All Reduce config: local_buffer = 8.00 MB\n"
    (build_dir / f"{provider}_disagg_prefill.log").write_text(common + metrics)
    (build_dir / f"{provider}_disagg_decode.log").write_text(common)


def test_v3_config_uses_standard_tp4_and_results_v2() -> None:
    config = Config.load(Path(__file__).parents[1] / "config_v3.yaml")

    assert config.evaluation_version == 3
    assert config.deployment_mode == "standard"
    assert config.role_tensor_parallel_sizes == (None, None)
    assert config.tensor_parallel_size == 4
    assert config.gpu_count == 4
    assert config.results_dir == "./results/v2"
    assert config.minimum_correctness_rate == 0.95
    assert config.require_request_count_parity
    assert config.output_token_ratio_tolerance == 0.10
    assert config.retain_response_text
    assert config.authoritative_output_token_count
    assert config.model_revision == "1605565b47bb9346c5515c34102e054115b4f98b"


def test_v4_config_uses_two_tp4_roles_and_results_v3() -> None:
    config = Config.load(Path(__file__).parents[1] / "config_v4.yaml")

    assert config.evaluation_version == 4
    assert config.deployment_mode == DISAGGREGATED_PREFILL_DECODE
    assert config.role_tensor_parallel_sizes == (4, 4)
    assert config.tensor_parallel_size == 4
    assert config.gpu_count == 8
    assert config.results_dir == "./results/v3"
    assert config.minimum_correctness_rate == 0.95
    assert config.require_request_count_parity
    assert config.output_token_ratio_tolerance == 0.10
    assert config.retain_response_text
    assert config.authoritative_output_token_count
    assert config.model_revision == "1605565b47bb9346c5515c34102e054115b4f98b"


def test_disaggregated_config_requires_pinned_model_revision() -> None:
    with pytest.raises(ValueError, match="requires a pinned 40-character"):
        Config(
            evaluation_version=4,
        )


def test_vllm_prefill_request_limits_both_openai_token_fields() -> None:
    original = {
        "model": "model",
        "messages": [{"role": "user", "content": "unseen"}],
        "max_tokens": 17,
        "max_completion_tokens": 19,
        "stream": True,
    }

    prefill = make_prefill_request(original)

    assert prefill["max_tokens"] == 1
    assert prefill["max_completion_tokens"] == 1
    assert prefill["stream"] is True
    assert original["max_tokens"] == 17


def test_vllm_mooncake_proxy_sets_upstream_transfer_contract() -> None:
    original = {
        "messages": [{"role": "user", "content": "unseen"}],
        "max_tokens": 17,
        "stream": True,
    }

    prefill = _prefill_body(original, "xfer-id")
    decode = _decode_body(
        original,
        transfer_id="xfer-id",
        bootstrap_address="http://127.0.0.1:8300",
        engine_id="engine-id",
    )

    assert prefill["max_tokens"] == 1
    assert prefill["stream"] is False
    assert prefill["kv_transfer_params"] == {
        "do_remote_decode": True,
        "do_remote_prefill": False,
        "transfer_id": "xfer-id",
    }
    assert decode["stream"] is True
    assert decode["kv_transfer_params"] == {
        "do_remote_decode": False,
        "do_remote_prefill": True,
        "remote_bootstrap_addr": "http://127.0.0.1:8300",
        "remote_engine_id": "engine-id",
        "transfer_id": "xfer-id",
    }
    assert original["max_tokens"] == 17


def test_vllm_model_probe_does_not_count_as_prefill_decode_pair() -> None:
    class FakeResponse:
        status = 200
        headers = {"content-type": "application/json"}

        async def read(self) -> bytes:
            return b'{"data": []}'

    class ResponseContext:
        async def __aenter__(self) -> FakeResponse:
            return FakeResponse()

        async def __aexit__(self, *_args) -> None:  # noqa: ANN002
            return None

    session = types.SimpleNamespace(get=lambda *_args, **_kwargs: ResponseContext())
    request = types.SimpleNamespace(
        app=types.SimpleNamespace(state=types.SimpleNamespace(session=session)),
        headers={},
    )
    registry = mock.Mock()
    registry.decode_http_address.return_value = "127.0.0.1:8100"
    audit = vllm_disagg_proxy._RequestAudit()

    with (
        mock.patch.object(vllm_disagg_proxy, "_registry", registry),
        mock.patch.object(vllm_disagg_proxy, "_audit", audit),
    ):
        response = asyncio.run(vllm_disagg_proxy.models(request))

    assert response.status_code == 200
    assert audit.snapshot()["request_pairs"] == 0


def test_config_rejects_role_specific_tp_fields(tmp_path: Path) -> None:
    path = tmp_path / "config.yaml"
    path.write_text(
        "evaluation_version: 4\n"
        f"model_revision: {'a' * 40}\n"
        "prefill_tensor_parallel_size: 1\n"
    )

    with pytest.raises(ValueError, match="prefill_tensor_parallel_size"):
        Config.load(path)


@pytest.mark.parametrize(
    "field",
    [
        "tensor_parallel_size: 4",
        "results_dir: ./results/v3",
        "minimum_correctness_rate: null",
        "require_request_count_parity: false",
        "output_token_ratio_tolerance: null",
        "retain_response_text: false",
        "authoritative_output_token_count: false",
    ],
)
def test_scored_config_rejects_version_derived_fields(
    tmp_path: Path,
    field: str,
) -> None:
    path = tmp_path / "config.yaml"
    path.write_text(
        "evaluation_version: 4\n"
        f"model_revision: {'a' * 40}\n"
        f"{field}\n"
    )

    with pytest.raises(ValueError, match="version-derived"):
        Config.load(path)


def test_config_rejects_explicit_deployment_mode(tmp_path: Path) -> None:
    path = tmp_path / "config.yaml"
    path.write_text(
        "evaluation_version: 4\n"
        f"model_revision: {'a' * 40}\n"
        "deployment_mode: standard\n"
    )

    with pytest.raises(ValueError, match="deployment_mode"):
        Config.load(path)


def test_config_rejects_missing_explicit_path(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="does not exist"):
        Config.load(tmp_path / "config_v4.yam")


@pytest.mark.parametrize("version", [3.9, 4.1, "4", True])
def test_config_rejects_non_integer_evaluation_versions(version) -> None:
    with pytest.raises(ValueError, match="must be an integer"):
        Config(evaluation_version=version)


def test_scored_version_rejects_mismatched_results_namespace() -> None:
    with pytest.raises(ValueError, match="results must be written to ./results/v2"):
        Config(
            evaluation_version=3,
            model_revision="a" * 40,
            results_dir="./results/v3",
        )


def test_scored_results_root_is_anchored_to_harness_checkout(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    config = Config.load(Path(__file__).parents[1] / "config_v3.yaml")
    monkeypatch.chdir(tmp_path)

    assert Path(config.resolved_results_dir) == (
        Path(__file__).parents[1] / "results" / "v2"
    ).resolve()


def test_scored_version_rejects_tensor_parallel_override() -> None:
    config = Config(
        evaluation_version=3,
        model_revision="a" * 40,
        hardware="4xH100",
        providers=list(SCORED_PROVIDERS),
        benchmarks=list(SCORED_BENCHMARKS),
    )

    with pytest.raises(ValueError, match="topology is implicit"):
        config.apply_overrides(tp=8)


@pytest.mark.parametrize(("version", "tp"), [(3, 8), (4, 1)])
def test_scored_version_rejects_noncanonical_topology(version: int, tp: int) -> None:
    with pytest.raises(ValueError, match="requires tensor parallel size"):
        Config(
            evaluation_version=version,
            model_revision="a" * 40,
            tensor_parallel_size=tp,
            hardware="8xH100",
            providers=list(SCORED_PROVIDERS),
            benchmarks=list(SCORED_BENCHMARKS),
        )


def test_scored_version_rejects_provider_or_benchmark_subsets() -> None:
    config = Config(
        evaluation_version=3,
        model_revision="a" * 40,
        hardware="4xH100",
        providers=list(SCORED_PROVIDERS),
        benchmarks=list(SCORED_BENCHMARKS),
    )

    with pytest.raises(ValueError, match="requires providers"):
        config.apply_overrides(providers=["torchinferno"])

    config = Config(
        evaluation_version=3,
        model_revision="a" * 40,
        hardware="4xH100",
        providers=list(SCORED_PROVIDERS),
        benchmarks=list(SCORED_BENCHMARKS),
    )
    with pytest.raises(ValueError, match="complete canonical benchmark suite"):
        config.apply_overrides(benchmarks=["multi_turn"])


def test_scored_version_rejects_http_concurrency_overrides(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("INFERENCE_BENCH_HTTP_MAX_CONNECTIONS", "1")

    with pytest.raises(ValueError, match="HTTP concurrency overrides"):
        Config.load(Path(__file__).parents[1] / "config_v3.yaml")


def test_gpu_roles_use_disjoint_visible_device_sets(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with mock.patch.dict(
        os.environ,
        {"CUDA_VISIBLE_DEVICES": "GPU-a,GPU-b,GPU-c,GPU-d,GPU-e,GPU-f,GPU-g,GPU-h"},
        clear=True,
    ), mock.patch.object(provider, "_query_gpu_memory", return_value=[]):
        prefill_env, decode_env = provider._disaggregated_gpu_envs()

    assert prefill_env["CUDA_VISIBLE_DEVICES"] == "GPU-a,GPU-b,GPU-c,GPU-d"
    assert decode_env["CUDA_VISIBLE_DEVICES"] == "GPU-e,GPU-f,GPU-g,GPU-h"


def test_disaggregated_roles_reject_duplicate_visible_devices(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(
            os.environ,
            {"CUDA_VISIBLE_DEVICES": "0,1,2,3,0,1,2,3"},
            clear=True,
        ),
        pytest.raises(ValueError, match="distinct CUDA_VISIBLE_DEVICES"),
    ):
        provider._disaggregated_gpu_envs()


def test_gpu_coverage_requires_all_selected_devices(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    gpu_rows = [
        {"index": 0, "uuid": "GPU-a", "total_mib": 100, "free_mib": 90},
        {"index": 1, "uuid": "GPU-b", "total_mib": 100, "free_mib": 90},
    ]
    app_rows = [
        {
            "raw": "10, python, GPU-a, 10",
            "pid": 10,
            "process_name": "python",
            "gpu_uuid": "GPU-a",
            "used_memory_mib": 10,
        }
    ]
    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(provider, "_query_gpu_memory", return_value=gpu_rows),
        mock.patch.object(provider, "_query_gpu_app_rows", return_value=app_rows),
        mock.patch.object(provider, "_server_process_group_pids", return_value={10}),
        pytest.raises(RuntimeError, match="GPU indices: 1"),
    ):
        provider.verify_gpu_coverage(2)


def test_disaggregated_run_cannot_disable_gpu_coverage(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_GPU_COVERAGE_CHECK": "0"},
            clear=True,
        ),
        pytest.raises(RuntimeError, match="cannot be disabled"),
    ):
        provider.verify_gpu_coverage(8)


def test_disaggregated_run_requires_nvidia_smi_coverage_data(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(provider, "_query_gpu_memory", return_value=[]),
        pytest.raises(RuntimeError, match="nvidia-smi GPU coverage data is required"),
    ):
        provider.verify_gpu_coverage(8)


def test_disaggregated_run_cannot_disable_gpu_isolation(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_GPU_ISOLATION_CHECK": "0"},
            clear=True,
        ),
        pytest.raises(RuntimeError, match="cannot be disabled"),
    ):
        provider.wait_for_gpu_isolation(8)

    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_GPU_ISOLATION_CHECK": "0"},
            clear=True,
        ),
        pytest.raises(RuntimeError, match="cannot be disabled"),
    ):
        with provider.gpu_isolation_monitor(8):
            pass


def test_disaggregated_h100_label_requires_observed_h100s(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    provider.hardware = "8xH100"
    rows = [
        {
            "index": index,
            "uuid": f"GPU-{index}",
            "name": "NVIDIA A100-SXM4-80GB",
            "total_mib": 81920,
            "free_mib": 80000,
        }
        for index in range(8)
    ]

    with (
        mock.patch.object(provider, "_query_gpu_memory", return_value=rows),
        pytest.raises(RuntimeError, match="requires H100 GPUs"),
    ):
        provider.verify_gpu_coverage(8)


def test_torchinferno_disaggregated_command_uses_native_mode(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    command = provider._server_cmd("model", tp=4, port=8001)

    assert command[command.index("--tensor-parallel-size") + 1] == "4"
    assert command[command.index("--disaggregation-mode") + 1] == "prefill-decode"
    assert Path(command[command.index("--model") + 1]).name == "a" * 40
    spec_path = Path(provider.extra_log_paths()["deployment_spec"])
    assert json.loads(spec_path.read_text())["command"] == command


def test_torchinferno_v4_build_installs_extra_and_prepares_tp4_artifacts(
    tmp_path: Path,
) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    provider.hardware = "8xH100"
    provider.configure_deployment(
        deployment_mode=DISAGGREGATED_PREFILL_DECODE,
        tensor_parallel_size=4,
        prefill_tensor_parallel_size=4,
        decode_tensor_parallel_size=4,
        model_revision="a" * 40,
        model="deepseek-ai/DeepSeek-V4-Flash",
    )
    snapshot = tmp_path / ("a" * 40)

    def prepare(command, **kwargs):  # noqa: ANN001, ANN003
        artifact_root = Path(command[3])
        (artifact_root / "tilelang").mkdir(parents=True)
        (artifact_root / "marlin").mkdir()
        assert kwargs["cwd"] == provider.repo_dir
        assert command[-2:] == ["--tensor-parallel-sizes", "4"]
        return mock.Mock(returncode=0)

    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(provider, "_create_venv"),
        mock.patch.object(provider, "_pip_install") as pip_install,
        mock.patch(
            "inference_bench.providers.torchinferno._cached_hf_snapshot",
            return_value=snapshot,
        ),
        mock.patch(
            "inference_bench.providers.torchinferno.subprocess.run",
            side_effect=prepare,
        ),
    ):
        provider.build()
        provider.prepare_model_assets("deepseek-ai/DeepSeek-V4-Flash")
        env = provider._server_env()

    pip_install.assert_has_calls(
        [
            mock.call("--upgrade", "pip"),
            mock.call(
                "-e",
                ".[serve,deepseek-v4,h100]",
                cwd=provider.repo_dir,
            ),
        ]
    )
    assert "flashinfer" not in str(pip_install.call_args_list)
    assert env["TORCHINFERNO_V4_KERNEL_ARTIFACT_DIR"].endswith(
        "deepseek-v4/tilelang"
    )
    assert env["TVM_FFI_CACHE_DIR"].endswith("deepseek-v4/marlin")
    assert env["CUDA_HOME"] == "/does/not/exist"
    assert env["TORCHINFERNO_OPENAI_DISAGG_MAX_BATCH_SIZE"] == "64"


def test_torchinferno_v4_rejects_external_artifact_paths(tmp_path: Path) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    provider.configure_deployment(
        deployment_mode=DISAGGREGATED_PREFILL_DECODE,
        tensor_parallel_size=4,
        prefill_tensor_parallel_size=4,
        decode_tensor_parallel_size=4,
        model_revision="a" * 40,
        model="deepseek-ai/DeepSeek-V4-Flash",
    )

    with (
        mock.patch.dict(
            os.environ,
            {"TORCHINFERNO_V4_KERNEL_ARTIFACT_DIR": "/tmp/unverified"},
            clear=True,
        ),
        pytest.raises(ValueError, match="override is prohibited"),
    ):
        provider.prepare_model_assets("deepseek-ai/DeepSeek-V4-Flash")


def test_torchinferno_disaggregated_mode_rejects_logits_cache_override(
    tmp_path: Path,
) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_TORCHINFERNO_ALLOW_LOGITS_CACHES": "1"},
            clear=True,
        ),
        pytest.raises(ValueError, match="prohibited"),
    ):
        provider._server_env()


def test_scored_disaggregated_mode_requires_pinned_cached_snapshot(
    tmp_path: Path,
) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT": "0"},
            clear=True,
        ),
        pytest.raises(ValueError, match="is prohibited"),
    ):
        provider._server_cmd("model", tp=4, port=8001)


def test_scored_disaggregated_mode_rejects_local_torchinferno_repo(
    tmp_path: Path,
) -> None:
    with mock.patch.dict(
        os.environ,
        {"TORCHINFERNO_LOCAL_REPO": str(tmp_path / "local")},
        clear=True,
    ):
        provider = TorchInfernoProvider(build_dir=str(tmp_path / "build"))
        _configure_disaggregated(provider)
        with pytest.raises(RuntimeError, match="LOCAL_REPO is prohibited"):
            provider.clone()


def test_scored_server_env_rejects_inherited_transport_selectors(
    tmp_path: Path,
) -> None:
    provider = SglangProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    inherited = {
        "MC_FORCE_TCP": "1",
        "MC_INTRANODE_NVLINK": "true",
        "MOONCAKE_PROTOCOL": "tcp",
        "VLLM_MOONCAKE_BOOTSTRAP_PORT": "1234",
        "SGLANG_MOONCAKE_CUSTOM_MEM_POOL": "NVLINK",
        "USE_BAREX": "1",
    }

    with (
        mock.patch.dict(os.environ, inherited, clear=True),
        pytest.raises(ValueError, match="Environment override is prohibited"),
    ):
        provider._server_env()


@pytest.mark.parametrize(
    ("provider_cls", "env_name"),
    [
        (VllmProvider, "INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION"),
        (SglangProvider, "INFERENCE_BENCH_SGLANG_MEM_FRACTION_STATIC"),
        (SglangProvider, "SGLANG_ATTENTION_BACKEND"),
        (TorchInfernoProvider, "TORCHINFERNO_OPENAI_TP_ONLINE_CONTINUOUS"),
    ],
)
def test_standard_v3_rejects_runtime_environment_overrides(
    tmp_path: Path,
    provider_cls,
    env_name: str,
) -> None:
    provider = provider_cls(build_dir=str(tmp_path))
    provider.configure_deployment(
        deployment_mode="standard",
        tensor_parallel_size=4,
        model_revision="a" * 40,
        model="model",
        evaluation_version=3,
    )

    with (
        mock.patch.dict(os.environ, {env_name: "1"}, clear=True),
        pytest.raises(ValueError, match="Environment override is prohibited"),
    ):
        if provider_cls is TorchInfernoProvider:
            provider._server_env()
        else:
            provider._server_cmd("model", tp=4, port=8001)


def test_standard_v3_scrubs_native_vllm_runtime_environment(tmp_path: Path) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    provider.configure_deployment(
        deployment_mode="standard",
        tensor_parallel_size=4,
        model_revision="a" * 40,
        model="model",
        evaluation_version=3,
    )

    with mock.patch.dict(os.environ, {"VLLM_USE_V1": "0"}, clear=True):
        env = provider._server_env()

    assert "VLLM_USE_V1" not in env


def test_torchinferno_attestation_is_provenance_not_runtime_evidence(
    tmp_path: Path,
) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with mock.patch.dict(os.environ, {}, clear=True):
        provider._server_env()

    queue_path = Path(provider.extra_log_paths()["queue_profile"])
    attestation = json.loads(queue_path.read_text())
    assert attestation["expected_tensor_parallel_size_per_role"] == 4
    assert attestation["expected_world_size"] == 8
    assert attestation["configured_disaggregated_max_batch_size"] == 128
    assert not any(key.startswith("runtime_") for key in attestation)


def test_standard_v3_requires_and_accepts_runtime_cache_counters(
    tmp_path: Path,
) -> None:
    provider = TorchInfernoProvider(build_dir=str(tmp_path))
    provider.configure_deployment(
        deployment_mode="standard",
        tensor_parallel_size=4,
        model_revision="a" * 40,
        model="model",
        evaluation_version=3,
    )
    profile_path = tmp_path / "queue_profile.jsonl"
    profile_path.write_text(
        json.dumps(
            {
                "event": "stream_group",
                **{name: 0 for name in REQUIRED_RUNTIME_COUNTERS},
            }
        )
        + "\n"
    )
    provider._extra_log_paths["queue_profile"] = str(profile_path)

    assert provider.verify_runtime_integrity() == {
        "cache_integrity_check": "passed",
        "runtime_shortcut_counters": "zero",
    }


@pytest.mark.parametrize(
    ("provider_cls", "env_name", "override", "message"),
    [
        (
            TorchInfernoProvider,
            "TORCHINFERNO_SERVER_ARGS",
            "--disaggregation-mode=none",
            "is prohibited",
        ),
        (
            VllmProvider,
            "INFERENCE_BENCH_VLLM_SERVER_ARGS",
            "--kv-transfer-config={}",
            "is prohibited",
        ),
        (
            SglangProvider,
            "INFERENCE_BENCH_SGLANG_SERVER_ARGS",
            "--disaggregation-transfer-backend=fake",
            "is prohibited",
        ),
        (
            VllmProvider,
            "INFERENCE_BENCH_VLLM_SERVER_ARGS",
            "--dtype=float16",
            "is prohibited",
        ),
        (
            SglangProvider,
            "INFERENCE_BENCH_SGLANG_SERVER_ARGS",
            "--dtype=float16",
            "is prohibited",
        ),
        (
            TorchInfernoProvider,
            "TORCHINFERNO_SERVER_ARGS",
            "--tokenizer=/tmp/alternate",
            "is prohibited",
        ),
        (
            SglangProvider,
            "INFERENCE_BENCH_SGLANG_SERVER_ARGS",
            "--model=/tmp/alternate",
            "is prohibited",
        ),
        (
            SglangProvider,
            "INFERENCE_BENCH_SGLANG_SERVER_ARGS",
            "--tensor-parallel-size=8",
            "is prohibited",
        ),
        (
            VllmProvider,
            "INFERENCE_BENCH_VLLM_SERVER_ARGS",
            "-q=awq",
            "is prohibited",
        ),
        (
            VllmProvider,
            "INFERENCE_BENCH_VLLM_SERVER_ARGS",
            "--logits-processors=custom.module:Processor",
            "is prohibited",
        ),
    ],
)
def test_disaggregated_cli_equals_overrides_are_rejected(
    tmp_path: Path,
    provider_cls,
    env_name: str,
    override: str,
    message: str,
) -> None:  # noqa: ANN001
    provider = provider_cls(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    with (
        mock.patch.dict(os.environ, {env_name: override}, clear=True),
        mock.patch.object(
            provider,
            "_reserve_local_ports",
            return_value=[8100, 8200, 8300],
        ),
        mock.patch.object(provider, "_reserve_local_port_block", return_value=8400),
        pytest.raises(ValueError, match=message),
    ):
        provider._server_cmd("model", tp=4, port=8001)


def test_vllm_disaggregated_spec_uses_p2p_nccl_and_split_gpus(
    tmp_path: Path,
) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(
            provider,
            "_reserve_local_ports",
            return_value=[8100, 8200, 8300],
        ),
        mock.patch.object(provider, "_reserve_local_port_block", return_value=8400),
    ):
        command = provider._server_cmd("model", tp=4, port=8001)

    spec = _read_spec(command)
    proxy = spec["phases"][0]["components"][0]
    prefill, decode = spec["phases"][1]["components"]
    prefill_command = prefill["command"]
    decode_command = decode["command"]
    prefill_transfer = json.loads(
        prefill_command[prefill_command.index("--kv-transfer-config") + 1]
    )
    decode_transfer = json.loads(
        decode_command[decode_command.index("--kv-transfer-config") + 1]
    )

    assert spec["transport"] == "P2pNcclConnector"
    assert proxy["command"][proxy["command"].index("--port") + 1] == "8001"
    assert prefill["env"]["CUDA_VISIBLE_DEVICES"] == "0,1,2,3"
    assert decode["env"]["CUDA_VISIBLE_DEVICES"] == "4,5,6,7"
    assert prefill_command[prefill_command.index("--tensor-parallel-size") + 1] == "4"
    assert decode_command[decode_command.index("--tensor-parallel-size") + 1] == "4"
    assert Path(prefill_command[prefill_command.index("--model") + 1]).name == "a" * 40
    assert Path(decode_command[decode_command.index("--model") + 1]).name == "a" * 40
    assert prefill_command[prefill_command.index("--gpu-memory-utilization") + 1] == "0.90"
    assert decode_command[decode_command.index("--gpu-memory-utilization") + 1] == "0.70"
    assert prefill_transfer["kv_role"] == "kv_producer"
    assert decode_transfer["kv_role"] == "kv_consumer"
    assert prefill_transfer["kv_connector"] == "P2pNcclConnector"
    assert decode_transfer["kv_connector"] == "P2pNcclConnector"
    assert "--compilation-config" not in prefill_command
    assert "--compilation-config" not in decode_command


def test_vllm_v4_disaggregated_spec_uses_hma_mooncake_connector(
    tmp_path: Path,
) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    provider.configure_deployment(
        deployment_mode=DISAGGREGATED_PREFILL_DECODE,
        tensor_parallel_size=4,
        prefill_tensor_parallel_size=4,
        decode_tensor_parallel_size=4,
        model_revision="a" * 40,
        model="deepseek-ai/DeepSeek-V4-Flash",
    )
    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(
            provider,
            "_reserve_local_ports",
            return_value=[8100, 8200, 8300],
        ),
    ):
        command = provider._server_cmd(
            "deepseek-ai/DeepSeek-V4-Flash",
            tp=4,
            port=8001,
        )

    spec = _read_spec(command)
    prefill, decode = spec["phases"][0]["components"]
    proxy = spec["phases"][1]["components"][0]
    prefill_transfer = json.loads(
        prefill["command"][prefill["command"].index("--kv-transfer-config") + 1]
    )
    decode_transfer = json.loads(
        decode["command"][decode["command"].index("--kv-transfer-config") + 1]
    )

    assert spec["transport"] == "MooncakeConnector"
    assert spec["mooncake_protocol"] == "rdma"
    assert spec["mooncake_data_plane_transport"] == "rdma"
    assert prefill_transfer == {
        "kv_connector": "MooncakeConnector",
        "kv_role": "kv_producer",
        "kv_connector_extra_config": {"mooncake_protocol": "rdma"},
    }
    assert decode_transfer == {
        "kv_connector": "MooncakeConnector",
        "kv_role": "kv_consumer",
        "kv_connector_extra_config": {"mooncake_protocol": "rdma"},
    }
    assert "--compilation-config" not in prefill["command"]
    assert "--compilation-config" not in decode["command"]
    assert prefill["env"]["VLLM_MOONCAKE_BOOTSTRAP_PORT"] == "8300"
    for component in (prefill, decode):
        assert component["env"]["MC_FORCE_HCA"] == "1"
        assert component["env"]["MC_LOG_LEVEL"] == "INFO"
        assert component["env"]["MC_RPC_PROTOCOL"] == "tcp"
        assert component["env"]["MOONCAKE_PROTOCOL"] == "rdma"
        assert "MC_INTRANODE_NVLINK" not in component["env"]
    assert "vllm_mooncake_proxy.py" in proxy["command"][1]
    assert proxy["command"][proxy["command"].index("--bootstrap-port") + 1] == "8300"


def test_vllm_v4_build_pins_cuda13_mooncake_dependency(tmp_path: Path) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    provider.configure_deployment(
        deployment_mode=DISAGGREGATED_PREFILL_DECODE,
        tensor_parallel_size=4,
        prefill_tensor_parallel_size=4,
        decode_tensor_parallel_size=4,
        model_revision="a" * 40,
        model="deepseek-ai/DeepSeek-V4-Flash",
    )

    with (
        mock.patch.object(provider, "_detect_precompiled_wheel_variant", return_value="cu130"),
        mock.patch.object(provider, "_pip_install") as pip_install,
    ):
        provider._install_deepseek_v4_disaggregated_dependencies()

    pip_install.assert_called_once_with(
        "mooncake-transfer-engine-cuda13==0.3.11.post1"
    )


def test_sglang_disaggregated_spec_uses_real_transfer_and_router(
    tmp_path: Path,
) -> None:
    provider = SglangProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(
            provider,
            "_reserve_local_ports",
            return_value=[8100, 8200, 8300],
        ),
    ):
        command = provider._server_cmd("model", tp=4, port=8001)

    spec = _read_spec(command)
    prefill, decode = spec["phases"][0]["components"]
    router = spec["phases"][1]["components"][0]

    assert spec["transport"] == "mooncake"
    assert spec["mooncake_protocol"] == "rdma"
    assert spec["mooncake_data_plane_transport"] == "rdma"
    assert prefill["env"]["CUDA_VISIBLE_DEVICES"] == "0,1,2,3"
    assert decode["env"]["CUDA_VISIBLE_DEVICES"] == "4,5,6,7"
    for component in (prefill, decode):
        assert component["env"]["MC_FORCE_HCA"] == "1"
        assert component["env"]["MC_LOG_LEVEL"] == "INFO"
        assert component["env"]["MC_RPC_PROTOCOL"] == "tcp"
        assert component["env"]["MOONCAKE_PROTOCOL"] == "rdma"
        assert component["env"]["SGLANG_MOONCAKE_CUSTOM_MEM_POOL"] == (
            "INTRA_NODE_NVLINK"
        )
        assert "MC_INTRANODE_NVLINK" not in component["env"]
    assert prefill["command"][prefill["command"].index("--disaggregation-mode") + 1] == "prefill"
    assert decode["command"][decode["command"].index("--disaggregation-mode") + 1] == "decode"
    assert Path(
        prefill["command"][prefill["command"].index("--model-path") + 1]
    ).name == "a" * 40
    assert Path(
        decode["command"][decode["command"].index("--model-path") + 1]
    ).name == "a" * 40
    assert "--pd-disaggregation" in router["command"]
    assert "--mini-lb" not in router["command"]
    assert "sglang_router.launch_router" in router["command"]
    assert router["command"][router["command"].index("--prefill") + 2] == "8300"


def test_sglang_fake_transfer_backend_is_rejected(tmp_path: Path) -> None:
    provider = SglangProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_SGLANG_DISAGG_TRANSFER_BACKEND": "fake"},
            clear=True,
        ),
        pytest.raises(ValueError, match="prohibited"),
    ):
        provider._server_cmd("model", tp=4, port=8001)


def test_vllm_runtime_integrity_requires_completed_request_pairs(tmp_path: Path) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    provider._port = 8001
    response = mock.Mock()
    response.json.return_value = {
        "prefill_instances": 1,
        "decode_instances": 1,
        "request_pairs": 7,
        "prefill_completed": 7,
        "decode_started": 7,
        "decode_completed": 7,
        "decode_aborted": 0,
        "upstream_errors": 0,
    }

    with mock.patch("inference_bench.providers.vllm.httpx.get", return_value=response):
        observation = provider.verify_runtime_integrity()

    response.raise_for_status.assert_called_once()
    assert observation["routed_request_pairs"] == 7


def test_vllm_mooncake_integrity_requires_native_rdma_transfer_evidence(
    tmp_path: Path,
) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    provider._port = 8001
    provider._disagg_connector = "MooncakeConnector"
    _write_mooncake_rdma_logs(
        tmp_path,
        provider="vllm",
        metrics=(
            "KV Transfer metrics: Num successful transfers=3, "
            "Avg MB per transfer=12.5, Num failed transfers=0, "
            "Num failed recvs=0, Num KV expired reqs=0\n"
        ),
    )
    response = mock.Mock()
    response.json.return_value = {
        "prefill_instances": 1,
        "decode_instances": 1,
        "request_pairs": 3,
        "prefill_completed": 3,
        "decode_started": 3,
        "decode_completed": 3,
        "decode_aborted": 0,
        "upstream_errors": 0,
    }

    with mock.patch("inference_bench.providers.vllm.httpx.get", return_value=response):
        observation = provider.verify_runtime_integrity()

    assert observation["mooncake_rdma_log_check"] == "passed"
    assert observation["mooncake_data_plane_transport"] == "rdma"
    assert observation["mooncake_discovered_hcas"] == {
        "prefill": 4,
        "decode": 4,
    }
    assert observation["native_successful_transfers"] == 3
    assert observation["native_transferred_mb_estimate"] == 37.5


def test_vllm_mooncake_integrity_rejects_failed_native_transfers(
    tmp_path: Path,
) -> None:
    provider = VllmProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    provider._port = 8001
    provider._disagg_connector = "MooncakeConnector"
    _write_mooncake_rdma_logs(
        tmp_path,
        provider="vllm",
        metrics=(
            "KV Transfer metrics: Num successful transfers=3, "
            "Avg MB per transfer=12.5, Num failed transfers=1, "
            "Num failed recvs=0, Num KV expired reqs=0\n"
        ),
    )
    response = mock.Mock()
    response.json.return_value = {
        "request_pairs": 3,
        "prefill_completed": 3,
        "decode_started": 3,
        "decode_completed": 3,
        "decode_aborted": 0,
        "upstream_errors": 0,
    }

    with (
        mock.patch("inference_bench.providers.vllm.httpx.get", return_value=response),
        pytest.raises(RuntimeError, match="reported transfer failures"),
    ):
        provider.verify_runtime_integrity()


def test_sglang_runtime_integrity_requires_native_kv_transfer_stats(
    tmp_path: Path,
) -> None:
    provider = SglangProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    provider._disagg_prefill_port = 8100
    provider._disagg_transfer_backend = "mooncake"
    _write_mooncake_rdma_logs(tmp_path, provider="sglang")
    response = mock.Mock()
    response.json.return_value = {
        "loads": [
            {
                "disaggregation": {
                    "mode": "prefill",
                    "kv_transfer_speed_gb_s": 91.5,
                    "kv_transfer_latency_ms": 0.7,
                }
            }
        ]
    }

    with mock.patch("inference_bench.providers.sglang.httpx.get", return_value=response):
        observation = provider.verify_runtime_integrity()

    response.raise_for_status.assert_called_once()
    assert observation["kv_handoff_check"] == "passed"
    assert observation["observed_kv_transfer_speed_gb_s"] == 91.5
    assert observation["mooncake_data_plane_transport"] == "rdma"
    assert observation["custom_allreduce_check"] == "passed"


def test_sglang_disaggregated_build_installs_router_and_transfer_engine(
    tmp_path: Path,
) -> None:
    provider = SglangProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)
    router_dir = (
        provider.repo_dir
        / "sgl-model-gateway"
        / "bindings"
        / "python"
    )
    router_dir.mkdir(parents=True)

    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(provider, "_create_venv"),
        mock.patch.object(provider, "_cuda_major_version", return_value=12),
        mock.patch.object(provider, "_pip_install") as pip_install,
    ):
        provider.build()

    pip_install.assert_has_calls(
        [
            mock.call("--upgrade", "pip"),
            mock.call("-e", ".", cwd=provider._python_dir),
            mock.call("-e", ".", cwd=router_dir),
            mock.call("mooncake-transfer-engine==0.3.11.post1"),
        ]
    )


def test_sglang_disaggregated_build_does_not_fallback_to_unrelated_wheel(
    tmp_path: Path,
) -> None:
    provider = SglangProvider(build_dir=str(tmp_path))
    _configure_disaggregated(provider)

    with (
        mock.patch.dict(os.environ, {}, clear=True),
        mock.patch.object(provider, "_create_venv"),
        mock.patch.object(
            provider,
            "_pip_install",
            side_effect=subprocess.CalledProcessError(1, "pip"),
        ),
        mock.patch.object(provider, "_pip_install_binary_wheel") as binary_fallback,
        pytest.raises(subprocess.CalledProcessError),
    ):
        provider.build()

    binary_fallback.assert_not_called()


def test_disaggregated_launcher_starts_and_stops_component_tree(
    tmp_path: Path,
) -> None:
    port = _free_port()
    component_log = tmp_path / "component.log"
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(
        json.dumps(
            {
                "component_startup_timeout_s": 10,
                "phases": [
                    {
                        "components": [
                            {
                                "name": "test-server",
                                "command": [
                                    sys.executable,
                                    "-m",
                                    "http.server",
                                    str(port),
                                    "--bind",
                                    "127.0.0.1",
                                ],
                                "ready_url": f"http://127.0.0.1:{port}/",
                                "log_path": str(component_log),
                            }
                        ]
                    }
                ],
            }
        )
    )
    launcher = Path(__file__).parents[1] / "inference_bench" / "disaggregated_launcher.py"
    process = subprocess.Popen(
        [sys.executable, str(launcher), str(spec_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    try:
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            try:
                if httpx.get(f"http://127.0.0.1:{port}/", timeout=0.5).status_code == 200:
                    break
            except httpx.HTTPError:
                time.sleep(0.1)
        else:
            pytest.fail("launcher component did not become ready")
        process.terminate()
        assert process.wait(timeout=10) == 0
        deadline = time.monotonic() + 5
        while time.monotonic() < deadline:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                if sock.connect_ex(("127.0.0.1", port)) != 0:
                    break
            time.sleep(0.1)
        else:
            pytest.fail("launcher left its child server running")
    finally:
        if process.poll() is None:
            process.kill()
            process.wait(timeout=5)


def test_disaggregated_launcher_signals_group_after_leader_exit(tmp_path: Path) -> None:
    component = _Component(
        name="server",
        command=["server"],
        env={},
        log_path=tmp_path / "server.log",
    )
    component.process = mock.Mock(pid=123, poll=mock.Mock(return_value=0))

    with mock.patch("inference_bench.disaggregated_launcher.os.killpg") as killpg:
        component.terminate()
        component.kill()

    assert killpg.call_args_list == [
        mock.call(123, signal.SIGTERM),
        mock.call(123, signal.SIGKILL),
    ]
