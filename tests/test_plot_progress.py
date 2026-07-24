from __future__ import annotations

import json

from scripts.plot_progress import load_all_runs, main as plot_progress


def _write_run(
    model_dir,
    name,
    *,
    providers,
    requested_providers=None,
    metric_schema_version=None,
    output_token_count_method=None,
    evaluation_version=2,
    finalized=None,
    requested_benchmarks=None,
    benchmark_metrics=None,
    build_time_s=0.0,
) -> None:
    run_dir = model_dir / "runs" / name
    run_dir.mkdir(parents=True)
    data = {
        "model": "model",
        "evaluation_version": evaluation_version,
        "tensor_parallel_size": 1,
        "providers": {
            provider: {
                "build_time_s": build_time_s,
                "benchmarks": {
                    benchmark: {"metrics": metrics}
                    for benchmark, metrics in (benchmark_metrics or {}).items()
                },
            }
            for provider in providers
        },
    }
    if requested_providers is not None:
        data["requested_providers"] = requested_providers
    if metric_schema_version is not None:
        data["metric_schema_version"] = metric_schema_version
    if output_token_count_method is not None:
        data["output_token_count_method"] = output_token_count_method
    if finalized is not None:
        data["finalized"] = finalized
    if requested_benchmarks is not None:
        data["requested_benchmarks"] = requested_benchmarks
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


def test_load_all_runs_rejects_unfinalized_or_partial_scored_runs(tmp_path) -> None:
    benchmarks = [
        "few_shot",
        "self_consistency",
        "multi_turn",
        "tree_of_thought",
        "long_output",
    ]
    providers = ("torchinferno", "vllm", "sglang")
    _write_run(
        tmp_path,
        "20260720_010000",
        providers=providers,
        requested_providers=list(providers),
        requested_benchmarks=benchmarks,
        evaluation_version=3,
        finalized=False,
    )
    _write_run(
        tmp_path,
        "20260720_020000",
        providers=("torchinferno",),
        requested_providers=["torchinferno"],
        requested_benchmarks=["multi_turn"],
        evaluation_version=3,
        finalized=True,
    )

    assert load_all_runs(tmp_path) == []


def test_plot_progress_generates_full_layout_for_first_scored_run(tmp_path) -> None:
    model_dir = tmp_path / "model"
    providers = ("torchinferno", "vllm", "sglang")
    benchmarks = (
        "few_shot",
        "self_consistency",
        "multi_turn",
        "tree_of_thought",
        "long_output",
    )
    benchmark_metrics = {
        benchmark: {
            "ttft_median_ms": 1.0,
            "tpot_median_ms": 0.0 if benchmark == "self_consistency" else 2.0,
            "e2e_median_ms": 3.0,
            "throughput_median_tps": 4.0,
            "correctness_rate": 1.0,
        }
        for benchmark in benchmarks
    }
    _write_run(
        model_dir,
        "20260720_010000",
        providers=providers,
        requested_providers=list(providers),
        requested_benchmarks=list(benchmarks),
        evaluation_version=3,
        finalized=True,
        benchmark_metrics=benchmark_metrics,
        build_time_s=1.0,
    )

    plot_progress(str(model_dir))

    generated = {
        path.relative_to(model_dir / "plots").as_posix()
        for path in (model_dir / "plots").rglob("*.png")
    }
    assert len(generated) == 30
    assert "cross_benchmark_averages/ttft_median_ms.png" in generated
    assert "multi_turn/throughput_median_tps.png" in generated
    assert "summary/build_times.png" in generated
    assert "self_consistency/tpot_median_ms.png" not in generated
