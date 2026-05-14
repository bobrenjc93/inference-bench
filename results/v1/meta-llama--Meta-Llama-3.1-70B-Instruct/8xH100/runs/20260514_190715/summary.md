# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:07 AM PT, May 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     312.8s (5.2m) | `58e4246` |
| vllm         |   1114.2s (18.6m) | `9898f94` |
| sglang       | **160.1s (2.7m)** | `88d3ed7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        313.3 |    164.3 | **133.6** |
| TPOT median (ms)          |        166.8 | **62.9** |      76.0 |
| E2E median (ms)           |        406.1 |    216.3 | **204.1** |
| Throughput median (tok/s) |          3.6 |  **6.7** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.4 | **193.7** |  205.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        329.8 | **248.0** |  334.0 |
| Throughput median (tok/s) |          3.0 |   **4.0** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        615.7 |     171.2 | **153.7** |
| TPOT median (ms)          |        179.7 |  **50.1** |     100.3 |
| E2E median (ms)           |        753.2 | **225.9** |     248.5 |
| Throughput median (tok/s) |          1.9 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        365.1 | **58.8** |   73.8 |
| TPOT median (ms)          |        262.8 | **27.4** |   55.6 |
| E2E median (ms)           |        582.6 | **79.6** |  144.7 |
| Throughput median (tok/s) |          2.2 | **15.4** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        576.4 |  **64.6** |   65.1 |
| TPOT median (ms)          |         16.2 |  **14.9** |   22.0 |
| E2E median (ms)           |       1265.8 | **606.4** |  823.7 |
| Throughput median (tok/s) |         25.9 |  **59.6** |   42.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        433.0 |     130.5 | **126.3** |
| TPOT median (ms)          |        125.1 |  **31.1** |      50.8 |
| E2E median (ms)           |        667.5 | **275.2** |     351.0 |
| Throughput median (tok/s) |          7.3 |  **18.4** |      13.4 |
| Correctness               |          99% |       99% |       98% |
