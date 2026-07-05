# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.0s (0.8m)** | `390fed4` |
| vllm         |    290.4s (4.8m) | `fa4321d` |
| sglang       |    206.7s (3.4m) | `3ea875f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        166.3 | **141.8** |  144.3 |
| TPOT median (ms)          |     **46.5** |      57.4 |   74.3 |
| E2E median (ms)           |        211.8 | **191.1** |  218.3 |
| Throughput median (tok/s) |          5.9 |   **7.4** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **160.6** | 226.1 |  224.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **175.4** | 252.2 |  382.4 |
| Throughput median (tok/s) |      **5.7** |   4.0 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        350.8 |     172.4 | **165.4** |
| TPOT median (ms)          |         61.7 |  **48.9** |     104.3 |
| E2E median (ms)           |        401.5 | **219.5** |     278.8 |
| Throughput median (tok/s) |          3.5 |   **6.3** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        123.5 | **62.6** |   76.5 |
| TPOT median (ms)          |         30.6 | **30.6** |   57.1 |
| E2E median (ms)           |        148.2 | **85.9** |  141.8 |
| Throughput median (tok/s) |          8.8 | **14.5** |    9.8 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        278.4 |      84.5 | **75.3** |
| TPOT median (ms)          |         19.6 |  **14.9** |     22.2 |
| E2E median (ms)           |       1003.4 | **634.3** |    823.6 |
| Throughput median (tok/s) |         36.0 |  **57.9** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        215.9 |     137.5 | **137.2** |
| TPOT median (ms)          |         31.7 |  **30.4** |      51.6 |
| E2E median (ms)           |        388.1 | **276.6** |     369.0 |
| Throughput median (tok/s) |         12.0 |  **18.0** |      12.9 |
| Correctness               |          98% |       99% |       98% |
