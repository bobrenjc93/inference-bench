from __future__ import annotations

import os
import shlex
import subprocess

import httpx

from . import register
from .base import Provider, _env_flag, _env_float, _verify_mooncake_rdma_logs

_MOONCAKE_TRANSFER_ENGINE_VERSION = "0.3.11.post1"


@register("sglang")
class SglangProvider(Provider):
    name = "sglang"
    repo_url = "https://github.com/sgl-project/sglang.git"

    @property
    def runtime_import_names(self) -> tuple[str, ...]:
        if self.is_disaggregated_prefill_decode:
            return ("sglang", "sglang_router")
        return ("sglang",)

    @property
    def _python_dir(self):
        return self.repo_dir / "python"

    def build(self) -> None:
        self._reject_scored_environment_overrides(
            prefixes=("INFERENCE_BENCH_SGLANG_", "SGLANG_"),
        )
        self._create_venv()
        self._pip_install("--upgrade", "pip")
        try:
            self._pip_install("-e", ".", cwd=self._python_dir)
        except subprocess.CalledProcessError:
            if self.is_scored_evaluation or not _env_flag(
                "INFERENCE_BENCH_SGLANG_FALLBACK_BINARY_WHEEL", True
            ):
                raise
            self._pip_install_binary_wheel()
        self._harden_custom_allreduce_tvm_ffi_compat()
        if self.is_disaggregated_prefill_decode:
            self._install_disaggregated_dependencies()

    def _harden_custom_allreduce_tvm_ffi_compat(self) -> None:
        ipc_header = (
            self._python_dir
            / "sglang"
            / "kernels"
            / "jit"
            / "csrc"
            / "distributed"
            / "ipc.cuh"
        )
        if not ipc_header.is_file():
            return
        text = ipc_header.read_text()
        replacements = {
            "to_ipc_handle(get<0>(pair))": "to_ipc_handle(pair.template get<0>())",
            "const auto offset = get<1>(pair);": (
                "const auto offset = pair.template get<1>();"
            ),
        }
        patched = text
        for old, new in replacements.items():
            patched = patched.replace(old, new)
        if patched != text:
            ipc_header.write_text(patched)

    def _install_disaggregated_dependencies(self) -> None:
        router_dir = (
            self.repo_dir
            / "sgl-model-gateway"
            / "bindings"
            / "python"
        )
        self._pip_install("-e", ".", cwd=router_dir)
        backend = self._disaggregation_transfer_backend()
        if backend == "mooncake":
            package = "mooncake-transfer-engine"
            if self._cuda_major_version() >= 13:
                package = "mooncake-transfer-engine-cuda13"
            self._pip_install(f"{package}=={_MOONCAKE_TRANSFER_ENGINE_VERSION}")

    def _cuda_major_version(self) -> int:
        command = [
            self.venv_python,
            "-c",
            "import torch; print(torch.version.cuda or '')",
        ]
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError as exc:
            raise RuntimeError(
                "Could not run SGLang's Python interpreter to determine its "
                "PyTorch CUDA version"
            ) from exc
        value = result.stdout.strip()
        if result.returncode != 0 or not value:
            raise RuntimeError(
                "Could not determine SGLang's PyTorch CUDA major version for "
                "the Mooncake package selection"
            )
        try:
            return int(value.split(".", 1)[0])
        except ValueError as exc:
            raise RuntimeError(f"Invalid PyTorch CUDA version: {value!r}") from exc

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
        if self.is_disaggregated_prefill_decode:
            return self._disaggregated_server_cmd(model, port)
        return self._server_instance_cmd(model, tp=tp, port=port)

    def _server_env(self) -> dict[str, str]:
        self._reject_scored_environment_overrides(
            prefixes=("INFERENCE_BENCH_SGLANG_", "SGLANG_"),
        )
        return super()._server_env()

    def _server_instance_cmd(
        self,
        model: str,
        *,
        tp: int,
        port: int,
        role: str | None = None,
        bootstrap_port: int | None = None,
        transfer_backend: str | None = None,
    ) -> list[str]:
        self._reject_scored_environment_overrides(
            prefixes=("INFERENCE_BENCH_SGLANG_", "SGLANG_"),
        )
        server_model = self._server_model(model)
        cmd = [
            self.server_python, "-m", "sglang.launch_server",
            "--model-path", server_model,
            "--tp-size", str(tp),
            "--port", str(port),
            "--trust-remote-code",
        ]
        if server_model == model and self.model_revision:
            cmd.extend(["--revision", self.model_revision])
        if server_model != model:
            cmd.extend(["--served-model-name", model])
        mem_fraction = os.environ.get("INFERENCE_BENCH_SGLANG_MEM_FRACTION_STATIC")
        if mem_fraction:
            cmd.extend(["--mem-fraction-static", mem_fraction])
        extra_args = os.environ.get("INFERENCE_BENCH_SGLANG_SERVER_ARGS", "").strip()
        extra_cmd = shlex.split(extra_args) if extra_args else []
        if self.is_scored_evaluation and extra_cmd:
            raise ValueError(
                "INFERENCE_BENCH_SGLANG_SERVER_ARGS is prohibited in a scored "
                "evaluation"
            )
        if role is not None:
            cmd.extend(
                [
                    "--host",
                    "127.0.0.1",
                    "--disaggregation-mode",
                    role,
                    "--disaggregation-bootstrap-port",
                    str(bootstrap_port),
                    "--disaggregation-transfer-backend",
                    str(transfer_backend),
                ]
            )
        cmd.extend(extra_cmd)
        return cmd

    def _disaggregation_transfer_backend(self) -> str:
        backend = os.environ.get(
            "INFERENCE_BENCH_SGLANG_DISAGG_TRANSFER_BACKEND",
            "mooncake",
        ).strip().lower()
        if backend == "fake":
            raise ValueError(
                "SGLang's fake disaggregation backend does not transfer KV state "
                "and is prohibited in scored evaluations"
            )
        if backend not in {"mooncake", "nixl"}:
            raise ValueError(f"Unsupported SGLang disaggregation backend: {backend!r}")
        return backend

    def _disaggregated_server_cmd(self, model: str, port: int) -> list[str]:
        prefill_tp = int(self.prefill_tensor_parallel_size or 0)
        decode_tp = int(self.decode_tensor_parallel_size or 0)
        prefill_env, decode_env = self._disaggregated_gpu_envs()
        backend = self._disaggregation_transfer_backend()
        if backend == "mooncake":
            for role_env in (prefill_env, decode_env):
                role_env.update(
                    {
                        "MC_FORCE_HCA": "1",
                        "MC_LOG_LEVEL": "INFO",
                        "MC_RPC_PROTOCOL": "tcp",
                        "MOONCAKE_DEVICE": "",
                        "MOONCAKE_PROTOCOL": "rdma",
                        "SGLANG_MOONCAKE_CUSTOM_MEM_POOL": "INTRA_NODE_NVLINK",
                    }
                )
        prefill_port, decode_port, bootstrap_port = self._reserve_local_ports(
            3, excluded={port}
        )
        self._disagg_prefill_port = prefill_port
        self._disagg_transfer_backend = backend
        prefill_cmd = self._server_instance_cmd(
            model,
            tp=prefill_tp,
            port=prefill_port,
            role="prefill",
            bootstrap_port=bootstrap_port,
            transfer_backend=backend,
        )
        decode_cmd = self._server_instance_cmd(
            model,
            tp=decode_tp,
            port=decode_port,
            role="decode",
            bootstrap_port=bootstrap_port,
            transfer_backend=backend,
        )
        router_cmd = [
            self.server_python,
            "-m",
            "sglang_router.launch_router",
            "--pd-disaggregation",
            "--prefill",
            f"http://127.0.0.1:{prefill_port}",
            str(bootstrap_port),
            "--decode",
            f"http://127.0.0.1:{decode_port}",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
        ]
        spec = {
            "schema_version": 1,
            "provider": self.name,
            "deployment_mode": self.deployment_mode,
            "prefill_tensor_parallel_size": prefill_tp,
            "decode_tensor_parallel_size": decode_tp,
            "transport": backend,
            "mooncake_protocol": (
                "rdma" if backend == "mooncake" else None
            ),
            "mooncake_data_plane_transport": (
                "rdma" if backend == "mooncake" else None
            ),
            "router_source": "local_sglang_checkout",
            "mooncake_transfer_engine_version": (
                _MOONCAKE_TRANSFER_ENGINE_VERSION
                if backend == "mooncake"
                else None
            ),
            "phases": [
                {
                    "components": [
                        {
                            "name": "prefill",
                            "command": prefill_cmd,
                            "env": prefill_env,
                            "cwd": str(self.repo_dir),
                            "ready_url": f"http://127.0.0.1:{prefill_port}/health",
                            "log_path": str(self.build_dir / "sglang_disagg_prefill.log"),
                        },
                        {
                            "name": "decode",
                            "command": decode_cmd,
                            "env": decode_env,
                            "cwd": str(self.repo_dir),
                            "ready_url": f"http://127.0.0.1:{decode_port}/health",
                            "log_path": str(self.build_dir / "sglang_disagg_decode.log"),
                        },
                    ]
                },
                {
                    "components": [
                        {
                            "name": "router",
                            "command": router_cmd,
                            "cwd": str(self.repo_dir),
                            "log_path": str(self.build_dir / "sglang_disagg_router.log"),
                        }
                    ]
                },
            ],
        }
        return self._disaggregated_supervisor_cmd(spec)

    def verify_runtime_integrity(self) -> dict[str, object]:
        if not self.is_disaggregated_prefill_decode:
            return self._verify_custom_allreduce_logs(
                {"standard": getattr(self, "_log_path", None)}
            )
        prefill_port = getattr(self, "_disagg_prefill_port", None)
        if not isinstance(prefill_port, int):
            raise RuntimeError("[sglang] Prefill runtime endpoint is unavailable")
        response = httpx.get(
            f"http://127.0.0.1:{prefill_port}/v1/loads?include=disagg",
            timeout=10,
        )
        response.raise_for_status()
        payload = response.json()
        loads = payload.get("loads") if isinstance(payload, dict) else None
        observations: list[tuple[float, float]] = []
        if isinstance(loads, list):
            for load in loads:
                if not isinstance(load, dict):
                    continue
                disagg = load.get("disaggregation")
                if not isinstance(disagg, dict) or disagg.get("mode") != "prefill":
                    continue
                speed = _nonnegative_float(disagg.get("kv_transfer_speed_gb_s"))
                latency = _nonnegative_float(disagg.get("kv_transfer_latency_ms"))
                observations.append((speed, latency))
        if not observations or not any(speed > 0 or latency > 0 for speed, latency in observations):
            raise RuntimeError(
                "[sglang] Prefill runtime reported no completed KV transfer: "
                f"{payload!r}"
            )
        observation = {
            "kv_handoff_check": "passed",
            "observed_kv_transfer_speed_gb_s": max(speed for speed, _ in observations),
            "observed_kv_transfer_latency_ms": max(latency for _, latency in observations),
            "transport": str(getattr(self, "_disagg_transfer_backend", "unknown")),
        }
        observation.update(
            self._verify_custom_allreduce_logs(
                {
                    "prefill": self.build_dir / "sglang_disagg_prefill.log",
                    "decode": self.build_dir / "sglang_disagg_decode.log",
                }
            )
        )
        backend = str(getattr(self, "_disagg_transfer_backend", "unknown"))
        if backend == "mooncake":
            observation.update(
                _verify_mooncake_rdma_logs(
                    {
                        "prefill": self.build_dir / "sglang_disagg_prefill.log",
                        "decode": self.build_dir / "sglang_disagg_decode.log",
                    },
                    provider=self.name,
                )
            )
        return observation

    def _verify_custom_allreduce_logs(
        self,
        log_paths: dict[str, object],
    ) -> dict[str, object]:
        if not self.is_scored_evaluation:
            return {}
        verified_roles: list[str] = []
        for role, raw_path in log_paths.items():
            if raw_path is None:
                raise RuntimeError(f"[sglang] {role} server log is unavailable")
            try:
                log_text = raw_path.read_text(errors="replace")
            except (AttributeError, OSError) as exc:
                raise RuntimeError(
                    f"[sglang] Could not read {role} server log: {raw_path}"
                ) from exc
            if "Setup Custom allreduce failed" in log_text:
                raise RuntimeError(
                    f"[sglang] {role} server fell back from custom all-reduce"
                )
            if "All Reduce config:" not in log_text:
                raise RuntimeError(
                    f"[sglang] {role} server did not report an active custom "
                    "all-reduce configuration"
                )
            verified_roles.append(role)
        return {
            "custom_allreduce_check": "passed",
            "custom_allreduce_roles": verified_roles,
        }

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


def _nonnegative_float(value: object) -> float:
    if isinstance(value, bool):
        return 0.0
    if isinstance(value, (int, float)):
        return max(0.0, float(value))
    return 0.0
