# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:48 AM PT, May 31 2026

## Scorecard

| Benchmark   | torchinferno |
| :---------- | -----------: |
| few_shot    |          0/4 |
| long_output |          0/4 |
| **Total**   |      **0/8** |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **4.1s (0.1m)** | `cac0917` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       6191.8 |
| TPOT median (ms)          |         79.5 |
| E2E median (ms)           |      14890.1 |
| Throughput median (tok/s) |          7.8 |
| Correctness               |           0% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        832.0 |
| TPOT median (ms)          |         72.4 |
| E2E median (ms)           |       4458.1 |
| Throughput median (tok/s) |          7.0 |
| Correctness               |           0% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       3511.9 |
| TPOT median (ms)          |         75.9 |
| E2E median (ms)           |       9674.1 |
| Throughput median (tok/s) |          7.4 |
| Correctness               |           0% |
