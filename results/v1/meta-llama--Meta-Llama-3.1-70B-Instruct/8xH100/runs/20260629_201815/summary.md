# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:18 PM PT, Jun 29 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     0/4 |       2/4 |          2/4 |
| self_consistency | **2/4** |       1/4 |          0/4 |
| multi_turn       |     0/4 |   **3/4** |          1/4 |
| tree_of_thought  |     0/4 |   **3/4** |          1/4 |
| long_output      |     0/4 |   **3/4** |          1/4 |
| **Total**        |    2/20 | **12/20** |         5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |
| torchinferno |     0.0s (0.0m) | `36c5c9a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 248.6 | **122.5** |        164.4 |
| TPOT median (ms)          |  86.8 |      82.7 |     **48.6** |
| E2E median (ms)           | 321.3 |     207.4 |    **205.9** |
| Throughput median (tok/s) |   4.5 |   **5.9** |          5.7 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     257.3 | **220.6** |        330.0 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **314.4** |     378.8 |        361.7 |
| Throughput median (tok/s) |   **3.2** |       2.6 |          2.8 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 266.9 | **158.7** |        328.9 |
| TPOT median (ms)          |  96.9 |     105.2 |     **62.9** |
| E2E median (ms)           | 354.1 | **274.2** |        385.2 |
| Throughput median (tok/s) |   4.3 |   **4.9** |          3.1 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 128.2 |  **62.0** |        296.5 |
| TPOT median (ms)          |  82.4 |      75.4 |     **47.2** |
| E2E median (ms)           | 187.6 | **147.9** |        313.6 |
| Throughput median (tok/s) |   6.7 |   **9.3** |          4.7 |
| Correctness               |   97% |       97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   96.5 |  **64.0** |        274.9 |
| TPOT median (ms)          |   28.7 |      24.2 |     **23.9** |
| E2E median (ms)           | 1097.0 | **921.6** |       1171.8 |
| Throughput median (tok/s) |   32.2 |  **39.1** |         32.5 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 199.5 | **125.6** |        278.9 |
| TPOT median (ms)          |  58.9 |      57.5 |     **36.5** |
| E2E median (ms)           | 454.9 | **386.0** |        487.7 |
| Throughput median (tok/s) |  10.2 |  **12.4** |          9.8 |
| Correctness               |   99% |       99% |          98% |
