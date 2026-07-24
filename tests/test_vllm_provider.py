from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from unittest import mock

from inference_bench.providers.vllm import VllmProvider


class VllmProviderTest(unittest.TestCase):
    def test_failed_forced_flash_attn_rebuild_does_not_fall_back_to_plain_install(
        self,
    ) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        installs: list[tuple[str, ...]] = []

        def fake_pip_install(*args, cwd=None):  # noqa: ANN001
            del cwd
            if args == ("--upgrade", "pip"):
                return None
            installs.append(args)
            if "--force-reinstall" in args:
                raise subprocess.CalledProcessError(1, ["pip", *args])

        failed_probe = subprocess.CompletedProcess(
            args=["python", "-c", "import vllm.vllm_flash_attn"],
            returncode=1,
            stdout="",
            stderr="bad extension",
        )
        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_create_venv"),
            mock.patch.object(provider, "_disable_fastapi_metrics_middleware"),
            mock.patch.object(provider, "_harden_optional_torchcodec_import"),
            mock.patch.object(provider, "_configure_cuda_arch_list"),
            mock.patch.object(provider, "_configure_conservative_source_build_retry"),
            mock.patch.object(provider, "_probe_flash_attn", return_value=failed_probe),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
            self.assertRaises(subprocess.CalledProcessError),
        ):
            provider.build()

        self.assertEqual(
            installs,
            [
                ("-e", "."),
                ("-e", ".", "--force-reinstall", "--no-deps"),
                ("-e", ".", "--force-reinstall", "--no-deps"),
            ],
        )

    def test_flash_attn_is_rechecked_after_forced_rebuild(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        failed_probe = subprocess.CompletedProcess(
            args=["python", "-c", "import vllm.vllm_flash_attn"],
            returncode=1,
            stdout="",
            stderr="bad extension",
        )
        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_create_venv"),
            mock.patch.object(provider, "_disable_fastapi_metrics_middleware"),
            mock.patch.object(provider, "_harden_optional_torchcodec_import"),
            mock.patch.object(provider, "_configure_cuda_arch_list"),
            mock.patch.object(provider, "_pip_install"),
            mock.patch.object(
                provider,
                "_probe_flash_attn",
                side_effect=[failed_probe, failed_probe],
            ) as probe,
            self.assertRaises(subprocess.CalledProcessError),
        ):
            provider.build()

        self.assertEqual(probe.call_count, 2)

    def test_flash_attn_probe_uses_scored_server_environment(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        completed = subprocess.CompletedProcess(
            args=["python"],
            returncode=0,
            stdout="",
            stderr="",
        )
        with (
            mock.patch.object(provider, "_server_env", return_value={"CLEAN": "1"}),
            mock.patch("inference_bench.providers.vllm.subprocess.run", return_value=completed) as run,
        ):
            provider._probe_flash_attn()

        self.assertEqual(run.call_args.kwargs["cwd"], provider.repo_dir)
        self.assertEqual(run.call_args.kwargs["env"], {"CLEAN": "1"})

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
            mock.patch.object(
                provider,
                "_probe_flash_attn",
                return_value=subprocess.CompletedProcess(
                    args=["python"],
                    returncode=0,
                    stdout="",
                    stderr="",
                ),
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

    def test_v3_standard_keeps_upstream_allreduce_rms_fusion(self) -> None:
        provider = VllmProvider(build_dir="/tmp/inference-bench-test")
        provider.configure_deployment(
            deployment_mode="standard",
            tensor_parallel_size=4,
            model_revision="a" * 40,
            evaluation_version=3,
        )
        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_server_model", return_value="model"),
        ):
            cmd = provider._server_cmd("model", tp=4, port=9000)

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

    def test_harden_optional_torchcodec_import_catches_runtime_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            provider = VllmProvider(build_dir=tmpdir)
            video_dir = provider.repo_dir / "vllm" / "multimodal"
            video_dir.mkdir(parents=True)
            video_py = video_dir / "video.py"
            video_py.write_text(
                """try:
    from torchcodec.decoders import VideoDecoder
except ImportError:
    VideoDecoder = PlaceholderModule("torchcodec").placeholder_attr(  # type: ignore[assignment]
        "decoders.VideoDecoder",
    )
"""
            )

            provider._harden_optional_torchcodec_import()

            patched = video_py.read_text()
            self.assertIn("except (ImportError, OSError, RuntimeError):", patched)
            self.assertIn("missing optional video backend", patched)

    def test_harden_optional_torchcodec_import_wraps_direct_import(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            provider = VllmProvider(build_dir=tmpdir)
            video_dir = provider.repo_dir / "vllm" / "multimodal"
            video_dir.mkdir(parents=True)
            video_py = video_dir / "video.py"
            video_py.write_text(
                """from vllm.utils.import_utils import PlaceholderModule
from torchcodec.decoders import VideoDecoder
"""
            )

            provider._harden_optional_torchcodec_import()

            patched = video_py.read_text()
            self.assertIn("except (ImportError, OSError, RuntimeError):", patched)
            self.assertIn("missing optional video backend", patched)
            self.assertNotIn("\nfrom torchcodec.decoders import VideoDecoder\n", patched)
            compile(patched, str(video_py), "exec")

    def test_harden_optional_torchcodec_import_preserves_direct_import_indent(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            provider = VllmProvider(build_dir=tmpdir)
            video_dir = provider.repo_dir / "vllm" / "multimodal"
            video_dir.mkdir(parents=True)
            video_py = video_dir / "video.py"
            video_py.write_text(
                """from vllm.utils.import_utils import PlaceholderModule
try:
    from torchcodec.decoders import VideoDecoder
except ImportError:
    VideoDecoder = PlaceholderModule("torchcodec").placeholder_attr(
        "decoders.VideoDecoder"
    )
"""
            )

            provider._harden_optional_torchcodec_import()

            patched = video_py.read_text()
            self.assertIn(
                "try:\n    try:\n        from torchcodec.decoders import VideoDecoder",
                patched,
            )
            self.assertIn("    except (ImportError, OSError, RuntimeError):", patched)
            self.assertNotIn("try:\ntry:", patched)
            compile(patched, str(video_py), "exec")

            provider._harden_optional_torchcodec_import()
            self.assertEqual(video_py.read_text(), patched)


if __name__ == "__main__":
    unittest.main()
