# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     362.9s (6.0m) | `9f91b40` |
| vllm         |   1253.7s (20.9m) | `b32fe41` |
| sglang       | **189.1s (3.2m)** | `af8f669` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        283.8 |    173.7 | **137.9** |
| TPOT median (ms)          |        152.5 | **62.7** |      74.8 |
| E2E median (ms)           |        378.4 |    227.6 | **211.0** |
| Throughput median (tok/s) |          4.0 |  **6.6** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.6 |     210.3 | **209.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        299.2 | **233.7** |     354.2 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       2.8 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        711.1 |     169.2 | **153.9** |
| TPOT median (ms)          |        115.1 |  **60.2** |     107.0 |
| E2E median (ms)           |        818.4 | **218.4** |     256.1 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        340.6 | **58.0** |   78.5 |
| TPOT median (ms)          |        132.1 | **27.2** |   53.7 |
| E2E median (ms)           |        437.9 | **78.4** |  144.9 |
| Throughput median (tok/s) |          3.3 | **15.5** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        797.3 |  **67.5** |   68.0 |
| TPOT median (ms)          |         15.3 |  **15.0** |   22.0 |
| E2E median (ms)           |       1435.8 | **617.8** |  820.2 |
| Throughput median (tok/s) |         22.7 |  **58.9** |   42.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        482.5 |     135.7 | **129.6** |
| TPOT median (ms)          |         83.0 |  **33.0** |      51.5 |
| E2E median (ms)           |        673.9 | **275.2** |     357.3 |
| Throughput median (tok/s) |          7.0 |  **18.3** |      13.2 |
| Correctness               |          99% |       98% |       98% |
