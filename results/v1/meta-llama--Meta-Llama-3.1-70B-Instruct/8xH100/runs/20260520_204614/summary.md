# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 PM PT, May 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **93.1s (1.6m)** | `9f91b40` |
| vllm         |  1254.6s (20.9m) | `2a43b40` |
| sglang       |    191.9s (3.2m) | `dac7876` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        306.9 |     167.0 | **149.0** |
| TPOT median (ms)          |        161.1 |  **58.3** |      76.0 |
| E2E median (ms)           |        422.5 | **217.3** |     220.9 |
| Throughput median (tok/s) |          3.3 |   **6.6** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        285.5 | **201.3** |  218.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        333.7 | **225.7** |  367.6 |
| Throughput median (tok/s) |          3.0 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        906.9 |     193.1 | **166.4** |
| TPOT median (ms)          |        105.5 |  **62.1** |     105.7 |
| E2E median (ms)           |       1009.2 | **251.8** |     278.0 |
| Throughput median (tok/s) |          1.3 |   **5.7** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        391.4 | **60.9** |   79.1 |
| TPOT median (ms)          |        137.6 | **27.4** |   71.6 |
| E2E median (ms)           |        505.4 | **81.5** |  160.7 |
| Throughput median (tok/s) |          2.6 | **14.9** |    8.8 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1198.5 |  **74.4** |   74.6 |
| TPOT median (ms)          |         16.8 |  **15.0** |   22.1 |
| E2E median (ms)           |       1851.2 | **656.8** |  816.0 |
| Throughput median (tok/s) |         17.8 |  **57.6** |   42.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        617.8 |     139.3 | **137.6** |
| TPOT median (ms)          |         84.2 |  **32.6** |      55.1 |
| E2E median (ms)           |        824.4 | **286.6** |     368.6 |
| Throughput median (tok/s) |          5.6 |  **17.8** |      12.7 |
| Correctness               |          98% |       99% |       99% |
