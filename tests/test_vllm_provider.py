from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from unittest import mock

from inference_bench.providers.vllm import VllmProvider


class VllmProviderTest(unittest.TestCase):
    def test_precompiled_failure_retries_nightly_before_source(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        install_envs: list[dict[str, str]] = []

        def fake_pip_install(*args, cwd=None):  # noqa: ANN001
            del cwd
            if args == ("--upgrade", "pip"):
                return None
            install_envs.append(
                {
                    "VLLM_USE_PRECOMPILED": os.environ.get("VLLM_USE_PRECOMPILED", ""),
                    "VLLM_PRECOMPILED_WHEEL_COMMIT": os.environ.get(
                        "VLLM_PRECOMPILED_WHEEL_COMMIT", ""
                    ),
                    "VLLM_PRECOMPILED_WHEEL_LOCATION": os.environ.get(
                        "VLLM_PRECOMPILED_WHEEL_LOCATION", ""
                    ),
                    "CMAKE_BUILD_TYPE": os.environ.get("CMAKE_BUILD_TYPE", ""),
                }
            )
            if len(install_envs) == 1:
                raise subprocess.CalledProcessError(1, ["pip", "install"])

        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_create_venv", return_value=None),
            mock.patch.object(provider, "_disable_fastapi_metrics_middleware", return_value=None),
            mock.patch.object(provider, "_configure_cuda_arch_list", return_value=None),
            mock.patch.object(
                provider,
                "_resolve_precompiled_nightly_wheel_location",
                return_value="https://wheels.vllm.ai/nightly/cu130/vllm/vllm.whl",
            ),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
        ):
            provider.build()

        self.assertEqual(
            install_envs,
            [
                {
                    "VLLM_USE_PRECOMPILED": "1",
                    "VLLM_PRECOMPILED_WHEEL_COMMIT": "",
                    "VLLM_PRECOMPILED_WHEEL_LOCATION": "",
                    "CMAKE_BUILD_TYPE": "",
                },
                {
                    "VLLM_USE_PRECOMPILED": "1",
                    "VLLM_PRECOMPILED_WHEEL_COMMIT": "",
                    "VLLM_PRECOMPILED_WHEEL_LOCATION": "https://wheels.vllm.ai/nightly/cu130/vllm/vllm.whl",
                    "CMAKE_BUILD_TYPE": "",
                },
            ],
        )

    def test_explicit_precompiled_commit_skips_nightly_retry(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        install_envs: list[dict[str, str]] = []

        def fake_pip_install(*args, cwd=None):  # noqa: ANN001
            del cwd
            if args == ("--upgrade", "pip"):
                return None
            install_envs.append(
                {
                    "VLLM_USE_PRECOMPILED": os.environ.get("VLLM_USE_PRECOMPILED", ""),
                    "VLLM_PRECOMPILED_WHEEL_COMMIT": os.environ.get(
                        "VLLM_PRECOMPILED_WHEEL_COMMIT", ""
                    ),
                }
            )
            if len(install_envs) == 1:
                raise subprocess.CalledProcessError(1, ["pip", "install"])

        with (
            mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_VLLM_PRECOMPILED_WHEEL_COMMIT": "abc123"},
                clear=True,
            ),
            mock.patch.object(provider, "_create_venv", return_value=None),
            mock.patch.object(provider, "_disable_fastapi_metrics_middleware", return_value=None),
            mock.patch.object(provider, "_configure_cuda_arch_list", return_value=None),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
            mock.patch.object(provider, "_configure_source_build_env", return_value=None) as source_env,
        ):
            provider.build()

        self.assertEqual(
            install_envs,
            [
                {
                    "VLLM_USE_PRECOMPILED": "1",
                    "VLLM_PRECOMPILED_WHEEL_COMMIT": "abc123",
                },
                {
                    "VLLM_USE_PRECOMPILED": "0",
                    "VLLM_PRECOMPILED_WHEEL_COMMIT": "abc123",
                },
            ],
        )
        self.assertGreaterEqual(source_env.call_count, 1)

    def test_select_precompiled_wheel_location_matches_platform(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        wheels = [
            {
                "package_name": "vllm",
                "platform_tag": "manylinux1_aarch64",
                "path": "../vllm-aarch64.whl",
            },
            {
                "package_name": "vllm",
                "platform_tag": "manylinux1_x86_64",
                "path": "../vllm-x86_64.whl",
            },
        ]

        with mock.patch("inference_bench.providers.vllm.platform.machine", return_value="x86_64"):
            location = provider._select_precompiled_wheel_location(
                wheels,
                repo_url="https://wheels.vllm.ai/nightly/cu130/vllm/",
                package="vllm",
            )

        self.assertEqual(
            location,
            "https://wheels.vllm.ai/nightly/cu130/vllm-x86_64.whl",
        )

    def test_server_cmd_appends_env_extra_args(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_VLLM_SERVER_ARGS": "--disable-custom-all-reduce --max-num-seqs 256"},
            clear=True,
        ):
            cmd = provider._server_cmd("model", tp=8, port=9000)

        self.assertIn("--disable-custom-all-reduce", cmd)
        self.assertEqual(cmd[cmd.index("--max-num-seqs") + 1], "256")
        self.assertEqual(
            json.loads(cmd[cmd.index("--compilation-config") + 1]),
            {"pass_config": {"fuse_allreduce_rms": False}},
        )

    def test_server_cmd_disables_allreduce_rms_fusion_by_default(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with mock.patch.dict(os.environ, {}, clear=True):
            cmd = provider._server_cmd("model", tp=8, port=9000)

        self.assertEqual(
            json.loads(cmd[cmd.index("--compilation-config") + 1]),
            {"pass_config": {"fuse_allreduce_rms": False}},
        )

    def test_server_cmd_respects_explicit_compilation_config(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        configured = '{"pass_config":{"fuse_allreduce_rms":true}}'
        with mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_VLLM_SERVER_ARGS": f"--compilation-config '{configured}'"},
            clear=True,
        ):
            cmd = provider._server_cmd("model", tp=8, port=9000)

        self.assertEqual(cmd.count("--compilation-config"), 1)
        self.assertEqual(
            json.loads(cmd[cmd.index("--compilation-config") + 1]),
            {"pass_config": {"fuse_allreduce_rms": True}},
        )

    def test_server_cmd_can_keep_allreduce_rms_fusion_default(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_VLLM_DISABLE_ALLREDUCE_RMS_FUSION": "0"},
            clear=True,
        ):
            cmd = provider._server_cmd("model", tp=8, port=9000)

        self.assertNotIn("--compilation-config", cmd)

    def test_server_env_sets_flashinfer_workspace_default(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with mock.patch.dict(os.environ, {}, clear=True):
            env = provider._server_env()

        self.assertEqual(
            env["VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE"],
            str(394 * 1024 * 1024),
        )

    def test_server_env_respects_flashinfer_workspace_override(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with mock.patch.dict(
            os.environ,
            {"INFERENCE_BENCH_VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE": str(8 * 1024 * 1024)},
            clear=True,
        ):
            env = provider._server_env()

        self.assertEqual(env["VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE"], str(8 * 1024 * 1024))

        with mock.patch.dict(
            os.environ,
            {
                "INFERENCE_BENCH_VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE": str(8 * 1024 * 1024),
                "VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE": str(16 * 1024 * 1024),
            },
            clear=True,
        ):
            env = provider._server_env()

        self.assertEqual(env["VLLM_FLASHINFER_WORKSPACE_BUFFER_SIZE"], str(16 * 1024 * 1024))

    def test_server_env_prepends_configured_libstdcxx_dir(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with tempfile.TemporaryDirectory() as tmpdir:
            lib_dir = os.path.join(tmpdir, "lib")
            os.makedirs(lib_dir)
            with open(os.path.join(lib_dir, "libstdc++.so.6"), "wb") as handle:
                handle.write(b"CXXABI_1.3.15")

            with mock.patch.dict(
                os.environ,
                {
                    "INFERENCE_BENCH_VLLM_LIBSTDCXX_DIR": lib_dir,
                    "LD_LIBRARY_PATH": "/old/lib",
                },
                clear=True,
            ):
                env = provider._server_env()

        self.assertEqual(
            env["LD_LIBRARY_PATH"].split(os.pathsep),
            [lib_dir, "/old/lib"],
        )

    def test_server_env_can_disable_libstdcxx_fixup(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        with tempfile.TemporaryDirectory() as tmpdir:
            lib_dir = os.path.join(tmpdir, "lib")
            os.makedirs(lib_dir)
            with open(os.path.join(lib_dir, "libstdc++.so.6"), "wb") as handle:
                handle.write(b"CXXABI_1.3.15")

            with mock.patch.dict(
                os.environ,
                {
                    "INFERENCE_BENCH_VLLM_LIBSTDCXX_DIR": lib_dir,
                    "INFERENCE_BENCH_VLLM_LIBSTDCXX_FIXUP": "0",
                    "LD_LIBRARY_PATH": "/old/lib",
                },
                clear=True,
            ):
                env = provider._server_env()

        self.assertEqual(env["LD_LIBRARY_PATH"], "/old/lib")


if __name__ == "__main__":
    unittest.main()
