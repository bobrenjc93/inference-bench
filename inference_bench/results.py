from __future__ import annotations

import csv
import io
import json
import math
import re
import shutil
import statistics
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from tabulate import tabulate

from .benchmarks.base import BenchmarkResult
from .integrity import warnings_for_live_provider


SUMMARY_SCORABLE_METRICS = (
    "ttft_median_ms",
    "tpot_median_ms",
    "e2e_median_ms",
    "throughput_median_tps",
)

_SAFE_RESULT_COMPONENT = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")


def _safe_result_component(value: str, *, field_name: str) -> str:
    component = str(value)
    if (
        component in {"", ".", ".."}
        or not _SAFE_RESULT_COMPONENT.fullmatch(component)
    ):
        raise ValueError(f"Unsafe {field_name} result path component: {value!r}")
    return component


def model_result_slug(model: str) -> str:
    parts = str(model).split("/")
    if not parts:
        raise ValueError("Model identifier is empty")
    if any("--" in part for part in parts):
        raise ValueError("Model result path components must not contain '--'")
    return "--".join(
        _safe_result_component(part, field_name="model") for part in parts
    )


def _reject_symlink_components(path: Path) -> None:
    current = Path(path.anchor) if path.is_absolute() else Path.cwd()
    parts = path.parts[1:] if path.is_absolute() else path.parts
    for part in parts:
        if part in {"", "."}:
            continue
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Result path must not contain symlinks: {current}")


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


def _format_console_metric(metric_key: str, value: int | float | str | bool) -> str:
    if not isinstance(value, float):
        return str(value)
    if metric_key == "correctness_rate":
        return f"{value:.3f}"
    return f"{value:.1f}"


def _numeric_metric(value: object) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    numeric = float(value)
    return numeric if math.isfinite(numeric) else None


def _integer_metric(value: object) -> int | None:
    numeric = _numeric_metric(value)
    if numeric is None or not numeric.is_integer() or numeric < 0:
        return None
    return int(numeric)


@dataclass
class ProviderResults:
    provider: str
    build_time_s: float = 0.0
    commit_hash: str = ""
    benchmarks: dict[str, BenchmarkResult] = field(default_factory=dict)
    errors: dict[str, str] = field(default_factory=dict)
    server_log_path: str = ""
    extra_log_paths: dict[str, str] = field(default_factory=dict)
    deployment_observation: dict[str, object] = field(default_factory=dict)
    comparable: bool = True
    integrity_warnings: list[str] = field(default_factory=list)


@dataclass
class RunResults:
    model: str
    tensor_parallel_size: int
    evaluation_version: int = 2
    model_revision: str | None = None
    deployment_mode: str = "standard"
    prefill_tensor_parallel_size: int | None = None
    decode_tensor_parallel_size: int | None = None
    gpu_count: int | None = None
    hardware: str = ""
    timestamp: str = field(default_factory=_utc_now_isoformat)
    requested_providers: tuple[str, ...] = ()
    requested_benchmarks: tuple[str, ...] = ()
    minimum_correctness_rate: float | None = None
    require_request_count_parity: bool = False
    output_token_ratio_tolerance: float | None = None
    retain_response_text: bool = False
    output_token_count_method: str = "sse_content_chunks"
    harness_provenance: dict[str, object] = field(default_factory=dict)
    finalized: bool = False
    providers: dict[str, ProviderResults] = field(default_factory=dict)

    def save(self, results_dir: str | Path) -> Path:
        self._refresh_integrity_status()
        run_dir = self._run_dir(results_dir)
        path = run_dir / "results.json"

        data = {
            "evaluation_version": self.evaluation_version,
            "finalized": self.finalized,
            "model": self.model,
            "model_revision": self.model_revision,
            "tensor_parallel_size": self.tensor_parallel_size,
            "deployment_mode": self.deployment_mode,
            "gpu_count": self.gpu_count or self.tensor_parallel_size,
            "hardware": self.hardware,
            "timestamp": self.timestamp,
            "requested_providers": list(self.requested_providers),
            "requested_benchmarks": list(self.requested_benchmarks),
            "metric_schema_version": (
                2 if self.output_token_count_method == "client_tokenizer" else 1
            ),
            "output_token_count_method": self.output_token_count_method,
            "harness_provenance": self.harness_provenance,
            "providers": {},
        }
        if self.minimum_correctness_rate is not None:
            data["minimum_correctness_rate"] = self.minimum_correctness_rate
        if self.require_request_count_parity:
            data["require_request_count_parity"] = True
        if self.output_token_ratio_tolerance is not None:
            data["output_token_ratio_tolerance"] = self.output_token_ratio_tolerance
        if self.retain_response_text:
            data["retain_response_text"] = True
        if self.prefill_tensor_parallel_size is not None:
            data["prefill_tensor_parallel_size"] = self.prefill_tensor_parallel_size
        if self.decode_tensor_parallel_size is not None:
            data["decode_tensor_parallel_size"] = self.decode_tensor_parallel_size
        for pname, pr in self.providers.items():
            prov_data: dict = {
                "build_time_s": pr.build_time_s,
                "commit_hash": pr.commit_hash,
                "comparable": pr.comparable,
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
                                "stream_content_chunks": rm.stream_content_chunks,
                                "throughput_tps": rm.throughput_tps,
                                "correct": rm.correct,
                                **(
                                    {"response_text": rm.response_text}
                                    if rm.response_text is not None
                                    else {}
                                ),
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
            extra_logs = {
                name: copied
                for name, source_path in pr.extra_log_paths.items()
                if (
                    copied := self._copy_provider_log(
                        run_dir,
                        f"{pname}_{name}",
                        source_path,
                    )
                )
            }
            if extra_logs:
                prov_data["extra_logs"] = extra_logs
            if pr.deployment_observation:
                prov_data["deployment_observation"] = pr.deployment_observation
            if pr.integrity_warnings:
                prov_data["integrity_warnings"] = pr.integrity_warnings
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
        rel_path = Path("provider_logs") / f"{safe_name}{source.suffix or '.log'}"
        dest = run_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, dest)
        return rel_path.as_posix()

    def save_csv(self, results_dir: str | Path) -> Path:
        self._refresh_integrity_status()
        run_dir = self._run_dir(results_dir)
        path = run_dir / "results.csv"

        provider_names = list(self.providers.keys())
        if not provider_names:
            return path

        buf = io.StringIO()
        w = csv.writer(buf)

        w.writerow(["evaluation_version", self.evaluation_version])
        w.writerow(["finalized", str(self.finalized).lower()])
        w.writerow(["model", self.model])
        if self.model_revision:
            w.writerow(["model_revision", self.model_revision])
        w.writerow(["tensor_parallel_size", self.tensor_parallel_size])
        w.writerow(["deployment_mode", self.deployment_mode])
        w.writerow(["gpu_count", self.gpu_count or self.tensor_parallel_size])
        w.writerow(
            [
                "metric_schema_version",
                2 if self.output_token_count_method == "client_tokenizer" else 1,
            ]
        )
        w.writerow(["output_token_count_method", self.output_token_count_method])
        if self.prefill_tensor_parallel_size is not None:
            w.writerow(
                ["prefill_tensor_parallel_size", self.prefill_tensor_parallel_size]
            )
        if self.decode_tensor_parallel_size is not None:
            w.writerow(
                ["decode_tensor_parallel_size", self.decode_tensor_parallel_size]
            )
        w.writerow(["timestamp", self.timestamp])
        w.writerow([])

        w.writerow(["Build Times"])
        w.writerow(["provider", "build_time_s"])
        for pname in provider_names:
            w.writerow([pname, f"{self.providers[pname].build_time_s:.1f}"])
        w.writerow([])

        w.writerow(["Provider Comparability"])
        w.writerow(["provider", "comparable"])
        for pname in provider_names:
            w.writerow([pname, str(self.providers[pname].comparable).lower()])
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
                        if pr.comparable:
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
            "provider", "comparable", "benchmark", "request_idx", "completion_idx",
            "ttft_ms", "tpot_ms", "e2e_latency_ms",
            "output_tokens", "stream_content_chunks", "throughput_tps", "correct",
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
                        pname, str(pr.comparable).lower(), bname, _request_idx(i, rm.metadata), i,
                        f"{rm.ttft_ms:.2f}",
                        f"{rm.tpot_ms:.2f}",
                        f"{rm.e2e_latency_ms:.2f}",
                        rm.output_tokens,
                        rm.stream_content_chunks,
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
            model_slug = model_result_slug(self.model)
            results_root = Path(results_dir)
            _reject_symlink_components(results_root)
            base = results_root / model_slug
            if self.hardware:
                base = base / _safe_result_component(
                    self.hardware,
                    field_name="hardware",
                )
            run_dir = base / "runs" / ts
            root_resolved = results_root.resolve(strict=False)
            try:
                run_dir.resolve(strict=False).relative_to(root_resolved)
            except ValueError as exc:
                raise ValueError("Result run directory escapes its version root") from exc
            _reject_symlink_components(run_dir.parent)
            self._cached_run_dir = run_dir
        self._cached_run_dir.mkdir(parents=True, exist_ok=True)
        _reject_symlink_components(self._cached_run_dir)
        return self._cached_run_dir

    def run_dir(self, results_dir: str | Path) -> Path:
        return self._run_dir(results_dir)

    def print_comparison(self) -> None:
        self._refresh_integrity_status()
        provider_names = list(self.providers.keys())
        if not provider_names:
            print("No results to compare.")
            return

        print("\n" + "=" * 80)
        print("INFERENCE ENGINE COMPARISON")
        allocation = f"TP: {self.tensor_parallel_size}"
        if self.prefill_tensor_parallel_size is not None:
            allocation = (
                f"Prefill TP: {self.prefill_tensor_parallel_size}  |  "
                f"Decode TP: {self.decode_tensor_parallel_size}"
            )
        print(
            f"Evaluation: v{self.evaluation_version}  |  Model: {self.model}  |  "
            f"{allocation}  |  "
            f"Deployment: {self.deployment_mode}"
        )
        print("=" * 80)

        self._print_integrity_warnings(provider_names)
        self._print_build_times(provider_names)
        comparable_provider_names = [
            name for name in provider_names if self.providers[name].comparable
        ]

        benchmark_names = set()
        for pr in self.providers.values():
            benchmark_names.update(pr.benchmarks.keys())

        for bname in sorted(benchmark_names):
            self._print_benchmark_comparison(
                bname,
                provider_names,
                comparable_provider_names,
            )

        self._print_summary(provider_names, comparable_provider_names)

    def _refresh_integrity_status(self) -> None:
        for pname, provider in self.providers.items():
            warnings = warnings_for_live_provider(pname, provider.extra_log_paths)
            self._add_integrity_warnings(provider, warnings)
        self._apply_result_eligibility_policy()

    @staticmethod
    def _add_integrity_warnings(
        provider: ProviderResults,
        warnings: list[str],
    ) -> None:
        for warning in warnings:
            if warning not in provider.integrity_warnings:
                provider.integrity_warnings.append(warning)
        if warnings:
            provider.comparable = False

    def _apply_result_eligibility_policy(self) -> None:
        enabled = (
            self.minimum_correctness_rate is not None
            or self.require_request_count_parity
            or self.output_token_ratio_tolerance is not None
        )
        if not enabled:
            return
        benchmark_names = list(self.requested_benchmarks)
        if not benchmark_names:
            benchmark_names = sorted(
                {name for provider in self.providers.values() for name in provider.benchmarks}
            )

        request_references: dict[str, int] = {}
        output_references: dict[str, float] = {}
        for benchmark_name in benchmark_names:
            counts = [
                _integer_metric(result.metrics.get("num_requests"))
                for provider in self.providers.values()
                if (result := provider.benchmarks.get(benchmark_name)) is not None
            ]
            valid_counts = [count for count in counts if count is not None]
            if valid_counts:
                request_references[benchmark_name] = max(valid_counts)
            outputs = [
                _numeric_metric(result.metrics.get("total_output_tokens"))
                for provider in self.providers.values()
                if (result := provider.benchmarks.get(benchmark_name)) is not None
            ]
            valid_outputs = [
                value for value in outputs if value is not None and value >= 0
            ]
            if valid_outputs:
                output_references[benchmark_name] = statistics.median(valid_outputs)

        for provider in self.providers.values():
            warnings: list[str] = []
            if provider.errors:
                warnings.append(
                    "Provider reported benchmark or deployment errors under the "
                    "result eligibility policy."
                )
            for benchmark_name in benchmark_names:
                result = provider.benchmarks.get(benchmark_name)
                if result is None:
                    warnings.append(
                        f"Benchmark {benchmark_name!r} has no completed result."
                    )
                    continue
                metrics = result.metrics
                if self.minimum_correctness_rate is not None:
                    rate = _numeric_metric(metrics.get("correctness_rate"))
                    if (
                        rate is None
                        or not 0.0 <= rate <= 1.0
                        or rate < self.minimum_correctness_rate
                    ):
                        rendered = "missing" if rate is None else f"{rate:.3f}"
                        warnings.append(
                            f"Benchmark {benchmark_name!r} correctness {rendered} is "
                            f"below the required {self.minimum_correctness_rate:.3f}."
                        )
                if self.require_request_count_parity:
                    count = _integer_metric(metrics.get("num_requests"))
                    expected = request_references.get(benchmark_name)
                    if count is None or expected is None or count != expected:
                        warnings.append(
                            f"Benchmark {benchmark_name!r} completed request count "
                            f"{count!r} does not match the run reference {expected!r}."
                        )
                    if count != len(result.raw_requests):
                        warnings.append(
                            f"Benchmark {benchmark_name!r} request metric does not "
                            "match its raw request records."
                        )
                if self.output_token_ratio_tolerance is not None:
                    output_tokens = _numeric_metric(metrics.get("total_output_tokens"))
                    reference = output_references.get(benchmark_name)
                    tolerance = self.output_token_ratio_tolerance
                    if (
                        output_tokens is None
                        or output_tokens < 0
                        or reference is None
                        or output_tokens < reference * (1.0 - tolerance)
                        or output_tokens > reference * (1.0 + tolerance)
                    ):
                        warnings.append(
                            f"Benchmark {benchmark_name!r} output token count "
                            f"{output_tokens!r} is outside the allowed +/-{tolerance:.0%} "
                            f"band around the run median {reference!r}."
                        )
                    raw_total = sum(request.output_tokens for request in result.raw_requests)
                    if output_tokens != raw_total:
                        warnings.append(
                            f"Benchmark {benchmark_name!r} output token metric does not "
                            "match its raw request records."
                        )
            self._add_integrity_warnings(provider, warnings)

    def _print_build_times(self, provider_names: list[str]) -> None:
        print("\n--- Build Times ---")
        rows = []
        for pname in provider_names:
            pr = self.providers[pname]
            mins = pr.build_time_s / 60
            rows.append([pname, f"{pr.build_time_s:.1f}s", f"{mins:.1f}m"])
        print(tabulate(rows, headers=["Provider", "Build Time", "Minutes"], tablefmt="simple"))

    def _print_integrity_warnings(self, provider_names: list[str]) -> None:
        warnings: list[str] = []
        for pname in provider_names:
            pr = self.providers[pname]
            warnings.extend(f"{pname}: {warning}" for warning in pr.integrity_warnings)
        if not warnings:
            return
        print("\n--- Integrity Warnings ---")
        for warning in warnings:
            print(f"! {warning}")

    def _print_benchmark_comparison(
        self,
        bname: str,
        provider_names: list[str],
        comparable_provider_names: list[str],
    ) -> None:
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
                    if pname in comparable_provider_names:
                        values[pname] = val
                    row.append(_format_console_metric(mk, val))
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
                    row.append(_format_console_metric(mk, val))
                else:
                    row.append("-")
            row.append("")
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="simple", disable_numparse=True))

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

    def _print_summary(
        self,
        provider_names: list[str],
        comparable_provider_names: list[str],
    ) -> None:
        print("\n" + "=" * 80)
        print("SUMMARY — Wins by Metric")
        print("=" * 80)
        wins: dict[str, int] = {p: 0 for p in comparable_provider_names}

        for bname in set().union(*(pr.benchmarks.keys() for pr in self.providers.values())):
            for mk in SUMMARY_SCORABLE_METRICS:
                values = {}
                for pname in comparable_provider_names:
                    pr = self.providers[pname]
                    if bname in pr.benchmarks and mk in pr.benchmarks[bname].metrics:
                        values[pname] = pr.benchmarks[bname].metrics[mk]
                if len(values) >= 2:
                    winner = self._pick_winner(mk, values)
                    if winner:
                        wins[winner] += 1

        rows = [
            [p, wins[p] if p in wins else "N/C"]
            for p in sorted(provider_names, key=lambda name: -wins.get(name, -1))
        ]
        print(tabulate(rows, headers=["Provider", "Metric Wins"], tablefmt="simple"))
        print()
