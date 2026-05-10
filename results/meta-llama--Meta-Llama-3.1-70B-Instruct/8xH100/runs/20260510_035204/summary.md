# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 PM PT, May 9 2026

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
| vllm         |  1356.9s (22.6m) |
| sglang       |    178.8s (3.0m) |
| torchinferno | **44.0s (0.7m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **23.4** |   30.9 |         25.9 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **33.5** |   40.9 |         38.6 |
| Throughput median (tok/s) | **29.8** |   24.5 |         25.9 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **55.1** |  519.0 |        308.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **70.9** |  528.6 |        389.2 |
| Throughput median (tok/s) | **14.1** |    1.9 |          2.6 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **23.2** |   31.6 |         24.4 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **33.3** |   40.6 |         38.0 |
| Throughput median (tok/s) | **30.0** |   24.6 |         26.3 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **30.3** |    48.4 |         46.6 |
| TPOT median (ms)          |     22.2 | **9.4** |         36.6 |
| E2E median (ms)           | **47.5** |    58.5 |         81.1 |
| Throughput median (tok/s) | **21.8** |    17.3 |         12.7 |
| Correctness               | **100%** |    100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **24.0** |      32.2 |         25.0 |
| TPOT median (ms)          |     10.2 |   **9.4** |         10.0 |
| E2E median (ms)           |    399.6 | **378.1** |        394.2 |
| Throughput median (tok/s) |     95.0 | **100.4** |         96.3 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          |  **31.2** |   132.4 |         86.0 |
| TPOT median (ms)          |       6.5 | **3.7** |          9.3 |
| E2E median (ms)           | **117.0** |   209.4 |        188.2 |
| Throughput median (tok/s) |  **38.2** |    33.7 |         32.8 |
| Correctness               |  **100%** |    100% |         100% |
