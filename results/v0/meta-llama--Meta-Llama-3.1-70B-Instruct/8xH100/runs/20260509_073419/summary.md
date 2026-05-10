# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:32 AM PT, May 9 2026

## Scorecard

| Benchmark        | torchinferno |
| :--------------- | -----------: |
| few_shot         |          0/5 |
| self_consistency |          0/5 |
| multi_turn       |          0/5 |
| tree_of_thought  |          0/5 |
| long_output      |          0/5 |
| **Total**        |     **0/25** |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |            Time |
| :----------- | --------------: |
| torchinferno | **0.0s (0.0m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        298.2 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        555.6 |
| Throughput median (tok/s) |          1.8 |
| Correctness               |         100% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       2132.2 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |       2451.2 |
| Throughput median (tok/s) |          0.4 |
| Correctness               |         100% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        363.4 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        632.3 |
| Throughput median (tok/s) |          1.6 |
| Correctness               |         100% |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        530.4 |
| TPOT median (ms)          |        346.7 |
| E2E median (ms)           |        708.6 |
| Throughput median (tok/s) |          1.4 |
| Correctness               |         100% |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        334.2 |
| TPOT median (ms)          |        269.3 |
| E2E median (ms)           |      10217.5 |
| Throughput median (tok/s) |          3.7 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        731.7 |
| TPOT median (ms)          |        123.2 |
| E2E median (ms)           |       2913.0 |
| Throughput median (tok/s) |          1.8 |
| Correctness               |         100% |
