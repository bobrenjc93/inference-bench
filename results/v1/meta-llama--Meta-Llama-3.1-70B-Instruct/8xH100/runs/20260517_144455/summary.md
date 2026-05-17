# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:02 AM PT, May 17 2026

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
| torchinferno | **85.9s (1.4m)** | `1cdab3f` |
| vllm         |  1246.1s (20.8m) | `0fa8884` |
| sglang       |    172.6s (2.9m) | `3bf7e34` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        308.7 |    166.8 | **149.6** |
| TPOT median (ms)          |        158.7 | **58.0** |      72.9 |
| E2E median (ms)           |        405.5 |    222.4 | **222.0** |
| Throughput median (tok/s) |          3.4 |  **6.5** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        227.8 | **162.9** |  217.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        317.0 | **189.2** |  367.0 |
| Throughput median (tok/s) |          3.2 |   **5.3** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        893.9 |     190.8 | **170.4** |
| TPOT median (ms)          |        113.2 |  **60.4** |     108.5 |
| E2E median (ms)           |        992.7 | **251.3** |     277.1 |
| Throughput median (tok/s) |          1.4 |   **5.6** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        396.3 | **60.5** |   79.5 |
| TPOT median (ms)          |        135.5 | **27.6** |   56.5 |
| E2E median (ms)           |        500.5 | **80.9** |  146.1 |
| Throughput median (tok/s) |          2.6 | **15.1** |    9.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        981.0 |      78.1 | **74.5** |
| TPOT median (ms)          |         15.9 |  **15.1** |     22.0 |
| E2E median (ms)           |       1670.0 | **675.9** |    817.5 |
| Throughput median (tok/s) |         20.8 |  **56.6** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        561.5 | **131.8** |  138.4 |
| TPOT median (ms)          |         84.7 |  **32.2** |   52.0 |
| E2E median (ms)           |        777.1 | **283.9** |  365.9 |
| Throughput median (tok/s) |          6.3 |  **17.8** |   12.7 |
| Correctness               |          98% |       99% |    98% |
