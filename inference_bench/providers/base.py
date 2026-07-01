from __future__ import annotations

import json
import os
import signal
import socket
import subprocess
import sys
import threading
import time
from abc import ABC, abstractmethod
from pathlib import Path

import httpx


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
    def server_python(self) -> str:
        override = self._server_python_override()
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

    def _server_env(self) -> dict[str, str]:
        return os.environ.copy()

    def _server_model(self, model: str) -> str:
        return _server_model_path(model)

    def _gpu_memory_wait_fraction(self) -> float | None:
        return None

    def wait_for_gpu_isolation(self, tp: int) -> None:
        if not _env_flag("INFERENCE_BENCH_GPU_ISOLATION_CHECK", True):
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
            env=env,
            stdout=self._log_file,
            stderr=subprocess.STDOUT,
            preexec_fn=os.setsid,
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

    @staticmethod
    def _query_gpu_memory() -> list[dict[str, int | str]]:
        cmd = [
            "nvidia-smi",
            "--query-gpu=index,uuid,memory.total,memory.free",
            "--format=csv,noheader,nounits",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        except FileNotFoundError:
            return []
        if result.returncode != 0:
            return []
        rows: list[dict[str, int | str]] = []
        for line in result.stdout.splitlines():
            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 4:
                continue
            try:
                rows.append(
                    {
                        "index": int(parts[0]),
                        "uuid": parts[1],
                        "total_mib": int(parts[2]),
                        "free_mib": int(parts[3]),
                    }
                )
            except ValueError:
                continue
        return rows

    @staticmethod
    def _query_gpu_apps() -> list[str]:
        return [row["raw"] for row in Provider._query_gpu_app_rows()]

    @staticmethod
    def _query_gpu_app_rows() -> list[dict[str, int | str]]:
        cmd = [
            "nvidia-smi",
            "--query-compute-apps=pid,process_name,gpu_uuid,used_memory",
            "--format=csv,noheader,nounits",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        except FileNotFoundError:
            return []
        if result.returncode != 0:
            return []
        rows: list[dict[str, int | str]] = []
        for line in result.stdout.splitlines():
            raw = line.strip()
            if not raw:
                continue
            parts = [part.strip() for part in raw.split(",", 3)]
            if len(parts) != 4:
                rows.append({"raw": raw, "pid": -1, "process_name": "", "gpu_uuid": "", "used_memory_mib": -1})
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
        self._log(f"[{self.name}] Stopping server (pid={self._server_process.pid})")
        try:
            os.killpg(os.getpgid(self._server_process.pid), signal.SIGTERM)
            self._server_process.wait(timeout=30)
        except (ProcessLookupError, subprocess.TimeoutExpired):
            try:
                os.killpg(os.getpgid(self._server_process.pid), signal.SIGKILL)
                self._server_process.wait(timeout=10)
            except (ProcessLookupError, subprocess.TimeoutExpired):
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


def _server_model_path(model: str) -> str:
    override = os.environ.get("INFERENCE_BENCH_SERVER_MODEL", "").strip()
    if override:
        return override
    if not _env_flag("INFERENCE_BENCH_USE_CACHED_HF_SNAPSHOT", True):
        return model
    cached = _cached_hf_snapshot(model)
    return str(cached) if cached is not None else model


def _cached_hf_snapshot(model: str) -> Path | None:
    candidate = Path(model).expanduser()
    if candidate.exists():
        return None
    repo_cache_name = f"models--{model.replace('/', '--')}"
    for cache_root in _hf_cache_roots():
        repo_cache = cache_root / repo_cache_name
        snapshots = repo_cache / "snapshots"
        if not snapshots.exists():
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
    for index_name in ("model.safetensors.index.json", "pytorch_model.bin.index.json"):
        index_path = snapshot / index_name
        if index_path.exists():
            try:
                index = json.loads(index_path.read_text())
            except json.JSONDecodeError:
                return False
            weight_map = index.get("weight_map", {})
            if not isinstance(weight_map, dict):
                return False
            files = {str(filename) for filename in weight_map.values()}
            return bool(files) and all((snapshot / filename).exists() for filename in files)
    return (snapshot / "model.safetensors").exists() or (snapshot / "pytorch_model.bin").exists()


class _GpuIsolationMonitor:
    def __init__(self, provider: Provider, tp: int):
        self.provider = provider
        self.tp = tp
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._contaminating_apps: list[str] = []

    def __enter__(self) -> "_GpuIsolationMonitor":
        if not _env_flag("INFERENCE_BENCH_GPU_ISOLATION_CHECK", True):
            return self
        poll_s = _env_float("INFERENCE_BENCH_GPU_ISOLATION_MONITOR_POLL_S", 1.0, minimum=0.25)

        def _run() -> None:
            while not self._stop.wait(poll_s):
                apps = self.provider._external_gpu_apps(self.tp)
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
        return False
