from __future__ import annotations

import json
import os
import shlex
import subprocess
from pathlib import Path

from ..integrity import TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS, torchinferno_logits_cache_warnings
from . import register
from .base import Provider, _cached_hf_snapshot, _env_float


def _env_flag(name: str, default: bool) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    return raw.strip().lower() not in {"0", "false", "no", "off"}


def _editable_install_spec(extras: str) -> str:
    extras = extras.strip()
    return f".[{extras}]" if extras else "."


@register("torchinferno")
class TorchInfernoProvider(Provider):
    name = "torchinferno"
    repo_url = "https://github.com/bobrenjc93/TorchInferno.git"
    runtime_import_names = ("torchinferno",)

    def __init__(self, build_dir: str = "./builds"):
        super().__init__(build_dir=build_dir)
        self._extra_log_paths: dict[str, str] = {}
        local = os.environ.get("TORCHINFERNO_LOCAL_REPO")
        if local:
            self.repo_dir = Path(local).resolve()
            self.venv_dir = self.repo_dir / "venv"

    def clone(self) -> None:
        if os.environ.get("TORCHINFERNO_LOCAL_REPO"):
            if self.is_scored_evaluation:
                raise RuntimeError(
                    "TORCHINFERNO_LOCAL_REPO is prohibited in a scored "
                    "evaluation"
                )
            return
        super().clone()

    def _create_venv(self) -> None:
        import subprocess
        import sys
        if not self.venv_dir.exists():
            self._log(f"[{self.name}] Creating virtualenv at {self.venv_dir}")
            subprocess.run(
                [sys.executable, "-m", "venv", "--system-site-packages", str(self.venv_dir)],
                check=True,
            )

    def build(self) -> None:
        self._reject_scored_environment_overrides(
            names=("TORCHINFERNO_LOCAL_REPO",),
            prefixes=("INFERENCE_BENCH_TORCHINFERNO_", "TORCHINFERNO_"),
        )
        is_deepseek_v4 = self._configured_for_deepseek_v4()
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        explicit_extras = os.environ.get("INFERENCE_BENCH_TORCHINFERNO_EXTRAS")
        if self.is_scored_evaluation and explicit_extras is not None:
            raise ValueError(
                "INFERENCE_BENCH_TORCHINFERNO_EXTRAS is prohibited in a scored "
                "evaluation"
            )
        h100_extras = "h100" in str(getattr(self, "hardware", "")).lower()
        default_flashinfer = (
            explicit_extras is None
            and not is_deepseek_v4
            and _env_flag("INFERENCE_BENCH_TORCHINFERNO_FLASHINFER", True)
        )
        default_extras = ["serve"]
        if is_deepseek_v4:
            default_extras.append("deepseek-v4")
        if default_flashinfer:
            default_extras.append("flashinfer")
        if h100_extras:
            default_extras.append("h100")
        extras = explicit_extras if explicit_extras is not None else ",".join(default_extras)
        if (
            self.is_disaggregated_prefill_decode
            and is_deepseek_v4
            and "deepseek-v4" not in {item.strip() for item in extras.split(",")}
        ):
            raise ValueError(
                "Scored DeepSeek V4 runs require the TorchInferno deepseek-v4 extra"
            )
        try:
            self._pip_install("-e", _editable_install_spec(extras), cwd=self.repo_dir)
        except subprocess.CalledProcessError:
            if not default_flashinfer:
                raise
            self._log(
                "[torchinferno] FlashInfer extra install failed; "
                "retrying without FlashInfer"
            )
            fallback = [item for item in default_extras if item != "flashinfer"]
            fallback_extras = ",".join(fallback)
            self._pip_install("-e", _editable_install_spec(fallback_extras), cwd=self.repo_dir)

    def _configured_for_deepseek_v4(self) -> bool:
        model = str(getattr(self, "_configured_model", "") or "")
        normalized = model.lower().replace("_", "-")
        if "deepseek-v4" in normalized:
            return True
        if not model or not self.model_revision:
            return False
        snapshot = _cached_hf_snapshot(model, revision=self.model_revision)
        if snapshot is None:
            return False
        try:
            config = json.loads((snapshot / "config.json").read_text())
        except (OSError, json.JSONDecodeError):
            return False
        return str(config.get("model_type", "")).lower() == "deepseek_v4"

    def prepare_model_assets(self, model: str) -> None:
        self._reject_scored_environment_overrides(
            prefixes=("INFERENCE_BENCH_TORCHINFERNO_", "TORCHINFERNO_"),
        )
        is_deepseek_v4 = self._configured_for_deepseek_v4()
        if "h100" in str(getattr(self, "hardware", "")).lower() and not is_deepseek_v4:
            artifact_root = self.build_dir / "torchinferno-kernel-artifacts"
            command = [
                self.venv_python,
                "-m",
                "torchinferno.kernels.sgl_fp8_out_builder",
                "--artifact-root",
                str(artifact_root),
            ]
            self._log(
                "[torchinferno] Preparing H100 FP8 output adapter: "
                + " ".join(command)
            )
            subprocess.run(command, cwd=self.repo_dir, check=True)
            libraries = tuple(artifact_root.glob("sgl-fp8-out/*/*.so"))
            if not libraries:
                raise RuntimeError(
                    "TorchInferno H100 FP8 output adapter preparation was incomplete"
                )
            self._h100_kernel_artifact_root = artifact_root
        if not self.is_disaggregated_prefill_decode or not is_deepseek_v4:
            return
        forbidden = [
            name
            for name in (
                "TORCHINFERNO_V4_KERNEL_ARTIFACT_DIR",
                "TVM_FFI_CACHE_DIR",
            )
            if os.environ.get(name, "").strip()
        ]
        if forbidden:
            raise ValueError(
                "External DeepSeek V4 artifact paths are prohibited in scored runs: "
                + ", ".join(forbidden)
            )
        snapshot = _cached_hf_snapshot(model, revision=self.model_revision)
        if snapshot is None:
            raise RuntimeError(
                "Scored DeepSeek V4 runs require the complete pinned checkpoint "
                "before offline kernel preparation"
            )
        artifact_root = self.repo_dir / ".inference-bench-artifacts" / "deepseek-v4"
        tp_sizes = sorted(
            {
                int(self.prefill_tensor_parallel_size or 0),
                int(self.decode_tensor_parallel_size or 0),
            }
            - {0}
        )
        command = [
            self.venv_python,
            str(self.repo_dir / "scripts" / "prepare_deepseek_v4_kernels.py"),
            str(snapshot),
            str(artifact_root),
            "--tensor-parallel-sizes",
            ",".join(str(size) for size in tp_sizes),
        ]
        self._log(f"[torchinferno] Preparing DeepSeek V4 kernels: {' '.join(command)}")
        subprocess.run(command, cwd=self.repo_dir, check=True)
        tilelang_root = artifact_root / "tilelang"
        marlin_root = artifact_root / "marlin"
        if not tilelang_root.is_dir() or not marlin_root.is_dir():
            raise RuntimeError("DeepSeek V4 offline kernel preparation was incomplete")
        self._v4_artifact_root = artifact_root

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        self._reject_scored_environment_overrides(
            names=("TORCHINFERNO_SERVER_ARGS",),
            prefixes=("INFERENCE_BENCH_TORCHINFERNO_",),
        )
        if self.is_disaggregated_prefill_decode:
            prefill_tp = int(self.prefill_tensor_parallel_size or 0)
            decode_tp = int(self.decode_tensor_parallel_size or 0)
            if prefill_tp != decode_tp:
                raise ValueError(
                    "TorchInferno currently requires equal prefill and decode "
                    "tensor-parallel sizes"
                )
            tp = prefill_tp
        server_model = self._server_model(model)
        cmd = [
            self.server_python,
            "-m",
            "torchinferno.openai_server",
            "--model",
            server_model,
            "--tensor-parallel-size",
            str(tp),
            "--port",
            str(port),
            "--trust-remote-code",
        ]
        if server_model == model and self.model_revision:
            cmd.extend(["--revision", self.model_revision])
        extra_args = os.environ.get("TORCHINFERNO_SERVER_ARGS", "").strip()
        extra_cmd = shlex.split(extra_args) if extra_args else []
        if self.is_scored_evaluation and extra_cmd:
            raise ValueError(
                "TORCHINFERNO_SERVER_ARGS is prohibited in a scored evaluation"
            )
        if self.is_disaggregated_prefill_decode:
            cmd.extend(["--disaggregation-mode", "prefill-decode"])
        cmd.extend(extra_cmd)
        if self.is_disaggregated_prefill_decode:
            self._record_disaggregated_spec(
                {
                    "schema_version": 1,
                    "provider": self.name,
                    "deployment_mode": self.deployment_mode,
                    "prefill_tensor_parallel_size": prefill_tp,
                    "decode_tensor_parallel_size": decode_tp,
                    "transport": "NCCL",
                    "command": cmd,
                }
            )
        return cmd

    def _server_env(self) -> dict[str, str]:
        self._reject_scored_environment_overrides(
            prefixes=("INFERENCE_BENCH_TORCHINFERNO_", "TORCHINFERNO_"),
        )
        env = super()._server_env()
        self._extra_log_paths = {}
        is_deepseek_v4 = self._configured_for_deepseek_v4()
        if "h100" in str(getattr(self, "hardware", "")).lower() and not is_deepseek_v4:
            artifact_root = getattr(self, "_h100_kernel_artifact_root", None)
            if not isinstance(artifact_root, Path):
                if self.is_scored_evaluation:
                    raise RuntimeError(
                        "TorchInferno H100 kernel artifacts were not prepared"
                    )
            else:
                env["TORCHINFERNO_KERNEL_ARTIFACT_DIR"] = str(artifact_root)
        if self.is_disaggregated_prefill_decode:
            env["TORCHINFERNO_OPENAI_DISAGG_MAX_BATCH_SIZE"] = (
                "64" if is_deepseek_v4 else "128"
            )
        if self.is_disaggregated_prefill_decode and is_deepseek_v4:
            artifact_root = getattr(self, "_v4_artifact_root", None)
            if not isinstance(artifact_root, Path):
                raise RuntimeError(
                    "DeepSeek V4 offline kernel artifacts were not prepared"
                )
            env["TORCHINFERNO_V4_KERNEL_ARTIFACT_DIR"] = str(
                artifact_root / "tilelang"
            )
            env["TVM_FFI_CACHE_DIR"] = str(artifact_root / "marlin")
            env["CUDA_HOME"] = "/does/not/exist"
        if self.is_scored_evaluation or _env_flag(
            "INFERENCE_BENCH_TORCHINFERNO_PROFILE", True
        ):
            self._set_profile_env_default(
                env,
                "queue_profile",
                "TORCHINFERNO_OPENAI_QUEUE_PROFILE_JSONL",
                "queue_profile.jsonl",
            )
            if _env_flag("INFERENCE_BENCH_TORCHINFERNO_FAST_HTTP_PROFILE", False):
                self._set_profile_env_default(
                    env,
                    "fast_http_profile",
                    "TORCHINFERNO_OPENAI_FAST_HTTP_PROFILE_JSONL",
                    "fast_http_profile.jsonl",
                )
        # Public TorchInferno runs have repeatedly stalled during NCCL startup
        # broadcasts on P2P/CUMEM paths. Keep CUMEM disabled by default and let
        # TorchInferno use its portable checkpoint loading default unless a run
        # explicitly opts into rank-0 checkpoint tensor broadcast.
        env.setdefault("NCCL_CUMEM_ENABLE", "0")
        # Public H100 runs are single-node. Avoid cloud RDMA/OFI plugin probes
        # for TorchInferno's auto-launched tensor-parallel workers unless the
        # caller explicitly requests a different NCCL transport.
        env.setdefault("NCCL_NET", "Socket")
        env.setdefault("NCCL_NET_PLUGIN", "none")
        env.setdefault("NCCL_IB_DISABLE", "1")
        # TorchInferno commit 390fed4 can hang during startup while capturing
        # FlashInfer decode CUDA graphs under tensor parallelism. Keep the
        # server on its standard decode graph path unless a run explicitly opts
        # back into FlashInfer decode graphs.
        env.setdefault("TORCHINFERNO_FI_DECODE_GRAPH", "off")
        # TorchInferno launches multiple workers before it can bind /health.
        # Inherited NCCL INFO logging can dominate startup logs on public runners
        # and obscure readiness failures. Keep the default quiet; set
        # INFERENCE_BENCH_TORCHINFERNO_NCCL_DEBUG=INFO for transport debugging.
        env["NCCL_DEBUG"] = os.environ.get("INFERENCE_BENCH_TORCHINFERNO_NCCL_DEBUG", "WARN")
        # Score-facing runs must not use exact-prompt/generated logits caches.
        # Normal KV prefix reuse stays enabled; these switches only block cached
        # logits paths that can turn repeated prompts into benchmark fingerprints.
        allow_logits_caches = _env_flag(
            "INFERENCE_BENCH_TORCHINFERNO_ALLOW_LOGITS_CACHES", False
        )
        if self.is_scored_evaluation and allow_logits_caches:
            raise ValueError(
                "Logits and prompt-result caches are prohibited in scored "
                "evaluations"
            )
        if not allow_logits_caches:
            for name in TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS:
                env[name] = "0"
        if self.is_disaggregated_prefill_decode:
            self._write_disaggregated_cache_attestation(env)
        # The tensor command path can leave TP workers on different collectives
        # after long online-serving runs. Prefer the supported object command
        # transport for public correctness runs unless explicitly overridden.
        env.setdefault("TORCHINFERNO_OPENAI_TP_TENSOR_COMMANDS", "0")
        if "TORCH_NCCL_ASYNC_ERROR_HANDLING" not in env and "NCCL_ASYNC_ERROR_HANDLING" in env:
            env["TORCH_NCCL_ASYNC_ERROR_HANDLING"] = env["NCCL_ASYNC_ERROR_HANDLING"]
        env.pop("NCCL_ASYNC_ERROR_HANDLING", None)
        return env

    def _write_disaggregated_cache_attestation(self, env: dict[str, str]) -> None:
        queue_profile = self._extra_log_paths.get("queue_profile")
        if not queue_profile:
            raise RuntimeError(
                "TorchInferno queue profiling is required for the scored "
                "disaggregated evaluation"
            )
        record: dict[str, object] = {
            "event": "inference_bench_cache_integrity_attestation",
            "deployment_mode": self.deployment_mode,
            "forced_cache_environment": {
                name: env.get(name) for name in TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS
            },
            "expected_tensor_parallel_size_per_role": int(
                self.prefill_tensor_parallel_size or 0
            ),
            "expected_world_size": int(self.prefill_tensor_parallel_size or 0)
            + int(self.decode_tensor_parallel_size or 0),
            "configured_disaggregated_max_batch_size": int(
                env["TORCHINFERNO_OPENAI_DISAGG_MAX_BATCH_SIZE"]
            ),
        }
        path = Path(queue_profile)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")

    def verify_runtime_integrity(self) -> dict[str, object]:
        if not self.is_scored_evaluation:
            return {}
        queue_profile = self._extra_log_paths.get("queue_profile")
        if not queue_profile:
            raise RuntimeError("[torchinferno] Queue profile path is unavailable")
        warnings = torchinferno_logits_cache_warnings(queue_profile)
        if warnings:
            raise RuntimeError("[torchinferno] " + " ".join(warnings))
        if not self.is_disaggregated_prefill_decode:
            return {
                "cache_integrity_check": "passed",
                "runtime_shortcut_counters": "zero",
            }
        handoff_groups = 0
        transferred_bytes = 0
        transferred_caches = 0
        attestations = 0
        topology: dict[str, object] = {}
        try:
            lines = Path(queue_profile).read_text().splitlines()
        except OSError as exc:
            raise RuntimeError(f"[torchinferno] Queue profile is unreadable: {exc}") from exc
        for line in lines:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if not isinstance(record, dict):
                continue
            if record.get("event") == "inference_bench_cache_integrity_attestation":
                attestations += 1
                continue
            if record.get("event") != "disaggregated_runtime_integrity":
                continue
            handoff_groups += 1
            transferred_bytes += int(record.get("transfer_bytes_delta", 0))
            transferred_caches += int(record.get("transfer_count_delta", 0))
            topology = {
                "transport": record.get("transport"),
                "world_size": record.get("world_size"),
                "tensor_parallel_size_per_role": record.get(
                    "tensor_parallel_size_per_role"
                ),
            }
        if (
            attestations != 1
            or handoff_groups <= 0
            or transferred_bytes <= 0
            or transferred_caches <= 0
        ):
            raise RuntimeError(
                "[torchinferno] Disaggregated runtime emitted no verified KV handoffs"
            )
        return {
            "kv_handoff_check": "passed",
            "observed_handoff_groups": handoff_groups,
            "observed_transferred_caches": transferred_caches,
            "observed_transferred_bytes": transferred_bytes,
            **topology,
        }

    def _set_profile_env_default(
        self,
        env: dict[str, str],
        log_name: str,
        env_name: str,
        filename: str,
    ) -> None:
        configured = env.get(env_name, "").strip()
        if configured:
            self._extra_log_paths[log_name] = configured
            return
        path = self.build_dir / f"{self.name}_{filename}"
        try:
            path.unlink()
        except FileNotFoundError:
            pass
        except OSError:
            pass
        env[env_name] = str(path)
        self._extra_log_paths[log_name] = str(path)

    def extra_log_paths(self) -> dict[str, str]:
        return {**super().extra_log_paths(), **self._extra_log_paths}

    def _gpu_memory_wait_fraction(self) -> float | None:
        if "INFERENCE_BENCH_TORCHINFERNO_MIN_GPU_FREE_FRACTION" in os.environ:
            return _env_float(
                "INFERENCE_BENCH_TORCHINFERNO_MIN_GPU_FREE_FRACTION",
                0.92,
                minimum=0.0,
            )
        return _env_float("INFERENCE_BENCH_GPU_MEMORY_FREE_FRACTION", 0.92, minimum=0.0)
