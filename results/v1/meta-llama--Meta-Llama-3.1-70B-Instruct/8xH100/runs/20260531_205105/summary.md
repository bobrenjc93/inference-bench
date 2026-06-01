# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:41 PM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |
| :--------------- | -----------: |
| few_shot         |          0/4 |
| long_output      |          0/4 |
| multi_turn       |          0/4 |
| tree_of_thought  |          0/4 |
| self_consistency |          0/4 |
| **Total**        |     **0/20** |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **4.0s (0.1m)** | `2849019` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        681.3 |
| TPOT median (ms)          |         65.4 |
| E2E median (ms)           |        734.6 |
| Throughput median (tok/s) |          1.5 |
| Correctness               |          98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       1324.2 |
| TPOT median (ms)          |         62.5 |
| E2E median (ms)           |       4514.1 |
| Throughput median (tok/s) |          5.8 |
| Correctness               |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       1414.3 |
| TPOT median (ms)          |        106.0 |
| E2E median (ms)           |       1512.0 |
| Throughput median (tok/s) |          0.8 |
| Correctness               |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        830.2 |
| TPOT median (ms)          |         53.0 |
| E2E median (ms)           |        873.8 |
| Throughput median (tok/s) |          1.4 |
| Correctness               |          97% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       1155.2 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |       1209.5 |
| Throughput median (tok/s) |          0.8 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       1081.1 |
| TPOT median (ms)          |         57.4 |
| E2E median (ms)           |       1768.8 |
| Throughput median (tok/s) |          2.1 |
| Correctness               |          99% |
