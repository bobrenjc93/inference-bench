from __future__ import annotations

import os
import subprocess

from . import register
from .base import Provider, _env_flag, _env_float


@register("vllm")
class VllmProvider(Provider):
    name = "vllm"
    repo_url = "https://github.com/vllm-project/vllm.git"

    def build(self) -> None:
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        self._disable_fastapi_metrics_middleware()
        precompiled_explicit = (
            "VLLM_USE_PRECOMPILED" in os.environ
            or "INFERENCE_BENCH_VLLM_USE_PRECOMPILED" in os.environ
        )
        os.environ.setdefault(
            "VLLM_USE_PRECOMPILED",
            os.environ.get("INFERENCE_BENCH_VLLM_USE_PRECOMPILED", "1"),
        )
        os.environ.setdefault(
            "MAX_JOBS",
            os.environ.get("INFERENCE_BENCH_VLLM_MAX_JOBS", "8"),
        )
        try:
            self._pip_install("-e", ".", cwd=self.repo_dir)
        except subprocess.CalledProcessError:
            if (
                precompiled_explicit
                or not _env_flag("INFERENCE_BENCH_VLLM_FALLBACK_SOURCE_BUILD", True)
                or not _env_flag("VLLM_USE_PRECOMPILED", True)
            ):
                raise
            self._log("[vllm] Precompiled wheel install failed; retrying with VLLM_USE_PRECOMPILED=0")
            os.environ["VLLM_USE_PRECOMPILED"] = "0"
            self._pip_install("-e", ".", cwd=self.repo_dir)

    def _disable_fastapi_metrics_middleware(self) -> None:
        metrics_py = self.repo_dir / "vllm" / "entrypoints" / "serve" / "instrumentator" / "metrics.py"
        if not metrics_py.exists():
            return
        text = metrics_py.read_text()
        old = """    Instrumentator(
        excluded_handlers=[
            "/metrics",
            "/health",
            "/load",
            "/ping",
            "/version",
            "/server_info",
        ],
        registry=registry,
    ).add().instrument(app).expose(app, response_class=PrometheusResponse)
"""
        new = """    # The request-metrics middleware from prometheus-fastapi-instrumentator
    # has broken against recent FastAPI/Starlette route objects in fresh vLLM
    # installs, causing every health probe to return HTTP 500. The benchmark only
    # needs the OpenAI API, so keep the /metrics ASGI mount below and skip the
    # middleware until vLLM or the dependency restores compatibility.
"""
        if old not in text or new in text:
            return
        metrics_py.write_text(text.replace(old, new))

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        cmd = [
            self.venv_python, "-m", "vllm.entrypoints.openai.api_server",
            "--model", model,
            "--tensor-parallel-size", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
        gpu_memory_utilization = os.environ.get("INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION")
        if gpu_memory_utilization:
            cmd.extend(["--gpu-memory-utilization", gpu_memory_utilization])
        return cmd

    def _gpu_memory_wait_fraction(self) -> float | None:
        if "INFERENCE_BENCH_VLLM_MIN_GPU_FREE_FRACTION" in os.environ:
            return _env_float("INFERENCE_BENCH_VLLM_MIN_GPU_FREE_FRACTION", 0.92, minimum=0.0)
        if "INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION" in os.environ:
            return _env_float("INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION", 0.92, minimum=0.0)
        return _env_float("INFERENCE_BENCH_GPU_MEMORY_FREE_FRACTION", 0.92, minimum=0.0)
