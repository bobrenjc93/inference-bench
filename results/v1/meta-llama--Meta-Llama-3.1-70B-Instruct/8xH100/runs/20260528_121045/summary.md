# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, May 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     371.4s (6.2m) | `f4c65f7` |
| vllm         |   1315.8s (21.9m) | `61288b5` |
| sglang       | **264.9s (4.4m)** | `f4eac50` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        259.7 |    171.7 | **144.6** |
| TPOT median (ms)          |         66.0 | **59.1** |      76.6 |
| E2E median (ms)           |        319.5 |    226.9 | **218.8** |
| Throughput median (tok/s) |          3.9 |  **6.4** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        282.1 | **198.8** |  206.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        325.1 | **225.2** |  344.8 |
| Throughput median (tok/s) |          3.1 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        722.6 |     173.7 | **166.9** |
| TPOT median (ms)          |         59.5 |  **51.2** |     118.1 |
| E2E median (ms)           |        777.5 | **224.9** |     274.8 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        161.0 | **60.7** |   83.3 |
| TPOT median (ms)          |     **27.3** |     27.4 |   47.4 |
| E2E median (ms)           |        185.4 | **81.6** |  143.6 |
| Throughput median (tok/s) |          6.9 | **15.1** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        744.1 |  **70.1** |   78.3 |
| TPOT median (ms)          |     **14.6** |      15.1 |   23.3 |
| E2E median (ms)           |       1356.5 | **610.5** |  868.3 |
| Throughput median (tok/s) |         26.1 |  **58.6** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        433.9 | **135.0** |  135.9 |
| TPOT median (ms)          |         33.5 |  **30.6** |   53.1 |
| E2E median (ms)           |        592.8 | **273.8** |  370.0 |
| Throughput median (tok/s) |          8.3 |  **18.1** |   12.6 |
| Correctness               |          99% |       98% |    99% |
