# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **4/5** |    1/5 |          0/5 |
| multi_turn       |   **3/5** |    2/5 |          0/5 |
| tree_of_thought  |   **4/5** |    1/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **18/25** |   7/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1327.5s (22.1m) | `21943d4` |
| sglang       |    176.6s (2.9m) | `d82e339` |
| torchinferno | **47.5s (0.8m)** | `a08239a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     148.1 | **135.1** |            - |
| TPOT median (ms)          |  **54.2** |      78.3 |            - |
| E2E median (ms)           | **196.8** |     209.2 |            - |
| Throughput median (tok/s) |   **7.5** |       5.8 |            - |
| Correctness               |       98% |   **98%** |            - |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     198.4 | **197.8** |            - |
| TPOT median (ms)          |   **0.0** |       0.0 |            - |
| E2E median (ms)           | **262.1** |     347.6 |            - |
| Throughput median (tok/s) |   **3.8** |       2.9 |            - |
| Correctness               |  **100%** |      100% |            - |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     187.5 | **157.2** |            - |
| TPOT median (ms)          |  **67.8** |     102.2 |            - |
| E2E median (ms)           | **246.8** |     258.3 |            - |
| Throughput median (tok/s) |   **5.8** |       5.2 |            - |
| Correctness               |       98% |   **98%** |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **58.0** |    75.7 |            - |
| TPOT median (ms)          | **26.8** |    57.0 |            - |
| E2E median (ms)           | **78.2** |   139.3 |            - |
| Throughput median (tok/s) | **15.9** |     9.8 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      69.0 | **65.8** |            - |
| TPOT median (ms)          |  **14.6** |     22.3 |            - |
| E2E median (ms)           | **629.5** |    896.5 |            - |
| Throughput median (tok/s) |  **60.9** |     42.4 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     132.2 | **126.3** |            - |
| TPOT median (ms)          |  **32.7** |      52.0 |            - |
| E2E median (ms)           | **282.7** |     370.2 |            - |
| Throughput median (tok/s) |  **18.8** |      13.2 |            - |
| Correctness               |       99% |   **99%** |            - |
