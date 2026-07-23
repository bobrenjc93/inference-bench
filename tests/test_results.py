from __future__ import annotations

import json
import math
import re
import sys
import types
from datetime import datetime, timezone

import pytest

from inference_bench.benchmarks.base import BenchmarkResult, RequestMetrics
from inference_bench.results import ProviderResults, RunResults
from scripts.generate_summary import generate


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


def test_save_records_disaggregated_resource_allocation(tmp_path) -> None:
    results = RunResults(
        model="model",
        tensor_parallel_size=4,
        deployment_mode="disaggregated_prefill_decode",
        prefill_tensor_parallel_size=4,
        decode_tensor_parallel_size=4,
        gpu_count=8,
        harness_provenance={
            "check": "passed",
            "commit": "a" * 40,
            "worktree_clean": True,
        },
    )
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        deployment_observation={
            "gpu_coverage_check": "passed",
            "expected_gpu_count": 8,
            "observed_gpu_count": 8,
        },
    )

    path = results.save(tmp_path / "results")
    data = json.loads(path.read_text())

    assert data["deployment_mode"] == "disaggregated_prefill_decode"
    assert data["prefill_tensor_parallel_size"] == 4
    assert data["decode_tensor_parallel_size"] == 4
    assert data["tensor_parallel_size"] == 4
    assert data["gpu_count"] == 8
    assert data["harness_provenance"]["commit"] == "a" * 40
    assert data["providers"]["torchinferno"]["deployment_observation"] == {
        "gpu_coverage_check": "passed",
        "expected_gpu_count": 8,
        "observed_gpu_count": 8,
    }
    markdown = generate(path)
    assert "**Deployment:** disaggregated prefill/decode" in markdown
    assert "**Prefill TP:** 4" in markdown
    assert "**Decode TP:** 4" in markdown
    assert "**Total GPUs:** 8" in markdown
    assert "**Observed GPU coverage:** torchinferno=8/8" in markdown
    assert f"**Harness commit:** `{'a' * 40}`" in markdown
    assert "**TP:** 4" not in markdown


def test_v3_result_eligibility_fails_closed_for_invalid_outputs() -> None:
    results = RunResults(
        model="model",
        tensor_parallel_size=4,
        requested_benchmarks=("bench",),
        minimum_correctness_rate=0.95,
        require_request_count_parity=True,
        output_token_ratio_tolerance=0.10,
    )

    def benchmark(
        *,
        correctness: float | None = 1.0,
        count: int = 2,
        raw_tokens: tuple[int, ...] = (5, 5),
        total_tokens: float = 10,
    ) -> BenchmarkResult:
        metrics: dict[str, float] = {
            "num_requests": count,
            "total_output_tokens": total_tokens,
        }
        if correctness is not None:
            metrics["correctness_rate"] = correctness
        return BenchmarkResult(
            name="bench",
            metrics=metrics,
            raw_requests=[RequestMetrics(output_tokens=value) for value in raw_tokens],
        )

    results.providers["valid"] = ProviderResults(
        provider="valid", benchmarks={"bench": benchmark()}
    )
    results.providers["low_correctness"] = ProviderResults(
        provider="low_correctness",
        benchmarks={"bench": benchmark(correctness=0.5)},
    )
    results.providers["missing_correctness"] = ProviderResults(
        provider="missing_correctness",
        benchmarks={"bench": benchmark(correctness=None)},
    )
    results.providers["missing_benchmark"] = ProviderResults(
        provider="missing_benchmark"
    )
    results.providers["reported_error"] = ProviderResults(
        provider="reported_error",
        benchmarks={"bench": benchmark()},
        errors={"_server": "integrity failed"},
    )
    results.providers["empty_raw"] = ProviderResults(
        provider="empty_raw",
        benchmarks={"bench": benchmark(raw_tokens=())},
    )
    results.providers["raw_output_mismatch"] = ProviderResults(
        provider="raw_output_mismatch",
        benchmarks={"bench": benchmark(raw_tokens=(4, 5))},
    )
    results.providers["output_outlier"] = ProviderResults(
        provider="output_outlier",
        benchmarks={
            "bench": benchmark(raw_tokens=(15, 15), total_tokens=30)
        },
    )
    results.providers["nan_correctness"] = ProviderResults(
        provider="nan_correctness",
        benchmarks={"bench": benchmark(correctness=math.nan)},
    )
    results.providers["infinite_output"] = ProviderResults(
        provider="infinite_output",
        benchmarks={
            "bench": benchmark(raw_tokens=(), total_tokens=math.inf)
        },
    )

    results._refresh_integrity_status()

    assert results.providers["valid"].comparable
    for name in results.providers.keys() - {"valid"}:
        assert not results.providers[name].comparable, name
        assert results.providers[name].integrity_warnings


def test_client_tokenizer_replaces_stream_chunk_count(monkeypatch) -> None:
    tokenizer_requests = []

    class FakeTokenizer:
        def encode(self, text: str, *, add_special_tokens: bool) -> list[int]:
            assert text == "answer"
            assert not add_special_tokens
            return [1, 2]

    monkeypatch.setattr(
        "inference_bench.benchmarks.base._tokenizer_for_model",
        lambda model, revision: (
            tokenizer_requests.append((model, revision)) or FakeTokenizer()
        ),
    )
    request = RequestMetrics(
        ttft_ms=10,
        e2e_latency_ms=30,
        output_tokens=20,
        stream_content_chunks=20,
        completion_text="answer",
    )
    result = BenchmarkResult(name="bench", raw_requests=[request])

    result.summarize(model="model", model_revision="pinned-revision")

    assert request.output_tokens == 2
    assert request.stream_content_chunks == 20
    assert request.tpot_ms == 20
    assert request.throughput_tps == pytest.approx(2 / 0.03)
    assert tokenizer_requests == [("model", "pinned-revision")]


def test_authoritative_tokenizer_falls_back_to_fast_tokenizer_for_new_model_config(
    monkeypatch,
) -> None:
    from inference_bench.benchmarks.base import _tokenizer_for_model

    sentinel = object()

    class UnsupportedAutoTokenizer:
        @classmethod
        def from_pretrained(cls, _model, **_kwargs):  # noqa: ANN001, ANN003
            raise AttributeError("unknown model config")

    class WorkingFastTokenizer:
        @classmethod
        def from_pretrained(cls, model, **kwargs):  # noqa: ANN001, ANN003
            assert model == "/verified/v4-snapshot"
            assert kwargs == {"revision": None, "trust_remote_code": True}
            return sentinel

    monkeypatch.setitem(
        sys.modules,
        "transformers",
        types.SimpleNamespace(
            AutoTokenizer=UnsupportedAutoTokenizer,
            PreTrainedTokenizerFast=WorkingFastTokenizer,
        ),
    )
    _tokenizer_for_model.cache_clear()

    assert _tokenizer_for_model("/verified/v4-snapshot", None) is sentinel
    _tokenizer_for_model.cache_clear()


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


def test_console_summary_warns_on_torchinferno_generated_prefix_reuse(
    capsys,
    tmp_path,
) -> None:
    queue_log = tmp_path / "torchinferno_queue_profile.jsonl"
    queue_log.write_text(
        '{"runtime_generated_prefix_reuse_requests": 7, '
        '"runtime_generated_prefix_reuse_tokens": 21, '
        '"runtime_prefix_reuse_route_counts": {"generated_prefix": 7}}\n'
    )
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        extra_log_paths={"queue_profile": str(queue_log)},
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={"ttft_median_ms": 1.0},
            )
        },
    )
    results.providers["vllm"] = ProviderResults(
        provider="vllm",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={"ttft_median_ms": 2.0},
            )
        },
    )

    results.print_comparison()

    output = capsys.readouterr().out
    assert "Integrity Warnings" in output
    assert "generated-prefix logits reuse" in output
    assert "generated-prefix reuse requests=7" in output
    assert re.search(r"^torchinferno\s+N/C$", output, re.MULTILINE)


def test_markdown_summary_warns_on_saved_torchinferno_generated_prefix_reuse(
    tmp_path,
) -> None:
    queue_log = tmp_path / "torchinferno_queue_profile.jsonl"
    queue_log.write_text(
        '{"runtime_generated_prefix_reuse_requests": 3, '
        '"runtime_generated_prefix_reuse_tokens": 9, '
        '"runtime_prefix_reuse_route_counts": {"generated_prefix": 3}}\n'
    )
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        extra_log_paths={"queue_profile": str(queue_log)},
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={"ttft_median_ms": 1.0},
            )
        },
    )
    results.providers["vllm"] = ProviderResults(
        provider="vllm",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={"ttft_median_ms": 2.0},
            )
        },
    )
    results_path = results.save(tmp_path / "results")

    markdown = generate(results_path)
    csv_text = results.save_csv(tmp_path / "results").read_text()

    assert "## Integrity Warnings" in markdown
    assert "**torchinferno:** TorchInferno queue profile reports generated-prefix logits reuse" in markdown
    assert "generated-prefix reuse requests=3" in markdown
    assert re.search(r"\|\s*bench\s*\|\s*N/C\s*\|\s*0/4\s*\|", markdown)
    assert "N/C = excluded from scoring" in markdown
    assert "torchinferno,false" in csv_text
    assert "ttft_median_ms,1.00,2.00," in csv_text


def test_console_summary_warns_on_torchinferno_prompt_shortcuts(
    capsys,
    tmp_path,
) -> None:
    queue_log = tmp_path / "torchinferno_queue_profile.jsonl"
    queue_log.write_text(
        '{"runtime_prompt_lookup_requests": 4, '
        '"runtime_prompt_lookup_accepted_tokens": 8, '
        '"runtime_repeated_sample_state_hits": 2, '
        '"runtime_repeated_sample_state_tokens": 5}\n'
    )
    results = RunResults(model="model", tensor_parallel_size=1)
    results.providers["torchinferno"] = ProviderResults(
        provider="torchinferno",
        extra_log_paths={"queue_profile": str(queue_log)},
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={"ttft_median_ms": 1.0},
            )
        },
    )
    results.providers["vllm"] = ProviderResults(
        provider="vllm",
        benchmarks={
            "bench": BenchmarkResult(
                name="bench",
                metrics={"ttft_median_ms": 2.0},
            )
        },
    )

    results.print_comparison()

    output = capsys.readouterr().out
    assert "Integrity Warnings" in output
    assert "prompt lookup requests=4" in output
    assert "accepted tokens=8" in output
    assert "repeated-sample state hits=2" in output
    assert "normal KV prefix reuse is still allowed" in output


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
