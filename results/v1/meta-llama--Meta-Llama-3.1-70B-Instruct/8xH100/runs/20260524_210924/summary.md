# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 PM PT, May 24 2026

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
| torchinferno |     301.9s (5.0m) | `9f91b40` |
| vllm         |   1236.9s (20.6m) | `d0a100c` |
| sglang       | **201.7s (3.4m)** | `fd94bd3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        347.4 |    159.2 | **140.1** |
| TPOT median (ms)          |        151.5 | **55.7** |      72.4 |
| E2E median (ms)           |        464.4 |    214.4 | **208.8** |
| Throughput median (tok/s) |          2.9 |  **6.9** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        263.5 | **194.5** |  200.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        338.2 | **231.9** |  341.6 |
| Throughput median (tok/s) |          3.0 |   **4.3** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        878.4 |     173.4 | **152.9** |
| TPOT median (ms)          |        175.3 |  **59.2** |     108.4 |
| E2E median (ms)           |        989.2 | **225.8** |     254.2 |
| Throughput median (tok/s) |          1.4 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        385.2 | **58.8** |   78.9 |
| TPOT median (ms)          |        133.0 | **26.9** |   68.0 |
| E2E median (ms)           |        488.8 | **80.1** |  157.8 |
| Throughput median (tok/s) |          2.9 | **15.5** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        979.2 |      71.1 | **63.8** |
| TPOT median (ms)          |         18.3 |  **14.9** |     22.2 |
| E2E median (ms)           |       1671.0 | **610.2** |    812.5 |
| Throughput median (tok/s) |         18.9 |  **58.9** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        570.7 |     131.4 | **127.3** |
| TPOT median (ms)          |         95.6 |  **31.4** |      54.2 |
| E2E median (ms)           |        790.3 | **272.5** |     355.0 |
| Throughput median (tok/s) |          5.8 |  **18.4** |      13.1 |
| Correctness               |          98% |       98% |       98% |
