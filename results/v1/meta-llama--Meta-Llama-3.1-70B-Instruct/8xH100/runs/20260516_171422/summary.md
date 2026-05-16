# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:01 AM PT, May 16 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **83.9s (1.4m)** | `db749af` |
| vllm         |  1001.0s (16.7m) | `8a56da3` |
| sglang       |    181.4s (3.0m) | `0be5390` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        310.7 |    169.6 | **147.2** |
| TPOT median (ms)          |        156.2 | **60.3** |      76.2 |
| E2E median (ms)           |        404.2 |    228.4 | **218.6** |
| Throughput median (tok/s) |          3.4 |  **6.3** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        306.6 | **192.5** |  221.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        343.4 | **224.8** |  373.3 |
| Throughput median (tok/s) |          2.9 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        941.6 |     188.7 | **171.7** |
| TPOT median (ms)          |        145.5 |  **63.9** |     107.7 |
| E2E median (ms)           |       1082.0 | **243.0** |     282.9 |
| Throughput median (tok/s) |          1.2 |   **5.7** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        386.2 | **61.1** |   81.0 |
| TPOT median (ms)          |        138.1 | **27.7** |   68.4 |
| E2E median (ms)           |        496.6 | **82.5** |  162.0 |
| Throughput median (tok/s) |          2.9 | **14.8** |    8.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.5 | **72.4** |
| TPOT median (ms)          |            - |  **14.9** |     22.7 |
| E2E median (ms)           |            - | **607.1** |    834.0 |
| Throughput median (tok/s) |            - |  **58.9** |     41.0 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        486.3 | **137.7** |  138.7 |
| TPOT median (ms)          |        109.9 |  **33.3** |   55.0 |
| E2E median (ms)           |        581.5 | **277.2** |  374.2 |
| Throughput median (tok/s) |          2.6 |  **18.0** |   12.6 |
| Correctness               |          98% |       98% |    99% |
