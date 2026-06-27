from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from inference_bench.benchmarks.base import BenchmarkResult
from inference_bench.results import ProviderResults, RunResults


def test_default_timestamp_is_utc_aware() -> None:
    results = RunResults(model="model", tensor_parallel_size=1)

    timestamp = datetime.fromisoformat(results.timestamp)

    assert timestamp.tzinfo is not None
    assert timestamp.utcoffset() == timezone.utc.utcoffset(timestamp)


def test_run_dir_uses_utc_timestamp(tmp_path) -> None:
    results = RunResults(
        model="org/model",
        tensor_parallel_size=8,
        timestamp="2026-06-24T17:52:45.966998+00:00",
    )

    results_path = results.save(tmp_path / "results")

    assert results_path.parent.name == "20260624_175245"


def test_save_copies_provider_logs(tmp_path) -> None:
    source_log = tmp_path / "torchinferno_server.log"
    source_log.write_text("server tail\n")
    results = RunResults(
        model="meta-llama/Meta-Llama-3.1-70B-Instruct",
        tensor_parallel_size=8,
        hardware="8xH100",
    )
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        commit_hash="abc123",
        server_log_path=str(source_log),
    )

    results_path = results.save(tmp_path / "results")

    data = json.loads(results_path.read_text())
    provider = data["providers"]["torchinferno"]
    assert provider["server_log"] == "provider_logs/torchinferno.log"
    copied_log = results_path.parent / provider["server_log"]
    assert copied_log.read_text() == "server tail\n"


def test_console_summary_scores_latency_and_throughput_only(capsys) -> None:
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["fast"] = ProviderResults(
        provider="fast",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={
                    "ttft_median_ms": 1.0,
                    "tpot_median_ms": 1.0,
                    "e2e_median_ms": 1.0,
                    "throughput_median_tps": 100.0,
                    "correctness_rate": 0.5,
                },
            )
        },
    )
    results.providers["accurate"] = ProviderResults(
        provider="accurate",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={
                    "ttft_median_ms": 2.0,
                    "tpot_median_ms": 2.0,
                    "e2e_median_ms": 2.0,
                    "throughput_median_tps": 50.0,
                    "correctness_rate": 1.0,
                },
            )
        },
    )

    results.print_comparison()

    output = capsys.readouterr().out
    assert re.search(r"^correctness_rate\s+0\.5\s+1\s+accurate$", output, re.MULTILINE)
    assert re.search(r"^fast\s+4$", output, re.MULTILINE)
    assert re.search(r"^accurate\s+0$", output, re.MULTILINE)
