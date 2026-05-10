# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, May 10 2026

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

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1313.7s (21.9m) |
| sglang       |    173.7s (2.9m) |
| torchinferno | **41.3s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     145.7 | **136.5** |            - |
| TPOT median (ms)          |  **51.8** |      75.7 |            - |
| E2E median (ms)           | **193.0** |     208.8 |            - |
| Throughput median (tok/s) |   **7.5** |       5.8 |            - |
| Correctness               |       98% |   **98%** |            - |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     207.4 | **198.7** |            - |
| TPOT median (ms)          |   **0.0** |       0.0 |            - |
| E2E median (ms)           | **269.5** |     344.5 |            - |
| Throughput median (tok/s) |   **3.7** |       2.9 |            - |
| Correctness               |  **100%** |      100% |            - |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     182.1 | **158.6** |            - |
| TPOT median (ms)          |  **67.5** |     103.0 |            - |
| E2E median (ms)           | **244.8** |     257.0 |            - |
| Throughput median (tok/s) |   **5.8** |       5.2 |            - |
| Correctness               |       98% |   **98%** |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **57.5** |    76.9 |            - |
| TPOT median (ms)          | **26.6** |    58.7 |            - |
| E2E median (ms)           | **77.8** |   142.2 |            - |
| Throughput median (tok/s) | **16.1** |     9.9 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      71.4 | **64.2** |            - |
| TPOT median (ms)          |  **14.5** |     22.3 |            - |
| E2E median (ms)           | **628.7** |    904.5 |            - |
| Throughput median (tok/s) |  **60.8** |     42.3 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     132.8 | **127.0** |            - |
| TPOT median (ms)          |  **32.1** |      51.9 |            - |
| E2E median (ms)           | **282.8** |     371.4 |            - |
| Throughput median (tok/s) |  **18.8** |      13.2 |            - |
| Correctness               |       99% |   **99%** |            - |
