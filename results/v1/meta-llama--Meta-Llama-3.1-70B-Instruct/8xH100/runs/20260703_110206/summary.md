# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         5/20 | **11/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **48.0s (0.8m)** | `3927cf1` |
| vllm         |    265.9s (4.4m) | `a14f57a` |
| sglang       |    148.5s (2.5m) | `42acfd1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        148.5 |   142.7 | **141.1** |
| TPOT median (ms)          |     **45.5** |    52.1 |      83.2 |
| E2E median (ms)           |    **187.1** |   189.7 |     218.4 |
| Throughput median (tok/s) |          6.5 | **7.7** |       5.8 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **146.0** | 218.4 |  217.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **155.2** | 244.1 |  380.3 |
| Throughput median (tok/s) |      **6.4** |   4.1 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        296.9 |     176.9 | **163.0** |
| TPOT median (ms)          |         59.6 |  **57.6** |     112.2 |
| E2E median (ms)           |        347.5 | **231.6** |     269.4 |
| Throughput median (tok/s) |          4.2 |   **5.9** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        129.0 | **62.7** |   74.6 |
| TPOT median (ms)          |         40.9 | **30.0** |   79.5 |
| E2E median (ms)           |        155.3 | **87.0** |  158.8 |
| Throughput median (tok/s) |          8.5 | **14.0** |    9.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        228.4 |      79.1 | **77.4** |
| TPOT median (ms)          |         20.9 |  **15.1** |     22.6 |
| E2E median (ms)           |        915.7 | **627.2** |    834.1 |
| Throughput median (tok/s) |         37.3 |  **57.1** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        189.8 |     135.9 | **134.8** |
| TPOT median (ms)          |         33.4 |  **31.0** |      59.5 |
| E2E median (ms)           |        352.2 | **275.9** |     372.2 |
| Throughput median (tok/s) |         12.6 |  **17.8** |      12.8 |
| Correctness               |          98% |       99% |       99% |
