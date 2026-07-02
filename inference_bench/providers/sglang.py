from __future__ import annotations

import os
import subprocess

from . import register
from .base import Provider, _env_flag, _env_float


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
        try:
            self._pip_install("-e", ".", cwd=self._python_dir)
        except subprocess.CalledProcessError:
            if not _env_flag("INFERENCE_BENCH_SGLANG_FALLBACK_BINARY_WHEEL", True):
                raise
            self._pip_install_binary_wheel()

    def _pip_install_binary_wheel(self) -> None:
        spec = os.environ.get("INFERENCE_BENCH_SGLANG_BINARY_WHEEL_SPEC", "").strip()
        if not spec:
            package = os.environ.get("INFERENCE_BENCH_SGLANG_BINARY_WHEEL_PACKAGE", "sglang")
            package = package.strip() or "sglang"
            version = os.environ.get("INFERENCE_BENCH_SGLANG_BINARY_WHEEL_VERSION", "").strip()
            spec = f"{package}=={version}" if version else package
        self._log(f"[sglang] Editable install failed; retrying with binary wheel {spec}")
        self._pip_install("--only-binary=:all:", spec)

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        server_model = self._server_model(model)
        cmd = [
            self.server_python, "-m", "sglang.launch_server",
            "--model-path", server_model,
            "--tp-size", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
        if server_model != model:
            cmd.extend(["--served-model-name", model])
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
