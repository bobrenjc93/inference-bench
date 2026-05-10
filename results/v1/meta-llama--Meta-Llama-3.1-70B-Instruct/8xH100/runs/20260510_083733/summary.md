# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **4/5** |    1/5 |          0/5 |
| self_consistency |   **4/5** |    1/5 |          0/5 |
| multi_turn       |   **3/5** |    2/5 |          0/5 |
| tree_of_thought  |   **4/5** |    1/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **19/25** |   6/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1423.9s (23.7m) |
| sglang       |    198.1s (3.3m) |
| torchinferno | **41.5s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     149.3 | **133.6** |            - |
| TPOT median (ms)          |  **55.2** |      75.2 |            - |
| E2E median (ms)           | **199.0** |     205.1 |            - |
| Throughput median (tok/s) |   **7.4** |       5.9 |            - |
| Correctness               |   **98%** |       98% |            - |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     198.8 | **197.2** |            - |
| TPOT median (ms)          |   **0.0** |       0.0 |            - |
| E2E median (ms)           | **264.7** |     340.2 |            - |
| Throughput median (tok/s) |   **3.8** |       2.9 |            - |
| Correctness               |  **100%** |      100% |            - |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     187.1 | **162.7** |            - |
| TPOT median (ms)          |  **65.3** |     102.9 |            - |
| E2E median (ms)           | **243.3** |     261.6 |            - |
| Throughput median (tok/s) |   **5.8** |       5.1 |            - |
| Correctness               |       98% |   **98%** |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **57.6** |    75.5 |            - |
| TPOT median (ms)          | **26.9** |    58.7 |            - |
| E2E median (ms)           | **78.0** |   142.0 |            - |
| Throughput median (tok/s) | **16.0** |     9.8 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      65.0 | **64.4** |            - |
| TPOT median (ms)          |  **14.6** |     22.3 |            - |
| E2E median (ms)           | **625.7** |    900.2 |            - |
| Throughput median (tok/s) |  **61.3** |     42.4 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     131.6 | **126.7** |            - |
| TPOT median (ms)          |  **32.4** |      51.8 |            - |
| E2E median (ms)           | **282.1** |     369.8 |            - |
| Throughput median (tok/s) |  **18.9** |      13.2 |            - |
| Correctness               |       99% |   **99%** |            - |
