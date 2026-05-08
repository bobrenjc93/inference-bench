#!/usr/bin/env python3
"""Generate cross-run progress charts from all inference-bench runs.

Usage:
    python scripts/plot_progress.py

Scans results/runs/*/results.json, extracts summary metrics per provider
per run, and generates time-series line charts to results/plots/.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

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
    ("ttft_median_ms", "TTFT Median (ms)", False),
    ("tpot_median_ms", "TPOT Median (ms)", False),
    ("e2e_median_ms", "E2E Median (ms)", False),
    ("throughput_median_tps", "Throughput Median (tok/s)", True),
    ("correctness_rate", "Correctness Rate", True),
]


def load_all_runs(results_dir: Path) -> list[dict]:
    runs = []
    runs_dir = results_dir / "runs"
    if not runs_dir.exists():
        return runs
    for run_dir in sorted(runs_dir.iterdir()):
        json_path = run_dir / "results.json"
        if not json_path.exists():
            continue
        with open(json_path) as f:
            data = json.load(f)
        data["_run_dir"] = str(run_dir.name)
        runs.append(data)
    return runs


def parse_run_time(run: dict) -> datetime:
    dirname = run["_run_dir"]
    return datetime.strptime(dirname, "%Y%m%d_%H%M%S")


def plot_metric_over_time(
    runs: list[dict],
    benchmark: str,
    metric_key: str,
    metric_label: str,
    higher_is_better: bool,
    plot_dir: Path,
) -> Path | None:
    providers_data: dict[str, list[tuple[datetime, float]]] = {}

    for run in runs:
        ts = parse_run_time(run)
        for pname, pdata in run["providers"].items():
            if benchmark not in pdata["benchmarks"]:
                continue
            metrics = pdata["benchmarks"][benchmark].get("metrics", {})
            if metric_key not in metrics:
                continue
            val = metrics[metric_key]
            if val == 0 and metric_key in ("tpot_median_ms",):
                continue
            providers_data.setdefault(pname, []).append((ts, val))

    if not providers_data:
        return None

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

    path = plot_dir / f"{benchmark}_{metric_key}.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_build_times_over_time(runs: list[dict], plot_dir: Path) -> Path | None:
    providers_data: dict[str, list[tuple[datetime, float]]] = {}

    for run in runs:
        ts = parse_run_time(run)
        for pname, pdata in run["providers"].items():
            bt = pdata.get("build_time_s", 0)
            if bt > 0:
                providers_data.setdefault(pname, []).append((ts, bt))

    if not providers_data:
        return None

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

    path = plot_dir / "build_times.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def main(results_dir: str = "results") -> None:
    results_path = Path(results_dir)
    runs = load_all_runs(results_path)
    if len(runs) < 2:
        print(f"Need at least 2 runs for progress charts (found {len(runs)})")
        return

    plot_dir = results_path / "plots"
    plot_dir.mkdir(parents=True, exist_ok=True)

    benchmarks: list[str] = []
    for run in runs:
        for pdata in run["providers"].values():
            for bname in pdata["benchmarks"]:
                if bname not in benchmarks:
                    benchmarks.append(bname)

    generated = 0
    for benchmark in benchmarks:
        for metric_key, metric_label, higher_better in TRACKED_METRICS:
            result = plot_metric_over_time(
                runs, benchmark, metric_key, metric_label,
                higher_better, plot_dir,
            )
            if result:
                generated += 1

    plot_build_times_over_time(runs, plot_dir)

    print(f"Generated {generated} progress charts from {len(runs)} runs")
    print(f"Progress plots saved to {plot_dir}/")


if __name__ == "__main__":
    results_dir = sys.argv[1] if len(sys.argv) > 1 else "results"
    main(results_dir)
