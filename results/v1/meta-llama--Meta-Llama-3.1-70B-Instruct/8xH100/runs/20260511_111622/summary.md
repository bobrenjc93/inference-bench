# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:02 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **4/5** |    1/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **21/25** |   4/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1284.0s (21.4m) | `17ed5e6` |
| sglang       |    190.3s (3.2m) | `6d30b57` |
| torchinferno | **42.8s (0.7m)** | `796f04c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    159.8 | **140.8** |        716.1 |
| TPOT median (ms)          | **58.1** |      72.2 |        302.3 |
| E2E median (ms)           |    209.8 | **207.5** |       1033.0 |
| Throughput median (tok/s) |  **6.7** |       5.8 |          1.4 |
| Correctness               |  **98%** |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **183.6** |  206.2 |        398.2 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **204.7** |  352.3 |        488.5 |
| Throughput median (tok/s) |   **4.9** |    2.8 |          2.0 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     168.5 | **160.2** |        660.4 |
| TPOT median (ms)          |  **57.7** |     111.1 |        333.4 |
| E2E median (ms)           | **215.7** |     271.2 |       1021.3 |
| Throughput median (tok/s) |   **6.3** |       4.9 |          1.3 |
| Correctness               |   **98%** |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **58.0** |   77.2 |            - |
| TPOT median (ms)          | **27.0** |   64.6 |            - |
| E2E median (ms)           | **78.3** |  155.4 |            - |
| Throughput median (tok/s) | **15.9** |    9.2 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      74.9 | **69.3** |            - |
| TPOT median (ms)          |  **15.1** |     22.4 |            - |
| E2E median (ms)           | **614.2** |    853.4 |            - |
| Throughput median (tok/s) |  **58.2** |     41.9 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **129.0** |  130.8 |        591.5 |
| TPOT median (ms)          |  **31.6** |   54.1 |        211.9 |
| E2E median (ms)           | **264.5** |  367.9 |        847.6 |
| Throughput median (tok/s) |  **18.4** |   12.9 |          1.6 |
| Correctness               |   **99%** |    99% |          99% |
