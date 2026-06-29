# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:43 AM PT, Jun 29 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     0/4 |   **3/4** |          1/4 |
| self_consistency | **2/4** |       1/4 |          0/4 |
| multi_turn       |     0/4 |   **3/4** |          1/4 |
| tree_of_thought  |     0/4 |   **3/4** |          1/4 |
| long_output      |     0/4 |   **4/4** |          0/4 |
| **Total**        |    2/20 | **14/20** |         3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |
| torchinferno |     0.0s (0.0m) | `cdf5c65` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 279.3 | **121.6** |        170.1 |
| TPOT median (ms)          |  99.1 |      83.4 |     **48.5** |
| E2E median (ms)           | 354.6 | **205.6** |        213.8 |
| Throughput median (tok/s) |   3.9 |   **5.8** |          5.3 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     251.7 | **200.6** |        303.3 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **303.7** |     387.5 |        343.7 |
| Throughput median (tok/s) |   **3.3** |       2.6 |          2.9 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 266.5 | **152.4** |        318.4 |
| TPOT median (ms)          | 105.5 |     118.5 |     **62.3** |
| E2E median (ms)           | 349.7 | **272.6** |        370.8 |
| Throughput median (tok/s) |   4.2 |   **4.8** |          3.7 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 123.2 |  **65.0** |        314.0 |
| TPOT median (ms)          |  82.7 |      74.0 |     **47.9** |
| E2E median (ms)           | 183.7 | **150.6** |        344.3 |
| Throughput median (tok/s) |   6.8 |   **9.4** |          4.2 |
| Correctness               |   97% |       97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   92.0 |  **60.2** |        272.5 |
| TPOT median (ms)          |   26.7 |  **24.9** |         25.2 |
| E2E median (ms)           | 1075.5 | **924.4** |       1271.9 |
| Throughput median (tok/s) |   33.8 |  **38.2** |         31.2 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 202.5 | **120.0** |        275.7 |
| TPOT median (ms)          |  62.8 |      60.2 |     **36.8** |
| E2E median (ms)           | 453.4 | **388.1** |        508.9 |
| Throughput median (tok/s) |  10.4 |  **12.2** |          9.5 |
| Correctness               |   99% |       99% |          99% |
