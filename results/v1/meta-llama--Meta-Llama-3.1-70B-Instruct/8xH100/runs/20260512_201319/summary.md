# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     443.2s (7.4m) | `708195d` |
| vllm         |   1027.0s (17.1m) | `0ce6613` |
| sglang       | **160.1s (2.7m)** | `52d4c69` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    164.1 | **137.0** |
| TPOT median (ms)          |            - | **58.0** |      74.3 |
| E2E median (ms)           |            - |    218.2 | **204.1** |
| Throughput median (tok/s) |            - |  **6.4** |       5.9 |
| Correctness               |            - |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **204.1** |  220.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **225.8** |  372.2 |
| Throughput median (tok/s) |            - |   **4.4** |    2.7 |
| Correctness               |            - |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     180.2 | **154.7** |
| TPOT median (ms)          |            - |  **56.1** |      98.8 |
| E2E median (ms)           |            - | **234.6** |     252.6 |
| Throughput median (tok/s) |            - |   **5.9** |       5.3 |
| Correctness               |            - |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.4** |   77.3 |
| TPOT median (ms)          |            - | **28.1** |   50.4 |
| E2E median (ms)           |            - | **80.1** |  137.6 |
| Throughput median (tok/s) |            - | **15.5** |    9.7 |
| Correctness               |            - |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      72.1 | **65.8** |
| TPOT median (ms)          |            - |  **15.0** |     22.2 |
| E2E median (ms)           |            - | **624.3** |    832.5 |
| Throughput median (tok/s) |            - |  **58.6** |     42.4 |
| Correctness               |            - |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     136.0 | **131.0** |
| TPOT median (ms)          |            - |  **31.5** |      49.1 |
| E2E median (ms)           |            - | **276.6** |     359.8 |
| Throughput median (tok/s) |            - |  **18.2** |      13.2 |
| Correctness               |            - |       99% |       99% |
