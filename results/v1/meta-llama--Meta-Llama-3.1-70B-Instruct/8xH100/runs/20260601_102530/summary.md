# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:18 AM PT, Jun 1 2026

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
| torchinferno | **7.5s (0.1m)** | `30a83be` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        182.6 |
| TPOT median (ms)          |         65.0 |
| E2E median (ms)           |        235.3 |
| Throughput median (tok/s) |          5.0 |
| Correctness               |          98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       1832.6 |
| TPOT median (ms)          |         49.7 |
| E2E median (ms)           |       3495.5 |
| Throughput median (tok/s) |         10.5 |
| Correctness               |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        819.1 |
| TPOT median (ms)          |         89.9 |
| E2E median (ms)           |       1080.1 |
| Throughput median (tok/s) |          1.3 |
| Correctness               |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        726.8 |
| TPOT median (ms)          |         52.2 |
| E2E median (ms)           |        765.6 |
| Throughput median (tok/s) |          2.4 |
| Correctness               |          97% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        261.5 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        399.3 |
| Throughput median (tok/s) |          2.5 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        764.5 |
| TPOT median (ms)          |         51.4 |
| E2E median (ms)           |       1195.1 |
| Throughput median (tok/s) |          4.3 |
| Correctness               |          98% |
