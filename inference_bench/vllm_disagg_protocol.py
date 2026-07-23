from __future__ import annotations


def make_prefill_request(request_data: dict) -> dict:
    prefill_request = dict(request_data)
    prefill_request["max_tokens"] = 1
    if "max_completion_tokens" in prefill_request:
        prefill_request["max_completion_tokens"] = 1
    return prefill_request
