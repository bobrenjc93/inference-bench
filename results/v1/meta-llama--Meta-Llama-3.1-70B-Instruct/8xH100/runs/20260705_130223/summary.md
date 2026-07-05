# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         6/20 | **10/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **33.9s (0.6m)** | `c85d39b` |
| vllm         |    255.2s (4.3m) | `8974ed8` |
| sglang       |    219.8s (3.7m) | `3ea875f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        156.7 |   151.9 | **141.7** |
| TPOT median (ms)          |     **46.7** |    57.1 |      75.0 |
| E2E median (ms)           |    **201.8** |   205.9 |     216.9 |
| Throughput median (tok/s) |          5.9 | **7.2** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **119.7** | 200.8 |  219.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **170.0** | 224.5 |  372.3 |
| Throughput median (tok/s) |      **5.9** |   4.5 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        371.5 |     175.1 | **170.2** |
| TPOT median (ms)          |         59.0 |  **55.8** |     109.2 |
| E2E median (ms)           |        423.8 | **227.5** |     276.2 |
| Throughput median (tok/s) |          3.3 |   **6.0** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        130.0 | **62.5** |   75.3 |
| TPOT median (ms)          |     **29.3** |     30.5 |   48.7 |
| E2E median (ms)           |        151.4 | **85.5** |  136.6 |
| Throughput median (tok/s) |          8.8 | **14.2** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        258.9 |      80.5 | **73.9** |
| TPOT median (ms)          |         20.6 |  **15.1** |     22.0 |
| E2E median (ms)           |        918.4 | **623.3** |    848.1 |
| Throughput median (tok/s) |         35.7 |  **57.8** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        207.4 | **134.2** |  136.0 |
| TPOT median (ms)          |     **31.1** |      31.7 |   51.0 |
| E2E median (ms)           |        373.1 | **273.3** |  370.0 |
| Throughput median (tok/s) |         11.9 |  **17.9** |   13.0 |
| Correctness               |          98% |       99% |    99% |
