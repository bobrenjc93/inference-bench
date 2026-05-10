# inference-bench

Benchmark and compare LLM inference engines (vllm, sglang, torchinferno).

See [`README.md`](README.md) for full project documentation (architecture,
benchmarks, CLI reference, results format, extending).

## Running benchmarks

### Local (machine has GPUs)

Detect hardware, set protoc, clean builds, and run:

```
rm -rf builds/ && \
PROTOC=/home/bobren/local/e/tools/protoc/bin/protoc \
PATH="/home/bobren/local/e/tools/protoc/bin:$PATH" \
python -m inference_bench \
  --port 8001 \
  --hardware 8xH100
```

The `PROTOC` env var is required because sglang's Rust gRPC build needs protoc,
and it's not on PATH by default on this machine. protoc lives at
`/home/bobren/local/e/tools/protoc/bin/protoc`.

Port 8000 is often occupied on dev machines. Always use `--port 8001`.

This takes several hours total (builds ~15 min each, server startup, 5 benchmarks × 10k requests per provider).

### Remote (via gpu-dev)

```
bash run_benchmark.sh
```

This reserves 8xH100 for 8 hours via `gpu-dev submit`, runs `_remote_benchmark.sh`
on the remote node (which installs deps including protoc, creates a venv, and
runs the benchmark), syncs results back, commits, and pushes.

### Skip build (reuse existing builds)

```
python -m inference_bench \
  --providers vllm sglang torchinferno \
  --skip-build \
  --build-times "vllm:807.8,sglang:87.5,torchinferno:38.3" \
  --port 8001 \
  --hardware 8xH100
```

### Single provider

```
python -m inference_bench \
  --providers torchinferno \
  --skip-build \
  --port 8001 \
  --hardware 8xH100
```

## Results

Results are versioned. `v0` contains the original low-volume latency-focused runs
(8-16 requests per benchmark). `v1` scales every benchmark to ~10,000 requests with
high concurrency for realistic throughput measurement.

After every benchmark run, results are saved to `results/v1/<model>/<hw>/runs/<timestamp>/` containing:
- `results.json` — full results with per-request raw data
- `results.csv` — human-readable CSV with summary tables and raw data
- `summary.md` — markdown scorecard with winner highlights
- `plots/` — auto-generated line charts and summary bar charts

Three scripts run automatically at the end of each benchmark:
- `scripts/generate_summary.py` — markdown summary with scorecard and per-benchmark tables
- `scripts/plot_results.py` — per-run charts (line charts per request, summary bars)
- `scripts/plot_progress.py` — cross-run progress charts tracking metrics over time

All results and plots should be committed to the repo so we can track performance over time.

### Results directory structure

```
results/
  v0/                                          # legacy low-volume runs
    meta-llama--Meta-Llama-3.1-70B-Instruct/
      ...
  v1/                                          # current: 10k requests/benchmark
    meta-llama--Meta-Llama-3.1-70B-Instruct/   # one dir per model
      8xH100/                                  # one dir per hardware
        plots/                                 # cross-run progress charts
        runs/
          20260510_123456/
            results.json
            results.csv
            summary.md
            plots/                             # per-run charts
```

## Adding a new provider

1. Create `inference_bench/providers/<name>.py` subclassing `Provider`
2. Add `@register("<name>")` decorator
3. Add lazy import in `inference_bench/providers/__init__.py`
4. Add to `config.yaml` providers list
