# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     356.8s (5.9m) | `578e117` |
| vllm         |     518.6s (8.6m) | `11a1230` |
| sglang       | **297.8s (5.0m)** | `da802dd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.2 | **136.7** |  150.3 |
| TPOT median (ms)          |     **45.3** |      46.1 |   78.8 |
| E2E median (ms)           |        184.2 | **175.5** |  224.1 |
| Throughput median (tok/s) |          6.4 |   **8.0** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        262.6 | **191.2** |  222.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        278.0 | **211.9** |  379.8 |
| Throughput median (tok/s) |          3.6 |   **4.7** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        353.5 |     165.5 | **164.0** |
| TPOT median (ms)          |         58.9 |  **50.7** |     103.7 |
| E2E median (ms)           |        412.2 | **209.8** |     268.0 |
| Throughput median (tok/s) |          3.3 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        269.8 | **63.2** |   84.3 |
| TPOT median (ms)          |         42.3 | **31.1** |   51.7 |
| E2E median (ms)           |        312.2 | **85.9** |  150.2 |
| Throughput median (tok/s) |          4.0 | **13.7** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        316.8 |      77.8 | **74.2** |
| TPOT median (ms)          |         22.1 |  **14.8** |     22.0 |
| E2E median (ms)           |       1126.9 | **619.6** |    831.9 |
| Throughput median (tok/s) |         33.5 |  **58.7** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        269.2 | **126.9** |  139.0 |
| TPOT median (ms)          |         33.7 |  **28.6** |   51.2 |
| E2E median (ms)           |        462.7 | **260.5** |  370.8 |
| Throughput median (tok/s) |         10.2 |  **18.3** |   13.0 |
| Correctness               |          99% |       99% |    99% |
