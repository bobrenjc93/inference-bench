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
) -> RunResults:
    results = RunResults(
        model=config.model,
        tensor_parallel_size=config.tensor_parallel_size,
    )
    build_times = build_times or {}

    for provider_name in config.providers:
        print(f"\n{'=' * 60}")
        print(f"PROVIDER: {provider_name}")
        print(f"{'=' * 60}")

        provider = get_provider(provider_name, build_dir=config.build_dir)
        pr = ProviderResults(provider=provider_name)

        if skip_build:
            pr.build_time_s = build_times.get(provider_name, 0.0)
            print(f"[{provider_name}] Skipping build (recorded time: {pr.build_time_s:.1f}s)")
        else:
            provider.clone()
            print(f"\n[{provider_name}] Building...")
            build_start = time.time()
            provider.build()
            pr.build_time_s = time.time() - build_start
            print(f"[{provider_name}] Build completed in {pr.build_time_s:.1f}s")

        try:
            provider.start_server(
                model=config.model,
                tp=config.tensor_parallel_size,
                port=config.server_port,
                timeout=config.server_startup_timeout,
            )

            for bench_name in config.benchmarks:
                print(f"\n--- Running benchmark: {bench_name} ---")
                benchmark = get_benchmark(bench_name)
                bench_result = benchmark.run(provider.api_base, config.model)
                pr.benchmarks[bench_name] = bench_result
                print(f"--- {bench_name} complete ---")

        finally:
            provider.stop_server()

        results.providers[provider_name] = pr

    return results
