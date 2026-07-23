from __future__ import annotations

import argparse
from pathlib import Path

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
        "--model-revision",
        type=str,
        default=None,
        help="Pinned 40-character Hugging Face revision for scored disaggregated runs",
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
        help="Tensor parallel size per server role (default: 8)",
    )
    p.add_argument(
        "--deployment-mode", type=str, default=None,
        help="Deployment mode: standard or disaggregated_prefill_decode",
    )
    p.add_argument(
        "--prefill-tp", type=int, default=None,
        help="Prefill tensor parallel size for disaggregated deployment",
    )
    p.add_argument(
        "--decode-tp", type=int, default=None,
        help="Decode tensor parallel size for disaggregated deployment",
    )
    p.add_argument(
        "--port", type=int, default=None,
        help="Server port (default: 8000)",
    )
    p.add_argument(
        "--server-startup-timeout", type=int, default=None,
        help="Maximum seconds to wait for each provider server to become ready",
    )
    p.add_argument(
        "--hardware", type=str, default=None,
        help="Hardware description (e.g. 8xH100, 4xA100). Included in results path.",
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
        help=(
            "Comma-separated provider:seconds pairs for pre-recorded build times "
            "(e.g. vllm:868,sglang:221)"
        ),
    )
    p.add_argument(
        "--debug", action="store_true",
        help="Save response text in results for correctness auditing",
    )
    p.add_argument(
        "--verbose", "-v", action="store_true",
        help="Print detailed progress (default: quiet, only milestones)",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()
    config = Config.load(args.config)
    config.apply_overrides(
        model=args.model,
        model_revision=args.model_revision,
        providers=args.providers,
        benchmarks=args.benchmarks,
        tp=args.tp,
        deployment_mode=args.deployment_mode,
        prefill_tp=args.prefill_tp,
        decode_tp=args.decode_tp,
        hardware=args.hardware,
        build_dir=args.build_dir,
        results_dir=args.results_dir,
        port=args.port,
        server_startup_timeout=args.server_startup_timeout,
    )

    print(
        f"inference-bench: {config.model} | "
        f"{', '.join(config.providers)} | "
        f"{config.hardware or 'no-hw'} | "
        f"{config.deployment_mode} ({config.gpu_count} GPUs)"
    )

    build_times = {}
    if args.build_times:
        for pair in args.build_times.split(","):
            name, secs = pair.split(":")
            build_times[name.strip()] = float(secs.strip())

    results = run_all(
        config,
        skip_build=args.skip_build,
        build_times=build_times,
        debug=args.debug,
        verbose=args.verbose,
    )
    results.print_comparison()
    json_path = results.save(config.results_dir)
    results.save_csv(config.results_dir)

    try:
        from scripts.generate_summary import main as summary_main
        summary_main(str(json_path))
    except Exception as exc:
        print(f"\nWarning: could not generate summary: {exc}")

    try:
        from scripts.plot_results import main as plot_main
        plot_main(str(json_path))
    except Exception as exc:
        print(f"\nWarning: could not generate per-run plots: {exc}")

    try:
        from scripts.plot_progress import main as progress_main
        model_slug = config.model.replace("/", "--")
        progress_dir = Path(config.results_dir) / model_slug
        if config.hardware:
            progress_dir = progress_dir / config.hardware
        progress_main(str(progress_dir))
    except Exception as exc:
        print(f"\nWarning: could not generate progress plots: {exc}")


if __name__ == "__main__":
    main()
