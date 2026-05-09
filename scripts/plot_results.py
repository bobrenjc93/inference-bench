#!/usr/bin/env python3
"""Generate per-request line charts from an inference-bench results JSON.

Usage:
    python scripts/plot_results.py results/<model>/runs/<ts>/results.json

Reads the JSON, produces one PNG per (benchmark, metric) pair into
plots/<benchmark>/ subdirectories next to the JSON.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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

RAW_METRICS = [
    "ttft_ms",
    "tpot_ms",
    "e2e_latency_ms",
    "throughput_tps",
]

METRIC_LABELS = {
    "ttft_ms": "Time to First Token (ms)",
    "tpot_ms": "Time Per Output Token (ms)",
    "e2e_latency_ms": "End-to-End Latency (ms)",
    "throughput_tps": "Throughput (tokens/sec)",
}

LONG_OUTPUT_DIGITS = [25, 50, 75, 100, 125, 150, 175, 200]

SUMMARY_METRICS = [
    ("ttft_median_ms", "TTFT Median (ms)", False),
    ("tpot_median_ms", "TPOT Median (ms)", False),
    ("e2e_median_ms", "E2E Median (ms)", False),
    ("throughput_median_tps", "Throughput (tok/s)", True),
]


def x_axis_for_benchmark(benchmark: str, n_requests: int) -> tuple[list, str]:
    if benchmark == "long_output" and n_requests == len(LONG_OUTPUT_DIGITS):
        return LONG_OUTPUT_DIGITS, "Output Digits"
    if benchmark == "multi_turn" and n_requests <= 8:
        return list(range(1, n_requests + 1)), "Turn"
    return list(range(1, n_requests + 1)), "Request"


def plot_benchmark_metric(
    plot_dir: Path,
    benchmark: str,
    metric: str,
    providers: dict,
) -> Path | None:
    bench_dir = plot_dir / benchmark
    bench_dir.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    has_data = False

    for pname, pdata in providers.items():
        if benchmark not in pdata["benchmarks"]:
            continue
        raw = pdata["benchmarks"][benchmark].get("raw_requests", [])
        if not raw:
            continue
        values = [r[metric] for r in raw]
        if all(v == 0 for v in values):
            continue
        xs, xlabel = x_axis_for_benchmark(benchmark, len(values))
        color = PROVIDER_COLORS.get(pname, None)
        marker = PROVIDER_MARKERS.get(pname, "o")
        ax.plot(
            xs, values,
            label=pname, color=color, marker=marker,
            linewidth=2, markersize=6,
        )
        has_data = True

    if not has_data:
        plt.close(fig)
        return None

    ax.set_title(f"{benchmark} — {METRIC_LABELS.get(metric, metric)}", fontsize=14)
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(METRIC_LABELS.get(metric, metric), fontsize=12)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()

    path = bench_dir / f"{metric}.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def plot_summary_bars(plot_dir: Path, data: dict) -> None:
    summary_dir = plot_dir / "summary"
    summary_dir.mkdir(parents=True, exist_ok=True)

    providers = data["providers"]
    pnames = list(providers.keys())
    benchmarks = []
    for pdata in providers.values():
        for bname in pdata["benchmarks"]:
            if bname not in benchmarks:
                benchmarks.append(bname)

    for metric_key, metric_label, higher_better in SUMMARY_METRICS:
        fig, ax = plt.subplots(figsize=(max(8, len(benchmarks) * 2.5), 5))
        x_positions = range(len(benchmarks))
        bar_width = 0.8 / len(pnames)
        has_data = False

        for i, pname in enumerate(pnames):
            values = []
            for bname in benchmarks:
                bdata = providers[pname]["benchmarks"].get(bname, {})
                val = bdata.get("metrics", {}).get(metric_key, 0)
                values.append(val)
            if all(v == 0 for v in values):
                continue
            offsets = [x + i * bar_width for x in x_positions]
            color = PROVIDER_COLORS.get(pname, None)
            ax.bar(offsets, values, bar_width, label=pname, color=color)
            has_data = True

        if not has_data:
            plt.close(fig)
            continue

        ax.set_title(f"Summary — {metric_label}", fontsize=14)
        ax.set_ylabel(metric_label, fontsize=12)
        ax.set_xticks([x + bar_width * (len(pnames) - 1) / 2 for x in x_positions])
        ax.set_xticklabels(benchmarks, fontsize=11)
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3, axis="y")
        fig.tight_layout()

        fig.savefig(summary_dir / f"{metric_key}.png", dpi=150)
        plt.close(fig)


def plot_build_times(plot_dir: Path, data: dict) -> None:
    summary_dir = plot_dir / "summary"
    summary_dir.mkdir(parents=True, exist_ok=True)

    providers = data["providers"]
    pnames = list(providers.keys())
    build_times = [providers[p]["build_time_s"] for p in pnames]

    fig, ax = plt.subplots(figsize=(6, 4))
    colors = [PROVIDER_COLORS.get(p, None) for p in pnames]
    ax.bar(pnames, build_times, color=colors)
    ax.set_title("Build Time (seconds)", fontsize=14)
    ax.set_ylabel("Seconds", fontsize=12)
    for i, (p, t) in enumerate(zip(pnames, build_times)):
        ax.text(i, t + max(build_times) * 0.02, f"{t:.0f}s", ha="center", fontsize=11)
    ax.grid(True, alpha=0.3, axis="y")
    fig.tight_layout()

    fig.savefig(summary_dir / "build_times.png", dpi=150)
    plt.close(fig)


def main(json_path: str) -> None:
    path = Path(json_path)
    if not path.exists():
        print(f"Error: {path} not found")
        sys.exit(1)

    with open(path) as f:
        data = json.load(f)

    run_dir = path.parent
    plot_dir = run_dir / "plots"
    providers = data["providers"]

    benchmarks = []
    for pdata in providers.values():
        for bname in pdata["benchmarks"]:
            if bname not in benchmarks:
                benchmarks.append(bname)

    generated = 0
    for benchmark in benchmarks:
        for metric in RAW_METRICS:
            result = plot_benchmark_metric(plot_dir, benchmark, metric, providers)
            if result:
                generated += 1

    plot_summary_bars(plot_dir, data)
    plot_build_times(plot_dir, data)

    print(f"Generated {generated} per-request charts + summary charts")
    print(f"Plots saved to {plot_dir}/")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <results.json>")
        sys.exit(1)
    main(sys.argv[1])
