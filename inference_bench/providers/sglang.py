from __future__ import annotations

from . import register
from .base import Provider


@register("sglang")
class SglangProvider(Provider):
    name = "sglang"
    repo_url = "https://github.com/sgl-project/sglang.git"

    def build(self) -> None:
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        self._pip_install("-e", ".[all]", cwd=self.repo_dir)

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        return [
            self.venv_python, "-m", "sglang.launch_server",
            "--model-path", model,
            "--tp", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
