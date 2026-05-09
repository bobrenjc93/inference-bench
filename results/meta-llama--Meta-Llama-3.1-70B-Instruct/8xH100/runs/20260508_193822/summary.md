# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 2026-05-08T19:13:16.021135

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
| vllm         |   916.1s (15.3m) |
| sglang       |     85.7s (1.4m) |
| torchinferno | **38.3s (0.6m)** |

## Per-Benchmark Results

### few_shot

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.0 | **30.5** |        308.2 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.7 | **41.6** |        571.6 |
| Throughput median (tok/s) |     22.4 | **24.0** |          1.7 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **62.8** |  475.5 |       1724.4 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **84.9** |  484.3 |       2038.7 |
| Throughput median (tok/s) | **11.8** |    2.1 |          0.5 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.4 | **31.0** |        356.9 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.3 | **41.8** |        615.9 |
| Throughput median (tok/s) |     22.6 | **23.9** |          1.6 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     51.0 | **39.9** |        656.1 |
| TPOT median (ms)          |     27.1 | **25.0** |        249.3 |
| E2E median (ms)           |     70.8 | **52.8** |        748.7 |
| Throughput median (tok/s) |     15.9 | **19.0** |          1.3 |
| Correctness               | **100%** |     100% |         100% |

### long_output

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **31.3** |      32.0 |        333.1 |
| TPOT median (ms)          |     14.0 |  **11.9** |        268.2 |
| E2E median (ms)           |    547.8 | **470.9** |      10105.9 |
| Throughput median (tok/s) |     69.3 |  **80.6** |          3.7 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **41.5** |    121.8 |        675.7 |
| TPOT median (ms)          |       8.2 |  **7.4** |        103.5 |
| E2E median (ms)           | **158.5** |    218.3 |       2816.2 |
| Throughput median (tok/s) |      28.4 | **29.9** |          1.8 |
| Correctness               |  **100%** |     100% |         100% |
