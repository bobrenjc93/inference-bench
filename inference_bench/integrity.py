from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REQUIRED_RUNTIME_COUNTERS = (
    "runtime_generated_prefix_store_requests",
    "runtime_generated_prefix_reuse_requests",
    "runtime_generated_prefix_reuse_tokens",
    "runtime_prompt_lookup_requests",
    "runtime_prompt_lookup_accepted_tokens",
    "runtime_repeated_sample_state_hits",
    "runtime_repeated_sample_state_tokens",
    "runtime_reusable_prefix_logits_entries",
    "runtime_reusable_prefix_logits_tokens",
    "runtime_reusable_prefix_sample_state_entries",
    "runtime_reusable_prefix_greedy_token_entries",
)

DISAGGREGATED_RUNTIME_SHORTCUT_COUNTERS = REQUIRED_RUNTIME_COUNTERS + (
    "runtime_continuous_stream_groups",
    "runtime_identical_prompt_batch_groups",
    "runtime_identical_prompt_batch_requests",
)

TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS = (
    "TORCHINFERNO_CONTINUOUS_GENERATED_PREFIX_CACHE",
    "TORCHINFERNO_CONTINUOUS_ADAPTIVE_GENERATED_PREFIX_CACHE",
    "TORCHINFERNO_OPENAI_TP_ONLINE_GENERATED_PREFIX_CACHE",
    "TORCHINFERNO_CONTINUOUS_PREFIX_CACHE_STORE_LOGITS",
    "TORCHINFERNO_CONTINUOUS_PINNED_FULL_PROMPT_STORE_LOGITS",
    "TORCHINFERNO_OPENAI_PROMPT_LOGITS_CACHE",
    "TORCHINFERNO_CONTINUOUS_PROMPT_LOOKUP_DECODE",
    "TORCHINFERNO_CONTINUOUS_CACHED_REPEATED_SAMPLE_STATE",
)


def _integrity_unavailable(detail: str) -> list[str]:
    return [
        "TorchInferno score-facing cache integrity could not be verified "
        f"({detail}). Treat TorchInferno metrics in this run as not comparable."
    ]


def torchinferno_logits_cache_warnings(queue_profile_path: str | Path) -> list[str]:
    path = Path(queue_profile_path)
    if not path.exists():
        return _integrity_unavailable("queue profile is missing")

    max_reuse_requests = 0
    max_reuse_tokens = 0
    max_store_requests = 0
    max_generated_route_count = 0
    max_prompt_lookup_requests = 0
    max_prompt_lookup_accepted_tokens = 0
    max_repeated_sample_hits = 0
    max_repeated_sample_tokens = 0
    max_prefix_logits_entries = 0
    max_prefix_logits_tokens = 0
    max_prefix_sample_states = 0
    max_prefix_greedy_tokens = 0
    runtime_records = 0
    malformed_lines = 0
    missing_counter_records = 0
    invalid_counter_records = 0
    disaggregated_attestations = 0
    invalid_attestations = 0
    records: list[dict[str, Any]] = []
    try:
        lines = path.read_text().splitlines()
    except OSError as exc:
        return _integrity_unavailable(f"queue profile is unreadable: {exc}")
    for line in lines:
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            malformed_lines += 1
            continue
        if not isinstance(record, dict):
            malformed_lines += 1
            continue
        records.append(record)
        event = record.get("event")
        if event == "inference_bench_cache_integrity_attestation":
            disaggregated_attestations += 1
            forced = record.get("forced_cache_environment")
            valid_forced_env = isinstance(forced, dict) and all(
                forced.get(name) == "0"
                for name in TORCHINFERNO_PROHIBITED_CACHE_ENV_VARS
            )
            if (
                record.get("deployment_mode")
                != "disaggregated_prefill_decode"
                or not valid_forced_env
                or not _is_positive_integer(
                    record.get("expected_tensor_parallel_size_per_role")
                )
                or not _is_positive_integer(record.get("expected_world_size"))
            ):
                invalid_attestations += 1
        is_runtime_record = event in {
            "online_batcher",
            "online_batcher_quiescent",
            "disaggregated_runtime_integrity",
        } or any(key.startswith("runtime_") for key in record)
        if not is_runtime_record:
            continue
        runtime_records += 1
        if any(key not in record for key in REQUIRED_RUNTIME_COUNTERS):
            missing_counter_records += 1
        elif any(not _is_nonnegative_integer(record[key]) for key in REQUIRED_RUNTIME_COUNTERS):
            invalid_counter_records += 1
        max_reuse_requests = max(
            max_reuse_requests,
            _nonnegative_int(record.get("runtime_generated_prefix_reuse_requests")),
        )
        max_reuse_tokens = max(
            max_reuse_tokens,
            _nonnegative_int(record.get("runtime_generated_prefix_reuse_tokens")),
        )
        max_store_requests = max(
            max_store_requests,
            _nonnegative_int(record.get("runtime_generated_prefix_store_requests")),
        )
        max_prompt_lookup_requests = max(
            max_prompt_lookup_requests,
            _nonnegative_int(record.get("runtime_prompt_lookup_requests")),
        )
        max_prompt_lookup_accepted_tokens = max(
            max_prompt_lookup_accepted_tokens,
            _nonnegative_int(record.get("runtime_prompt_lookup_accepted_tokens")),
        )
        max_repeated_sample_hits = max(
            max_repeated_sample_hits,
            _nonnegative_int(record.get("runtime_repeated_sample_state_hits")),
        )
        max_repeated_sample_tokens = max(
            max_repeated_sample_tokens,
            _nonnegative_int(record.get("runtime_repeated_sample_state_tokens")),
        )
        max_prefix_logits_entries = max(
            max_prefix_logits_entries,
            _nonnegative_int(record.get("runtime_reusable_prefix_logits_entries")),
        )
        max_prefix_logits_tokens = max(
            max_prefix_logits_tokens,
            _nonnegative_int(record.get("runtime_reusable_prefix_logits_tokens")),
        )
        max_prefix_sample_states = max(
            max_prefix_sample_states,
            _nonnegative_int(record.get("runtime_reusable_prefix_sample_state_entries")),
        )
        max_prefix_greedy_tokens = max(
            max_prefix_greedy_tokens,
            _nonnegative_int(record.get("runtime_reusable_prefix_greedy_token_entries")),
        )
        route_counts = record.get("runtime_prefix_reuse_route_counts")
        if isinstance(route_counts, dict):
            max_generated_route_count = max(
                max_generated_route_count,
                _nonnegative_int(route_counts.get("generated_prefix")),
            )

    warnings: list[str] = []
    if malformed_lines:
        warnings.extend(
            _integrity_unavailable(
                f"queue profile has {malformed_lines} malformed record(s)"
            )
        )
    warnings.extend(_disaggregated_runtime_warnings(records))
    if runtime_records <= 0:
        warnings.extend(_integrity_unavailable("queue profile has no runtime records"))
        return warnings
    if missing_counter_records:
        warnings.extend(
            _integrity_unavailable(
                f"{missing_counter_records} runtime record(s) omit required cache counters"
            )
        )
    if invalid_counter_records:
        warnings.extend(
            _integrity_unavailable(
                f"{invalid_counter_records} runtime record(s) have invalid cache counters"
            )
        )
    if invalid_attestations:
        warnings.extend(
            _integrity_unavailable(
                f"{invalid_attestations} disaggregated cache attestation(s) are invalid"
            )
        )
    if (
        max_store_requests <= 0
        and max_reuse_requests <= 0
        and max_generated_route_count <= 0
        and max_prompt_lookup_accepted_tokens <= 0
        and max_repeated_sample_hits <= 0
        and max_prefix_logits_entries <= 0
        and max_prefix_logits_tokens <= 0
        and max_prefix_sample_states <= 0
        and max_prefix_greedy_tokens <= 0
    ):
        return warnings
    details = []
    if max_store_requests > 0 or max_reuse_requests > 0 or max_generated_route_count > 0:
        details.append(
            f"generated-prefix store requests={max_store_requests}, "
            f"generated-prefix reuse requests={max_reuse_requests}, "
            f"reuse tokens={max_reuse_tokens}, "
            f"generated-prefix route count={max_generated_route_count}"
        )
    if max_prompt_lookup_accepted_tokens > 0:
        details.append(
            f"prompt lookup requests={max_prompt_lookup_requests}, "
            f"accepted tokens={max_prompt_lookup_accepted_tokens}"
        )
    if max_repeated_sample_hits > 0:
        details.append(
            f"repeated-sample state hits={max_repeated_sample_hits}, "
            f"tokens={max_repeated_sample_tokens}"
        )
    if (
        max_prefix_logits_entries > 0
        or max_prefix_logits_tokens > 0
        or max_prefix_sample_states > 0
        or max_prefix_greedy_tokens > 0
    ):
        details.append(
            f"reusable-prefix logits entries={max_prefix_logits_entries}, "
            f"logit tokens={max_prefix_logits_tokens}, "
            f"sample states={max_prefix_sample_states}, "
            f"greedy tokens={max_prefix_greedy_tokens}"
        )
    detail = "; ".join(details)
    warnings.append(
        "TorchInferno queue profile reports generated-prefix logits reuse "
        "or related prompt shortcuts "
        f"({detail}). Treat TorchInferno score-facing metrics in this run as "
        "not comparable; normal KV prefix reuse is still allowed."
    )
    return warnings


def _disaggregated_runtime_warnings(records: list[dict[str, Any]]) -> list[str]:
    attestations = [
        record
        for record in records
        if record.get("event") == "inference_bench_cache_integrity_attestation"
    ]
    if not attestations:
        if any(
            record.get("event") == "disaggregated_runtime_integrity"
            for record in records
        ):
            return _integrity_unavailable(
                "disaggregated runtime evidence has no harness topology attestation"
            )
        return []
    first_attestation = attestations[0]
    expected_tp = first_attestation.get("expected_tensor_parallel_size_per_role")
    expected_world_size = first_attestation.get("expected_world_size")
    warnings: list[str] = []
    if len(attestations) != 1:
        warnings.extend(
            _integrity_unavailable(
                f"expected one disaggregated topology attestation, found {len(attestations)}"
            )
        )
    active: dict[str, Any] | None = None
    successful_windows = 0
    previous_count = 0
    previous_bytes = 0

    for record in records:
        event = record.get("event")
        if event == "benchmark_start":
            if active is not None:
                warnings.extend(_integrity_unavailable("benchmark profile windows overlap"))
            active = {
                "benchmark": record.get("benchmark"),
                "streams": {},
                "handoffs": {},
            }
            continue
        if event == "stream_group":
            if active is None:
                warnings.extend(
                    _integrity_unavailable("stream group appears outside a benchmark window")
                )
                continue
            sequence = record.get("stream_group_sequence")
            streams = active["streams"]
            if not _is_nonnegative_integer(sequence) or sequence in streams:
                warnings.extend(
                    _integrity_unavailable("stream group sequence is invalid or duplicated")
                )
                continue
            streams[sequence] = record
            continue
        if event == "disaggregated_runtime_integrity":
            sequence = record.get("stream_group_sequence")
            if active is None:
                warnings.extend(
                    _integrity_unavailable("KV handoff evidence appears outside a benchmark window")
                )
            elif not _is_nonnegative_integer(sequence) or sequence in active["handoffs"]:
                warnings.extend(
                    _integrity_unavailable("KV handoff sequence is invalid or duplicated")
                )
            else:
                active["handoffs"][sequence] = record

            count = record.get("transfer_count")
            transfer_bytes = record.get("transfer_bytes")
            count_delta = record.get("transfer_count_delta")
            bytes_delta = record.get("transfer_bytes_delta")
            valid_counters = all(
                _is_nonnegative_integer(value)
                for value in (count, transfer_bytes, count_delta, bytes_delta)
            )
            if not valid_counters:
                warnings.extend(
                    _integrity_unavailable("KV handoff transfer counters are malformed")
                )
            else:
                assert isinstance(count, int)
                assert isinstance(transfer_bytes, int)
                assert isinstance(count_delta, int)
                assert isinstance(bytes_delta, int)
                if count_delta <= 0 or bytes_delta <= 0:
                    warnings.extend(
                        _integrity_unavailable(
                            "a profiled stream group has no positive KV handoff delta"
                        )
                    )
                if (
                    count != previous_count + count_delta
                    or transfer_bytes != previous_bytes + bytes_delta
                ):
                    warnings.extend(
                        _integrity_unavailable(
                            "KV handoff cumulative counters are not monotonic"
                        )
                    )
                previous_count = count
                previous_bytes = transfer_bytes
            if (
                record.get("mode") != "prefill-decode"
                or record.get("transport") != "nccl-p2p"
                or record.get("tensor_parallel_size_per_role") != expected_tp
                or record.get("world_size") != expected_world_size
            ):
                warnings.extend(
                    _integrity_unavailable(
                        "KV handoff runtime topology does not match the configured deployment"
                    )
                )
            if any(
                not _is_nonnegative_integer(record.get(name))
                or record.get(name) != 0
                for name in DISAGGREGATED_RUNTIME_SHORTCUT_COUNTERS
            ):
                warnings.extend(
                    _integrity_unavailable(
                        "disaggregated runtime reports malformed or nonzero shortcut counters"
                    )
                )
            continue
        if event != "benchmark_end":
            continue
        if active is None or record.get("benchmark") != active.get("benchmark"):
            warnings.extend(_integrity_unavailable("benchmark profile window is unmatched"))
            active = None
            continue
        if record.get("status") == "ok":
            successful_windows += 1
            streams = active["streams"]
            handoffs = active["handoffs"]
            if not streams or set(streams) != set(handoffs):
                warnings.extend(
                    _integrity_unavailable(
                        f"benchmark {active['benchmark']!r} lacks one-to-one "
                        "stream/KV handoff evidence"
                    )
                )
            for sequence in set(streams).intersection(handoffs):
                stream = streams[sequence]
                handoff = handoffs[sequence]
                if (
                    not _is_positive_integer(stream.get("emitted_tokens"))
                    or not _is_positive_integer(stream.get("batch_size"))
                    or not _is_positive_integer(handoff.get("emitted_tokens"))
                    or not _is_positive_integer(handoff.get("batch_size"))
                    or stream.get("batch_size") != handoff.get("batch_size")
                    or stream.get("emitted_tokens") != handoff.get("emitted_tokens")
                ):
                    warnings.extend(
                        _integrity_unavailable(
                            "stream group and KV handoff evidence do not describe the same work"
                        )
                    )
        active = None

    if active is not None:
        warnings.extend(_integrity_unavailable("benchmark profile window is incomplete"))
    if successful_windows <= 0:
        warnings.extend(
            _integrity_unavailable("queue profile has no successful benchmark window")
        )
    return _dedupe(warnings)


def warnings_for_saved_provider(
    provider_name: str,
    provider_data: dict[str, Any],
    *,
    run_dir: str | Path,
) -> list[str]:
    if provider_name != "torchinferno":
        return []
    extra_logs = provider_data.get("extra_logs")
    if not isinstance(extra_logs, dict):
        return _integrity_unavailable("saved provider has no extra logs")
    queue_profile = extra_logs.get("queue_profile")
    if not isinstance(queue_profile, str) or not queue_profile:
        return _integrity_unavailable("saved provider has no queue profile")
    return torchinferno_logits_cache_warnings(Path(run_dir) / queue_profile)


def warnings_for_live_provider(
    provider_name: str,
    extra_log_paths: dict[str, str],
) -> list[str]:
    if provider_name != "torchinferno":
        return []
    queue_profile = extra_log_paths.get("queue_profile", "")
    if not queue_profile:
        return _integrity_unavailable("live provider has no queue profile")
    return torchinferno_logits_cache_warnings(queue_profile)


def _nonnegative_int(value: object) -> int:
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return max(0, value)
    if isinstance(value, float) and value.is_integer():
        return max(0, int(value))
    return 0


def _is_nonnegative_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _is_positive_integer(value: object) -> bool:
    return _is_nonnegative_integer(value) and int(value) > 0


def _dedupe(values: list[str]) -> list[str]:
    return list(dict.fromkeys(values))
