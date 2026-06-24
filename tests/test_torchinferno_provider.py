from __future__ import annotations

import os
import unittest
from unittest import mock

from inference_bench.providers.torchinferno import TorchInfernoProvider


class TorchInfernoProviderTest(unittest.TestCase):
    def test_server_env_disables_nccl_cumem_by_default(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(os.environ, {}, clear=True):
            env = provider._server_env()

        self.assertEqual(env["NCCL_CUMEM_ENABLE"], "0")

    def test_server_env_preserves_explicit_nccl_cumem_override(self) -> None:
        provider = TorchInfernoProvider(build_dir="/tmp/inference-bench-test")

        with mock.patch.dict(os.environ, {"NCCL_CUMEM_ENABLE": "1"}, clear=True):
            env = provider._server_env()

        self.assertEqual(env["NCCL_CUMEM_ENABLE"], "1")


if __name__ == "__main__":
    unittest.main()
