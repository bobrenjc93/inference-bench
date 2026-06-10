# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 9 2026

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
| torchinferno |     355.7s (5.9m) | `a870596` |
| vllm         |   1407.2s (23.5m) | `47930b5` |
| sglang       | **204.1s (3.4m)** | `95d8a75` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        301.6 |     160.2 | **158.5** |
| TPOT median (ms)          |         95.7 |  **58.4** |      68.6 |
| E2E median (ms)           |        399.2 | **214.3** |     231.6 |
| Throughput median (tok/s) |          3.0 |   **7.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        421.0 | **187.8** |  204.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        571.1 | **218.3** |  344.9 |
| Throughput median (tok/s) |          1.8 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        649.4 |     179.3 | **173.4** |
| TPOT median (ms)          |         68.7 |  **65.8** |     103.1 |
| E2E median (ms)           |        739.7 | **234.1** |     272.4 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.3 | **61.9** |   85.0 |
| TPOT median (ms)          |         56.4 | **28.7** |   49.7 |
| E2E median (ms)           |        401.2 | **83.1** |  149.3 |
| Throughput median (tok/s) |          3.3 | **14.1** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.8 |  **73.1** |   81.9 |
| TPOT median (ms)          |         26.7 |  **15.1** |   23.6 |
| E2E median (ms)           |       1217.0 | **632.1** |  895.2 |
| Throughput median (tok/s) |         31.0 |  **57.9** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        379.6 | **132.5** |  140.7 |
| TPOT median (ms)          |         49.5 |  **33.6** |   49.0 |
| E2E median (ms)           |        665.7 | **276.4** |  378.7 |
| Throughput median (tok/s) |          8.2 |  **17.9** |   12.2 |
| Correctness               |          98% |       99% |    99% |
