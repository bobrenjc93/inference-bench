#!/usr/bin/env python3
"""Generate cross-run progress charts from all inference-bench runs.

Usage:
    python scripts/plot_progress.py results/meta-llama--Meta-Llama-3.1-70B-Instruct

Scans <model_dir>/runs/*/results.json, generates time-series charts
to <model_dir>/plots/<benchmark>/<metric>.png.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from inference_bench.results import model_result_slug

PROVIDER_COLORS = {
    "vllm": "#1f77b4",
    "sglang": "#ff7f0e",
    "torchinferno": "#2ca02c",
}

PROVIDER_MARKERS = {
    "vllm": "o",
    "sglang": "s",
    "torchinferno": "^",
}

TRACKED_METRICS = [
    ("ttft_median_ms", "TTFT Median (ms)"),
    ("tpot_median_ms", "TPOT Median (ms)"),
    ("e2e_median_ms", "E2E Median (ms)"),
    ("throughput_median_tps", "Throughput Median (tok/s)"),
    ("correctness_rate", "Correctness Rate"),
]


EXPECTED_PROVIDERS = {"torchinferno", "vllm", "sglang"}
EXPECTED_BENCHMARKS = {
    "few_shot",
    "self_consistency",
    "multi_turn",
    "tree_of_thought",
    "long_output",
}


def load_all_runs(model_dir: Path) -> list[dict]:
    runs = []
    runs_dir = model_dir / "runs"
    if not runs_dir.exists():
        return runs
    for run_dir in sorted(runs_dir.iterdir()):
        json_path = run_dir / "results.json"
        if not json_path.exists():
            continue
        with open(json_path) as f:
            data = json.load(f)
        evaluation_version = data.get("evaluation_version", 2)
        if evaluation_version >= 3:
            hardware = str(data.get("hardware", ""))
            expected_model_slug = (
                model_dir.parent.name
                if hardware and model_dir.name == hardware
                else model_dir.name
            )
            try:
                if model_result_slug(str(data.get("model", ""))) != expected_model_slug:
                    continue
            except ValueError:
                continue
            if data.get("finalized") is not True:
                continue
            if set(data.get("requested_providers", ())) != EXPECTED_PROVIDERS:
                continue
            if set(data.get("requested_benchmarks", ())) != EXPECTED_BENCHMARKS:
                continue
        present_providers = set(data.get("providers", {}))
        requested_providers = data.get("requested_providers")
        if isinstance(requested_providers, list) and requested_providers:
            required_providers = {
                provider
                for provider in requested_providers
                if isinstance(provider, str) and provider
            }
        else:
            # Legacy results did not record the requested subset, so preserve
            # the old fail-closed rule for those runs.
            required_providers = EXPECTED_PROVIDERS
        if evaluation_version >= 3 and any(
            not EXPECTED_BENCHMARKS
            <= set(data["providers"][provider].get("benchmarks", {}))
            for provider in EXPECTED_PROVIDERS
            if provider in data.get("providers", {})
        ):
            continue
        if not required_providers or not required_providers <= present_providers:
            continue
        data["_run_dir"] = str(run_dir.name)
        runs.append(data)
    if runs:
        latest_schema = (
            runs[-1].get("metric_schema_version", 1),
            runs[-1].get("output_token_count_method", "sse_content_chunks"),
        )
        runs = [
            run
            for run in runs
            if (
                run.get("metric_schema_version", 1),
                run.get("output_token_count_method", "sse_content_chunks"),
            )
            == latest_schema
        ]
    return runs


def parse_run_time(run: dict) -> datetime:
    return datetime.strptime(run["_run_dir"], "%Y%m%d_%H%M%S")


def plot_metric_over_time(
    plot_dir: Path,
    runs: list[dict],
    benchmark: str,
    metric_key: str,
    metric_label: str,
) -> Path | None:
    providers_data: dict[str, list[tuple[datetime, float]]] = {}

    for run in runs:
        ts = parse_run_time(run)
        for pname, pdata in run["providers"].items():
            if not pdata.get("comparable", True):
                continue
            if benchmark not in pdata["benchmarks"]:
                continue
            metrics = pdata["benchmarks"][benchmark].get("metrics", {})
            if metric_key not in metrics:
                continue
            val = metrics[metric_key]
            if val == 0 and metric_key == "tpot_median_ms":
                continue
            providers_data.setdefault(pname, []).append((ts, val))

    if not providers_data:
        return None

    bench_dir = plot_dir / benchmark
    bench_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))

    for pname, points in sorted(providers_data.items()):
        times, values = zip(*points)
        color = PROVIDER_COLORS.get(pname)
        marker = PROVIDER_MARKERS.get(pname, "o")
        ax.plot(
            times, values,
            label=pname, color=color, marker=marker,
            linewidth=2, markersize=7,
        )

    ax.set_title(f"{benchmark} — {metric_label}", fontsize=14)
    ax.set_ylabel(metric_label, fontsize=12)
    ax.set_xlabel("Run", fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d %H:%M"))
    fig.autofmt_xdate(rotation=30)
    fig.tight_layout()

    path = bench_dir / f"{metric_key}.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_build_times_over_time(plot_dir: Path, runs: list[dict]) -> Path | None:
    providers_data: dict[str, list[tuple[datetime, float]]] = {}

    for run in runs:
        ts = parse_run_time(run)
        for pname, pdata in run["providers"].items():
            bt = pdata.get("build_time_s", 0)
            if bt > 0:
                providers_data.setdefault(pname, []).append((ts, bt))

    if not providers_data:
        return None

    summary_dir = plot_dir / "summary"
    summary_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))

    for pname, points in sorted(providers_data.items()):
        times, values = zip(*points)
        color = PROVIDER_COLORS.get(pname)
        marker = PROVIDER_MARKERS.get(pname, "o")
        ax.plot(
            times, values,
            label=pname, color=color, marker=marker,
            linewidth=2, markersize=7,
        )

    ax.set_title("Build Time Over Runs", fontsize=14)
    ax.set_ylabel("Build Time (seconds)", fontsize=12)
    ax.set_xlabel("Run", fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d %H:%M"))
    fig.autofmt_xdate(rotation=30)
    fig.tight_layout()

    path = summary_dir / "build_times.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_cross_benchmark_averages(
    plot_dir: Path,
    runs: list[dict],
) -> int:
    """Plot cross-benchmark average for each metric over time."""
    avg_dir = plot_dir / "cross_benchmark_averages"
    avg_dir.mkdir(parents=True, exist_ok=True)
    generated = 0

    for metric_key, metric_label in TRACKED_METRICS:
        providers_data: dict[str, list[tuple[datetime, float]]] = {}

        for run in runs:
            ts = parse_run_time(run)
            for pname, pdata in run["providers"].items():
                if not pdata.get("comparable", True):
                    continue
                vals = []
                for bdata in pdata["benchmarks"].values():
                    metrics = bdata.get("metrics", {})
                    if metric_key in metrics:
                        val = metrics[metric_key]
                        if val == 0 and metric_key == "tpot_median_ms":
                            continue
                        vals.append(val)
                if vals:
                    avg = sum(vals) / len(vals)
                    providers_data.setdefault(pname, []).append((ts, avg))

        if not providers_data:
            continue

        fig, ax = plt.subplots(figsize=(9, 5))

        for pname, points in sorted(providers_data.items()):
            times, values = zip(*points)
            color = PROVIDER_COLORS.get(pname)
            marker = PROVIDER_MARKERS.get(pname, "o")
            ax.plot(
                times, values,
                label=pname, color=color, marker=marker,
                linewidth=2, markersize=7,
            )

        ax.set_title(f"Cross-Benchmark Avg — {metric_label}", fontsize=14)
        ax.set_ylabel(metric_label, fontsize=12)
        ax.set_xlabel("Run", fontsize=12)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)

        ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d %H:%M"))
        fig.autofmt_xdate(rotation=30)
        fig.tight_layout()

        path = avg_dir / f"{metric_key}.png"
        fig.savefig(path, dpi=150)
        plt.close(fig)
        generated += 1

    return generated


def main(model_dir: str) -> None:
    model_path = Path(model_dir)
    runs = load_all_runs(model_path)
    if len(runs) < 2:
        print(f"Need at least 2 runs for progress charts (found {len(runs)})")
        return

    plot_dir = model_path / "plots"

    benchmarks: list[str] = []
    for run in runs:
        for pdata in run["providers"].values():
            for bname in pdata["benchmarks"]:
                if bname not in benchmarks:
                    benchmarks.append(bname)

    generated = 0
    for benchmark in benchmarks:
        for metric_key, metric_label in TRACKED_METRICS:
            result = plot_metric_over_time(
                plot_dir, runs, benchmark, metric_key, metric_label,
            )
            if result:
                generated += 1

    plot_build_times_over_time(plot_dir, runs)
    generated += plot_cross_benchmark_averages(plot_dir, runs)

    print(f"Generated {generated} progress charts from {len(runs)} runs")
    print(f"Progress plots saved to {plot_dir}/")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <model_dir>")
        sys.exit(1)
    main(sys.argv[1])
