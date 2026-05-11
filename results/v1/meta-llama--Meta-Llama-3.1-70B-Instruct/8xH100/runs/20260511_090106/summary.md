# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:02 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **3/5** |     2/5 |          0/5 |
| tree_of_thought  |   **5/5** |     0/5 |          0/5 |
| long_output      |   **4/5** |     1/5 |          0/5 |
| **Total**        | **19/25** |    6/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1394.6s (23.2m) | `f9f770c` |
| sglang       |    182.8s (3.0m) | `c027ae6` |
| torchinferno | **42.7s (0.7m)** | `695b0f6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    166.0 | **136.9** |        519.4 |
| TPOT median (ms)          | **61.0** |      75.8 |        536.2 |
| E2E median (ms)           |    222.2 | **210.5** |       1024.5 |
| Throughput median (tok/s) |  **6.4** |       5.7 |          1.2 |
| Correctness               |      98% |   **98%** |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **200.6** |  213.5 |        504.6 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **271.9** |  357.6 |        607.4 |
| Throughput median (tok/s) |   **3.7** |    2.8 |          1.6 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     168.3 | **160.6** |            - |
| TPOT median (ms)          |  **58.2** |     100.2 |            - |
| E2E median (ms)           | **218.7** |     260.0 |            - |
| Throughput median (tok/s) |   **6.4** |       5.2 |            - |
| Correctness               |       98% |   **98%** |            - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **57.9** |   77.3 |            - |
| TPOT median (ms)          | **26.7** |   62.4 |            - |
| E2E median (ms)           | **78.3** |  149.6 |            - |
| Throughput median (tok/s) | **15.9** |    9.6 |            - |
| Correctness               |  **97%** |    96% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      72.0 | **67.2** |            - |
| TPOT median (ms)          |  **15.1** |     22.1 |            - |
| E2E median (ms)           | **629.0** |    828.0 |            - |
| Throughput median (tok/s) |  **58.9** |     42.6 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     132.9 | **131.1** |        512.0 |
| TPOT median (ms)          |  **32.2** |      52.1 |        268.1 |
| E2E median (ms)           | **284.0** |     361.1 |        815.9 |
| Throughput median (tok/s) |  **18.3** |      13.2 |          1.4 |
| Correctness               |       98% |       98% |      **99%** |
