from __future__ import annotations

STANDARD_DEPLOYMENT = "standard"
DISAGGREGATED_PREFILL_DECODE = "disaggregated_prefill_decode"

_EVALUATION_DEPLOYMENTS = {
    2: STANDARD_DEPLOYMENT,
    3: STANDARD_DEPLOYMENT,
    4: DISAGGREGATED_PREFILL_DECODE,
}

_EVALUATION_TENSOR_PARALLEL_SIZES = {
    2: 8,
    3: 4,
    4: 4,
}

_DEPLOYMENT_ALIASES = {
    "standard": STANDARD_DEPLOYMENT,
    "disaggregated_prefill_decode": DISAGGREGATED_PREFILL_DECODE,
    "disaggregated-prefill-decode": DISAGGREGATED_PREFILL_DECODE,
    "prefill_decode": DISAGGREGATED_PREFILL_DECODE,
    "prefill-decode": DISAGGREGATED_PREFILL_DECODE,
}


def _strict_evaluation_version(evaluation_version: object) -> int:
    if isinstance(evaluation_version, bool) or not isinstance(
        evaluation_version,
        int,
    ):
        raise ValueError(
            f"evaluation_version must be an integer, got {evaluation_version!r}"
        )
    return evaluation_version


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


def deployment_mode_for_evaluation(evaluation_version: int) -> str:
    version = _strict_evaluation_version(evaluation_version)
    try:
        return _EVALUATION_DEPLOYMENTS[version]
    except KeyError as exc:
        choices = ", ".join(f"v{value}" for value in _EVALUATION_DEPLOYMENTS)
        raise ValueError(
            f"Unsupported evaluation_version {version!r}; expected one of: {choices}"
        ) from exc


def results_dir_for_evaluation(evaluation_version: int) -> str:
    version = _strict_evaluation_version(evaluation_version)
    deployment_mode_for_evaluation(version)
    return f"./results/v{version - 1}"


def tensor_parallel_size_for_evaluation(evaluation_version: int) -> int:
    version = _strict_evaluation_version(evaluation_version)
    deployment_mode_for_evaluation(version)
    return _EVALUATION_TENSOR_PARALLEL_SIZES[version]


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
                "prefill/decode tensor parallel sizes require evaluation v4"
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
