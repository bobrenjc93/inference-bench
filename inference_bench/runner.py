from __future__ import annotations

import time

from .benchmarks import get_benchmark
from .config import Config
from .providers import get_provider
from .results import ProviderResults, RunResults


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

    for provider_name in config.providers:
        print(f"\n[{provider_name}] Starting...")

        provider = get_provider(provider_name, build_dir=config.build_dir)
        provider.verbose = verbose
        pr = ProviderResults(provider=provider_name)

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
            provider.start_server(
                model=config.model,
                tp=config.tensor_parallel_size,
                port=config.server_port,
                timeout=config.server_startup_timeout,
            )

            for bench_name in config.benchmarks:
                try:
                    benchmark = get_benchmark(bench_name)
                    benchmark.debug = debug
                    benchmark.verbose = verbose
                    bench_result = benchmark.run(provider.api_base, config.model)
                    pr.benchmarks[bench_name] = bench_result
                except Exception as exc:
                    print(f"--- {bench_name} FAILED: {exc} ---")

        except Exception as exc:
            print(f"[{provider_name}] Server error: {exc}")
        finally:
            provider.stop_server()

        results.providers[provider_name] = pr

    return results
