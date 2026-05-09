# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 12:12 AM PT, May 8 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **3/5** |     2/5 |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **3/5** |     2/5 |          0/5 |
| tree_of_thought  |       1/5 | **4/5** |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **14/25** |   11/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |   807.8s (13.5m) |
| sglang       |     87.5s (1.5m) |
| torchinferno | **38.3s (0.6m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **30.7** |     31.6 |         98.2 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.3 | **42.4** |        180.3 |
| Throughput median (tok/s) |     22.6 | **23.6** |          5.5 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **66.7** |  379.0 |       1413.5 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **89.1** |  388.8 |       1495.9 |
| Throughput median (tok/s) | **11.2** |    2.6 |          0.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **30.7** |     31.1 |        105.3 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.1 | **41.8** |        187.1 |
| Throughput median (tok/s) |     22.7 | **23.9** |          5.3 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     45.4 | **39.5** |        271.5 |
| TPOT median (ms)          |     28.0 | **23.4** |        163.6 |
| E2E median (ms)           |     59.1 | **53.4** |        353.5 |
| Throughput median (tok/s) |     17.5 | **18.9** |          2.8 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **30.5** |      32.0 |        105.8 |
| TPOT median (ms)          |     14.0 |  **12.1** |         84.3 |
| E2E median (ms)           |    544.6 | **479.3** |       3222.0 |
| Throughput median (tok/s) |     69.5 |  **79.2** |         11.8 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **40.8** |    102.6 |        398.9 |
| TPOT median (ms)          |       8.4 |  **7.1** |         49.6 |
| E2E median (ms)           | **156.2** |    201.1 |       1087.8 |
| Throughput median (tok/s) |      28.7 | **29.6** |          5.2 |
| Correctness               |  **100%** |     100% |         100% |
