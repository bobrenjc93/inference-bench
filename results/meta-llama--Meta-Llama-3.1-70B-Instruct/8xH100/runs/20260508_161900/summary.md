# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 2026-05-08T16:13:28.988962

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **3/5** |     2/5 |          0/5 |
| tree_of_thought  |   **3/5** |     2/5 |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **15/25** |   10/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |   807.8s (13.5m) |
| sglang       |     87.5s (1.5m) |
| torchinferno | **39.0s (0.7m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.5 | **31.1** |        299.0 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     45.4 | **42.0** |        556.4 |
| Throughput median (tok/s) |     22.1 | **23.8** |          1.8 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **63.5** |  433.4 |       1545.5 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **87.4** |  441.5 |       1866.2 |
| Throughput median (tok/s) | **11.4** |    2.3 |          0.5 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **30.8** |     32.2 |        359.5 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.2 | **42.8** |        621.4 |
| Throughput median (tok/s) |     22.6 | **23.3** |          1.6 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **33.7** |     41.2 |        302.1 |
| TPOT median (ms)          |     28.1 | **24.0** |        345.2 |
| E2E median (ms)           |     56.5 | **56.2** |        560.7 |
| Throughput median (tok/s) | **19.9** |     18.1 |          1.8 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **31.1** |      32.8 |        334.2 |
| TPOT median (ms)          |     14.1 |  **12.1** |        265.8 |
| E2E median (ms)           |    551.8 | **480.1** |      10136.5 |
| Throughput median (tok/s) |     68.8 |  **79.1** |          3.7 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **38.1** |    114.1 |        568.1 |
| TPOT median (ms)          |       8.4 |  **7.2** |        122.2 |
| E2E median (ms)           | **157.0** |    212.5 |       2748.2 |
| Throughput median (tok/s) |      29.0 | **29.3** |          1.9 |
| Correctness               |  **100%** |     100% |         100% |
