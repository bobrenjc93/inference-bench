# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 6:19 AM PT, May 8 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     2/5 |   **3/5** |          0/5 |
| self_consistency | **5/5** |       0/5 |          0/5 |
| multi_turn       |     2/5 |   **3/5** |          0/5 |
| tree_of_thought  |     1/5 |   **4/5** |          0/5 |
| long_output      |     2/5 |   **3/5** |          0/5 |
| **Total**        |   12/25 | **13/25** |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |   807.8s (13.5m) |
| sglang       |     87.5s (1.5m) |
| torchinferno | **39.2s (0.7m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.7 | **30.7** |         94.5 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     45.4 | **41.7** |        173.5 |
| Throughput median (tok/s) |     22.0 | **24.0** |          5.8 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **69.3** |  427.8 |       1143.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **91.4** |  437.9 |       1459.3 |
| Throughput median (tok/s) | **10.9** |    2.3 |          0.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.2 | **30.9** |        356.8 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.8 | **41.8** |        627.4 |
| Throughput median (tok/s) |     22.3 | **23.9** |          1.6 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     45.6 | **40.3** |        318.3 |
| TPOT median (ms)          |     29.1 | **22.1** |        353.7 |
| E2E median (ms)           |     60.0 | **53.7** |        588.6 |
| Throughput median (tok/s) |     17.1 | **18.8** |          2.3 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **31.4** |      32.1 |        326.7 |
| TPOT median (ms)          |     14.1 |  **12.1** |        271.1 |
| E2E median (ms)           |    550.6 | **479.6** |      10338.5 |
| Throughput median (tok/s) |     69.0 |  **79.2** |          3.7 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **41.9** |    112.3 |        447.9 |
| TPOT median (ms)          |       8.6 |  **6.8** |        125.0 |
| E2E median (ms)           | **158.4** |    210.9 |       2637.4 |
| Throughput median (tok/s) |      28.3 | **29.6** |          2.8 |
| Correctness               |  **100%** |     100% |         100% |
