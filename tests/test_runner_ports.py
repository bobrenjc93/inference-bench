from __future__ import annotations

import json
import unittest
from contextlib import nullcontext
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import mock

from inference_bench.benchmarks.base import BenchmarkResult, RequestMetrics
from inference_bench.config import Config
from inference_bench.runner import (
    _append_torchinferno_queue_profile_marker,
    _capture_harness_provenance,
    _next_provider_port,
    run_all,
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


class RunnerHarnessProvenanceTest(unittest.TestCase):
    @staticmethod
    def _git_output(*args: str, dirty: bool = False) -> str:
        commit = "a" * 40
        outputs = {
            ("rev-parse", "HEAD"): commit,
            ("rev-parse", "origin/main"): commit,
            ("remote", "get-url", "origin"): (
                "https://github.com/bobrenjc93/inference-bench.git"
            ),
            ("status", "--porcelain", "--untracked-files=all"): (
                " M inference_bench/runner.py" if dirty else ""
            ),
            (
                "ls-remote",
                "https://github.com/bobrenjc93/inference-bench.git",
                "refs/heads/main",
            ): f"{commit}\trefs/heads/main",
        }
        return outputs[args]

    def test_records_clean_canonical_remote_main(self) -> None:
        with mock.patch(
            "inference_bench.runner._harness_git",
            side_effect=lambda _root, *args: self._git_output(*args),
        ):
            provenance = _capture_harness_provenance(verify_remote=True)

        self.assertEqual(provenance["check"], "passed")
        self.assertEqual(provenance["commit"], "a" * 40)
        self.assertEqual(provenance["origin_main"], "a" * 40)
        self.assertTrue(provenance["worktree_clean"])

    def test_rejects_dirty_harness(self) -> None:
        with (
            mock.patch(
                "inference_bench.runner._harness_git",
                side_effect=lambda _root, *args: self._git_output(
                    *args, dirty=True
                ),
            ),
            self.assertRaisesRegex(RuntimeError, "clean worktree"),
        ):
            _capture_harness_provenance(verify_remote=True)


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


class _IntegrityFailingProvider:
    name = "vllm"
    api_base = "http://127.0.0.1:8001/v1"

    def configure_deployment(self, **_kwargs) -> None:  # noqa: ANN003
        return None

    def prepare_source_provenance(self, *, skip_build: bool) -> dict[str, object]:
        assert skip_build
        return {}

    def prepare_model_assets(self, _model: str) -> None:
        return None

    def verify_source_provenance(self) -> dict[str, object]:
        return {}

    def verify_model_provenance(self, _model: str) -> dict[str, object]:
        return {}

    def wait_for_gpu_isolation(self, _tp: int) -> None:
        return None

    def start_server(self, **_kwargs) -> None:  # noqa: ANN003
        return None

    def verify_gpu_coverage(self, _count: int) -> dict[str, object]:
        return {"gpu_coverage_check": "passed"}

    def gpu_isolation_monitor(self, _tp: int):  # noqa: ANN201
        return nullcontext()

    def verify_runtime_integrity(self) -> dict[str, object]:
        raise RuntimeError("missing handoff evidence")

    def get_commit_hash(self) -> str:
        return "abc123"

    def stop_server(self) -> None:
        return None

    def extra_log_paths(self) -> dict[str, str]:
        return {}


class _SuccessfulBenchmark:
    debug = False
    verbose = False
    authoritative_output_token_count = False

    def run(self, _api_base: str, _model: str) -> BenchmarkResult:
        return BenchmarkResult(
            name="bench",
            metrics={
                "correctness_rate": 1.0,
                "num_requests": 1,
                "total_output_tokens": 1,
            },
            raw_requests=[RequestMetrics(output_tokens=1, correct=True)],
        )


class _SuccessfulProvider(_IntegrityFailingProvider):
    def verify_model_provenance(self, _model: str) -> dict[str, object]:
        return {"resolved_snapshot": "/verified/pinned-snapshot"}

    def verify_runtime_integrity(self) -> dict[str, object]:
        return {}


def test_runner_passes_verified_snapshot_to_authoritative_tokenizer() -> None:
    provider = _SuccessfulProvider()
    benchmark = _SuccessfulBenchmark()
    config = Config(
        model="model",
        tensor_parallel_size=1,
        providers=["vllm"],
        benchmarks=["bench"],
        authoritative_output_token_count=True,
    )
    with (
        mock.patch("inference_bench.runner.get_provider", return_value=provider),
        mock.patch("inference_bench.runner.get_benchmark", return_value=benchmark),
        mock.patch("inference_bench.runner._next_provider_port", return_value=8001),
        mock.patch("inference_bench.runner._free_gpu_memory"),
        mock.patch("inference_bench.runner.time.sleep"),
    ):
        run_all(config, skip_build=True)

    assert benchmark.authoritative_tokenizer_path == "/verified/pinned-snapshot"


def test_post_benchmark_integrity_failure_is_non_comparable() -> None:
    provider = _IntegrityFailingProvider()
    config = Config(
        model="model",
        tensor_parallel_size=1,
        providers=["vllm"],
        benchmarks=["bench"],
        minimum_correctness_rate=0.95,
        require_request_count_parity=True,
        output_token_ratio_tolerance=0.10,
    )
    with (
        mock.patch("inference_bench.runner.get_provider", return_value=provider),
        mock.patch(
            "inference_bench.runner.get_benchmark",
            return_value=_SuccessfulBenchmark(),
        ),
        mock.patch("inference_bench.runner._next_provider_port", return_value=8001),
        mock.patch("inference_bench.runner._free_gpu_memory"),
        mock.patch("inference_bench.runner.time.sleep"),
    ):
        results = run_all(config, skip_build=True)

    saved = results.providers["vllm"]
    assert "bench" in saved.benchmarks
    assert not saved.comparable
    assert "missing handoff evidence" in saved.errors["_server"]
    assert any("integrity could not be verified" in item for item in saved.integrity_warnings)


if __name__ == "__main__":
    unittest.main()
