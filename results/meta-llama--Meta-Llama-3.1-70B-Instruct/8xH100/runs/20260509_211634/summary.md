# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:42 PM PT, May 9 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **5/5** |     0/5 |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **5/5** |     0/5 |          0/5 |
| tree_of_thought  |   **4/5** |     1/5 |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **21/25** |    4/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1022.8s (17.0m) |
| sglang       |    295.5s (4.9m) |
| torchinferno | **73.2s (1.2m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **25.3** |   31.6 |         36.8 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **36.0** |   40.0 |         46.7 |
| Throughput median (tok/s) | **27.8** |   25.0 |         21.4 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **71.5** |  511.2 |        740.3 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **86.0** |  521.8 |       1613.0 |
| Throughput median (tok/s) | **11.6** |    1.9 |          0.6 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.4** |   29.5 |        468.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.1** |   38.3 |        787.8 |
| Throughput median (tok/s) | **28.5** |   26.1 |          1.3 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **38.5** |     45.8 |         83.6 |
| TPOT median (ms)          |     76.2 | **18.0** |        115.9 |
| E2E median (ms)           | **51.3** |     56.3 |        198.7 |
| Throughput median (tok/s) | **20.0** |     17.9 |          5.1 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **25.2** |      29.9 |        211.2 |
| TPOT median (ms)          |     11.1 |   **9.3** |         10.0 |
| E2E median (ms)           |    436.4 | **378.0** |        579.6 |
| Throughput median (tok/s) |     87.0 | **100.5** |         65.4 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          |  **37.0** |   129.6 |        308.0 |
| TPOT median (ms)          |      17.5 | **5.5** |         25.2 |
| E2E median (ms)           | **129.0** |   206.9 |        645.2 |
| Throughput median (tok/s) |  **35.0** |    34.3 |         18.8 |
| Correctness               |  **100%** |    100% |         100% |
