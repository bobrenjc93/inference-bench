# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:59 AM PT, May 31 2026

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
| torchinferno | **4.2s (0.1m)** | `86c466b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |      54739.9 |
| TPOT median (ms)          |        542.5 |
| E2E median (ms)           |      55327.5 |
| Throughput median (tok/s) |          0.0 |
| Correctness               |          91% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |      14993.3 |
| TPOT median (ms)          |        241.1 |
| E2E median (ms)           |      24054.1 |
| Throughput median (tok/s) |          1.8 |
| Correctness               |          56% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |      34866.6 |
| TPOT median (ms)          |        391.8 |
| E2E median (ms)           |      39690.8 |
| Throughput median (tok/s) |          0.9 |
| Correctness               |          74% |
