from __future__ import annotations

import json

from scripts.plot_progress import load_all_runs


def _write_run(model_dir, name, *, providers, requested_providers=None) -> None:
    run_dir = model_dir / "runs" / name
    run_dir.mkdir(parents=True)
    data = {
        "model": "model",
        "tensor_parallel_size": 1,
        "providers": {provider: {"benchmarks": {}} for provider in providers},
    }
    if requested_providers is not None:
        data["requested_providers"] = requested_providers
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
