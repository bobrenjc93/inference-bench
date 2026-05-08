from __future__ import annotations

import argparse
import sys

from .config import Config
from .runner import run_all


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Benchmark and compare LLM inference engines",
    )
    p.add_argument(
        "--config", type=str, default=None,
        help="Path to config.yaml (default: config.yaml in repo root)",
    )
    p.add_argument(
        "--model", type=str, default=None,
        help="Model name/path (e.g. meta-llama/Meta-Llama-3.1-70B-Instruct)",
    )
    p.add_argument(
        "--providers", nargs="+", default=None,
        help="Providers to benchmark (e.g. vllm sglang)",
    )
    p.add_argument(
        "--benchmarks", nargs="+", default=None,
        help="Benchmarks to run (e.g. few_shot self_consistency multi_turn tree_of_thought)",
    )
    p.add_argument(
        "--tp", type=int, default=None,
        help="Tensor parallel size (default: 8)",
    )
    p.add_argument(
        "--port", type=int, default=None,
        help="Server port (default: 8000)",
    )
    p.add_argument(
        "--build-dir", type=str, default=None,
        help="Directory for cloned repos and venvs (default: ./builds)",
    )
    p.add_argument(
        "--results-dir", type=str, default=None,
        help="Directory for result JSON files (default: ./results)",
    )
    p.add_argument(
        "--skip-build", action="store_true",
        help="Skip clone+build steps (assumes builds already exist)",
    )
    p.add_argument(
        "--build-times", type=str, default=None,
        help="Comma-separated provider:seconds pairs for pre-recorded build times (e.g. vllm:868,sglang:221)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    config = Config.load(args.config)
    config.apply_overrides(
        model=args.model,
        providers=args.providers,
        benchmarks=args.benchmarks,
        tp=args.tp,
        build_dir=args.build_dir,
        results_dir=args.results_dir,
        port=args.port,
    )

    print("=" * 60)
    print("inference-bench")
    print("=" * 60)
    print(f"  Model:      {config.model}")
    print(f"  TP:         {config.tensor_parallel_size}")
    print(f"  Providers:  {', '.join(config.providers)}")
    print(f"  Benchmarks: {', '.join(config.benchmarks)}")
    print(f"  Build dir:  {config.build_dir}")
    print(f"  Results dir: {config.results_dir}")
    print("=" * 60)

    build_times = {}
    if args.build_times:
        for pair in args.build_times.split(","):
            name, secs = pair.split(":")
            build_times[name.strip()] = float(secs.strip())

    results = run_all(config, skip_build=args.skip_build, build_times=build_times)
    results.print_comparison()
    json_path = results.save(config.results_dir)
    results.save_csv(config.results_dir)

    try:
        from scripts.plot_results import main as plot_main
        plot_main(str(json_path))
    except Exception as exc:
        print(f"\nWarning: could not generate plots: {exc}")


if __name__ == "__main__":
    main()
