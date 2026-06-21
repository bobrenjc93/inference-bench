from __future__ import annotations

import os

from . import register
from .base import Provider, _env_float


@register("sglang")
class SglangProvider(Provider):
    name = "sglang"
    repo_url = "https://github.com/sgl-project/sglang.git"

    @property
    def _python_dir(self):
        return self.repo_dir / "python"

    def build(self) -> None:
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        self._pip_install("-e", ".", cwd=self._python_dir)

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        cmd = [
            self.venv_python, "-m", "sglang.launch_server",
            "--model-path", model,
            "--tp", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
        mem_fraction = os.environ.get("INFERENCE_BENCH_SGLANG_MEM_FRACTION_STATIC")
        if mem_fraction:
            cmd.extend(["--mem-fraction-static", mem_fraction])
        return cmd

    def _gpu_memory_wait_fraction(self) -> float | None:
        if "INFERENCE_BENCH_SGLANG_MIN_GPU_FREE_FRACTION" in os.environ:
            return _env_float(
                "INFERENCE_BENCH_SGLANG_MIN_GPU_FREE_FRACTION",
                0.85,
                minimum=0.0,
            )
        if "INFERENCE_BENCH_SGLANG_MEM_FRACTION_STATIC" in os.environ:
            return _env_float(
                "INFERENCE_BENCH_SGLANG_MEM_FRACTION_STATIC",
                0.85,
                minimum=0.0,
            )
        return _env_float("INFERENCE_BENCH_GPU_MEMORY_FREE_FRACTION", 0.85, minimum=0.0)
