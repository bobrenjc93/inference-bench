"""Generate a single markdown summary file from a benchmark results.json."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path


BENCHMARK_INFO = {
    "few_shot": {
        "description": "5-shot math × 1k requests (64 concurrent) — tests prefill speed under load",
        "source": "inference_bench/benchmarks/few_shot.py",
    },
    "self_consistency": {
        "description": "1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching",
        "source": "inference_bench/benchmarks/self_consistency.py",
    },
    "multi_turn": {
        "description": "125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load",
        "source": "inference_bench/benchmarks/multi_turn.py",
    },
    "tree_of_thought": {
        "description": "32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load",
        "source": "inference_bench/benchmarks/tree_of_thought.py",
    },
    "long_output": {
        "description": "1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load",
        "source": "inference_bench/benchmarks/long_output.py",
    },
}


SCORABLE_METRICS = [
    "ttft_median_ms",
    "tpot_median_ms",
    "e2e_median_ms",
    "throughput_median_tps",
]

DISPLAY_METRICS = SCORABLE_METRICS + ["correctness_rate"]

HIGHER_IS_BETTER = {"throughput_median_tps"}

METRIC_LABELS = {
    "ttft_median_ms": "TTFT median (ms)",
    "tpot_median_ms": "TPOT median (ms)",
    "e2e_median_ms": "E2E median (ms)",
    "throughput_median_tps": "Throughput median (tok/s)",
    "correctness_rate": "Correctness",
}

METRIC_FMT = {
    "ttft_median_ms": lambda v: f"{v:.1f}",
    "tpot_median_ms": lambda v: f"{v:.1f}",
    "e2e_median_ms": lambda v: f"{v:.1f}",
    "throughput_median_tps": lambda v: f"{v:.1f}",
    "correctness_rate": lambda v: f"{v:.0%}",
}


def _pick_winner(metric: str, values: dict[str, float]) -> str | None:
    if len(values) < 2:
        return None
    if metric in HIGHER_IS_BETTER:
        return max(values, key=lambda k: values[k])
    return min(values, key=lambda k: values[k])


def _fmt(metric: str, value: float) -> str:
    return METRIC_FMT.get(metric, lambda v: f"{v:.2f}")(value)


def _md_table(headers: list[str], rows: list[list[str]]) -> str:
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    def fmt_row(cells: list[str]) -> str:
        parts = []
        for i, cell in enumerate(cells):
            if i == 0:
                parts.append(cell.ljust(col_widths[i]))
            else:
                parts.append(cell.rjust(col_widths[i]))
        return "| " + " | ".join(parts) + " |"

    lines = [fmt_row(headers)]
    seps = []
    for i, w in enumerate(col_widths):
        if i == 0:
            seps.append(":" + "-" * (w - 1))
        else:
            seps.append("-" * (w - 1) + ":")
    lines.append("| " + " | ".join(seps) + " |")
    for row in rows:
        lines.append(fmt_row(row))
    return "\n".join(lines)


def _bold(text: str) -> str:
    return f"**{text}**"


def _find_repo_root(start: Path) -> Path | None:
    p = start.resolve()
    while p != p.parent:
        if (p / "inference_bench").is_dir():
            return p
        p = p.parent
    return None


def generate(results_json: str | Path) -> str:
    results_json = Path(results_json)
    with open(results_json) as f:
        data = json.load(f)

    repo_root = _find_repo_root(results_json)
    summary_dir = results_json.resolve().parent

    model = data["model"]
    tp = data["tensor_parallel_size"]
    hardware = data.get("hardware", "")
    timestamp = data.get("timestamp", "")
    providers_data = data["providers"]
    provider_names = list(providers_data.keys())

    benchmark_names: list[str] = []
    for pd in providers_data.values():
        for bn in pd.get("benchmarks", {}):
            if bn not in benchmark_names:
                benchmark_names.append(bn)

    lines: list[str] = []
    lines.append(f"# Benchmark Summary")
    lines.append("")
    lines.append(f"- **Model:** {model}")
    lines.append(f"- **TP:** {tp}")
    if hardware:
        lines.append(f"- **Hardware:** {hardware}")
    if timestamp:
        try:
            dt = datetime.fromisoformat(timestamp)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            pt = dt.astimezone(timezone(timedelta(hours=-7)))
            friendly = pt.strftime("%-I:%M %p PT, %b %-d %Y")
            lines.append(f"- **Timestamp:** {friendly}")
        except (ValueError, TypeError):
            lines.append(f"- **Timestamp:** {timestamp}")
    lines.append("")

    # -- Scorecard: one row per benchmark, one column per provider, cell = wins --
    lines.append("## Scorecard")
    lines.append("")

    wins_by_bench: dict[str, dict[str, int]] = {}
    for bn in benchmark_names:
        wins_by_bench[bn] = {p: 0 for p in provider_names}
        for mk in SCORABLE_METRICS:
            values = {}
            for pn in provider_names:
                metrics = providers_data[pn].get("benchmarks", {}).get(bn, {}).get("metrics", {})
                if mk in metrics:
                    values[pn] = metrics[mk]
            winner = _pick_winner(mk, values)
            if winner:
                wins_by_bench[bn][winner] += 1

    total_wins = {p: 0 for p in provider_names}
    rows = []
    for bn in benchmark_names:
        row = [bn]
        best_count = max(wins_by_bench[bn].values())
        for pn in provider_names:
            w = wins_by_bench[bn][pn]
            total_wins[pn] += w
            cell = f"{w}/{len(SCORABLE_METRICS)}"
            if w == best_count and w > 0:
                cell = _bold(cell)
            row.append(cell)
        rows.append(row)

    best_total = max(total_wins.values())
    total_row = ["**Total**"]
    for pn in provider_names:
        t = total_wins[pn]
        cell = f"{t}/{len(SCORABLE_METRICS) * len(benchmark_names)}"
        if t == best_total:
            cell = _bold(cell)
        total_row.append(cell)
    rows.append(total_row)

    lines.append(_md_table(["Benchmark"] + provider_names, rows))
    lines.append("")
    lines.append(f"Each cell = metric wins out of {len(SCORABLE_METRICS)} "
                 f"(TTFT, TPOT, E2E, throughput). "
                 f"**Bold** = best in row.")
    lines.append("")

    # -- Build times --
    lines.append("## Build Times")
    lines.append("")
    build_rows = []
    build_vals = {}
    has_commits = False
    for pn in provider_names:
        secs = providers_data[pn].get("build_time_s", 0)
        build_vals[pn] = secs
        if providers_data[pn].get("commit_hash"):
            has_commits = True
    fastest = min(build_vals, key=lambda k: build_vals[k]) if build_vals else None
    for pn in provider_names:
        secs = build_vals[pn]
        cell = f"{secs:.1f}s ({secs / 60:.1f}m)"
        if pn == fastest:
            cell = _bold(cell)
        row = [pn, cell]
        if has_commits:
            commit = providers_data[pn].get("commit_hash", "")
            row.append(f"`{commit[:7]}`" if commit else "-")
        build_rows.append(row)
    headers = ["Provider", "Time"]
    if has_commits:
        headers.append("Commit")
    lines.append(_md_table(headers, build_rows))
    lines.append("")

    # -- Per-benchmark detail tables --
    lines.append("## Per-Benchmark Results")
    lines.append("")

    for bn in benchmark_names:
        lines.append(f"### {bn}")
        info = BENCHMARK_INFO.get(bn)
        if info:
            desc = info["description"]
            if repo_root:
                rel = os.path.relpath(repo_root / info["source"], summary_dir)
                lines.append(f"> {desc} ([source]({rel}))")
            else:
                lines.append(f"> {desc}")
        lines.append("")
        rows = []
        for mk in DISPLAY_METRICS:
            values: dict[str, float] = {}
            for pn in provider_names:
                metrics = providers_data[pn].get("benchmarks", {}).get(bn, {}).get("metrics", {})
                if mk in metrics:
                    values[pn] = metrics[mk]

            if not values:
                continue

            winner = _pick_winner(mk, values) if mk in SCORABLE_METRICS else None
            row = [METRIC_LABELS.get(mk, mk)]
            for pn in provider_names:
                if pn in values:
                    cell = _fmt(mk, values[pn])
                    if pn == winner:
                        cell = _bold(cell)
                    row.append(cell)
                else:
                    row.append("-")
            rows.append(row)
        lines.append(_md_table(["Metric"] + provider_names, rows))
        lines.append("")

    # -- Cross-benchmark averages --
    lines.append("## Cross-Benchmark Averages")
    lines.append("")

    avg_rows = []
    for mk in DISPLAY_METRICS:
        row = [METRIC_LABELS.get(mk, mk)]
        averages: dict[str, float] = {}
        for pn in provider_names:
            vals = []
            for bn in benchmark_names:
                metrics = providers_data[pn].get("benchmarks", {}).get(bn, {}).get("metrics", {})
                if mk in metrics:
                    vals.append(metrics[mk])
            if vals:
                averages[pn] = sum(vals) / len(vals)
        winner = _pick_winner(mk, averages) if mk in SCORABLE_METRICS and len(averages) >= 2 else None
        for pn in provider_names:
            if pn in averages:
                cell = _fmt(mk, averages[pn])
                if pn == winner:
                    cell = _bold(cell)
                row.append(cell)
            else:
                row.append("-")
        avg_rows.append(row)
    lines.append(_md_table(["Metric"] + provider_names, avg_rows))
    lines.append("")

    return "\n".join(lines)


def main(results_json: str) -> str:
    results_path = Path(results_json)
    run_dir = results_path.parent
    md = generate(results_path)
    out_path = run_dir / "summary.md"
    out_path.write_text(md)
    print(f"Summary saved to {out_path}")
    return str(out_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <results.json>")
        sys.exit(1)
    main(sys.argv[1])
