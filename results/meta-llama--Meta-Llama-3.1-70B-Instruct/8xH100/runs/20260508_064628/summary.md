# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 2026-05-08T06:42:04.154409

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **3/5** |     2/5 |          0/5 |
| tree_of_thought  |       1/5 | **4/5** |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **13/25** |   12/25 |         0/25 |

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
| TTFT median (ms)          |     31.1 | **30.2** |         98.3 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.5 | **41.3** |        180.6 |
| Throughput median (tok/s) |     22.5 | **24.2** |          5.5 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **64.0** |  429.5 |       1421.2 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **86.6** |  438.6 |       1503.5 |
| Throughput median (tok/s) | **11.5** |    2.3 |          0.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **31.0** |     31.5 |        105.7 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.4 | **42.2** |        188.0 |
| Throughput median (tok/s) |     22.5 | **23.7** |          5.3 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     43.3 | **35.3** |        271.6 |
| TPOT median (ms)          |     25.3 | **22.8** |        163.8 |
| E2E median (ms)           |     57.7 | **51.5** |        355.3 |
| Throughput median (tok/s) |     17.8 | **20.9** |          2.8 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **31.4** |      31.8 |        107.1 |
| TPOT median (ms)          |     14.2 |  **12.1** |         84.7 |
| E2E median (ms)           |    549.2 | **478.8** |       3234.1 |
| Throughput median (tok/s) |     68.2 |  **79.3** |         11.7 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **40.1** |    111.7 |        400.8 |
| TPOT median (ms)          |       7.9 |  **7.0** |         49.7 |
| E2E median (ms)           | **156.5** |    210.5 |       1092.3 |
| Throughput median (tok/s) |      28.5 | **30.1** |          5.2 |
| Correctness               |  **100%** |     100% |         100% |
