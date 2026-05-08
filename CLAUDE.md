# inference-bench

Benchmark and compare LLM inference engines (vllm, sglang, torchinferno).

## Benchmark workflow

After every benchmark run, results are saved to `results/runs/<timestamp>/` containing:
- `results.json` — full results with per-request raw data
- `results.csv` — human-readable CSV with summary tables and raw data
- `plots/` — auto-generated line charts and summary bar charts

The plotting script runs automatically at the end of each benchmark. To regenerate plots manually:
```
python scripts/plot_results.py \
  results/runs/<timestamp>/results.json
```

All results and plots should be committed to the repo so we can track performance over time.

## Running benchmarks

Full run (clone + build + benchmark all providers):
```
python -m inference_bench --port 8001
```

Skip build (reuse existing builds, inject recorded build times):
```
python -m inference_bench \
  --providers vllm sglang torchinferno \
  --skip-build \
  --build-times "vllm:807.8,sglang:87.5,torchinferno:38.3" \
  --port 8001
```

Single provider:
```
python -m inference_bench \
  --providers torchinferno \
  --skip-build \
  --port 8001
```

## Results directory structure

```
results/
  runs/
    20260508_064628/
      results.json
      results.csv
      plots/
        build_times.png
        few_shot_ttft_ms.png
        long_output_throughput_tps.png
        summary_throughput_median_tps.png
        ...
```

## Adding a new provider

1. Create `inference_bench/providers/<name>.py` subclassing `Provider`
2. Add `@register("<name>")` decorator
3. Add lazy import in `inference_bench/providers/__init__.py`
4. Add to `config.yaml` providers list

## Port 8000

Port 8000 is often occupied on dev machines. Default to `--port 8001`.
