from __future__ import annotations

import json
import os
import platform
import re
import shlex
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen

import httpx

from . import register
from .base import (
    Provider,
    _env_flag,
    _env_float,
    _has_cli_option,
    _verify_mooncake_rdma_logs,
    _visible_gpu_tokens,
)

_DEFAULT_FLASHINFER_WORKSPACE_BUFFER_SIZE = 394 * 1024 * 1024
_DEFAULT_COMPILATION_CONFIG = json.dumps(
    {"pass_config": {"fuse_allreduce_rms": False}},
    separators=(",", ":"),
)
_MOONCAKE_TRANSFER_ENGINE_VERSION = "0.3.11.post1"


@register("vllm")
class VllmProvider(Provider):
    name = "vllm"
    repo_url = "https://github.com/vllm-project/vllm.git"
    runtime_import_names = ("vllm",)

    def build(self) -> None:
        if self.is_disaggregated_prefill_decode:
            prohibited_precompiled_overrides = (
                "VLLM_PRECOMPILED_WHEEL_COMMIT",
                "VLLM_PRECOMPILED_WHEEL_LOCATION",
                "INFERENCE_BENCH_VLLM_PRECOMPILED_WHEEL_COMMIT",
                "INFERENCE_BENCH_VLLM_FALLBACK_PRECOMPILED_WHEEL_LOCATION",
            )
            configured = [
                name
                for name in prohibited_precompiled_overrides
                if os.environ.get(name, "").strip()
            ]
            if configured:
                raise ValueError(
                    "Precompiled vLLM commit/location overrides are prohibited "
                    "in a scored disaggregated build: "
                    + ", ".join(configured)
                )
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        self._disable_fastapi_metrics_middleware()
        self._harden_optional_torchcodec_import()
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
            self._verify_precompiled_flash_attn_or_rebuild(precompiled_explicit)
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
                    self._install_deepseek_v4_disaggregated_dependencies()
                    return
                self._log("[vllm] Precompiled wheel install failed; retrying with VLLM_USE_PRECOMPILED=0")
                os.environ["VLLM_USE_PRECOMPILED"] = "0"
                self._configure_source_build_env()
                self._pip_install_source_with_retry()
                self._install_deepseek_v4_disaggregated_dependencies()
                return
            self._pip_install_source_with_retry()
        self._install_deepseek_v4_disaggregated_dependencies()

    def _verify_precompiled_flash_attn_or_rebuild(self, precompiled_explicit: bool) -> None:
        """Rebuild from source if a precompiled install lacks working flash-attn.

        A precompiled wheel can `pip install` cleanly yet ship flash-attn CUDA
        extensions (_vllm_fa2_C/_vllm_fa3_C) that don't match the runtime CUDA
        (e.g. a cu12x wheel on a CUDA-13 image), so vllm.vllm_flash_attn only
        ImportErrors at server start -- after build() has "succeeded". Detect
        that here and fall back to the source build, which compiles matching
        extensions. Skipped when precompiled was explicitly requested or the
        source-build fallback is disabled.
        """
        if not _env_flag("VLLM_USE_PRECOMPILED", True):
            return
        if precompiled_explicit or not _env_flag(
            "INFERENCE_BENCH_VLLM_FALLBACK_SOURCE_BUILD", True
        ):
            return
        check = subprocess.run(
            [self.venv_python, "-c", "import vllm.vllm_flash_attn"],
            capture_output=True,
            text=True,
        )
        if check.returncode == 0:
            return
        self._log(
            "[vllm] precompiled install lacks working flash-attn extensions "
            "(_vllm_fa2_C/_vllm_fa3_C); rebuilding from source with "
            "VLLM_USE_PRECOMPILED=0"
        )
        os.environ["VLLM_USE_PRECOMPILED"] = "0"
        self._configure_source_build_env()
        self._pip_install_source_with_retry()

    def _configured_for_deepseek_v4(self) -> bool:
        model = str(getattr(self, "_configured_model", "") or "")
        return "deepseek-v4" in model.lower().replace("_", "-")

    def _install_deepseek_v4_disaggregated_dependencies(self) -> None:
        if not (
            self.is_disaggregated_prefill_decode
            and self._configured_for_deepseek_v4()
        ):
            return
        package = "mooncake-transfer-engine"
        if self._detect_precompiled_wheel_variant() == "cu130":
            package = "mooncake-transfer-engine-cuda13"
        self._pip_install(f"{package}=={_MOONCAKE_TRANSFER_ENGINE_VERSION}")

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
                ["/usr/bin/nvidia-smi"],
                env=(
                    self._trusted_system_probe_env()
                    if self.is_disaggregated_prefill_decode
                    else None
                ),
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
                    "/usr/bin/nvidia-smi",
                    "--query-gpu=index,uuid,compute_cap",
                    "--format=csv,noheader,nounits",
                ],
                env=(
                    self._trusted_system_probe_env()
                    if self.is_disaggregated_prefill_decode
                    else None
                ),
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

    def _harden_optional_torchcodec_import(self) -> None:
        video_py = self.repo_dir / "vllm" / "multimodal" / "video.py"
        if not video_py.exists():
            return
        text = video_py.read_text()
        patched = """try:
    from torchcodec.decoders import VideoDecoder
except (ImportError, OSError, RuntimeError):
    # TorchCodec can be installed but unusable when FFmpeg shared libraries
    # are absent or incompatible with the installed PyTorch. Treat that like a
    # missing optional video backend; text-only OpenAI serving does not need it.
    VideoDecoder = PlaceholderModule("torchcodec").placeholder_attr(  # type: ignore[assignment]
        "decoders.VideoDecoder",
    )
"""
        if patched in text:
            return
        old_with_comma = """try:
    from torchcodec.decoders import VideoDecoder
except ImportError:
    VideoDecoder = PlaceholderModule("torchcodec").placeholder_attr(  # type: ignore[assignment]
        "decoders.VideoDecoder",
    )
"""
        old_without_comma = """try:
    from torchcodec.decoders import VideoDecoder
except ImportError:
    VideoDecoder = PlaceholderModule("torchcodec").placeholder_attr(  # type: ignore[assignment]
        "decoders.VideoDecoder"
    )
"""
        direct_import = "from torchcodec.decoders import VideoDecoder"
        if old_with_comma in text:
            video_py.write_text(text.replace(old_with_comma, patched))
        elif old_without_comma in text:
            video_py.write_text(text.replace(old_without_comma, patched))
        elif "except (ImportError, OSError, RuntimeError):" not in text:
            lines = text.splitlines(keepends=True)
            for index, line in enumerate(lines):
                stripped = line.lstrip(" \t")
                if stripped.strip() != direct_import:
                    continue
                indent = line[: len(line) - len(stripped)]
                indented_patch = "\n".join(
                    f"{indent}{patched_line}"
                    for patched_line in patched.rstrip("\n").splitlines()
                )
                if line.endswith("\n"):
                    indented_patch += "\n"
                lines[index] = indented_patch
                video_py.write_text("".join(lines))
                break

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        if self.is_disaggregated_prefill_decode:
            return self._disaggregated_server_cmd(model, port)
        return self._server_instance_cmd(model, tp=tp, port=port)

    def _server_instance_cmd(
        self,
        model: str,
        *,
        tp: int,
        port: int,
        kv_transfer_config: dict | None = None,
        gpu_memory_utilization: str | None = None,
    ) -> list[str]:
        server_model = self._server_model(model)
        cmd = [
            self.server_python, "-m", "vllm.entrypoints.openai.api_server",
            "--model", server_model,
            "--tensor-parallel-size", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
        if server_model == model and self.model_revision:
            cmd.extend(["--revision", self.model_revision])
        if server_model != model:
            cmd.extend(["--served-model-name", model])
        if gpu_memory_utilization is None:
            gpu_memory_utilization = os.environ.get(
                "INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION"
            )
        if gpu_memory_utilization:
            cmd.extend(["--gpu-memory-utilization", gpu_memory_utilization])
        extra_args = os.environ.get("INFERENCE_BENCH_VLLM_SERVER_ARGS", "").strip()
        extra_cmd = shlex.split(extra_args) if extra_args else []
        if kv_transfer_config is not None:
            if extra_cmd:
                raise ValueError(
                    "INFERENCE_BENCH_VLLM_SERVER_ARGS is prohibited in the "
                    "scored disaggregated evaluation"
                )
            cmd.extend(
                [
                    "--host",
                    "127.0.0.1",
                    "--kv-transfer-config",
                    json.dumps(kv_transfer_config, separators=(",", ":")),
                ]
            )
        if self._should_disable_allreduce_rms_fusion(extra_cmd):
            cmd.extend(["--compilation-config", _DEFAULT_COMPILATION_CONFIG])
        cmd.extend(extra_cmd)
        return cmd

    def _disaggregated_server_cmd(self, model: str, port: int) -> list[str]:
        if self._configured_for_deepseek_v4():
            return self._mooncake_disaggregated_server_cmd(model, port)
        prefill_tp = int(self.prefill_tensor_parallel_size or 0)
        decode_tp = int(self.decode_tensor_parallel_size or 0)
        prefill_env, decode_env = self._disaggregated_gpu_envs()
        prefill_env["VLLM_HOST_IP"] = "127.0.0.1"
        decode_env["VLLM_HOST_IP"] = "127.0.0.1"
        (
            prefill_port,
            decode_port,
            registration_port,
        ) = self._reserve_local_ports(3, excluded={port})
        kv_port_base = self._reserve_local_port_block(
            prefill_tp + decode_tp,
            excluded={port, prefill_port, decode_port, registration_port},
        )
        prefill_kv_port = kv_port_base
        decode_kv_port = kv_port_base + prefill_tp

        def transfer_config(*, role: str, http_port: int, kv_port: int) -> dict:
            return {
                "kv_connector": "P2pNcclConnector",
                "kv_role": role,
                "kv_buffer_size": "1e1" if role == "kv_producer" else "8e9",
                "kv_port": kv_port,
                "kv_connector_extra_config": {
                    "proxy_ip": "127.0.0.1",
                    "proxy_port": registration_port,
                    "http_ip": "127.0.0.1",
                    "http_port": http_port,
                    "send_type": "PUT_ASYNC",
                    "nccl_num_channels": "16",
                },
            }

        common_memory = os.environ.get("INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION")
        prefill_memory = (
            os.environ.get("INFERENCE_BENCH_VLLM_PREFILL_GPU_MEMORY_UTILIZATION")
            or common_memory
            or "0.90"
        )
        decode_memory = (
            os.environ.get("INFERENCE_BENCH_VLLM_DECODE_GPU_MEMORY_UTILIZATION")
            or common_memory
            or "0.70"
        )
        prefill_cmd = self._server_instance_cmd(
            model,
            tp=prefill_tp,
            port=prefill_port,
            kv_transfer_config=transfer_config(
                role="kv_producer",
                http_port=prefill_port,
                kv_port=prefill_kv_port,
            ),
            gpu_memory_utilization=prefill_memory,
        )
        decode_cmd = self._server_instance_cmd(
            model,
            tp=decode_tp,
            port=decode_port,
            kv_transfer_config=transfer_config(
                role="kv_consumer",
                http_port=decode_port,
                kv_port=decode_kv_port,
            ),
            gpu_memory_utilization=decode_memory,
        )
        proxy_script = Path(__file__).resolve().parents[1] / "vllm_disagg_proxy.py"
        proxy_cmd = [
            self.server_python,
            str(proxy_script),
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
            "--registration-host",
            "127.0.0.1",
            "--registration-port",
            str(registration_port),
        ]
        spec = {
            "schema_version": 1,
            "provider": self.name,
            "deployment_mode": self.deployment_mode,
            "prefill_tensor_parallel_size": prefill_tp,
            "decode_tensor_parallel_size": decode_tp,
            "transport": "P2pNcclConnector",
            "phases": [
                {
                    "settle_seconds": 1.0,
                    "components": [
                        {
                            "name": "proxy",
                            "command": proxy_cmd,
                            "log_path": str(self.build_dir / "vllm_disagg_proxy.log"),
                        }
                    ],
                },
                {
                    "components": [
                        {
                            "name": "prefill",
                            "command": prefill_cmd,
                            "env": prefill_env,
                            "cwd": str(self.repo_dir),
                            "ready_url": f"http://127.0.0.1:{prefill_port}/v1/models",
                            "log_path": str(self.build_dir / "vllm_disagg_prefill.log"),
                        },
                        {
                            "name": "decode",
                            "command": decode_cmd,
                            "env": decode_env,
                            "cwd": str(self.repo_dir),
                            "ready_url": f"http://127.0.0.1:{decode_port}/v1/models",
                            "log_path": str(self.build_dir / "vllm_disagg_decode.log"),
                        },
                    ]
                },
            ],
        }
        self._disagg_connector = "P2pNcclConnector"
        return self._disaggregated_supervisor_cmd(spec)

    def _mooncake_disaggregated_server_cmd(
        self,
        model: str,
        port: int,
    ) -> list[str]:
        prefill_tp = int(self.prefill_tensor_parallel_size or 0)
        decode_tp = int(self.decode_tensor_parallel_size or 0)
        prefill_env, decode_env = self._disaggregated_gpu_envs()
        prefill_port, decode_port, bootstrap_port = self._reserve_local_ports(
            3,
            excluded={port},
        )
        for role_env in (prefill_env, decode_env):
            role_env.update(
                {
                    "MC_FORCE_HCA": "1",
                    "MC_LOG_LEVEL": "INFO",
                    "MC_RPC_PROTOCOL": "tcp",
                    "MOONCAKE_DEVICE": "",
                    "MOONCAKE_PROTOCOL": "rdma",
                }
            )
        prefill_env["VLLM_MOONCAKE_BOOTSTRAP_PORT"] = str(bootstrap_port)
        common_memory = os.environ.get("INFERENCE_BENCH_VLLM_GPU_MEMORY_UTILIZATION")
        prefill_memory = (
            os.environ.get("INFERENCE_BENCH_VLLM_PREFILL_GPU_MEMORY_UTILIZATION")
            or common_memory
            or "0.90"
        )
        decode_memory = (
            os.environ.get("INFERENCE_BENCH_VLLM_DECODE_GPU_MEMORY_UTILIZATION")
            or common_memory
            or "0.70"
        )
        prefill_cmd = self._server_instance_cmd(
            model,
            tp=prefill_tp,
            port=prefill_port,
            kv_transfer_config={
                "kv_connector": "MooncakeConnector",
                "kv_role": "kv_producer",
                "kv_connector_extra_config": {"mooncake_protocol": "rdma"},
            },
            gpu_memory_utilization=prefill_memory,
        )
        decode_cmd = self._server_instance_cmd(
            model,
            tp=decode_tp,
            port=decode_port,
            kv_transfer_config={
                "kv_connector": "MooncakeConnector",
                "kv_role": "kv_consumer",
                "kv_connector_extra_config": {"mooncake_protocol": "rdma"},
            },
            gpu_memory_utilization=decode_memory,
        )
        proxy_script = Path(__file__).resolve().parents[1] / "vllm_mooncake_proxy.py"
        proxy_cmd = [
            self.server_python,
            str(proxy_script),
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
            "--prefill-url",
            f"http://127.0.0.1:{prefill_port}",
            "--decode-url",
            f"http://127.0.0.1:{decode_port}",
            "--bootstrap-port",
            str(bootstrap_port),
        ]
        spec = {
            "schema_version": 1,
            "provider": self.name,
            "deployment_mode": self.deployment_mode,
            "prefill_tensor_parallel_size": prefill_tp,
            "decode_tensor_parallel_size": decode_tp,
            "transport": "MooncakeConnector",
            "mooncake_protocol": "rdma",
            "mooncake_data_plane_transport": "rdma",
            "mooncake_transfer_engine_version": _MOONCAKE_TRANSFER_ENGINE_VERSION,
            "phases": [
                {
                    "components": [
                        {
                            "name": "prefill",
                            "command": prefill_cmd,
                            "env": prefill_env,
                            "cwd": str(self.repo_dir),
                            "ready_url": f"http://127.0.0.1:{prefill_port}/health",
                            "log_path": str(
                                self.build_dir / "vllm_disagg_prefill.log"
                            ),
                        },
                        {
                            "name": "decode",
                            "command": decode_cmd,
                            "env": decode_env,
                            "cwd": str(self.repo_dir),
                            "ready_url": f"http://127.0.0.1:{decode_port}/health",
                            "log_path": str(
                                self.build_dir / "vllm_disagg_decode.log"
                            ),
                        },
                    ]
                },
                {
                    "components": [
                        {
                            "name": "proxy",
                            "command": proxy_cmd,
                            "log_path": str(
                                self.build_dir / "vllm_disagg_proxy.log"
                            ),
                        }
                    ]
                },
            ],
        }
        self._disagg_connector = "MooncakeConnector"
        return self._disaggregated_supervisor_cmd(spec)

    def _should_disable_allreduce_rms_fusion(self, extra_cmd: list[str]) -> bool:
        if self.is_disaggregated_prefill_decode:
            return False
        if not _env_flag("INFERENCE_BENCH_VLLM_DISABLE_ALLREDUCE_RMS_FUSION", True):
            return False
        return not _has_cli_option(extra_cmd, "--compilation-config")

    def verify_runtime_integrity(self) -> dict[str, object]:
        if not self.is_disaggregated_prefill_decode:
            return {}
        response = httpx.get(f"http://127.0.0.1:{self._port}/health", timeout=10)
        response.raise_for_status()
        audit = response.json()
        count_names = (
            "request_pairs",
            "prefill_completed",
            "decode_started",
            "decode_completed",
        )
        counts = {name: int(audit.get(name, 0)) for name in count_names}
        if counts["request_pairs"] <= 0 or len(set(counts.values())) != 1:
            raise RuntimeError(
                "[vllm] Disaggregated proxy did not observe matching completed "
                f"prefill/decode request pairs: {counts}"
            )
        if int(audit.get("decode_aborted", 0)) or int(audit.get("upstream_errors", 0)):
            raise RuntimeError(f"[vllm] Disaggregated proxy reported errors: {audit}")
        connector = str(
            getattr(self, "_disagg_connector", "P2pNcclConnector")
        )
        observation = {
            "kv_handoff_check": "passed",
            "routed_request_pairs": counts["request_pairs"],
            "registered_prefill_instances": int(audit.get("prefill_instances", 0)),
            "registered_decode_instances": int(audit.get("decode_instances", 0)),
            "transport": connector,
        }
        if connector == "MooncakeConnector":
            observation.update(self._verify_mooncake_transfer_log())
        return observation

    def _verify_mooncake_transfer_log(self) -> dict[str, object]:
        log_paths = {
            "prefill": self.build_dir / "vllm_disagg_prefill.log",
            "decode": self.build_dir / "vllm_disagg_decode.log",
        }
        observation = _verify_mooncake_rdma_logs(log_paths, provider=self.name)
        rows: list[dict[str, float]] = []
        for log_path in log_paths.values():
            text = log_path.read_text(encoding="utf-8", errors="replace")
            for line in text.splitlines():
                marker = "KV Transfer metrics:"
                if marker not in line:
                    continue
                fields: dict[str, float] = {}
                for item in line.split(marker, 1)[1].split(","):
                    name, separator, raw_value = item.partition("=")
                    if not separator:
                        continue
                    try:
                        fields[name.strip()] = float(raw_value.strip())
                    except ValueError:
                        continue
                if fields:
                    rows.append(fields)
        successful = int(
            sum(row.get("Num successful transfers", 0.0) for row in rows)
        )
        failed_transfers = int(
            sum(row.get("Num failed transfers", 0.0) for row in rows)
        )
        failed_recvs = int(sum(row.get("Num failed recvs", 0.0) for row in rows))
        expired = int(sum(row.get("Num KV expired reqs", 0.0) for row in rows))
        transferred_mb = sum(
            row.get("Num successful transfers", 0.0)
            * row.get("Avg MB per transfer", 0.0)
            for row in rows
        )
        if successful <= 0 or transferred_mb <= 0:
            raise RuntimeError(
                "[vllm] Mooncake reported no successful positive-byte KV transfers"
            )
        if failed_transfers or failed_recvs or expired:
            raise RuntimeError(
                "[vllm] Mooncake reported transfer failures: "
                f"failed_transfers={failed_transfers}, failed_recvs={failed_recvs}, "
                f"expired={expired}"
            )
        observation.update({
            "native_kv_transfer_check": "passed",
            "native_successful_transfers": successful,
            "native_transferred_mb_estimate": transferred_mb,
            "native_failed_transfers": failed_transfers,
            "native_failed_recvs": failed_recvs,
            "native_expired_requests": expired,
        })
        return observation

    def _server_env(self) -> dict[str, str]:
        env = super()._server_env()
        env.setdefault(
            "VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE",
            env.get(
                "INFERENCE_BENCH_VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE",
                str(_DEFAULT_FLASHINFER_WORKSPACE_BUFFER_SIZE),
            ),
        )
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
        candidates.append(Path(self.server_python).expanduser().resolve().parent.parent / "lib")
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
