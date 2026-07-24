from __future__ import annotations

import gc
import json
import os
import socket
import subprocess
import time
from pathlib import Path

from .benchmarks import get_benchmark
from .config import Config
from .providers import get_provider
from .results import ProviderResults, RunResults


_HARNESS_REPO_URL = "https://github.com/bobrenjc93/inference-bench.git"


def _harness_git(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["/usr/bin/git", *args],
        cwd=root,
        env=_harness_git_env(),
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Harness git {' '.join(args)} failed: {result.stderr.strip()}"
        )
    return result.stdout.strip()


def _harness_git_env() -> dict[str, str]:
    env = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith("GIT_")
        and key
        not in {
            "ALL_PROXY",
            "CURL_CA_BUNDLE",
            "HTTPS_PROXY",
            "HTTP_PROXY",
            "NO_PROXY",
            "SSL_CERT_DIR",
            "SSL_CERT_FILE",
            "all_proxy",
            "https_proxy",
            "http_proxy",
            "no_proxy",
        }
    }
    env.update(
        {
            "GIT_ALLOW_PROTOCOL": "https",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_SYSTEM": os.devnull,
            "GIT_TERMINAL_PROMPT": "0",
        }
    )
    return env


def _capture_harness_provenance(
    *,
    verify_remote: bool,
    allowed_untracked_root: Path | None = None,
) -> dict[str, object]:
    root = Path(__file__).resolve().parents[1]
    if not (root / ".git").is_dir():
        raise RuntimeError("Scored inference-bench harness must run from a Git checkout")
    commit = _harness_git(root, "rev-parse", "HEAD")
    origin_main = _harness_git(root, "rev-parse", "origin/main")
    remote = _harness_git(root, "remote", "get-url", "origin")
    tracked_status = _harness_git(
        root,
        "status",
        "--porcelain",
        "--untracked-files=no",
    )
    untracked = [
        path
        for path in _harness_git(
            root,
            "ls-files",
            "--others",
            "--exclude-standard",
            "-z",
        ).split("\0")
        if path
    ]
    if commit != origin_main:
        raise RuntimeError("Scored inference-bench harness must be exactly origin/main")
    normalized_remote = remote.strip().removesuffix(".git").rstrip("/").lower()
    expected_remote = _HARNESS_REPO_URL.removesuffix(".git").lower()
    if normalized_remote != expected_remote:
        raise RuntimeError("Scored inference-bench harness remote is not canonical")
    if tracked_status:
        raise RuntimeError("Scored inference-bench harness must have a clean worktree")
    if allowed_untracked_root is None:
        unexpected_untracked = untracked
    else:
        allowed = allowed_untracked_root.resolve(strict=False)
        unexpected_untracked = []
        for relative in untracked:
            candidate = (root / relative).resolve(strict=False)
            try:
                candidate.relative_to(allowed)
            except ValueError:
                unexpected_untracked.append(relative)
    if unexpected_untracked:
        raise RuntimeError(
            "Scored inference-bench harness has unexpected untracked files: "
            + ", ".join(unexpected_untracked)
        )
    if verify_remote:
        remote_main = _harness_git(
            root,
            "ls-remote",
            _HARNESS_REPO_URL,
            "refs/heads/main",
        ).split()
        if len(remote_main) != 2 or remote_main[0] != commit:
            raise RuntimeError(
                "Scored inference-bench harness does not match canonical remote main"
            )
    return {
        "check": "passed",
        "commit": commit,
        "origin_main": origin_main,
        "remote": remote,
        "worktree_clean": True,
        "entrypoint": str(Path(__file__).resolve()),
    }


def _port_can_bind(port: int) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(("0.0.0.0", int(port)))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def _next_provider_port(requested_port: int, used_ports: set[int]) -> int:
    port = max(1, int(requested_port))
    while port in used_ports or not _port_can_bind(port):
        port += 1
    used_ports.add(port)
    return port


def _free_gpu_memory() -> None:
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
    except ImportError:
        pass
    gc.collect()


def _append_torchinferno_queue_profile_marker(
    provider: object,
    *,
    event: str,
    benchmark: str,
    status: str | None = None,
    error: str | None = None,
) -> None:
    if getattr(provider, "name", None) != "torchinferno":
        return
    extra_log_paths = getattr(provider, "extra_log_paths", None)
    if not callable(extra_log_paths):
        if getattr(provider, "is_disaggregated_prefill_decode", False):
            raise RuntimeError("TorchInferno queue profile logging is unavailable")
        return
    queue_profile = extra_log_paths().get("queue_profile")
    if not queue_profile:
        if getattr(provider, "is_disaggregated_prefill_decode", False):
            raise RuntimeError("TorchInferno queue profile path is unavailable")
        return
    record = {
        "event": event,
        "provider": "torchinferno",
        "benchmark": benchmark,
        "timestamp_s": time.time(),
    }
    if status is not None:
        record["status"] = status
    if error is not None:
        record["error"] = error
    path = Path(queue_profile)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
    except OSError as exc:
        if getattr(provider, "is_disaggregated_prefill_decode", False):
            raise RuntimeError(
                f"TorchInferno benchmark integrity marker could not be written: {exc}"
            ) from exc


def run_all(
    config: Config,
    skip_build: bool = False,
    build_times: dict[str, float] | None = None,
    debug: bool = False,
    verbose: bool = False,
) -> RunResults:
    config.validate()
    harness_provenance = (
        _capture_harness_provenance(verify_remote=True)
        if config.evaluation_version >= 3
        else {}
    )
    prefill_tp, decode_tp = config.role_tensor_parallel_sizes
    results = RunResults(
        evaluation_version=config.evaluation_version,
        model=config.model,
        model_revision=config.model_revision,
        tensor_parallel_size=config.tensor_parallel_size,
        deployment_mode=config.deployment_mode,
        prefill_tensor_parallel_size=prefill_tp,
        decode_tensor_parallel_size=decode_tp,
        gpu_count=config.gpu_count,
        hardware=config.hardware,
        requested_providers=tuple(config.providers),
        requested_benchmarks=tuple(config.benchmarks),
        minimum_correctness_rate=config.minimum_correctness_rate,
        require_request_count_parity=config.require_request_count_parity,
        output_token_ratio_tolerance=config.output_token_ratio_tolerance,
        retain_response_text=config.retain_response_text or debug,
        output_token_count_method=(
            "client_tokenizer"
            if config.authoritative_output_token_count
            else "sse_content_chunks"
        ),
        sampling_top_p=(1.0 if config.evaluation_version >= 3 else None),
        harness_provenance=harness_provenance,
    )
    build_times = build_times or {}
    used_ports: set[int] = set()

    for provider_index, provider_name in enumerate(config.providers):
        print(f"\n[{provider_name}] Starting...")

        provider = get_provider(provider_name, build_dir=config.build_dir)
        provider.verbose = verbose
        provider.hardware = config.hardware
        provider.configure_deployment(
            deployment_mode=config.deployment_mode,
            tensor_parallel_size=config.tensor_parallel_size,
            prefill_tensor_parallel_size=config.prefill_tensor_parallel_size,
            decode_tensor_parallel_size=config.decode_tensor_parallel_size,
            model_revision=config.model_revision,
            model=config.model,
            evaluation_version=config.evaluation_version,
        )
        pr = ProviderResults(provider=provider_name)
        requested_port = config.server_port + provider_index
        provider_port = _next_provider_port(requested_port, used_ports)
        if provider_port != requested_port:
            print(f"[{provider_name}] Port {requested_port} unavailable; using {provider_port}")

        # Build/clone/commit-hash run inside the try so a single provider's
        # build failure is recorded and skipped instead of propagating out of
        # run_all and discarding results from providers that already completed.
        try:
            if skip_build:
                pr.deployment_observation.update(
                    provider.prepare_source_provenance(skip_build=True)
                )
                pr.build_time_s = build_times.get(provider_name, 0.0)
            else:
                provider.clone()
                provider.prepare_source_provenance(skip_build=False)
                build_start = time.time()
                provider.build()
                provider.wait_for_gpu_isolation(config.gpu_count)
                with provider.gpu_isolation_monitor(config.gpu_count):
                    provider.prepare_model_assets(config.model)
                pr.build_time_s = time.time() - build_start
                pr.deployment_observation.update(
                    provider.finalize_source_provenance()
                )
                print(f"[{provider_name}] Build completed in {pr.build_time_s:.1f}s")

            pr.commit_hash = provider.get_commit_hash()
            if pr.commit_hash:
                print(f"[{provider_name}] Commit: {pr.commit_hash[:12]}")

            provider.wait_for_gpu_isolation(config.gpu_count)
            provider.start_server(
                model=config.model,
                tp=config.gpu_count,
                port=provider_port,
                timeout=config.server_startup_timeout,
            )
            model_provenance = provider.verify_model_provenance(config.model)
            pr.deployment_observation.update(model_provenance)
            pr.deployment_observation.update(
                provider.verify_gpu_coverage(config.gpu_count)
            )

            for bench_name in config.benchmarks:
                benchmark = None
                marker_started = False
                bench_error: str | None = None
                try:
                    provider.wait_for_gpu_isolation(config.gpu_count)
                    benchmark = get_benchmark(bench_name)
                    benchmark.debug = debug or config.retain_response_text
                    benchmark.authoritative_output_token_count = (
                        config.authoritative_output_token_count
                    )
                    benchmark.model_revision = config.model_revision
                    resolved_snapshot = model_provenance.get("resolved_snapshot")
                    benchmark.authoritative_tokenizer_path = (
                        str(resolved_snapshot) if resolved_snapshot else None
                    )
                    benchmark.verbose = verbose
                    _append_torchinferno_queue_profile_marker(
                        provider,
                        event="benchmark_start",
                        benchmark=bench_name,
                    )
                    marker_started = True
                    with provider.gpu_isolation_monitor(config.gpu_count):
                        bench_result = benchmark.run(provider.api_base, config.model)
                    pr.benchmarks[bench_name] = bench_result
                except Exception as exc:
                    bench_error = str(exc)
                    pr.errors[bench_name] = str(exc)
                    if getattr(provider, "is_scored_evaluation", False):
                        pr.comparable = False
                        warning = (
                            f"Scored benchmark {bench_name!r} failed and "
                            "cannot be scored."
                        )
                        if warning not in pr.integrity_warnings:
                            pr.integrity_warnings.append(warning)
                    print(f"--- {bench_name} FAILED: {exc} ---")
                finally:
                    if marker_started:
                        _append_torchinferno_queue_profile_marker(
                            provider,
                            event="benchmark_end",
                            benchmark=bench_name,
                            status="error" if bench_error is not None else "ok",
                            error=bench_error,
                        )
                    if benchmark is not None:
                        close_clients = getattr(benchmark, "_close_open_clients", None)
                        if callable(close_clients):
                            close_clients()

            try:
                pr.deployment_observation.update(
                    provider.verify_source_provenance()
                )
                pr.deployment_observation.update(provider.verify_runtime_integrity())
            except Exception as exc:
                pr.comparable = False
                pr.integrity_warnings.append(
                    f"Runtime deployment integrity could not be verified: {exc}"
                )
                raise

        except Exception as exc:
            pr.errors["_server"] = str(exc)
            if getattr(provider, "is_scored_evaluation", False):
                pr.comparable = False
            print(f"[{provider_name}] Server error: {exc}")
        finally:
            provider.stop_server()
            extra_log_paths = getattr(provider, "extra_log_paths", None)
            if callable(extra_log_paths):
                pr.extra_log_paths = {
                    str(name): str(path)
                    for name, path in extra_log_paths().items()
                    if path
                }
            _free_gpu_memory()
            time.sleep(5)

        results.providers[provider_name] = pr
        # Persist after each provider so a later provider's failure can't
        # discard results that already completed. save() is idempotent for a
        # run: it rewrites the same timestamped run directory each call.
        try:
            results.save(config.resolved_results_dir)
        except Exception as exc:
            print(f"Warning: incremental results save failed: {exc}")

    if harness_provenance:
        final_harness = _capture_harness_provenance(
            verify_remote=False,
            allowed_untracked_root=results.run_dir(config.resolved_results_dir),
        )
        if final_harness != harness_provenance:
            raise RuntimeError("Inference-bench harness changed during the scored run")

    results.finalized = True
    results.save(config.resolved_results_dir)
    return results
