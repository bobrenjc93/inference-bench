# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:22 AM PT, May 31 2026

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
| torchinferno | **4.0s (0.1m)** | `aa56bb1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        208.1 |
| TPOT median (ms)          |         65.1 |
| E2E median (ms)           |        277.6 |
| Throughput median (tok/s) |          4.3 |
| Correctness               |          98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        631.7 |
| TPOT median (ms)          |         43.5 |
| E2E median (ms)           |       2294.6 |
| Throughput median (tok/s) |         15.4 |
| Correctness               |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       1697.0 |
| TPOT median (ms)          |        145.1 |
| E2E median (ms)           |       1923.4 |
| Throughput median (tok/s) |          0.6 |
| Correctness               |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        913.0 |
| TPOT median (ms)          |         50.2 |
| E2E median (ms)           |       1035.1 |
| Throughput median (tok/s) |          1.6 |
| Correctness               |          96% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        741.8 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        953.3 |
| Throughput median (tok/s) |          1.0 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        838.3 |
| TPOT median (ms)          |         60.8 |
| E2E median (ms)           |       1296.8 |
| Throughput median (tok/s) |          4.6 |
| Correctness               |          98% |
