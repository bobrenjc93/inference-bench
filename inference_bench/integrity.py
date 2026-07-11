from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def torchinferno_logits_cache_warnings(queue_profile_path: str | Path) -> list[str]:
    path = Path(queue_profile_path)
    if not path.exists():
        return []

    max_reuse_requests = 0
    max_reuse_tokens = 0
    max_generated_route_count = 0
    parsed_records = 0
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(record, dict):
            continue
        parsed_records += 1
        max_reuse_requests = max(
            max_reuse_requests,
            _nonnegative_int(record.get("runtime_generated_prefix_reuse_requests")),
        )
        max_reuse_tokens = max(
            max_reuse_tokens,
            _nonnegative_int(record.get("runtime_generated_prefix_reuse_tokens")),
        )
        route_counts = record.get("runtime_prefix_reuse_route_counts")
        if isinstance(route_counts, dict):
            max_generated_route_count = max(
                max_generated_route_count,
                _nonnegative_int(route_counts.get("generated_prefix")),
            )

    if parsed_records <= 0:
        return []
    if max_reuse_requests <= 0 and max_generated_route_count <= 0:
        return []
    detail = (
        f"generated-prefix reuse requests={max_reuse_requests}, "
        f"reuse tokens={max_reuse_tokens}, "
        f"generated-prefix route count={max_generated_route_count}"
    )
    return [
        "TorchInferno queue profile reports generated-prefix logits reuse "
        f"({detail}). Treat TorchInferno score-facing metrics in this run as "
        "not comparable; normal KV prefix reuse is still allowed."
    ]


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
        return []
    queue_profile = extra_logs.get("queue_profile")
    if not isinstance(queue_profile, str) or not queue_profile:
        return []
    return torchinferno_logits_cache_warnings(Path(run_dir) / queue_profile)


def warnings_for_live_provider(
    provider_name: str,
    extra_log_paths: dict[str, str],
) -> list[str]:
    if provider_name != "torchinferno":
        return []
    queue_profile = extra_log_paths.get("queue_profile", "")
    if not queue_profile:
        return []
    return torchinferno_logits_cache_warnings(queue_profile)


def _nonnegative_int(value: object) -> int:
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return max(0, value)
    if isinstance(value, float) and value.is_integer():
        return max(0, int(value))
    return 0
