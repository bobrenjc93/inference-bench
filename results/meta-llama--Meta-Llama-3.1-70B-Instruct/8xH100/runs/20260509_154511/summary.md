# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2026-05-09T15:11:50.909353

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
| vllm         |  1074.4s (17.9m) |
| sglang       |    165.6s (2.8m) |
| torchinferno | **40.5s (0.7m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **25.3** |   32.5 |        104.7 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **36.2** |   41.3 |        114.4 |
| Throughput median (tok/s) | **27.6** |   24.2 |          8.7 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **64.1** |  509.8 |       1541.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **83.5** |  522.4 |       1603.2 |
| Throughput median (tok/s) | **12.0** |    1.9 |          0.6 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.4** |   28.7 |        253.5 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.3** |   37.6 |        269.3 |
| Throughput median (tok/s) | **28.4** |   26.6 |          3.7 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **37.7** |     46.3 |        211.7 |
| TPOT median (ms)          |     21.9 | **19.1** |         96.3 |
| E2E median (ms)           | **49.9** |     56.9 |        275.5 |
| Throughput median (tok/s) | **20.9** |     17.8 |          3.7 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **24.9** |      29.4 |        245.8 |
| TPOT median (ms)          |     11.2 |   **9.4** |          9.9 |
| E2E median (ms)           |    439.3 | **378.1** |        610.5 |
| Throughput median (tok/s) |     86.5 | **100.5** |         62.1 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          |  **35.3** |   129.4 |        471.4 |
| TPOT median (ms)          |       6.6 | **5.7** |         21.2 |
| E2E median (ms)           | **128.8** |   207.2 |        574.6 |
| Throughput median (tok/s) |  **35.0** |    34.2 |         15.8 |
| Correctness               |  **100%** |    100% |         100% |
