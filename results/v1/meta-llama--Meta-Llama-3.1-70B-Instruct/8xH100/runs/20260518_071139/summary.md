# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:09 PM PT, May 17 2026

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
| torchinferno |     307.9s (5.1m) | `3f0f3bc` |
| vllm         |   1150.2s (19.2m) | `c1f7854` |
| sglang       | **172.3s (2.9m)** | `8d5ed33` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        281.7 |    159.9 | **141.5** |
| TPOT median (ms)          |        151.2 | **60.3** |      73.6 |
| E2E median (ms)           |        376.7 |    214.1 | **212.9** |
| Throughput median (tok/s) |          4.0 |  **6.7** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        271.3 |     204.7 | **203.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        295.1 | **232.3** |     338.9 |
| Throughput median (tok/s) |          3.4 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        553.4 |     174.1 | **160.9** |
| TPOT median (ms)          |        188.7 |  **65.7** |     102.1 |
| E2E median (ms)           |        661.2 | **229.6** |     265.3 |
| Throughput median (tok/s) |          1.9 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        314.8 | **57.5** |   73.0 |
| TPOT median (ms)          |        130.6 | **27.1** |   70.1 |
| E2E median (ms)           |        414.7 | **78.3** |  158.2 |
| Throughput median (tok/s) |          3.3 | **15.5** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        721.0 |  **66.0** |   68.1 |
| TPOT median (ms)          |         15.5 |  **15.1** |   22.3 |
| E2E median (ms)           |       1331.1 | **597.4** |  821.8 |
| Throughput median (tok/s) |         26.5 |  **59.5** |   42.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        428.4 |     132.4 | **129.4** |
| TPOT median (ms)          |         97.2 |  **33.6** |      53.6 |
| E2E median (ms)           |        615.8 | **270.3** |     359.4 |
| Throughput median (tok/s) |          7.8 |  **18.4** |      13.0 |
| Correctness               |          98% |       99% |       98% |
