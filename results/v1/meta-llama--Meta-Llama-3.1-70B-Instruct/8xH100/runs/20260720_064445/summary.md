# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:44 PM PT, Jul 19 2026

## Scorecard

| Benchmark        | torchinferno |
| :--------------- | -----------: |
| few_shot         |          0/4 |
| self_consistency |          0/4 |
| multi_turn       |          0/4 |
| tree_of_thought  |          0/4 |
| long_output      |          0/4 |
| **Total**        |     **0/20** |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **0.0s (0.0m)** | `3ffe0eb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         46.5 |
| TPOT median (ms)          |         43.4 |
| E2E median (ms)           |         75.7 |
| Throughput median (tok/s) |         17.6 |
| Correctness               |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         32.5 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |         48.6 |
| Throughput median (tok/s) |         20.6 |
| Correctness               |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         42.1 |
| TPOT median (ms)          |         37.8 |
| E2E median (ms)           |         69.4 |
| Throughput median (tok/s) |         17.9 |
| Correctness               |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         28.5 |
| TPOT median (ms)          |         18.9 |
| E2E median (ms)           |         41.7 |
| Throughput median (tok/s) |         33.4 |
| Correctness               |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         48.6 |
| TPOT median (ms)          |         14.8 |
| E2E median (ms)           |        612.5 |
| Throughput median (tok/s) |         61.7 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         39.6 |
| TPOT median (ms)          |         23.0 |
| E2E median (ms)           |        169.6 |
| Throughput median (tok/s) |         30.2 |
| Correctness               |          99% |
