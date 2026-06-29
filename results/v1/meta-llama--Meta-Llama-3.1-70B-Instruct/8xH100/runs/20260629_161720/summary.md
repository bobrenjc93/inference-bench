# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:17 AM PT, Jun 29 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     0/4 |       2/4 |          2/4 |
| self_consistency | **2/4** |       0/4 |          1/4 |
| multi_turn       |     0/4 |   **3/4** |          1/4 |
| tree_of_thought  |     0/4 |   **3/4** |          1/4 |
| long_output      |     0/4 |   **4/4** |          0/4 |
| **Total**        |    2/20 | **12/20** |         5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |
| torchinferno |     0.0s (0.0m) | `8bf4c1c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 222.5 | **128.9** |        164.2 |
| TPOT median (ms)          |  89.6 |      78.4 |     **48.7** |
| E2E median (ms)           | 302.3 |     205.7 |    **204.9** |
| Throughput median (tok/s) |   5.4 |   **5.8** |          5.6 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |     235.2 |  217.9 |    **213.3** |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **286.5** |  373.3 |        325.9 |
| Throughput median (tok/s) |   **3.5** |    2.7 |          3.1 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 290.6 | **154.0** |        320.2 |
| TPOT median (ms)          | 103.0 |     115.1 |     **58.9** |
| E2E median (ms)           | 383.2 | **274.7** |        380.3 |
| Throughput median (tok/s) |   3.7 |   **4.9** |          3.5 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 121.3 |  **60.5** |        270.2 |
| TPOT median (ms)          |  81.9 |      74.6 |     **47.8** |
| E2E median (ms)           | 181.7 | **149.1** |        314.0 |
| Throughput median (tok/s) |   7.0 |   **9.4** |          4.3 |
| Correctness               |   97% |       97% |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          |  86.9 |  **63.3** |        283.0 |
| TPOT median (ms)          |  25.3 |  **24.6** |         25.3 |
| E2E median (ms)           | 984.6 | **915.5** |       1193.3 |
| Throughput median (tok/s) |  36.0 |  **38.5** |         31.0 |
| Correctness               |  100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 191.3 | **124.9** |        250.2 |
| TPOT median (ms)          |  60.0 |      58.5 |     **36.1** |
| E2E median (ms)           | 427.7 | **383.7** |        483.7 |
| Throughput median (tok/s) |  11.1 |  **12.3** |          9.5 |
| Correctness               |   98% |       99% |          98% |
