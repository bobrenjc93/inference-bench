# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 AM PT, Jun 8 2026

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
| torchinferno |     402.9s (6.7m) | `e46c781` |
| vllm         |   1376.2s (22.9m) | `dc68bd8` |
| sglang       | **205.1s (3.4m)** | `b047bb3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        326.3 |     160.9 | **149.7** |
| TPOT median (ms)          |         94.8 |  **52.0** |      70.2 |
| E2E median (ms)           |        414.3 | **211.7** |     216.9 |
| Throughput median (tok/s) |          3.0 |   **7.0** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        413.7 | **198.3** |  208.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        539.0 | **219.4** |  334.4 |
| Throughput median (tok/s) |          1.9 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        726.9 |     180.2 | **161.9** |
| TPOT median (ms)          |         69.3 |  **63.4** |      97.0 |
| E2E median (ms)           |        784.1 | **234.7** |     265.8 |
| Throughput median (tok/s) |          1.6 |   **5.9** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        422.0 | **63.5** |   80.9 |
| TPOT median (ms)          |         61.3 | **29.4** |   43.9 |
| E2E median (ms)           |        473.5 | **85.9** |  144.5 |
| Throughput median (tok/s) |          3.0 | **14.0** |    9.7 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        517.0 |  **71.2** |   79.1 |
| TPOT median (ms)          |         20.8 |  **15.1** |   23.3 |
| E2E median (ms)           |       1283.0 | **624.5** |  896.5 |
| Throughput median (tok/s) |         28.9 |  **58.4** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        481.2 | **134.8** |  136.0 |
| TPOT median (ms)          |         49.2 |  **32.0** |   46.9 |
| E2E median (ms)           |        698.8 | **275.2** |  371.6 |
| Throughput median (tok/s) |          7.7 |  **18.0** |   12.6 |
| Correctness               |          98% |       98% |    98% |
