# inference-bench

Benchmark and compare LLM inference engines (vllm, sglang, torchinferno).

## Benchmark workflow

After every benchmark run, results are saved to `results/runs/<timestamp>/` containing:
- `results.json` — full results with per-request raw data
- `results.csv` — human-readable CSV with summary tables and raw data
- `plots/` — auto-generated line charts and summary bar charts

Two plotting scripts run automatically at the end of each benchmark:
- `scripts/plot_results.py` — per-run charts (line charts per request, summary bars)
- `scripts/plot_progress.py` — cross-run progress charts tracking metrics over time

To regenerate manually:
```
python scripts/plot_results.py \
  results/meta-llama--Meta-Llama-3.1-70B-Instruct/8xH100/runs/<timestamp>/results.json
python scripts/plot_progress.py \
  results/meta-llama--Meta-Llama-3.1-70B-Instruct/8xH100
```

All results and plots should be committed to the repo so we can track performance over time.

## Running benchmarks

Full run (clone + build + benchmark all providers):
```
python -m inference_bench \
  --port 8001 \
  --hardware 8xH100
```

Skip build (reuse existing builds, inject recorded build times):
```
python -m inference_bench \
  --providers vllm sglang torchinferno \
  --skip-build \
  --build-times "vllm:807.8,sglang:87.5,torchinferno:38.3" \
  --port 8001 \
  --hardware 8xH100
```

Single provider:
```
python -m inference_bench \
  --providers torchinferno \
  --skip-build \
  --port 8001 \
  --hardware 8xH100
```

Via gpu-dev (reserves 8xH100, runs benchmark, syncs results back, commits):
```
bash run_benchmark.sh
```

## Results directory structure

```
results/
  meta-llama--Meta-Llama-3.1-70B-Instruct/   # one dir per model
    8xH100/                                    # one dir per hardware
      plots/                                   # cross-run progress charts
        few_shot/
          ttft_median_ms.png
          throughput_median_tps.png
        summary/
          build_times.png
      runs/
        20260508_064628/
          results.json
          results.csv
          plots/                               # per-run charts
            few_shot/
              ttft_ms.png
              throughput_tps.png
            summary/
              build_times.png
              throughput_median_tps.png
```

## Adding a new provider

1. Create `inference_bench/providers/<name>.py` subclassing `Provider`
2. Add `@register("<name>")` decorator
3. Add lazy import in `inference_bench/providers/__init__.py`
4. Add to `config.yaml` providers list

## Port 8000

Port 8000 is often occupied on dev machines. Default to `--port 8001`.
