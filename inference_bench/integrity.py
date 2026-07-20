from __future__ import annotations

import json
from pathlib import Path
from typing import Any


_REQUIRED_RUNTIME_COUNTERS = (
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
        event = record.get("event")
        is_runtime_record = event in {"online_batcher", "online_batcher_quiescent"} or any(
            key.startswith("runtime_") for key in record
        )
        if not is_runtime_record:
            continue
        runtime_records += 1
        if any(key not in record for key in _REQUIRED_RUNTIME_COUNTERS):
            missing_counter_records += 1
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
    if runtime_records <= 0:
        warnings.extend(_integrity_unavailable("queue profile has no runtime records"))
        return warnings
    if missing_counter_records:
        warnings.extend(
            _integrity_unavailable(
                f"{missing_counter_records} runtime record(s) omit required cache counters"
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
