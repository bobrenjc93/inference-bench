from __future__ import annotations

import os
import signal
import socket
import subprocess
import sys
import time
from abc import ABC, abstractmethod
from pathlib import Path

import httpx


class Provider(ABC):
    name: str
    repo_url: str

    def __init__(self, build_dir: str = "./builds"):
        self.build_dir = Path(build_dir).resolve()
        self.repo_dir = self.build_dir / self.name
        self.venv_dir = self.repo_dir / "venv"
        self.verbose: bool = False
        self._server_process: subprocess.Popen | None = None

    def _log(self, msg: str) -> None:
        if self.verbose:
            print(msg)

    @property
    def venv_python(self) -> str:
        return str(self.venv_dir / "bin" / "python")

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
        return result.stdout.strip() if result.returncode == 0 else ""

    def clone(self) -> None:
        if (self.repo_dir / ".git").exists():
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
            ["git", "clone", self.repo_url, str(self.repo_dir)],
            check=True,
        )

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

    @abstractmethod
    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        ...

    def start_server(self, model: str, tp: int, port: int, timeout: int = 600) -> None:
        self._port = port
        cmd = self._server_cmd(model, tp, port)
        env = os.environ.copy()
        env["PATH"] = str(self.venv_dir / "bin") + ":" + env.get("PATH", "")

        self._log_path = self.build_dir / f"{self.name}_server.log"
        self._log_file = open(self._log_path, "w")

        self._log(f"[{self.name}] Starting server: {' '.join(cmd)}")
        self._log(f"[{self.name}] Server log: {self._log_path}")
        self._server_process = subprocess.Popen(
            cmd,
            env=env,
            stdout=self._log_file,
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid,
        )

        self._wait_for_health(timeout)

    def _wait_for_health(self, timeout: int) -> None:
        self._log(f"[{self.name}] Waiting for server to be ready (timeout={timeout}s)...")
        start = time.time()
        while time.time() - start < timeout:
            try:
                resp = httpx.get(f"http://localhost:{self._port}/v1/models", timeout=5)
                if resp.status_code == 200:
                    print(f"[{self.name}] Server ready in {time.time() - start:.1f}s")
                    return
            except (httpx.ConnectError, httpx.ReadTimeout, httpx.RemoteProtocolError):
                pass

            if self._server_process and self._server_process.poll() is not None:
                self._log_file.flush()
                log_tail = ""
                try:
                    with open(self._log_path) as f:
                        log_tail = f.read()[-3000:]
                except Exception:
                    pass
                raise RuntimeError(
                    f"[{self.name}] Server process exited with code "
                    f"{self._server_process.returncode}.\nLog tail:\n{log_tail}"
                )
            time.sleep(5)
        raise TimeoutError(
            f"[{self.name}] Server did not become ready within {timeout}s"
        )

    def stop_server(self) -> None:
        if self._server_process is None:
            return
        port = getattr(self, "_port", None)
        self._log(f"[{self.name}] Stopping server (pid={self._server_process.pid})")
        try:
            os.killpg(os.getpgid(self._server_process.pid), signal.SIGTERM)
            self._server_process.wait(timeout=30)
        except (ProcessLookupError, subprocess.TimeoutExpired):
            try:
                os.killpg(os.getpgid(self._server_process.pid), signal.SIGKILL)
            except ProcessLookupError:
                pass
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
