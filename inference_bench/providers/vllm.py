from __future__ import annotations

import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen

from . import register
from .base import Provider, _env_flag, _env_float, _visible_gpu_tokens


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
        precompiled_commit_explicit = (
            "VLLM_PRECOMPILED_WHEEL_COMMIT" in os.environ
            or "INFERENCE_BENCH_VLLM_PRECOMPILED_WHEEL_COMMIT" in os.environ
        )
        os.environ.setdefault(
            "VLLM_USE_PRECOMPILED",
            os.environ.get("INFERENCE_BENCH_VLLM_USE_PRECOMPILED", "1"),
        )
        if "INFERENCE_BENCH_VLLM_PRECOMPILED_WHEEL_COMMIT" in os.environ:
            os.environ.setdefault(
                "VLLM_PRECOMPILED_WHEEL_COMMIT",
                os.environ["INFERENCE_BENCH_VLLM_PRECOMPILED_WHEEL_COMMIT"],
            )
        os.environ.setdefault(
            "MAX_JOBS",
            os.environ.get("INFERENCE_BENCH_VLLM_MAX_JOBS", "8"),
        )
        self._configure_cuda_arch_list()
        if not _env_flag("VLLM_USE_PRECOMPILED", True):
            self._configure_source_build_env()
        try:
            self._pip_install("-e", ".", cwd=self.repo_dir)
        except subprocess.CalledProcessError:
            if _env_flag("VLLM_USE_PRECOMPILED", True):
                if (
                    precompiled_explicit
                    or not _env_flag("INFERENCE_BENCH_VLLM_FALLBACK_SOURCE_BUILD", True)
                ):
                    raise
                if self._try_precompiled_nightly_retry(
                    precompiled_commit_explicit=precompiled_commit_explicit
                ):
                    return
                self._log("[vllm] Precompiled wheel install failed; retrying with VLLM_USE_PRECOMPILED=0")
                os.environ["VLLM_USE_PRECOMPILED"] = "0"
                self._configure_source_build_env()
                self._pip_install_source_with_retry()
                return
            self._pip_install_source_with_retry()

    def _pip_install_source_with_retry(self) -> None:
        self._configure_source_build_env()
        try:
            self._pip_install("-e", ".", cwd=self.repo_dir)
        except subprocess.CalledProcessError:
            if not _env_flag("INFERENCE_BENCH_VLLM_RETRY_CONSERVATIVE_SOURCE_BUILD", True):
                raise
            self._configure_conservative_source_build_retry()
            self._pip_install("-e", ".", cwd=self.repo_dir)

    def _configure_source_build_env(self) -> None:
        if "CMAKE_BUILD_TYPE" not in os.environ:
            os.environ["CMAKE_BUILD_TYPE"] = os.environ.get(
                "INFERENCE_BENCH_VLLM_SOURCE_CMAKE_BUILD_TYPE",
                "Release",
            )

    def _try_precompiled_nightly_retry(self, *, precompiled_commit_explicit: bool) -> bool:
        if precompiled_commit_explicit:
            return False
        if not _env_flag("INFERENCE_BENCH_VLLM_FALLBACK_PRECOMPILED_NIGHTLY", True):
            return False
        wheel_location = os.environ.get(
            "INFERENCE_BENCH_VLLM_FALLBACK_PRECOMPILED_WHEEL_LOCATION"
        ) or self._resolve_precompiled_nightly_wheel_location()
        if not wheel_location:
            return False
        self._log(
            "[vllm] Precompiled wheel install failed; retrying with "
            f"VLLM_PRECOMPILED_WHEEL_LOCATION={wheel_location}"
        )
        os.environ["VLLM_USE_PRECOMPILED"] = "1"
        os.environ.pop("VLLM_PRECOMPILED_WHEEL_COMMIT", None)
        os.environ["VLLM_PRECOMPILED_WHEEL_LOCATION"] = wheel_location
        try:
            self._pip_install("-e", ".", cwd=self.repo_dir)
        except subprocess.CalledProcessError:
            self._log("[vllm] Precompiled nightly wheel install failed; falling back to source build")
            return False
        return True

    def _resolve_precompiled_nightly_wheel_location(self) -> str:
        package = "vllm"
        variant = self._detect_precompiled_wheel_variant()
        variants = [variant, None] if variant else [None]
        for candidate in variants:
            try:
                wheels, repo_url = self._fetch_precompiled_wheel_metadata(
                    commit="nightly",
                    variant=candidate,
                    package=package,
                )
            except Exception as exc:
                label = candidate if candidate else "default"
                self._log(f"[vllm] Could not fetch nightly wheel metadata for {label}: {exc}")
                continue
            location = self._select_precompiled_wheel_location(
                wheels,
                repo_url=repo_url,
                package=package,
            )
            if location:
                return location
        return ""

    def _fetch_precompiled_wheel_metadata(
        self,
        *,
        commit: str,
        variant: str | None,
        package: str,
    ) -> tuple[list[dict[str, object]], str]:
        variant_dir = f"{variant}/" if variant else ""
        repo_url = f"https://wheels.vllm.ai/{commit}/{variant_dir}{package}/"
        meta_url = repo_url + "metadata.json"
        with urlopen(meta_url, timeout=30) as response:
            wheels = json.loads(response.read().decode("utf-8"))
        if not isinstance(wheels, list):
            raise ValueError(f"nightly wheel metadata is not a list: {meta_url}")
        return wheels, repo_url

    def _select_precompiled_wheel_location(
        self,
        wheels: list[dict[str, object]],
        *,
        repo_url: str,
        package: str,
    ) -> str:
        arch = platform.machine()
        for wheel in wheels:
            if wheel.get("package_name") != package:
                continue
            platform_tag = str(wheel.get("platform_tag", ""))
            if arch not in platform_tag:
                continue
            path = wheel.get("path")
            if not isinstance(path, str) or not path:
                continue
            return urljoin(repo_url, path)
        return ""

    def _detect_precompiled_wheel_variant(self) -> str:
        configured = os.environ.get(
            "INFERENCE_BENCH_VLLM_FALLBACK_PRECOMPILED_WHEEL_VARIANT"
        ) or os.environ.get("VLLM_PRECOMPILED_WHEEL_VARIANT")
        if configured:
            return configured
        main_cuda = os.environ.get("VLLM_MAIN_CUDA_VERSION")
        if main_cuda:
            return "cu" + main_cuda.replace(".", "")[:3]
        try:
            result = subprocess.run(
                ["nvidia-smi"],
                capture_output=True,
                text=True,
                check=False,
                timeout=10,
            )
        except (FileNotFoundError, subprocess.SubprocessError):
            return "cu130"
        match = re.search(r"CUDA Version:\s*(\d+)\.(\d+)", result.stdout)
        if not match:
            return "cu130"
        major = int(match.group(1))
        if major <= 12:
            return "cu129"
        return "cu130"

    def _configure_conservative_source_build_retry(self) -> None:
        max_jobs = os.environ.get("INFERENCE_BENCH_VLLM_SOURCE_RETRY_MAX_JOBS", "1")
        os.environ["MAX_JOBS"] = max_jobs
        if "CMAKE_BUILD_TYPE" not in os.environ:
            os.environ["CMAKE_BUILD_TYPE"] = os.environ.get(
                "INFERENCE_BENCH_VLLM_SOURCE_RETRY_CMAKE_BUILD_TYPE",
                "Release",
            )
        if _env_flag("INFERENCE_BENCH_VLLM_SOURCE_RETRY_DISABLE_SCCACHE", True):
            os.environ.setdefault("VLLM_DISABLE_SCCACHE", "1")
        if _env_flag("INFERENCE_BENCH_VLLM_SOURCE_RETRY_DISABLE_COMPILER_LAUNCHER", True):
            self._append_cmake_args(
                "-DCMAKE_C_COMPILER_LAUNCHER=",
                "-DCMAKE_CXX_COMPILER_LAUNCHER=",
                "-DCMAKE_CUDA_COMPILER_LAUNCHER=",
                "-DCMAKE_HIP_COMPILER_LAUNCHER=",
            )
        self._log(
            "[vllm] Source build failed; retrying with "
            f"MAX_JOBS={os.environ.get('MAX_JOBS')} "
            f"CMAKE_BUILD_TYPE={os.environ.get('CMAKE_BUILD_TYPE', '')} "
            f"VLLM_DISABLE_SCCACHE={os.environ.get('VLLM_DISABLE_SCCACHE', '')} "
            f"CMAKE_ARGS={os.environ.get('CMAKE_ARGS', '')}"
        )

    def _append_cmake_args(self, *args: str) -> None:
        existing = os.environ.get("CMAKE_ARGS", "").strip()
        extra = " ".join(arg for arg in args if arg)
        os.environ["CMAKE_ARGS"] = f"{existing} {extra}".strip() if existing else extra

    def _configure_cuda_arch_list(self) -> None:
        if "TORCH_CUDA_ARCH_LIST" in os.environ:
            return
        configured = os.environ.get("INFERENCE_BENCH_VLLM_CUDA_ARCH_LIST") or os.environ.get(
            "INFERENCE_BENCH_CUDA_ARCH_LIST"
        )
        if configured:
            os.environ["TORCH_CUDA_ARCH_LIST"] = configured
            return
        detected = self._detect_cuda_arch_list()
        if not detected:
            return
        os.environ["TORCH_CUDA_ARCH_LIST"] = detected
        self._log(f"[vllm] Using TORCH_CUDA_ARCH_LIST={detected}")

    def _detect_cuda_arch_list(self) -> str:
        try:
            result = subprocess.run(
                [
                    "nvidia-smi",
                    "--query-gpu=index,uuid,compute_cap",
                    "--format=csv,noheader,nounits",
                ],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            return ""
        if result.returncode != 0:
            return ""

        visible = _visible_gpu_tokens()
        rows: list[tuple[str, str, str]] = []
        for line in result.stdout.splitlines():
            parts = [part.strip() for part in line.split(",")]
            if len(parts) != 3:
                continue
            index, uuid, compute_cap = parts
            if visible is not None and index not in visible and uuid not in visible:
                continue
            if compute_cap:
                rows.append((index, uuid, compute_cap))
        if visible is not None and not rows:
            return ""
        archs = sorted({compute_cap for _index, _uuid, compute_cap in rows})
        return ";".join(archs)

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
        server_model = self._server_model(model)
        cmd = [
            self.venv_python, "-m", "vllm.entrypoints.openai.api_server",
            "--model", server_model,
            "--tensor-parallel-size", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
        if server_model != model:
            cmd.extend(["--served-model-name", model])
        gpu_memory_utilization = os.environ.get("INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION")
        if gpu_memory_utilization:
            cmd.extend(["--gpu-memory-utilization", gpu_memory_utilization])
        return cmd

    def _server_env(self) -> dict[str, str]:
        env = super()._server_env()
        libstdcxx_dir = self._find_compatible_libstdcxx_dir(env)
        if libstdcxx_dir:
            self._prepend_env_path(env, "LD_LIBRARY_PATH", libstdcxx_dir)
        return env

    def _find_compatible_libstdcxx_dir(self, env: dict[str, str]) -> str:
        if not _env_flag("INFERENCE_BENCH_VLLM_LIBSTDCXX_FIXUP", True):
            return ""
        required_symbol = env.get("INFERENCE_BENCH_VLLM_LIBSTDCXX_REQUIRED_SYMBOL", "CXXABI_1.3.15")
        for directory in self._candidate_libstdcxx_dirs(env):
            library = directory / "libstdc++.so.6"
            if self._libstdcxx_has_symbol(library, required_symbol):
                return str(directory)
        return ""

    def _candidate_libstdcxx_dirs(self, env: dict[str, str]) -> list[Path]:
        candidates: list[Path] = []
        explicit = env.get("INFERENCE_BENCH_VLLM_LIBSTDCXX_DIR") or env.get(
            "INFERENCE_BENCH_VLLM_LIBSTDCPP_DIR",
            "",
        )
        for raw in explicit.split(os.pathsep):
            if raw:
                candidates.append(Path(raw).expanduser())
        conda_prefix = env.get("CONDA_PREFIX", "")
        if conda_prefix:
            candidates.append(Path(conda_prefix).expanduser() / "lib")
        conda_python = env.get("CONDA_PYTHON_EXE", "")
        if conda_python:
            candidates.append(Path(conda_python).expanduser().resolve().parent.parent / "lib")
        candidates.append(Path(self.venv_python).expanduser().resolve().parent.parent / "lib")
        candidates.append(Path(sys.executable).expanduser().resolve().parent.parent / "lib")
        home = Path.home()
        candidates.extend(sorted((home / ".conda" / "envs").glob("*/lib")))
        candidates.append(Path("/opt/miniconda3/lib"))

        deduped: list[Path] = []
        seen: set[str] = set()
        for candidate in candidates:
            key = str(candidate)
            if key in seen:
                continue
            seen.add(key)
            deduped.append(candidate)
        return deduped

    def _libstdcxx_has_symbol(self, library: Path, symbol: str) -> bool:
        if not symbol:
            return library.exists()
        try:
            return symbol.encode("utf-8") in library.read_bytes()
        except OSError:
            return False

    def _prepend_env_path(self, env: dict[str, str], name: str, directory: str) -> None:
        existing = [part for part in env.get(name, "").split(os.pathsep) if part]
        if directory in existing:
            existing.remove(directory)
        env[name] = os.pathsep.join([directory, *existing])

    def _gpu_memory_wait_fraction(self) -> float | None:
        if "INFERENCE_BENCH_VLLM_MIN_GPU_FREE_FRACTION" in os.environ:
            return _env_float("INFERENCE_BENCH_VLLM_MIN_GPU_FREE_FRACTION", 0.92, minimum=0.0)
        if "INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION" in os.environ:
            return _env_float("INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION", 0.92, minimum=0.0)
        return _env_float("INFERENCE_BENCH_GPU_MEMORY_FREE_FRACTION", 0.92, minimum=0.0)
