# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2026-05-09T19:53:33.642687

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
| vllm         |  1026.2s (17.1m) |
| sglang       |    310.4s (5.2m) |
| torchinferno | **77.2s (1.3m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **25.5** |   33.2 |         36.6 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **36.3** |   41.3 |         46.5 |
| Throughput median (tok/s) | **27.5** |   24.2 |         21.5 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **65.3** |  504.5 |        925.2 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **84.3** |  515.5 |       1438.2 |
| Throughput median (tok/s) | **11.9** |    1.9 |          0.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.6** |   28.9 |        629.2 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.4** |   38.0 |        965.6 |
| Throughput median (tok/s) | **28.2** |   26.3 |          1.1 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **37.9** |     46.1 |         82.0 |
| TPOT median (ms)          |     22.7 | **18.5** |        113.4 |
| E2E median (ms)           | **49.1** |     56.3 |        194.2 |
| Throughput median (tok/s) | **21.4** |     18.0 |          5.2 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **25.7** |      30.2 |        501.9 |
| TPOT median (ms)          |     11.2 |   **9.3** |          9.8 |
| E2E median (ms)           |    442.0 | **376.7** |       1065.9 |
| Throughput median (tok/s) |     85.9 | **100.8** |         30.8 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          |  **35.8** |   128.6 |        434.9 |
| TPOT median (ms)          |       6.8 | **5.6** |         24.6 |
| E2E median (ms)           | **129.4** |   205.6 |        742.1 |
| Throughput median (tok/s) |  **35.0** |    34.2 |         11.9 |
| Correctness               |  **100%** |    100% |         100% |
