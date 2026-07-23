from __future__ import annotations

import json
import os
import shlex
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from threading import Event
from typing import Any


@dataclass
class _Component:
    name: str
    command: list[str]
    env: dict[str, str]
    log_path: Path
    ready_url: str = ""
    cwd: str | None = None
    process: subprocess.Popen | None = None
    log_file: Any = None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> _Component:
        name = str(data.get("name", "")).strip()
        command = data.get("command")
        log_path = str(data.get("log_path", "")).strip()
        if not name:
            raise ValueError("Every component needs a non-empty name")
        if not isinstance(command, list) or not command or not all(
            isinstance(item, str) and item for item in command
        ):
            raise ValueError(f"Component {name!r} needs a non-empty string command")
        if not log_path:
            raise ValueError(f"Component {name!r} needs a log_path")
        raw_env = data.get("env", {})
        if not isinstance(raw_env, dict):
            raise ValueError(f"Component {name!r} env must be an object")
        return cls(
            name=name,
            command=list(command),
            env={str(key): str(value) for key, value in raw_env.items()},
            log_path=Path(log_path),
            ready_url=str(data.get("ready_url", "")).strip(),
            cwd=str(data["cwd"]) if data.get("cwd") else None,
        )

    def start(self) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_path.open("w", encoding="utf-8")
        env = os.environ.copy()
        env.update(self.env)
        print(f"[disagg] Starting {self.name}: {shlex.join(self.command)}", flush=True)
        print(f"[disagg] {self.name} log: {self.log_path}", flush=True)
        try:
            self.process = subprocess.Popen(
                self.command,
                cwd=self.cwd,
                env=env,
                stdout=self.log_file,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
        except Exception:
            self.log_file.close()
            self.log_file = None
            raise

    def poll(self) -> int | None:
        return None if self.process is None else self.process.poll()

    def log_tail(self, max_chars: int = 6000) -> str:
        if self.log_file is not None:
            try:
                self.log_file.flush()
            except OSError:
                pass
        try:
            return self.log_path.read_text(encoding="utf-8", errors="replace")[-max_chars:]
        except OSError:
            return ""

    def terminate(self) -> None:
        if self.process is None:
            return
        try:
            os.killpg(self.process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass

    def kill(self) -> None:
        if self.process is None:
            return
        try:
            os.killpg(self.process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass

    def close_log(self) -> None:
        if self.log_file is not None:
            self.log_file.close()
            self.log_file = None


def _http_ready(url: str) -> bool:
    try:
        with urllib.request.urlopen(url, timeout=2) as response:
            return 200 <= int(response.status) < 300
    except (OSError, urllib.error.URLError):
        return False


def _raise_if_exited(components: list[_Component]) -> None:
    for component in components:
        returncode = component.poll()
        if returncode is None:
            continue
        raise RuntimeError(
            f"Component {component.name!r} exited with code {returncode}.\n"
            f"Log tail:\n{component.log_tail()}"
        )


def _wait_for_phase(
    phase_components: list[_Component],
    all_components: list[_Component],
    *,
    timeout_s: float,
    settle_s: float,
    stopping: Event,
) -> None:
    pending = [component for component in phase_components if component.ready_url]
    deadline = time.monotonic() + timeout_s
    while pending and not stopping.is_set():
        _raise_if_exited(all_components)
        pending = [
            component
            for component in pending
            if not _http_ready(component.ready_url)
        ]
        if not pending:
            break
        if time.monotonic() >= deadline:
            waiting = ", ".join(
                f"{component.name} ({component.ready_url})" for component in pending
            )
            raise TimeoutError(
                f"Timed out after {timeout_s:.0f}s waiting for: {waiting}"
            )
        time.sleep(1)

    settle_deadline = time.monotonic() + max(0.0, settle_s)
    while time.monotonic() < settle_deadline and not stopping.is_set():
        _raise_if_exited(all_components)
        time.sleep(min(0.1, settle_deadline - time.monotonic()))


def _shutdown(components: list[_Component]) -> None:
    for component in reversed(components):
        component.terminate()
    deadline = time.monotonic() + 20
    for component in reversed(components):
        process = component.process
        if process is None:
            continue
        remaining = max(0.0, deadline - time.monotonic())
        try:
            process.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            component.kill()
    for component in reversed(components):
        process = component.process
        if process is not None and process.poll() is None:
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                pass
        component.close_log()


def run_spec(spec: dict[str, Any]) -> int:
    phases = spec.get("phases")
    if not isinstance(phases, list) or not phases:
        raise ValueError("Deployment spec needs at least one phase")
    timeout_s = float(
        os.environ.get(
            "INFERENCE_BENCH_DISAGG_COMPONENT_TIMEOUT_S",
            spec.get("component_startup_timeout_s", 3600),
        )
    )
    if timeout_s <= 0:
        raise ValueError("component_startup_timeout_s must be positive")

    stopping = Event()

    def request_stop(signum: int, _frame: Any) -> None:
        print(f"[disagg] Received signal {signum}; stopping components", flush=True)
        stopping.set()

    signal.signal(signal.SIGTERM, request_stop)
    signal.signal(signal.SIGINT, request_stop)

    started: list[_Component] = []
    try:
        names: set[str] = set()
        for phase_index, raw_phase in enumerate(phases):
            if not isinstance(raw_phase, dict):
                raise ValueError(f"Phase {phase_index} must be an object")
            raw_components = raw_phase.get("components")
            if not isinstance(raw_components, list) or not raw_components:
                raise ValueError(f"Phase {phase_index} needs at least one component")
            phase_components = [
                _Component.from_dict(component) for component in raw_components
            ]
            phase_names = [component.name for component in phase_components]
            if len(set(phase_names)) != len(phase_names):
                raise ValueError(f"Phase {phase_index} has duplicate component names")
            duplicate = next(
                (component.name for component in phase_components if component.name in names),
                None,
            )
            if duplicate is not None:
                raise ValueError(f"Duplicate component name {duplicate!r}")
            names.update(component.name for component in phase_components)
            for component in phase_components:
                component.start()
                started.append(component)
            _wait_for_phase(
                phase_components,
                started,
                timeout_s=timeout_s,
                settle_s=float(raw_phase.get("settle_seconds", 0.5)),
                stopping=stopping,
            )
            if stopping.is_set():
                return 0

        print("[disagg] All deployment components are running", flush=True)
        while not stopping.wait(1):
            _raise_if_exited(started)
        return 0
    finally:
        _shutdown(started)


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} SPEC.json", file=sys.stderr)
        return 2
    spec_path = Path(sys.argv[1])
    try:
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        if not isinstance(spec, dict):
            raise ValueError("Deployment spec root must be an object")
        return run_spec(spec)
    except Exception as exc:
        print(f"[disagg] Launcher failed: {exc}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
