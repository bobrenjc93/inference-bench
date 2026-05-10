# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:42 PM PT, May 9 2026

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
| vllm         |  1201.9s (20.0m) |
| sglang       |    174.7s (2.9m) |
| torchinferno | **48.5s (0.8m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.9** |   31.2 |         35.9 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.9** |   39.9 |         47.8 |
| Throughput median (tok/s) | **27.9** |   25.1 |         20.9 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **166.4** |  505.6 |        282.0 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **183.9** |  519.4 |        363.4 |
| Throughput median (tok/s) |   **5.4** |    1.9 |          2.8 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.6** |   29.6 |         34.7 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.5** |   38.7 |         47.8 |
| Throughput median (tok/s) | **28.2** |   25.9 |         20.9 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **37.1** |     46.4 |         45.5 |
| TPOT median (ms)          |     25.9 | **18.0** |         36.6 |
| E2E median (ms)           | **50.5** |     56.3 |         81.3 |
| Throughput median (tok/s) | **20.3** |     17.8 |         12.8 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **25.1** |      30.2 |        320.8 |
| TPOT median (ms)          |     11.3 |   **9.4** |         10.1 |
| E2E median (ms)           |    442.3 | **377.8** |        695.6 |
| Throughput median (tok/s) |     85.9 | **100.5** |         54.5 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **55.6** |    128.6 |        143.8 |
| TPOT median (ms)          |       7.4 |  **5.5** |          9.3 |
| E2E median (ms)           | **149.6** |    206.4 |        247.2 |
| Throughput median (tok/s) |      33.5 | **34.2** |         22.4 |
| Correctness               |  **100%** |     100% |         100% |
