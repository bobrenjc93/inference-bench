from __future__ import annotations

import csv
import io
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path

from tabulate import tabulate

from .benchmarks.base import BenchmarkResult


@dataclass
class ProviderResults:
    provider: str
    build_time_s: float = 0.0
    benchmarks: dict[str, BenchmarkResult] = field(default_factory=dict)


@dataclass
class RunResults:
    model: str
    tensor_parallel_size: int
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    providers: dict[str, ProviderResults] = field(default_factory=dict)

    def save(self, results_dir: str | Path) -> Path:
        results_dir = Path(results_dir)
        results_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = results_dir / f"results_{ts}.json"

        data = {
            "model": self.model,
            "tensor_parallel_size": self.tensor_parallel_size,
            "timestamp": self.timestamp,
            "providers": {},
        }
        for pname, pr in self.providers.items():
            data["providers"][pname] = {
                "build_time_s": pr.build_time_s,
                "benchmarks": {
                    bname: {
                        "metrics": br.metrics,
                        "num_requests": len(br.raw_requests),
                    }
                    for bname, br in pr.benchmarks.items()
                },
            }

        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"\nResults saved to {path}")
        return path

    def save_csv(self, results_dir: str | Path) -> Path:
        results_dir = Path(results_dir)
        results_dir.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = results_dir / f"results_{ts}.csv"

        provider_names = list(self.providers.keys())
        if not provider_names:
            return path

        buf = io.StringIO()
        w = csv.writer(buf)

        w.writerow(["model", self.model])
        w.writerow(["tensor_parallel_size", self.tensor_parallel_size])
        w.writerow(["timestamp", self.timestamp])
        w.writerow([])

        w.writerow(["Build Times"])
        w.writerow(["provider", "build_time_s"])
        for pname in provider_names:
            w.writerow([pname, f"{self.providers[pname].build_time_s:.1f}"])
        w.writerow([])

        benchmark_names: list[str] = []
        for pr in self.providers.values():
            for bname in pr.benchmarks:
                if bname not in benchmark_names:
                    benchmark_names.append(bname)

        all_metric_keys: list[str] = []
        for pr in self.providers.values():
            for br in pr.benchmarks.values():
                for mk in br.metrics:
                    if mk not in all_metric_keys:
                        all_metric_keys.append(mk)

        for bname in benchmark_names:
            w.writerow([bname])
            w.writerow(["metric"] + provider_names + ["winner"])
            for mk in all_metric_keys:
                values: dict[str, float] = {}
                row = [mk]
                for pname in provider_names:
                    pr = self.providers[pname]
                    if bname in pr.benchmarks and mk in pr.benchmarks[bname].metrics:
                        val = pr.benchmarks[bname].metrics[mk]
                        values[pname] = val
                        row.append(f"{val:.2f}" if isinstance(val, float) else str(val))
                    else:
                        row.append("")
                winner = self._pick_winner(mk, values)
                row.append(winner)
                w.writerow(row)
            w.writerow([])

        w.writerow(["Per-Request Raw Data"])
        w.writerow([
            "provider", "benchmark", "request_idx",
            "ttft_ms", "tpot_ms", "e2e_latency_ms",
            "output_tokens", "throughput_tps",
        ])
        for pname in provider_names:
            pr = self.providers[pname]
            for bname in benchmark_names:
                if bname not in pr.benchmarks:
                    continue
                for i, rm in enumerate(pr.benchmarks[bname].raw_requests):
                    w.writerow([
                        pname, bname, i,
                        f"{rm.ttft_ms:.2f}",
                        f"{rm.tpot_ms:.2f}",
                        f"{rm.e2e_latency_ms:.2f}",
                        rm.output_tokens,
                        f"{rm.throughput_tps:.2f}",
                    ])

        with open(path, "w", newline="") as f:
            f.write(buf.getvalue())
        print(f"CSV saved to {path}")
        return path

    def print_comparison(self) -> None:
        provider_names = list(self.providers.keys())
        if not provider_names:
            print("No results to compare.")
            return

        print("\n" + "=" * 80)
        print("INFERENCE ENGINE COMPARISON")
        print(f"Model: {self.model}  |  TP: {self.tensor_parallel_size}")
        print("=" * 80)

        self._print_build_times(provider_names)

        benchmark_names = set()
        for pr in self.providers.values():
            benchmark_names.update(pr.benchmarks.keys())

        for bname in sorted(benchmark_names):
            self._print_benchmark_comparison(bname, provider_names)

        self._print_summary(provider_names)

    def _print_build_times(self, provider_names: list[str]) -> None:
        print("\n--- Build Times ---")
        rows = []
        for pname in provider_names:
            pr = self.providers[pname]
            mins = pr.build_time_s / 60
            rows.append([pname, f"{pr.build_time_s:.1f}s", f"{mins:.1f}m"])
        print(tabulate(rows, headers=["Provider", "Build Time", "Minutes"], tablefmt="simple"))

    def _print_benchmark_comparison(self, bname: str, provider_names: list[str]) -> None:
        print(f"\n--- {bname} ---")

        metric_keys = set()
        for pname in provider_names:
            pr = self.providers[pname]
            if bname in pr.benchmarks:
                metric_keys.update(pr.benchmarks[bname].metrics.keys())

        display_metrics = [
            "ttft_median_ms",
            "ttft_p99_ms",
            "tpot_median_ms",
            "e2e_median_ms",
            "e2e_p99_ms",
            "throughput_median_tps",
            "total_output_tokens",
            "num_requests",
        ]

        headers = ["Metric"] + provider_names + ["Winner"]
        rows = []
        for mk in display_metrics:
            if mk not in metric_keys:
                continue
            row = [mk]
            values = {}
            for pname in provider_names:
                pr = self.providers[pname]
                if bname in pr.benchmarks and mk in pr.benchmarks[bname].metrics:
                    val = pr.benchmarks[bname].metrics[mk]
                    values[pname] = val
                    row.append(f"{val:.1f}" if isinstance(val, float) else str(val))
                else:
                    row.append("-")

            winner = self._pick_winner(mk, values)
            row.append(winner)
            rows.append(row)

        extra_metrics = sorted(metric_keys - set(display_metrics))
        for mk in extra_metrics:
            row = [mk]
            values = {}
            for pname in provider_names:
                pr = self.providers[pname]
                if bname in pr.benchmarks and mk in pr.benchmarks[bname].metrics:
                    val = pr.benchmarks[bname].metrics[mk]
                    values[pname] = val
                    row.append(f"{val:.1f}" if isinstance(val, float) else str(val))
                else:
                    row.append("-")
            row.append("")
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="simple"))

    def _pick_winner(self, metric_key: str, values: dict[str, float]) -> str:
        if len(values) < 2:
            return ""
        higher_is_better = {"throughput_median_tps", "total_output_tokens"}
        if metric_key in higher_is_better:
            best = max(values, key=lambda k: values[k])
        elif metric_key == "num_requests":
            return ""
        else:
            best = min(values, key=lambda k: values[k])
        return best

    def _print_summary(self, provider_names: list[str]) -> None:
        print("\n" + "=" * 80)
        print("SUMMARY — Wins by Metric")
        print("=" * 80)
        wins: dict[str, int] = {p: 0 for p in provider_names}

        for pr in self.providers.values():
            for br in pr.benchmarks.values():
                pass

        scorable = [
            "ttft_median_ms", "tpot_median_ms", "e2e_median_ms",
            "throughput_median_tps",
        ]

        for bname in set().union(*(pr.benchmarks.keys() for pr in self.providers.values())):
            for mk in scorable:
                values = {}
                for pname in provider_names:
                    pr = self.providers[pname]
                    if bname in pr.benchmarks and mk in pr.benchmarks[bname].metrics:
                        values[pname] = pr.benchmarks[bname].metrics[mk]
                if len(values) >= 2:
                    winner = self._pick_winner(mk, values)
                    if winner:
                        wins[winner] += 1

        rows = [[p, w] for p, w in sorted(wins.items(), key=lambda x: -x[1])]
        print(tabulate(rows, headers=["Provider", "Metric Wins"], tablefmt="simple"))
        print()
