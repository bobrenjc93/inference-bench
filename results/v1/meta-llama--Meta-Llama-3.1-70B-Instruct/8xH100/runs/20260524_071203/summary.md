# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |      **2/4** |       0/4 |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **13/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     293.9s (4.9m) | `9f91b40` |
| vllm         |   1267.4s (21.1m) | `0902d8e` |
| sglang       | **192.2s (3.2m)** | `d6d9f12` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        274.6 |     161.3 | **143.4** |
| TPOT median (ms)          |        154.7 |  **54.9** |      81.8 |
| E2E median (ms)           |        368.9 | **214.0** |     221.3 |
| Throughput median (tok/s) |          4.0 |   **6.9** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        266.3 | 213.4 | **202.9** |
| TPOT median (ms)          |          0.0 |   0.0 |       0.0 |
| E2E median (ms)           |    **292.8** | 300.3 |     348.2 |
| Throughput median (tok/s) |      **3.4** |   3.3 |       2.9 |
| Correctness               |         100% |  100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        755.5 |     180.9 | **160.9** |
| TPOT median (ms)          |        122.8 |  **63.1** |     110.0 |
| E2E median (ms)           |        873.6 | **237.5** |     260.6 |
| Throughput median (tok/s) |          1.5 |   **5.7** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        353.7 | **57.8** |   74.6 |
| TPOT median (ms)          |        134.0 | **26.5** |   64.9 |
| E2E median (ms)           |        448.4 | **78.0** |  157.2 |
| Throughput median (tok/s) |          3.2 | **15.7** |    9.0 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        834.6 |      74.8 | **68.7** |
| TPOT median (ms)          |         15.1 |  **14.9** |     22.5 |
| E2E median (ms)           |       1325.7 | **613.9** |    855.5 |
| Throughput median (tok/s) |         23.0 |  **58.5** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        497.0 |     137.6 | **130.1** |
| TPOT median (ms)          |         85.3 |  **31.9** |      55.9 |
| E2E median (ms)           |        661.9 | **288.7** |     368.6 |
| Throughput median (tok/s) |          7.1 |  **18.0** |      12.8 |
| Correctness               |          99% |       98% |       99% |
