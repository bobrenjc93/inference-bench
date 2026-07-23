from __future__ import annotations

import gc
import json
import socket
import time
from pathlib import Path

from .benchmarks import get_benchmark
from .config import Config
from .providers import get_provider
from .results import ProviderResults, RunResults


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
        return
    queue_profile = extra_log_paths().get("queue_profile")
    if not queue_profile:
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
    except OSError:
        return


def run_all(
    config: Config,
    skip_build: bool = False,
    build_times: dict[str, float] | None = None,
    debug: bool = False,
    verbose: bool = False,
) -> RunResults:
    results = RunResults(
        model=config.model,
        tensor_parallel_size=config.tensor_parallel_size,
        hardware=config.hardware,
        requested_providers=tuple(config.providers),
    )
    build_times = build_times or {}
    used_ports: set[int] = set()

    for provider_index, provider_name in enumerate(config.providers):
        print(f"\n[{provider_name}] Starting...")

        provider = get_provider(provider_name, build_dir=config.build_dir)
        provider.verbose = verbose
        provider.hardware = config.hardware
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
                pr.build_time_s = build_times.get(provider_name, 0.0)
            else:
                provider.clone()
                build_start = time.time()
                provider.build()
                pr.build_time_s = time.time() - build_start
                print(f"[{provider_name}] Build completed in {pr.build_time_s:.1f}s")

            pr.commit_hash = provider.get_commit_hash()
            if pr.commit_hash:
                print(f"[{provider_name}] Commit: {pr.commit_hash[:12]}")

            provider.wait_for_gpu_isolation(config.tensor_parallel_size)
            provider.start_server(
                model=config.model,
                tp=config.tensor_parallel_size,
                port=provider_port,
                timeout=config.server_startup_timeout,
            )

            for bench_name in config.benchmarks:
                benchmark = None
                marker_started = False
                bench_error: str | None = None
                try:
                    provider.wait_for_gpu_isolation(config.tensor_parallel_size)
                    benchmark = get_benchmark(bench_name)
                    benchmark.debug = debug
                    benchmark.verbose = verbose
                    _append_torchinferno_queue_profile_marker(
                        provider,
                        event="benchmark_start",
                        benchmark=bench_name,
                    )
                    marker_started = True
                    with provider.gpu_isolation_monitor(config.tensor_parallel_size):
                        bench_result = benchmark.run(provider.api_base, config.model)
                    pr.benchmarks[bench_name] = bench_result
                except Exception as exc:
                    bench_error = str(exc)
                    pr.errors[bench_name] = str(exc)
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

        except Exception as exc:
            pr.errors["_server"] = str(exc)
            print(f"[{provider_name}] Server error: {exc}")
        finally:
            provider.stop_server()
            log_path = getattr(provider, "_log_path", None)
            if log_path is not None:
                pr.server_log_path = str(log_path)
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
            results.save(config.results_dir)
        except Exception as exc:
            print(f"Warning: incremental results save failed: {exc}")

    return results
