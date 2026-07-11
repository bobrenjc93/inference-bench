from __future__ import annotations

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from inference_bench.runner import (
    _append_torchinferno_queue_profile_marker,
    _next_provider_port,
)


class _FakeProvider:
    def __init__(self, name: str, queue_profile: str):
        self.name = name
        self._queue_profile = queue_profile

    def extra_log_paths(self) -> dict[str, str]:
        return {"queue_profile": self._queue_profile}


class RunnerPortSelectionTest(unittest.TestCase):
    def test_next_provider_port_skips_busy_and_already_assigned_ports(self) -> None:
        used_ports: set[int] = set()

        def fake_can_bind(port: int) -> bool:
            return port not in {8001, 8002}

        with mock.patch("inference_bench.runner._port_can_bind", side_effect=fake_can_bind):
            self.assertEqual(_next_provider_port(8000, used_ports), 8000)
            self.assertEqual(_next_provider_port(8001, used_ports), 8003)
            self.assertEqual(_next_provider_port(8002, used_ports), 8004)

        self.assertEqual(used_ports, {8000, 8003, 8004})


class RunnerQueueProfileMarkerTest(unittest.TestCase):
    def test_appends_torchinferno_benchmark_marker(self) -> None:
        with TemporaryDirectory() as tmp, mock.patch("time.time", return_value=123.5):
            path = Path(tmp) / "queue_profile.jsonl"
            provider = _FakeProvider("torchinferno", str(path))

            _append_torchinferno_queue_profile_marker(
                provider,
                event="benchmark_start",
                benchmark="tree_of_thought",
            )
            _append_torchinferno_queue_profile_marker(
                provider,
                event="benchmark_end",
                benchmark="tree_of_thought",
                status="ok",
            )

            records = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
            ]

        self.assertEqual(
            records,
            [
                {
                    "benchmark": "tree_of_thought",
                    "event": "benchmark_start",
                    "provider": "torchinferno",
                    "timestamp_s": 123.5,
                },
                {
                    "benchmark": "tree_of_thought",
                    "event": "benchmark_end",
                    "provider": "torchinferno",
                    "status": "ok",
                    "timestamp_s": 123.5,
                },
            ],
        )

    def test_skips_non_torchinferno_provider(self) -> None:
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "queue_profile.jsonl"
            provider = _FakeProvider("vllm", str(path))

            _append_torchinferno_queue_profile_marker(
                provider,
                event="benchmark_start",
                benchmark="long_output",
            )

            self.assertFalse(path.exists())


if __name__ == "__main__":
    unittest.main()
