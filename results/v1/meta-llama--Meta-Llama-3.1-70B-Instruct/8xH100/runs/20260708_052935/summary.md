# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:29 PM PT, Jul 7 2026

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
| torchinferno | **0.0s (0.0m)** | `03eadd4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        176.7 |
| TPOT median (ms)          |         45.2 |
| E2E median (ms)           |        219.7 |
| Throughput median (tok/s) |          5.5 |
| Correctness               |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        312.2 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        333.7 |
| Throughput median (tok/s) |          3.0 |
| Correctness               |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        258.1 |
| TPOT median (ms)          |         64.9 |
| E2E median (ms)           |        316.7 |
| Throughput median (tok/s) |          4.1 |
| Correctness               |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |         91.9 |
| TPOT median (ms)          |         50.0 |
| E2E median (ms)           |        133.1 |
| Throughput median (tok/s) |         11.0 |
| Correctness               |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        250.3 |
| TPOT median (ms)          |         22.4 |
| E2E median (ms)           |       1088.2 |
| Throughput median (tok/s) |         34.5 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        217.8 |
| TPOT median (ms)          |         36.5 |
| E2E median (ms)           |        418.3 |
| Throughput median (tok/s) |         11.6 |
| Correctness               |          98% |
