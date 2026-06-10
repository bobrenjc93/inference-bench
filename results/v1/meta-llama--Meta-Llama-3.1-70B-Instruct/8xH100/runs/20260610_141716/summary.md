# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 10 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     411.9s (6.9m) | `a870596` |
| vllm         |   1344.4s (22.4m) | `6850839` |
| sglang       | **210.4s (3.5m)** | `53ed34c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        248.8 |     157.8 | **143.9** |
| TPOT median (ms)          |         92.5 |  **51.7** |      76.5 |
| E2E median (ms)           |        329.0 | **204.3** |     212.1 |
| Throughput median (tok/s) |          3.6 |   **7.4** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        404.4 | **201.2** |  213.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        564.4 | **265.9** |  367.1 |
| Throughput median (tok/s) |          1.8 |   **3.8** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        683.6 |     173.3 | **157.4** |
| TPOT median (ms)          |         66.3 |  **65.9** |     101.2 |
| E2E median (ms)           |        753.4 | **234.5** |     255.2 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        413.0 | **61.1** |   82.6 |
| TPOT median (ms)          |         61.0 | **27.4** |   46.9 |
| E2E median (ms)           |        470.1 | **82.5** |  142.6 |
| Throughput median (tok/s) |          3.0 | **14.4** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.0 |  **79.8** |   82.4 |
| TPOT median (ms)          |         26.9 |  **14.8** |   23.2 |
| E2E median (ms)           |       1203.2 | **626.0** |  893.7 |
| Throughput median (tok/s) |         30.5 |  **58.4** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        388.2 | **134.6** |  136.0 |
| TPOT median (ms)          |         49.3 |  **32.0** |   49.6 |
| E2E median (ms)           |        664.0 | **282.6** |  374.1 |
| Throughput median (tok/s) |          8.1 |  **18.0** |   12.6 |
| Correctness               |          99% |       98% |    98% |
