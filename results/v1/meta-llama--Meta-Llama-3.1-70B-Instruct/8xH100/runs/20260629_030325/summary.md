# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    725.4s (12.1m) | `9b0f24c` |
| vllm         |    640.2s (10.7m) | `5274c11` |
| sglang       | **302.5s (5.0m)** | `2260e61` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        166.2 | **132.3** |  145.5 |
| TPOT median (ms)          |         48.2 |  **45.1** |   71.0 |
| E2E median (ms)           |        207.4 | **170.9** |  216.7 |
| Throughput median (tok/s) |          5.5 |   **7.9** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        282.0 | **204.6** |  221.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        301.4 | **231.7** |  368.3 |
| Throughput median (tok/s) |          3.3 |   **4.3** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        314.9 |     171.3 | **161.2** |
| TPOT median (ms)          |         59.0 |  **56.3** |      99.4 |
| E2E median (ms)           |        369.9 | **219.3** |     254.8 |
| Throughput median (tok/s) |          3.7 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        189.1 | **65.8** |   80.5 |
| TPOT median (ms)          |         58.2 | **33.3** |   57.9 |
| E2E median (ms)           |        232.7 | **91.6** |  146.1 |
| Throughput median (tok/s) |          6.0 | **13.6** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        354.7 |      74.3 | **67.7** |
| TPOT median (ms)          |         21.6 |  **14.9** |     22.6 |
| E2E median (ms)           |       1110.8 | **608.4** |    826.9 |
| Throughput median (tok/s) |         32.5 |  **58.5** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        261.4 | **129.7** |  135.3 |
| TPOT median (ms)          |         37.4 |  **29.9** |   50.2 |
| E2E median (ms)           |        444.5 | **264.4** |  362.6 |
| Throughput median (tok/s) |         10.2 |  **18.1** |   13.0 |
| Correctness               |          99% |       99% |    99% |
