# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **2/5** | **2/5** |          1/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **4/5** |     1/5 |          0/5 |
| tree_of_thought  |   **5/5** |     0/5 |          0/5 |
| long_output      |   **4/5** |     1/5 |          0/5 |
| **Total**        | **20/25** |    4/25 |         1/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1033.5s (17.2m) | `5cba683` |
| sglang       |    285.4s (4.8m) | `044bb88` |
| torchinferno | **80.0s (1.3m)** | `d1935bd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    165.2 | **150.5** |        586.8 |
| TPOT median (ms)          | **59.6** |      73.0 |        588.4 |
| E2E median (ms)           |    226.7 | **219.7** |       1158.6 |
| Throughput median (tok/s) |  **6.6** |       5.4 |          1.0 |
| Correctness               |      98% |       98% |      **98%** |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **179.7** |  224.5 |        492.4 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **203.0** |  381.7 |        589.9 |
| Throughput median (tok/s) |   **4.9** |    2.6 |          1.7 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     191.7 | **181.6** |            - |
| TPOT median (ms)          |  **67.5** |     105.4 |            - |
| E2E median (ms)           | **249.0** |     296.8 |            - |
| Throughput median (tok/s) |   **5.7** |       4.3 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **61.9** |   81.4 |            - |
| TPOT median (ms)          | **28.1** |   72.2 |            - |
| E2E median (ms)           | **84.7** |  164.3 |            - |
| Throughput median (tok/s) | **14.9** |    8.7 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      87.5 | **78.9** |            - |
| TPOT median (ms)          |  **15.0** |     21.9 |            - |
| E2E median (ms)           | **646.6** |    797.7 |            - |
| Throughput median (tok/s) |  **56.7** |     42.1 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **137.2** |  143.4 |        539.6 |
| TPOT median (ms)          |  **34.0** |   54.5 |        294.2 |
| E2E median (ms)           | **282.0** |  372.0 |        874.2 |
| Throughput median (tok/s) |  **17.8** |   12.6 |          1.3 |
| Correctness               |       99% |    99% |      **99%** |
