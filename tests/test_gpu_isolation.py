from __future__ import annotations

import os
import time
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
