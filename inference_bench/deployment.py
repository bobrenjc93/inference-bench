from __future__ import annotations

STANDARD_DEPLOYMENT = "standard"
DISAGGREGATED_PREFILL_DECODE = "disaggregated_prefill_decode"

_DEPLOYMENT_ALIASES = {
    "standard": STANDARD_DEPLOYMENT,
    "disaggregated_prefill_decode": DISAGGREGATED_PREFILL_DECODE,
    "disaggregated-prefill-decode": DISAGGREGATED_PREFILL_DECODE,
    "prefill_decode": DISAGGREGATED_PREFILL_DECODE,
    "prefill-decode": DISAGGREGATED_PREFILL_DECODE,
}


def normalize_deployment_mode(mode: str) -> str:
    normalized = str(mode).strip().lower()
    try:
        return _DEPLOYMENT_ALIASES[normalized]
    except KeyError as exc:
        choices = ", ".join(
            (STANDARD_DEPLOYMENT, DISAGGREGATED_PREFILL_DECODE)
        )
        raise ValueError(
            f"Unsupported deployment_mode {mode!r}; expected one of: {choices}"
        ) from exc


def resolve_role_tensor_parallel_sizes(
    *,
    deployment_mode: str,
    tensor_parallel_size: int,
    prefill_tensor_parallel_size: int | None,
    decode_tensor_parallel_size: int | None,
) -> tuple[int | None, int | None]:
    mode = normalize_deployment_mode(deployment_mode)
    tp = int(tensor_parallel_size)
    if tp < 1:
        raise ValueError("tensor_parallel_size must be at least 1")
    if mode == STANDARD_DEPLOYMENT:
        if (
            prefill_tensor_parallel_size is not None
            or decode_tensor_parallel_size is not None
        ):
            raise ValueError(
                "prefill/decode tensor parallel sizes require "
                "deployment_mode=disaggregated_prefill_decode"
            )
        return None, None

    prefill_tp = (
        tp
        if prefill_tensor_parallel_size is None
        else int(prefill_tensor_parallel_size)
    )
    decode_tp = (
        tp
        if decode_tensor_parallel_size is None
        else int(decode_tensor_parallel_size)
    )
    if prefill_tp < 1 or decode_tp < 1:
        raise ValueError(
            "prefill_tensor_parallel_size and decode_tensor_parallel_size "
            "must both be at least 1"
        )
    return prefill_tp, decode_tp
