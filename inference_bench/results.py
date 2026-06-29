from __future__ import annotations

import csv
import io
import json
import shutil
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from tabulate import tabulate

from .benchmarks.base import BenchmarkResult


SUMMARY_SCORABLE_METRICS = (
    "ttft_median_ms",
    "tpot_median_ms",
    "e2e_median_ms",
    "throughput_median_tps",
)


def _utc_now_isoformat() -> str:
    return datetime.now(timezone.utc).isoformat()


def _utc_timestamp(timestamp: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(timestamp)
    except ValueError:
        return datetime.now(timezone.utc)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _request_idx(completion_idx: int, metadata: dict[str, int | float | str | bool]) -> int:
    raw = metadata.get("request_idx")
    if isinstance(raw, bool):
        return completion_idx
    if isinstance(raw, int):
        return raw
    if isinstance(raw, float) and raw.is_integer():
        return int(raw)
    return completion_idx


def _metadata_fields(
    metadata: dict[str, int | float | str | bool],
) -> dict[str, int | float | str | bool]:
    return {f"metadata_{key}": value for key, value in metadata.items()}


@dataclass
class ProviderResults:
    provider: str
    build_time_s: float = 0.0
    commit_hash: str = ""
    benchmarks: dict[str, BenchmarkResult] = field(default_factory=dict)
    errors: dict[str, str] = field(default_factory=dict)
    server_log_path: str = ""


@dataclass
class RunResults:
    model: str
    tensor_parallel_size: int
    hardware: str = ""
    timestamp: str = field(default_factory=_utc_now_isoformat)
    providers: dict[str, ProviderResults] = field(default_factory=dict)

    def save(self, results_dir: str | Path) -> Path:
        run_dir = self._run_dir(results_dir)
        path = run_dir / "results.json"

        data = {
            "model": self.model,
            "tensor_parallel_size": self.tensor_parallel_size,
            "hardware": self.hardware,
            "timestamp": self.timestamp,
            "providers": {},
        }
        for pname, pr in self.providers.items():
            prov_data: dict = {
                "build_time_s": pr.build_time_s,
                "commit_hash": pr.commit_hash,
                "benchmarks": {
                    bname: {
                        "metrics": br.metrics,
                        "raw_requests": [
                            {
                                "request_idx": _request_idx(i, rm.metadata),
                                "completion_idx": i,
                                "ttft_ms": rm.ttft_ms,
                                "tpot_ms": rm.tpot_ms,
                                "e2e_latency_ms": rm.e2e_latency_ms,
                                "output_tokens": rm.output_tokens,
                                "throughput_tps": rm.throughput_tps,
                                "correct": rm.correct,
                                **({"response_text": rm.response_text} if rm.response_text is not None else {}),
                                **({"metadata": rm.metadata} if rm.metadata else {}),
                                **(_metadata_fields(rm.metadata) if rm.metadata else {}),
                            }
                            for i, rm in enumerate(br.raw_requests)
                        ],
                    }
                    for bname, br in pr.benchmarks.items()
                },
            }
            server_log = self._copy_provider_log(run_dir, pname, pr.server_log_path)
            if server_log:
                prov_data["server_log"] = server_log
            if pr.errors:
                prov_data["errors"] = pr.errors
            data["providers"][pname] = prov_data

        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        return path

    def _copy_provider_log(self, run_dir: Path, provider_name: str, source_path: str) -> str:
        if not source_path:
            return ""
        source = Path(source_path)
        if not source.exists():
            return ""
        safe_name = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in provider_name)
        rel_path = Path("provider_logs") / f"{safe_name}.log"
        dest = run_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
        return rel_path.as_posix()

    def save_csv(self, results_dir: str | Path) -> Path:
        run_dir = self._run_dir(results_dir)
        path = run_dir / "results.csv"

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

        for bname in benchmark_names:
            bench_metric_keys: list[str] = []
            for pname in provider_names:
                pr = self.providers[pname]
                if bname in pr.benchmarks:
                    for mk in pr.benchmarks[bname].metrics:
                        if mk not in bench_metric_keys:
                            bench_metric_keys.append(mk)

            w.writerow([bname])
            w.writerow(["metric"] + provider_names + ["winner"])
            for mk in bench_metric_keys:
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

        has_response_text = any(
            rm.response_text is not None
            for pr in self.providers.values()
            for br in pr.benchmarks.values()
            for rm in br.raw_requests
        )
        metadata_keys = sorted(
            {
                key
                for pr in self.providers.values()
                for br in pr.benchmarks.values()
                for rm in br.raw_requests
                for key in rm.metadata
            }
        )

        w.writerow(["Per-Request Raw Data"])
        header = [
            "provider", "benchmark", "request_idx", "completion_idx",
            "ttft_ms", "tpot_ms", "e2e_latency_ms",
            "output_tokens", "throughput_tps", "correct",
        ]
        header.extend(f"metadata_{key}" for key in metadata_keys)
        if has_response_text:
            header.append("response_text")
        w.writerow(header)
        for pname in provider_names:
            pr = self.providers[pname]
            for bname in benchmark_names:
                if bname not in pr.benchmarks:
                    continue
                for i, rm in enumerate(pr.benchmarks[bname].raw_requests):
                    row = [
                        pname, bname, _request_idx(i, rm.metadata), i,
                        f"{rm.ttft_ms:.2f}",
                        f"{rm.tpot_ms:.2f}",
                        f"{rm.e2e_latency_ms:.2f}",
                        rm.output_tokens,
                        f"{rm.throughput_tps:.2f}",
                        "" if rm.correct is None else int(rm.correct),
                    ]
                    row.extend(rm.metadata.get(key, "") for key in metadata_keys)
                    if has_response_text:
                        row.append(rm.response_text or "")
                    w.writerow(row)

        with open(path, "w", newline="") as f:
            f.write(buf.getvalue())
        return path

    def _run_dir(self, results_dir: str | Path) -> Path:
        if not hasattr(self, "_cached_run_dir"):
            ts = _utc_timestamp(self.timestamp).strftime("%Y%m%d_%H%M%S")
            model_slug = self.model.replace("/", "--")
            base = Path(results_dir) / model_slug
            if self.hardware:
                base = base / self.hardware
            self._cached_run_dir = base / "runs" / ts
        self._cached_run_dir.mkdir(parents=True, exist_ok=True)
        return self._cached_run_dir

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
            "correctness_rate",
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
        higher_is_better = {"throughput_median_tps", "total_output_tokens", "correctness_rate"}
        if metric_key in higher_is_better:
            best_value = max(values.values())
        elif metric_key == "num_requests":
            return ""
        else:
            best_value = min(values.values())
        tied = [provider for provider, value in values.items() if value == best_value]
        return tied[0] if len(tied) == 1 else ""

    def _print_summary(self, provider_names: list[str]) -> None:
        print("\n" + "=" * 80)
        print("SUMMARY — Wins by Metric")
        print("=" * 80)
        wins: dict[str, int] = {p: 0 for p in provider_names}

        for bname in set().union(*(pr.benchmarks.keys() for pr in self.providers.values())):
            for mk in SUMMARY_SCORABLE_METRICS:
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
