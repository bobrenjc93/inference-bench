from __future__ import annotations

import os
import signal
import subprocess
import time
import types
import unittest
from unittest import mock

from inference_bench.providers.base import Provider


class FakeProvider(Provider):
    name = "fake"
    repo_url = "https://example.invalid/fake.git"

    def build(self) -> None:
        return None

    def _server_cmd(self, model: str, tp: int, port: int) -> list[str]:
        return ["python", "-m", "fake_server"]


class GpuIsolationTest(unittest.TestCase):
    def test_external_gpu_apps_ignores_server_process_group(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        gpu_rows = [
            {"index": 0, "uuid": "gpu-0", "total_mib": 100, "free_mib": 100},
            {"index": 1, "uuid": "gpu-1", "total_mib": 100, "free_mib": 100},
        ]
        app_rows = [
            {
                "raw": "101, server, gpu-0, 40000",
                "pid": 101,
                "process_name": "server",
                "gpu_uuid": "gpu-0",
                "used_memory_mib": 40000,
            },
            {
                "raw": "202, external, gpu-1, 12000",
                "pid": 202,
                "process_name": "external",
                "gpu_uuid": "gpu-1",
                "used_memory_mib": 12000,
            },
        ]

        with (
            mock.patch.object(provider, "_query_gpu_memory", return_value=gpu_rows),
            mock.patch.object(provider, "_query_gpu_app_rows", return_value=app_rows),
            mock.patch.object(provider, "_server_process_group_pids", return_value={100, 101}),
        ):
            self.assertEqual(provider._external_gpu_apps(tp=2), ["202, external, gpu-1, 12000"])

    def test_server_process_group_pids_includes_descendants(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        provider._server_process = types.SimpleNamespace(pid=100)

        def fake_run(cmd, **kwargs):  # noqa: ANN001, ANN003
            del kwargs
            if cmd == ["pgrep", "-g", "999"]:
                return subprocess.CompletedProcess(cmd, 0, stdout="100\n200\n", stderr="")
            if cmd == ["ps", "-eo", "pid=,ppid="]:
                return subprocess.CompletedProcess(
                    cmd,
                    0,
                    stdout="100 1\n200 100\n201 200\n300 1\n",
                    stderr="",
                )
            raise AssertionError(f"unexpected command: {cmd}")

        with (
            mock.patch("inference_bench.providers.base.os.getpgid", return_value=999),
            mock.patch("inference_bench.providers.base.subprocess.run", side_effect=fake_run),
        ):
            self.assertEqual(provider._server_process_group_pids(), {100, 200, 201})

    def test_stop_server_terminates_surviving_group_processes(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        process = mock.Mock()
        process.pid = 100
        provider._server_process = process
        provider._port = 8001
        provider._log_file = mock.Mock()

        with (
            mock.patch.object(provider, "_server_process_group_pids", return_value={100, 200}),
            mock.patch.object(provider, "_terminate_surviving_processes") as terminate_survivors,
            mock.patch.object(provider, "_wait_for_port_release"),
            mock.patch.dict(os.environ, {"INFERENCE_BENCH_PROVIDER_CLEANUP_WAIT_S": "0"}),
            mock.patch("inference_bench.providers.base.os.getpgid", return_value=999),
            mock.patch("inference_bench.providers.base.os.killpg") as killpg,
        ):
            provider.stop_server()

        killpg.assert_called_once_with(999, signal.SIGTERM)
        process.wait.assert_called_once_with(timeout=30)
        terminate_survivors.assert_called_once_with({100, 200})
        self.assertIsNone(provider._server_process)

    def test_terminate_surviving_processes_escalates_to_sigkill(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")

        with (
            mock.patch.object(
                provider,
                "_wait_for_pids_exit",
                side_effect=[{200}, {200}, set()],
            ) as wait_for_pids,
            mock.patch("inference_bench.providers.base.os.kill") as kill,
        ):
            provider._terminate_surviving_processes({200})

        self.assertEqual(wait_for_pids.call_count, 3)
        kill.assert_has_calls(
            [
                mock.call(200, signal.SIGTERM),
                mock.call(200, signal.SIGKILL),
            ]
        )

    def test_wait_for_gpu_isolation_returns_after_clean_poll(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        with (
            mock.patch.dict(
                os.environ,
                {
                    "INFERENCE_BENCH_GPU_ISOLATION_TIMEOUT_S": "1",
                    "INFERENCE_BENCH_GPU_ISOLATION_POLL_S": "0",
                    "INFERENCE_BENCH_GPU_ISOLATION_CLEAN_WAIT_S": "0",
                },
            ),
            mock.patch.object(
                provider,
                "_external_gpu_apps",
                side_effect=[["202, external, gpu-0, 12000"], []],
            ) as external_apps,
            mock.patch("inference_bench.providers.base.time.sleep", return_value=None),
        ):
            provider.wait_for_gpu_isolation(tp=1)

        self.assertEqual(external_apps.call_count, 2)

    def test_gpu_isolation_monitor_raises_on_mid_run_contamination(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        contaminating_app = "202, external, gpu-0, 12000"
        with (
            mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_GPU_ISOLATION_MONITOR_POLL_S": "0.25"},
            ),
            mock.patch.object(provider, "_external_gpu_apps", return_value=[contaminating_app]),
        ):
            monitor = provider.gpu_isolation_monitor(tp=1)
            with self.assertRaisesRegex(RuntimeError, "GPU isolation was violated"):
                with monitor:
                    deadline = time.time() + 2.0
                    while not monitor._contaminating_apps and time.time() < deadline:
                        time.sleep(0.05)

    def test_disaggregated_monitor_fails_closed_when_telemetry_drops(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        provider.configure_deployment(
            deployment_mode="disaggregated_prefill_decode",
            tensor_parallel_size=1,
            prefill_tensor_parallel_size=1,
            decode_tensor_parallel_size=1,
        )
        with (
            mock.patch.dict(
                os.environ,
                {"INFERENCE_BENCH_GPU_ISOLATION_MONITOR_POLL_S": "0.25"},
            ),
            mock.patch.object(
                provider,
                "_external_gpu_apps",
                side_effect=RuntimeError("nvidia-smi unavailable"),
            ),
        ):
            monitor = provider.gpu_isolation_monitor(tp=2)
            with self.assertRaisesRegex(RuntimeError, "could not be verified"):
                with monitor:
                    deadline = time.time() + 2.0
                    while monitor._monitor_error is None and time.time() < deadline:
                        time.sleep(0.05)

    def test_gpu_memory_ready_reports_blocking_gpus_first(self) -> None:
        provider = FakeProvider(build_dir="/tmp/inference-bench-test")
        gpu_rows = [
            {"index": 0, "uuid": "gpu-0", "total_mib": 100, "free_mib": 100},
            {"index": 1, "uuid": "gpu-1", "total_mib": 100, "free_mib": 10},
            {"index": 2, "uuid": "gpu-2", "total_mib": 100, "free_mib": 100},
        ]

        with (
            mock.patch.object(provider, "_query_gpu_memory", return_value=gpu_rows),
            mock.patch.object(provider, "_query_gpu_apps", return_value=[]),
        ):
            ready, detail = provider._gpu_memory_ready_once(tp=3, required_fraction=0.9)

        self.assertFalse(ready)
        self.assertTrue(detail.splitlines()[0].startswith("gpu=1 "))


if __name__ == "__main__":
    unittest.main()
