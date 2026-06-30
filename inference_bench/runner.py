from __future__ import annotations

import gc
import socket
import time

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
    )
    build_times = build_times or {}
    used_ports: set[int] = set()

    for provider_index, provider_name in enumerate(config.providers):
        print(f"\n[{provider_name}] Starting...")

        provider = get_provider(provider_name, build_dir=config.build_dir)
        provider.verbose = verbose
        pr = ProviderResults(provider=provider_name)
        requested_port = config.server_port + provider_index
        provider_port = _next_provider_port(requested_port, used_ports)
        if provider_port != requested_port:
            print(f"[{provider_name}] Port {requested_port} unavailable; using {provider_port}")

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

        try:
            provider.wait_for_gpu_isolation(config.tensor_parallel_size)
            provider.start_server(
                model=config.model,
                tp=config.tensor_parallel_size,
                port=provider_port,
                timeout=config.server_startup_timeout,
            )

            for bench_name in config.benchmarks:
                benchmark = None
                try:
                    provider.wait_for_gpu_isolation(config.tensor_parallel_size)
                    benchmark = get_benchmark(bench_name)
                    benchmark.debug = debug
                    benchmark.verbose = verbose
                    with provider.gpu_isolation_monitor(config.tensor_parallel_size):
                        bench_result = benchmark.run(provider.api_base, config.model)
                    pr.benchmarks[bench_name] = bench_result
                except Exception as exc:
                    pr.errors[bench_name] = str(exc)
                    print(f"--- {bench_name} FAILED: {exc} ---")
                finally:
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

    return results
