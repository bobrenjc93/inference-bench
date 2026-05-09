# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:14 AM PT, May 9 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     2/5 |   **3/5** |          0/5 |
| self_consistency | **5/5** |       0/5 |          0/5 |
| multi_turn       |     2/5 |   **3/5** |          0/5 |
| tree_of_thought  |     1/5 |   **4/5** |          0/5 |
| long_output      |     1/5 |   **4/5** |          0/5 |
| **Total**        |   11/25 | **14/25** |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |   837.6s (14.0m) |
| sglang       |    139.7s (2.3m) |
| torchinferno | **38.3s (0.6m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     52.7 | **30.7** |         37.4 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     67.5 | **41.0** |         49.2 |
| Throughput median (tok/s) |     14.8 | **24.4** |         20.3 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **172.9** |  469.3 |        524.0 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **188.8** |  482.7 |        707.2 |
| Throughput median (tok/s) |   **5.3** |    2.1 |          1.4 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     48.5 | **30.8** |        306.5 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     65.0 | **41.4** |        383.3 |
| Throughput median (tok/s) |     15.4 | **24.2** |          2.6 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     87.2 | **41.4** |         76.2 |
| TPOT median (ms)          |     36.8 | **22.5** |         89.4 |
| E2E median (ms)           |    107.2 | **54.4** |        161.0 |
| Throughput median (tok/s) |      9.6 | **18.5** |          6.3 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |     47.7 |  **32.2** |        923.1 |
| TPOT median (ms)          |     16.9 |  **11.9** |         13.3 |
| E2E median (ms)           |    674.0 | **471.2** |       1518.7 |
| Throughput median (tok/s) |     56.4 |  **80.6** |         22.0 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **81.8** |     120.9 |        373.5 |
| TPOT median (ms)          |     10.7 |   **6.9** |         20.6 |
| E2E median (ms)           |    220.5 | **218.1** |        563.9 |
| Throughput median (tok/s) |     20.3 |  **29.9** |         10.5 |
| Correctness               | **100%** |      100% |         100% |
