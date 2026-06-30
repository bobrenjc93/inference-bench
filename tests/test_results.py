from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from inference_bench.benchmarks.base import BenchmarkResult, RequestMetrics
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


def test_save_copies_extra_provider_logs(tmp_path) -> None:
    queue_log = tmp_path / "torchinferno_queue_profile.jsonl"
    http_log = tmp_path / "torchinferno_fast_http_profile.jsonl"
    queue_log.write_text('{"queue": 1}\n')
    http_log.write_text('{"http": 1}\n')
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        extra_log_paths={
            "queue_profile": str(queue_log),
            "fast_http_profile": str(http_log),
        },
    )

    results_path = results.save(tmp_path / "results")

    data = json.loads(results_path.read_text())
    provider = data["providers"]["torchinferno"]
    assert provider["extra_logs"] == {
        "queue_profile": "provider_logs/torchinferno_queue_profile.jsonl",
        "fast_http_profile": "provider_logs/torchinferno_fast_http_profile.jsonl",
    }
    assert (
        results_path.parent / provider["extra_logs"]["queue_profile"]
    ).read_text() == '{"queue": 1}\n'
    assert (
        results_path.parent / provider["extra_logs"]["fast_http_profile"]
    ).read_text() == '{"http": 1}\n'


def test_save_preserves_raw_request_metadata(tmp_path) -> None:
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        benchmarks={
            "multi_turn": BenchmarkResult(
                name="multi_turn",
                raw_requests=[
                    RequestMetrics(
                        ttft_ms=1.0,
                        metadata={"conversation_idx": 7, "turn_idx": 3},
                    )
                ],
            )
        },
    )

    results_path = results.save(tmp_path / "results")
    data = json.loads(results_path.read_text())

    raw = data["providers"]["torchinferno"]["benchmarks"]["multi_turn"]["raw_requests"]
    assert raw[0]["metadata"] == {"conversation_idx": 7, "turn_idx": 3}
    assert raw[0]["metadata_conversation_idx"] == 7
    assert raw[0]["metadata_turn_idx"] == 3


def test_save_uses_stable_request_idx_and_completion_idx(tmp_path) -> None:
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        benchmarks={
            "few_shot": BenchmarkResult(
                name="few_shot",
                raw_requests=[
                    RequestMetrics(ttft_ms=1.0, metadata={"request_idx": 9}),
                    RequestMetrics(ttft_ms=2.0, metadata={"request_idx": 3}),
                ],
            )
        },
    )

    results_path = results.save(tmp_path / "results")
    data = json.loads(results_path.read_text())

    raw = data["providers"]["torchinferno"]["benchmarks"]["few_shot"]["raw_requests"]
    assert [item["request_idx"] for item in raw] == [9, 3]
    assert [item["completion_idx"] for item in raw] == [0, 1]


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
    assert re.search(r"^correctness_rate\s+0\.500\s+1\.000\s+accurate$", output, re.MULTILINE)
    assert re.search(r"^fast\s+4$", output, re.MULTILINE)
    assert re.search(r"^accurate\s+0$", output, re.MULTILINE)


def test_console_summary_does_not_round_near_perfect_correctness(capsys) -> None:
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["almost"] = ProviderResults(
        provider="almost",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={
                    "ttft_median_ms": 1.0,
                    "correctness_rate": 0.977,
                },
            )
        },
    )
    results.providers["perfect"] = ProviderResults(
        provider="perfect",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={
                    "ttft_median_ms": 2.0,
                    "correctness_rate": 1.0,
                },
            )
        },
    )

    results.print_comparison()

    output = capsys.readouterr().out
    assert re.search(r"^correctness_rate\s+0\.977\s+1\.000\s+perfect$", output, re.MULTILINE)


def test_console_summary_does_not_score_tied_metrics(capsys) -> None:
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["fast"] = ProviderResults(
        provider="fast",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={
                    "ttft_median_ms": 1.0,
                    "tpot_median_ms": 0.0,
                    "e2e_median_ms": 1.0,
                    "throughput_median_tps": 100.0,
                },
            )
        },
    )
    results.providers["same_tpot"] = ProviderResults(
        provider="same_tpot",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={
                    "ttft_median_ms": 2.0,
                    "tpot_median_ms": 0.0,
                    "e2e_median_ms": 2.0,
                    "throughput_median_tps": 50.0,
                },
            )
        },
    )

    results.print_comparison()

    output = capsys.readouterr().out
    assert re.search(r"^tpot_median_ms\s+0\.0\s+0\.0\s*$", output, re.MULTILINE)
    assert re.search(r"^fast\s+3$", output, re.MULTILINE)
    assert re.search(r"^same_tpot\s+0$", output, re.MULTILINE)
