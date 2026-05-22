# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 AM PT, May 22 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     325.4s (5.4m) | `9f91b40` |
| vllm         |   1264.0s (21.1m) | `d3d1cf6` |
| sglang       | **182.6s (3.0m)** | `8c916a7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        286.9 |     152.6 | **140.3** |
| TPOT median (ms)          |        150.0 |  **55.4** |      75.9 |
| E2E median (ms)           |        383.9 | **202.6** |     211.2 |
| Throughput median (tok/s) |          3.9 |   **6.9** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.9 | **196.5** |  198.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        306.8 | **219.4** |  340.5 |
| Throughput median (tok/s) |          3.3 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        656.8 |     179.6 | **160.0** |
| TPOT median (ms)          |        102.9 |  **60.5** |     101.0 |
| E2E median (ms)           |        760.6 | **236.3** |     261.1 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        400.7 | **57.9** |   75.6 |
| TPOT median (ms)          |        129.6 | **26.7** |   69.1 |
| E2E median (ms)           |        514.9 | **78.2** |  158.1 |
| Throughput median (tok/s) |          2.7 | **15.4** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        822.6 |      73.5 | **67.5** |
| TPOT median (ms)          |         18.7 |  **15.1** |     22.6 |
| E2E median (ms)           |       1443.6 | **615.9** |    838.6 |
| Throughput median (tok/s) |         23.9 |  **58.3** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        483.2 |     132.0 | **128.5** |
| TPOT median (ms)          |         80.2 |  **31.5** |      53.7 |
| E2E median (ms)           |        682.0 | **270.5** |     361.9 |
| Throughput median (tok/s) |          7.1 |  **18.2** |      12.9 |
| Correctness               |          98% |       99% |       98% |
