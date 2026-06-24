# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:52 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.9s (0.1m)** | `76107de` |
| vllm         |    86.2s (1.4m) | `1cd3e0e` |
| sglang       |     9.0s (0.1m) | `4a4f063` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        167.9 | **130.9** |  159.2 |
| TPOT median (ms)          |         53.1 |  **52.2** |   92.3 |
| E2E median (ms)           |        217.9 | **176.3** |  248.8 |
| Throughput median (tok/s) |          5.5 |   **7.7** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        327.8 |     238.4 | **214.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        415.0 | **267.2** |     416.9 |
| Throughput median (tok/s) |          2.4 |   **3.7** |       2.4 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        479.1 | **169.3** |  172.3 |
| TPOT median (ms)          |         64.8 |  **55.4** |  114.1 |
| E2E median (ms)           |        586.2 | **216.8** |  287.3 |
| Throughput median (tok/s) |          2.1 |   **6.3** |    4.5 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        277.1 | **72.5** |   76.9 |
| TPOT median (ms)          |         50.0 | **35.1** |   86.2 |
| E2E median (ms)           |        330.2 | **99.2** |  173.2 |
| Throughput median (tok/s) |          4.4 | **12.2** |    8.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        430.3 |  **79.3** |   80.3 |
| TPOT median (ms)          |         25.1 |  **18.8** |   27.9 |
| E2E median (ms)           |       1508.1 | **766.3** | 1010.1 |
| Throughput median (tok/s) |         25.4 |  **47.4** |   33.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        336.4 | **138.1** |  140.7 |
| TPOT median (ms)          |         38.6 |  **32.3** |   64.1 |
| E2E median (ms)           |        611.5 | **305.2** |  427.3 |
| Throughput median (tok/s) |          8.0 |  **15.5** |   10.7 |
| Correctness               |          98% |       98% |    99% |
