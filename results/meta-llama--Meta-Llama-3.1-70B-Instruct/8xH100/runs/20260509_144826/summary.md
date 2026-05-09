# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2026-05-09T14:27:55.415009

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
| vllm         |   711.5s (11.9m) |
| sglang       |     94.7s (1.6m) |
| torchinferno | **38.1s (0.6m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.8 | **30.8** |         37.3 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     45.5 | **41.4** |         49.1 |
| Throughput median (tok/s) |     22.0 | **24.2** |         20.4 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **66.5** |  430.7 |         89.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **88.1** |  440.7 |        107.3 |
| Throughput median (tok/s) | **11.3** |    2.3 |          9.5 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **30.3** |     31.0 |        185.9 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     43.6 | **41.6** |        260.4 |
| Throughput median (tok/s) |     23.0 | **24.0** |          3.9 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     42.8 | **40.8** |         47.5 |
| TPOT median (ms)          |     28.2 | **21.6** |         30.8 |
| E2E median (ms)           |     57.9 | **53.9** |         76.7 |
| Throughput median (tok/s) |     17.7 | **18.7** |         13.4 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **31.5** |      32.5 |        180.3 |
| TPOT median (ms)          |     14.0 |  **11.9** |         11.9 |
| E2E median (ms)           |    548.9 | **471.0** |        623.9 |
| Throughput median (tok/s) |     69.2 |  **80.6** |         60.8 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **40.6** |    113.2 |        108.0 |
| TPOT median (ms)          |       8.4 |  **6.7** |          8.5 |
| E2E median (ms)           | **156.8** |    209.7 |        223.5 |
| Throughput median (tok/s) |      28.6 | **29.9** |         21.6 |
| Correctness               |  **100%** |     100% |         100% |
