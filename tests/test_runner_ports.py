from __future__ import annotations

import unittest
from unittest import mock

from inference_bench.runner import _next_provider_port


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


if __name__ == "__main__":
    unittest.main()
