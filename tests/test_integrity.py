from __future__ import annotations

import json

from inference_bench.integrity import torchinferno_logits_cache_warnings


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
