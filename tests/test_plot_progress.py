from __future__ import annotations

import json

from scripts.plot_progress import load_all_runs


def _write_run(
    model_dir,
    name,
    *,
    providers,
    requested_providers=None,
    metric_schema_version=None,
    output_token_count_method=None,
) -> None:
    run_dir = model_dir / "runs" / name
    run_dir.mkdir(parents=True)
    data = {
        "model": "model",
        "tensor_parallel_size": 1,
        "providers": {provider: {"benchmarks": {}} for provider in providers},
    }
    if requested_providers is not None:
        data["requested_providers"] = requested_providers
    if metric_schema_version is not None:
        data["metric_schema_version"] = metric_schema_version
    if output_token_count_method is not None:
        data["output_token_count_method"] = output_token_count_method
    (run_dir / "results.json").write_text(json.dumps(data))


def test_load_all_runs_accepts_completed_requested_provider_subset(tmp_path) -> None:
    _write_run(
        tmp_path,
        "20260720_010000",
        providers=("torchinferno",),
        requested_providers=["torchinferno"],
    )
    _write_run(
        tmp_path,
        "20260720_020000",
        providers=("torchinferno",),
        requested_providers=["torchinferno", "vllm"],
    )
    _write_run(
        tmp_path,
        "20260720_030000",
        providers=("torchinferno",),
    )

    runs = load_all_runs(tmp_path)

    assert [run["_run_dir"] for run in runs] == ["20260720_010000"]


def test_load_all_runs_does_not_mix_output_token_schemas(tmp_path) -> None:
    for hour, version, method in (
        (1, 1, "sse_content_chunks"),
        (2, 2, "client_tokenizer"),
        (3, 2, "client_tokenizer"),
    ):
        _write_run(
            tmp_path,
            f"20260720_0{hour}0000",
            providers=("vllm",),
            requested_providers=["vllm"],
            metric_schema_version=version,
            output_token_count_method=method,
        )

    runs = load_all_runs(tmp_path)

    assert [run["_run_dir"] for run in runs] == [
        "20260720_020000",
        "20260720_030000",
    ]
