# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:09 PM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     299.6s (5.0m) | `3f0f3bc` |
| vllm         |   1122.1s (18.7m) | `990f49b` |
| sglang       | **170.1s (2.8m)** | `6ccc5b8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        278.4 |    171.4 | **135.3** |
| TPOT median (ms)          |        155.8 | **60.6** |      77.8 |
| E2E median (ms)           |        374.1 |    232.6 | **207.0** |
| Throughput median (tok/s) |          4.0 |  **6.5** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        305.2 | **188.1** |  205.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        332.7 | **211.9** |  348.7 |
| Throughput median (tok/s) |          3.0 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        549.1 |     175.2 | **151.2** |
| TPOT median (ms)          |        134.2 |  **55.5** |     106.1 |
| E2E median (ms)           |        643.0 | **219.5** |     251.4 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.9 | **58.1** |   76.0 |
| TPOT median (ms)          |        132.2 | **26.8** |   61.9 |
| E2E median (ms)           |        438.6 | **78.8** |  148.3 |
| Throughput median (tok/s) |          3.3 | **15.4** |    9.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        790.7 |      67.2 | **66.7** |
| TPOT median (ms)          |         16.9 |  **15.1** |     22.3 |
| E2E median (ms)           |       1419.8 | **616.8** |    834.0 |
| Throughput median (tok/s) |         21.7 |  **58.5** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        452.3 |     132.0 | **126.9** |
| TPOT median (ms)          |         87.8 |  **31.6** |      53.6 |
| E2E median (ms)           |        641.6 | **271.9** |     357.9 |
| Throughput median (tok/s) |          6.8 |  **18.3** |      13.1 |
| Correctness               |          98% |       99% |       99% |
