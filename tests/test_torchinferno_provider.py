from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from inference_bench.providers.torchinferno import TorchInfernoProvider


class TorchInfernoProviderTest(unittest.TestCase):
    def test_server_env_disables_nccl_cumem_and_leaves_checkpoint_broadcast_default(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(os.environ, {}, clear=True):
            env = provider._server_env()

        self.assertEqual(env["NCCL_CUMEM_ENABLE"], "0")
        self.assertEqual(env["TORCHINFERNO_FI_DECODE_GRAPH"], "off")
        self.assertNotIn("TORCHINFERNO_TP_RANK0_CHECKPOINT_BROADCAST", env)

    def test_server_env_defaults_torchinferno_queue_profile_log(self) -> None:
        with TemporaryDirectory() as tmp:
            provider = TorchInfernoProvider(build_dir=tmp)
            build_dir = Path(tmp).resolve()
            stale_queue = build_dir / "torchinferno_queue_profile.jsonl"
            stale_fast_http = build_dir / "torchinferno_fast_http_profile.jsonl"
            stale_queue.write_text("stale\n")
            stale_fast_http.write_text("stale\n")

            with mock.patch.dict(os.environ, {}, clear=True):
                env = provider._server_env()

            self.assertEqual(
                env["TORCHINFERNO_OPENAI_QUEUE_PROFILE_JSONL"],
                str(build_dir / "torchinferno_queue_profile.jsonl"),
            )
            self.assertNotIn("TORCHINFERNO_OPENAI_FAST_HTTP_PROFILE_JSONL", env)
            self.assertEqual(
                provider.extra_log_paths(),
                {
                    "queue_profile": str(build_dir / "torchinferno_queue_profile.jsonl"),
                },
            )
            self.assertFalse(stale_queue.exists())
            self.assertTrue(stale_fast_http.exists())

    def test_server_env_can_opt_into_torchinferno_fast_http_profile_log(self) -> None:
        with TemporaryDirectory() as tmp:
            provider = TorchInfernoProvider(build_dir=tmp)
            build_dir = Path(tmp).resolve()
            stale_fast_http = build_dir / "torchinferno_fast_http_profile.jsonl"
            stale_fast_http.write_text("stale\n")

            with mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_TORCHINFERNO_FAST_HTTP_PROFILE": "1"},
                clear=True,
            ):
                env = provider._server_env()

            self.assertEqual(
                env["TORCHINFERNO_OPENAI_FAST_HTTP_PROFILE_JSONL"],
                str(build_dir / "torchinferno_fast_http_profile.jsonl"),
            )
            self.assertEqual(
                provider.extra_log_paths(),
                {
                    "queue_profile": str(build_dir / "torchinferno_queue_profile.jsonl"),
                    "fast_http_profile": str(
                        build_dir / "torchinferno_fast_http_profile.jsonl"
                    ),
                },
            )
            self.assertFalse(stale_fast_http.exists())

    def test_build_installs_flashinfer_extra_by_default(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_create_venv"),
            mock.patch.object(provider, "_pip_install") as pip_install,
        ):
            provider.build()

        pip_install.assert_has_calls(
            [
                mock.call("--upgrade", "pip"),
                mock.call("-e", ".[serve,flashinfer]", cwd=provider.repo_dir),
            ]
        )

    def test_build_can_disable_flashinfer_extra(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with (
            mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_TORCHINFERNO_FLASHINFER": "0"},
                clear=True,
            ),
            mock.patch.object(provider, "_create_venv"),
            mock.patch.object(provider, "_pip_install") as pip_install,
        ):
            provider.build()

        pip_install.assert_has_calls(
            [
                mock.call("--upgrade", "pip"),
                mock.call("-e", ".[serve]", cwd=provider.repo_dir),
            ]
        )

    def test_build_falls_back_to_serve_when_default_flashinfer_extra_fails(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")
        calls: list[tuple[tuple[str, ...], object]] = []

        def fake_pip_install(*args: str, cwd=None) -> None:  # noqa: ANN001
            calls.append((args, cwd))
            if args == ("-e", ".[serve,flashinfer]"):
                raise subprocess.CalledProcessError(1, "pip")

        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_create_venv"),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
        ):
            provider.build()

        self.assertEqual(
            calls,
            [
                (("--upgrade", "pip"), None),
                (("-e", ".[serve,flashinfer]"), provider.repo_dir),
                (("-e", ".[serve]"), provider.repo_dir),
            ],
        )

    def test_server_env_preserves_explicit_nccl_cumem_override(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(os.environ, {"NCCL_CUMEM_ENABLE": "1"}, clear=True):
            env = provider._server_env()

        self.assertEqual(env["NCCL_CUMEM_ENABLE"], "1")

    def test_server_env_preserves_explicit_rank0_checkpoint_broadcast_override(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(
            os.environ,
            {"TORCHINFERNO_TP_RANK0_CHECKPOINT_BROADCAST": "0"},
            clear=True,
        ):
            env = provider._server_env()

        self.assertEqual(env["TORCHINFERNO_TP_RANK0_CHECKPOINT_BROADCAST"], "0")

    def test_server_env_preserves_explicit_flashinfer_decode_graph_override(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(os.environ, {"TORCHINFERNO_FI_DECODE_GRAPH": "sampled"}, clear=True):
            env = provider._server_env()

        self.assertEqual(env["TORCHINFERNO_FI_DECODE_GRAPH"], "sampled")

    def test_server_cmd_appends_env_extra_args(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(os.environ, {"TORCHINFERNO_SERVER_ARGS": "--max-batch-size 256"}, clear=True):
            cmd = provider._server_cmd("model", tp=8, port=9000)

        self.assertEqual(cmd[-2:], ["--max-batch-size", "256"])


if __name__ == "__main__":
    unittest.main()
