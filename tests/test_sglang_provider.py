from __future__ import annotations

import os
import subprocess
import unittest
from pathlib import Path
from unittest import mock

from inference_bench.deployment import DISAGGREGATED_PREFILL_DECODE
from inference_bench.providers.sglang import SglangProvider


class SglangProviderTest(unittest.TestCase):
    def test_runtime_imports_match_version_derived_topology(self) -> None:
        standard = SglangProvider(build_dir="/tmp/inference-bench-test")
        standard.configure_deployment(
            deployment_mode="standard",
            tensor_parallel_size=8,
            model_revision="a" * 40,
            evaluation_version=3,
        )
        disaggregated = SglangProvider(build_dir="/tmp/inference-bench-test")
        disaggregated.configure_deployment(
            deployment_mode=DISAGGREGATED_PREFILL_DECODE,
            tensor_parallel_size=4,
            prefill_tensor_parallel_size=4,
            decode_tensor_parallel_size=4,
            model_revision="a" * 40,
            evaluation_version=4,
        )

        self.assertEqual(standard.runtime_import_names, ("sglang",))
        self.assertEqual(
            disaggregated.runtime_import_names,
            ("sglang", "sglang_router"),
        )

    def test_server_cmd_uses_current_tensor_parallel_flag(self) -> None:
        provider = SglangProvider(build_dir="/tmp/inference-bench-test")

        cmd = provider._server_cmd("model", tp=8, port=9000)

        self.assertIn("--tp-size", cmd)
        self.assertEqual(cmd[cmd.index("--tp-size") + 1], "8")
        self.assertNotIn("--tp", cmd)

    def test_editable_failure_retries_binary_wheel(self) -> None:
        provider = SglangProvider(build_dir="/tmp/inference-bench-test")
        calls: list[tuple[tuple[str, ...], Path | None]] = []

        def fake_pip_install(*args, cwd=None):  # noqa: ANN001
            calls.append((args, cwd))
            if args == ("-e", "."):
                raise subprocess.CalledProcessError(1, ["pip", "install"])

        with (
            mock.patch.dict(os.environ, {}, clear=True),
            mock.patch.object(provider, "_create_venv", return_value=None),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
        ):
            provider.build()

        self.assertEqual(
            calls,
            [
                (("--upgrade", "pip"), None),
                (("-e", "."), provider._python_dir),
                (("--only-binary=:all:", "sglang"), None),
            ],
        )

    def test_binary_wheel_spec_can_be_configured(self) -> None:
        provider = SglangProvider(build_dir="/tmp/inference-bench-test")
        calls: list[tuple[str, ...]] = []

        def fake_pip_install(*args, cwd=None):  # noqa: ANN001
            del cwd
            calls.append(args)
            if args == ("-e", "."):
                raise subprocess.CalledProcessError(1, ["pip", "install"])

        with (
            mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_SGLANG_BINARY_WHEEL_SPEC": "sglang==0.5.13.post1"},
                clear=True,
            ),
            mock.patch.object(provider, "_create_venv", return_value=None),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
        ):
            provider.build()

        self.assertEqual(calls[-1], ("--only-binary=:all:", "sglang==0.5.13.post1"))

    def test_binary_wheel_fallback_can_be_disabled(self) -> None:
        provider = SglangProvider(build_dir="/tmp/inference-bench-test")
        calls: list[tuple[str, ...]] = []

        def fake_pip_install(*args, cwd=None):  # noqa: ANN001
            del cwd
            calls.append(args)
            if args == ("-e", "."):
                raise subprocess.CalledProcessError(1, ["pip", "install"])

        with (
            mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_SGLANG_FALLBACK_BINARY_WHEEL": "0"},
                clear=True,
            ),
            mock.patch.object(provider, "_create_venv", return_value=None),
            mock.patch.object(provider, "_pip_install", side_effect=fake_pip_install),
            self.assertRaises(subprocess.CalledProcessError),
        ):
            provider.build()

        self.assertEqual(calls, [("--upgrade", "pip"), ("-e", ".")])


if __name__ == "__main__":
    unittest.main()
