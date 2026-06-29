# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:55 AM PT, Jun 29 2026

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
| torchinferno |     0.0s (0.0m) | `23395db` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 234.1 | **123.8** |        166.5 |
| TPOT median (ms)          |  89.6 |      73.9 |     **50.2** |
| E2E median (ms)           | 312.6 | **199.3** |        210.1 |
| Throughput median (tok/s) |   5.0 |   **6.2** |          5.5 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     244.1 | **216.7** |        358.9 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **299.4** |     375.9 |        394.9 |
| Throughput median (tok/s) |   **3.3** |       2.7 |          2.5 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 256.7 | **167.1** |        308.0 |
| TPOT median (ms)          |  93.5 |     127.6 |     **66.6** |
| E2E median (ms)           | 361.6 | **288.1** |        368.2 |
| Throughput median (tok/s) |   4.2 |   **4.5** |          3.5 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 123.9 |  **62.1** |        282.9 |
| TPOT median (ms)          |  81.7 |      66.1 |     **46.7** |
| E2E median (ms)           | 186.3 | **140.7** |        324.2 |
| Throughput median (tok/s) |   6.8 |   **9.8** |          4.5 |
| Correctness               |   97% |       97% |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   89.1 |  **61.6** |        296.1 |
| TPOT median (ms)          |   26.5 |  **24.5** |         25.1 |
| E2E median (ms)           | 1082.9 | **911.6** |       1246.8 |
| Throughput median (tok/s) |   34.7 |  **38.2** |         30.7 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 189.6 | **126.3** |        282.5 |
| TPOT median (ms)          |  58.3 |      58.4 |     **37.7** |
| E2E median (ms)           | 448.6 | **383.1** |        508.8 |
| Throughput median (tok/s) |  10.8 |  **12.3** |          9.3 |
| Correctness               |   99% |       99% |          98% |
