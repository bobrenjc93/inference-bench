# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.3s (0.8m)** | `92889de` |
| vllm         |    351.7s (5.9m) | `cc1d020` |
| sglang       |    205.0s (3.4m) | `602c861` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        153.5 | **137.6** |  148.0 |
| TPOT median (ms)          |     **46.8** |      52.6 |   74.1 |
| E2E median (ms)           |        202.5 | **178.0** |  224.1 |
| Throughput median (tok/s) |          5.9 |   **7.6** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.0 | **195.1** |  221.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        317.3 | **218.6** |  370.4 |
| Throughput median (tok/s) |          3.2 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        309.8 |     173.5 | **166.2** |
| TPOT median (ms)          |         62.2 |  **51.7** |     106.0 |
| E2E median (ms)           |        361.5 | **221.5** |     268.5 |
| Throughput median (tok/s) |          4.1 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        121.7 | **61.6** |   74.7 |
| TPOT median (ms)          |     **29.1** |     30.3 |   52.0 |
| E2E median (ms)           |        145.4 | **85.4** |  134.5 |
| Throughput median (tok/s) |          9.3 | **13.9** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        280.1 |      77.8 | **73.3** |
| TPOT median (ms)          |         19.3 |  **15.0** |     22.2 |
| E2E median (ms)           |        922.3 | **638.1** |    835.6 |
| Throughput median (tok/s) |         37.7 |  **57.7** |     41.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        228.6 | **129.1** |  136.7 |
| TPOT median (ms)          |         31.5 |  **29.9** |   50.8 |
| E2E median (ms)           |        389.8 | **268.3** |  366.6 |
| Throughput median (tok/s) |         12.0 |  **18.0** |   12.9 |
| Correctness               |          98% |       98% |    99% |
