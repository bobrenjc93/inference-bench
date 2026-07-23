from __future__ import annotations

import json

import pytest

from inference_bench.integrity import (
    DISAGGREGATED_RUNTIME_SHORTCUT_COUNTERS,
    TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS,
    torchinferno_logits_cache_warnings,
)


def _clean_runtime_record() -> dict[str, object]:
    return {
        "event": "online_batcher",
        "runtime_generated_prefix_store_requests": 0,
        "runtime_generated_prefix_reuse_requests": 0,
        "runtime_generated_prefix_reuse_tokens": 0,
        "runtime_prompt_lookup_requests": 0,
        "runtime_prompt_lookup_accepted_tokens": 0,
        "runtime_repeated_sample_state_hits": 0,
        "runtime_repeated_sample_state_tokens": 0,
        "runtime_reusable_prefix_logits_entries": 0,
        "runtime_reusable_prefix_logits_tokens": 0,
        "runtime_reusable_prefix_sample_state_entries": 0,
        "runtime_reusable_prefix_greedy_token_entries": 0,
        "runtime_prefix_reuse_route_counts": {"common_prefix": 4},
    }


def _disaggregated_records() -> list[dict[str, object]]:
    attestation = {
        "event": "inference_bench_cache_integrity_attestation",
        "deployment_mode": "disaggregated_prefill_decode",
        "expected_tensor_parallel_size_per_role": 4,
        "expected_world_size": 8,
        "forced_cache_environment": {
            name: "0" for name in TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS
        },
    }
    handoff = {
        "event": "disaggregated_runtime_integrity",
        "stream_group_sequence": 0,
        "batch_size": 2,
        "emitted_tokens": 4,
        "mode": "prefill-decode",
        "transport": "nccl-p2p",
        "tensor_parallel_size_per_role": 4,
        "world_size": 8,
        "transfer_count": 1,
        "transfer_bytes": 1024,
        "transfer_count_delta": 1,
        "transfer_bytes_delta": 1024,
        **{name: 0 for name in DISAGGREGATED_RUNTIME_SHORTCUT_COUNTERS},
    }
    return [
        attestation,
        {"event": "benchmark_start", "benchmark": "few_shot"},
        {
            "event": "stream_group",
            "stream_group_sequence": 0,
            "batch_size": 2,
            "emitted_tokens": 4,
        },
        handoff,
        {
            "event": "benchmark_end",
            "benchmark": "few_shot",
            "status": "ok",
        },
    ]


def _write_records(path, records: list[dict[str, object]]) -> None:  # noqa: ANN001
    path.write_text("".join(json.dumps(record) + "\n" for record in records))


def test_torchinferno_integrity_accepts_complete_zero_counters(tmp_path) -> None:
    path = tmp_path / "queue.jsonl"
    path.write_text(json.dumps(_clean_runtime_record()) + "\n")

    assert torchinferno_logits_cache_warnings(path) == []


def test_torchinferno_integrity_fails_closed_for_missing_profile(tmp_path) -> None:
    warnings = torchinferno_logits_cache_warnings(tmp_path / "missing.jsonl")

    assert "not comparable" in warnings[0]
    assert "missing" in warnings[0]


def test_torchinferno_integrity_fails_closed_for_missing_counter(tmp_path) -> None:
    record = _clean_runtime_record()
    del record["runtime_reusable_prefix_logits_entries"]
    path = tmp_path / "queue.jsonl"
    path.write_text(json.dumps(record) + "\n")

    warnings = torchinferno_logits_cache_warnings(path)

    assert "omit required cache counters" in warnings[0]


def test_torchinferno_integrity_rejects_prefix_payloads(tmp_path) -> None:
    record = _clean_runtime_record()
    record["runtime_reusable_prefix_greedy_token_entries"] = 1
    path = tmp_path / "queue.jsonl"
    path.write_text(json.dumps(record) + "\n")

    warnings = torchinferno_logits_cache_warnings(path)

    assert "greedy tokens=1" in warnings[0]


def test_torchinferno_integrity_accepts_per_group_disaggregated_handoff(tmp_path) -> None:
    path = tmp_path / "queue.jsonl"
    _write_records(path, _disaggregated_records())

    assert torchinferno_logits_cache_warnings(path) == []


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        (lambda records: records.pop(0), "no harness topology attestation"),
        (
            lambda records: records[3].__setitem__("transfer_count_delta", 0),
            "no positive KV handoff delta",
        ),
        (
            lambda records: records[3].__setitem__("transfer_bytes", 2048),
            "not monotonic",
        ),
        (
            lambda records: records[3].__setitem__("world_size", 4),
            "topology does not match",
        ),
        (
            lambda records: records[3].__setitem__(
                "runtime_generated_prefix_reuse_requests", 1
            ),
            "nonzero shortcut counters",
        ),
        (
            lambda records: records[3].__setitem__("transfer_count", 1.0),
            "transfer counters are malformed",
        ),
        (
            lambda records: records[3].pop("batch_size"),
            "do not describe the same work",
        ),
        (
            lambda records: records.pop(3),
            "lacks one-to-one stream/KV handoff evidence",
        ),
    ],
)
def test_torchinferno_integrity_rejects_invalid_disaggregated_evidence(
    tmp_path,
    mutation,
    message,
) -> None:  # noqa: ANN001
    records = _disaggregated_records()
    mutation(records)
    path = tmp_path / "queue.jsonl"
    _write_records(path, records)

    warnings = torchinferno_logits_cache_warnings(path)

    assert any(message in warning for warning in warnings)
