# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 2:50 PM PT, May 8 2026

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

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        304.8 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        566.8 |
| Throughput median (tok/s) |          1.8 |
| Correctness               |         100% |

### self_consistency

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |       2410.0 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |       2722.4 |
| Throughput median (tok/s) |          0.4 |
| Correctness               |         100% |

### multi_turn

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        359.8 |
| TPOT median (ms)          |          0.0 |
| E2E median (ms)           |        622.0 |
| Throughput median (tok/s) |          1.6 |
| Correctness               |         100% |

### tree_of_thought

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        376.5 |
| TPOT median (ms)          |        434.1 |
| E2E median (ms)           |        756.4 |
| Throughput median (tok/s) |          1.7 |
| Correctness               |         100% |

### long_output

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        334.3 |
| TPOT median (ms)          |        270.8 |
| E2E median (ms)           |      10243.3 |
| Throughput median (tok/s) |          3.7 |
| Correctness               |         100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |
| :------------------------ | -----------: |
| TTFT median (ms)          |        757.1 |
| TPOT median (ms)          |        141.0 |
| E2E median (ms)           |       2982.2 |
| Throughput median (tok/s) |          1.8 |
| Correctness               |         100% |
