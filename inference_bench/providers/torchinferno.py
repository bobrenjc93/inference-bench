from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

from . import register
from .base import Provider, _env_float


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

    def __init__(self, build_dir: str = "./builds"):
        super().__init__(build_dir=build_dir)
        self._extra_log_paths: dict[str, str] = {}
        local = os.environ.get("TORCHINFERNO_LOCAL_REPO")
        if local:
            self.repo_dir = Path(local).resolve()
            self.venv_dir = self.repo_dir / "venv"

    def clone(self) -> None:
        if os.environ.get("TORCHINFERNO_LOCAL_REPO"):
            return
        super().clone()

    def _create_venv(self) -> None:
        import subprocess, sys
        if not self.venv_dir.exists():
            self._log(f"[{self.name}] Creating virtualenv at {self.venv_dir}")
            subprocess.run(
                [sys.executable, "-m", "venv", "--system-site-packages", str(self.venv_dir)],
                check=True,
            )

    def build(self) -> None:
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        explicit_extras = os.environ.get("INFERENCE_BENCH_TORCHINFERNO_EXTRAS")
        default_flashinfer = (
            explicit_extras is None
            and _env_flag("INFERENCE_BENCH_TORCHINFERNO_FLASHINFER", True)
        )
        extras = explicit_extras if explicit_extras is not None else (
            "serve,flashinfer" if default_flashinfer else "serve"
        )
        try:
            self._pip_install("-e", _editable_install_spec(extras), cwd=self.repo_dir)
        except subprocess.CalledProcessError:
            if not default_flashinfer:
                raise
            self._log(
                "[torchinferno] FlashInfer extra install failed; "
                "retrying with the plain serve extra"
            )
            self._pip_install("-e", ".[serve]", cwd=self.repo_dir)

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
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
        extra_args = os.environ.get("TORCHINFERNO_SERVER_ARGS", "").strip()
        if extra_args:
            cmd.extend(shlex.split(extra_args))
        return cmd

    def _server_env(self) -> dict[str, str]:
        env = super()._server_env()
        self._extra_log_paths = {}
        if _env_flag("INFERENCE_BENCH_TORCHINFERNO_PROFILE", True):
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
        # Public 8xH100 runs are single-node. Avoid cloud RDMA/OFI plugin probes
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
        # TorchInferno launches eight worker processes before it can bind /health.
        # Inherited NCCL INFO logging can dominate startup logs on public runners
        # and obscure readiness failures. Keep the default quiet; set
        # INFERENCE_BENCH_TORCHINFERNO_NCCL_DEBUG=INFO for transport debugging.
        env["NCCL_DEBUG"] = os.environ.get("INFERENCE_BENCH_TORCHINFERNO_NCCL_DEBUG", "WARN")
        # The tensor command path can leave TP workers on different collectives
        # after long online-serving runs. Prefer the supported object command
        # transport for public correctness runs unless explicitly overridden.
        env.setdefault("TORCHINFERNO_OPENAI_TP_TENSOR_COMMANDS", "0")
        if "TORCH_NCCL_ASYNC_ERROR_HANDLING" not in env and "NCCL_ASYNC_ERROR_HANDLING" in env:
            env["TORCH_NCCL_ASYNC_ERROR_HANDLING"] = env["NCCL_ASYNC_ERROR_HANDLING"]
        env.pop("NCCL_ASYNC_ERROR_HANDLING", None)
        return env

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
        return dict(self._extra_log_paths)

    def _gpu_memory_wait_fraction(self) -> float | None:
        if "INFERENCE_BENCH_TORCHINFERNO_MIN_GPU_FREE_FRACTION" in os.environ:
            return _env_float(
                "INFERENCE_BENCH_TORCHINFERNO_MIN_GPU_FREE_FRACTION",
                0.92,
                minimum=0.0,
            )
        return _env_float("INFERENCE_BENCH_GPU_MEMORY_FREE_FRACTION", 0.92, minimum=0.0)
