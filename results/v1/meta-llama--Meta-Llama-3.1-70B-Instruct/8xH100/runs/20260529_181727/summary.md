# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, May 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     392.0s (6.5m) | `b619d24` |
| vllm         |   1371.1s (22.9m) | `84b2a8a` |
| sglang       | **263.7s (4.4m)** | `ec075d8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        248.0 |     162.6 | **157.5** |
| TPOT median (ms)          |         59.8 |  **58.0** |      72.3 |
| E2E median (ms)           |        309.7 | **218.1** |     225.3 |
| Throughput median (tok/s) |          4.1 |   **6.9** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        235.5 | **178.6** |  233.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        266.0 | **200.8** |  364.1 |
| Throughput median (tok/s) |          3.8 |   **5.0** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        733.8 |     173.1 | **160.3** |
| TPOT median (ms)          |     **54.9** |      65.2 |      98.8 |
| E2E median (ms)           |        790.3 | **226.2** |     257.6 |
| Throughput median (tok/s) |          1.9 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        185.2 | **60.8** |   82.9 |
| TPOT median (ms)          |         28.0 | **27.4** |   43.6 |
| E2E median (ms)           |        212.5 | **81.2** |  143.4 |
| Throughput median (tok/s) |          6.1 | **14.8** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        505.2 |  **75.7** |   83.4 |
| TPOT median (ms)          |         15.2 |  **14.9** |   22.8 |
| E2E median (ms)           |       1338.3 | **622.5** |  873.3 |
| Throughput median (tok/s) |         28.5 |  **58.4** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        381.5 | **130.1** |  143.6 |
| TPOT median (ms)          |     **31.6** |      33.1 |   47.5 |
| E2E median (ms)           |        583.4 | **269.8** |  372.7 |
| Throughput median (tok/s) |          8.9 |  **18.2** |   12.6 |
| Correctness               |          99% |       99% |    99% |
