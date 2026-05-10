# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **4/5** |    1/5 |          0/5 |
| self_consistency |   **4/5** |    1/5 |          0/5 |
| multi_turn       |   **4/5** |    1/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **21/25** |   4/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1367.4s (22.8m) |
| sglang       |    190.7s (3.2m) |
| torchinferno | **43.1s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     147.5 | **134.6** |        379.2 |
| TPOT median (ms)          |  **52.6** |      73.9 |        164.1 |
| E2E median (ms)           | **194.1** |     204.8 |        557.5 |
| Throughput median (tok/s) |   **7.5** |       5.9 |          2.4 |
| Correctness               |   **98%** |       98% |          98% |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     251.8 | **198.3** |            - |
| TPOT median (ms)          |   **0.0** |       0.0 |            - |
| E2E median (ms)           | **302.0** |     343.6 |            - |
| Throughput median (tok/s) |   **3.3** |       2.9 |            - |
| Correctness               |  **100%** |      100% |            - |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     189.8 | **158.3** |            - |
| TPOT median (ms)          |  **67.4** |     102.7 |            - |
| E2E median (ms)           | **249.9** |     256.6 |            - |
| Throughput median (tok/s) |   **5.7** |       5.2 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **58.1** |   76.3 |            - |
| TPOT median (ms)          | **27.0** |   59.2 |            - |
| E2E median (ms)           | **78.6** |  139.8 |            - |
| Throughput median (tok/s) | **16.0** |   10.2 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      67.5 | **65.4** |            - |
| TPOT median (ms)          |  **14.6** |     22.0 |            - |
| E2E median (ms)           | **624.5** |    886.2 |            - |
| Throughput median (tok/s) |  **61.1** |     42.7 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     142.9 | **126.6** |        379.2 |
| TPOT median (ms)          |  **32.3** |      51.6 |        164.1 |
| E2E median (ms)           | **289.9** |     366.2 |        557.5 |
| Throughput median (tok/s) |  **18.7** |      13.4 |          2.4 |
| Correctness               |   **99%** |       99% |          98% |
