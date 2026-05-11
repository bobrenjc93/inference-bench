# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:01 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **4/5** |     1/5 |          0/5 |
| tree_of_thought  |   **4/5** |     1/5 |          0/5 |
| long_output      |   **5/5** |     0/5 |          0/5 |
| **Total**        | **20/25** |    5/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1003.3s (16.7m) | `3f9c0c2` |
| sglang       |    274.0s (4.6m) | `2e69266` |
| torchinferno | **85.3s (1.4m)** | `af56747` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    167.8 | **148.0** |        405.8 |
| TPOT median (ms)          | **62.7** |      73.7 |        266.0 |
| E2E median (ms)           |    230.4 | **221.6** |        649.9 |
| Throughput median (tok/s) |  **6.7** |       5.3 |          2.1 |
| Correctness               |      98% |   **98%** |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **171.3** |  233.3 |        475.9 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **194.1** |  383.6 |        590.0 |
| Throughput median (tok/s) |   **5.2** |    2.6 |          1.7 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     193.2 | **166.3** |            - |
| TPOT median (ms)          |  **59.4** |     107.6 |            - |
| E2E median (ms)           | **251.5** |     267.2 |            - |
| Throughput median (tok/s) |   **5.6** |       4.8 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **63.2** |    74.5 |            - |
| TPOT median (ms)          | **27.4** |    71.1 |            - |
| E2E median (ms)           | **84.4** |   155.5 |            - |
| Throughput median (tok/s) | **14.7** |     9.1 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **74.1** |   74.7 |            - |
| TPOT median (ms)          |  **14.9** |   21.9 |            - |
| E2E median (ms)           | **625.4** |  844.0 |            - |
| Throughput median (tok/s) |  **58.4** |   42.2 |            - |
| Correctness               |  **100%** |   100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **133.9** |  139.3 |        440.8 |
| TPOT median (ms)          |  **32.9** |   54.9 |        133.0 |
| E2E median (ms)           | **277.2** |  374.4 |        619.9 |
| Throughput median (tok/s) |  **18.1** |   12.8 |          1.9 |
| Correctness               |       98% |    99% |      **99%** |
