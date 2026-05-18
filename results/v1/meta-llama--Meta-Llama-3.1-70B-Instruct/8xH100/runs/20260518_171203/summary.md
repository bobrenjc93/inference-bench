# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:08 AM PT, May 18 2026

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
| torchinferno |     248.9s (4.1m) | `c837893` |
| vllm         |   1140.8s (19.0m) | `8c296de` |
| sglang       | **171.6s (2.9m)** | `f21fe6a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        277.6 |    151.3 | **132.0** |
| TPOT median (ms)          |        150.3 | **50.5** |      71.0 |
| E2E median (ms)           |        372.8 |    198.1 | **197.5** |
| Throughput median (tok/s) |          4.1 |  **7.1** |       6.3 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        269.2 | **193.5** |  198.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        288.4 | **220.6** |  332.2 |
| Throughput median (tok/s) |          3.5 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        561.1 |     170.9 | **151.4** |
| TPOT median (ms)          |        165.1 |  **62.8** |      99.9 |
| E2E median (ms)           |        648.1 | **226.7** |     247.1 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        299.9 | **57.7** |   74.4 |
| TPOT median (ms)          |        130.9 | **26.8** |   61.5 |
| E2E median (ms)           |        393.6 | **77.9** |  155.0 |
| Throughput median (tok/s) |          3.6 | **16.0** |    9.4 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        659.4 |      77.1 | **66.6** |
| TPOT median (ms)          |         15.2 |  **15.0** |     22.2 |
| E2E median (ms)           |       1199.7 | **627.9** |    823.7 |
| Throughput median (tok/s) |         28.5 |  **57.8** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        413.4 |     130.1 | **124.5** |
| TPOT median (ms)          |         92.3 |  **31.0** |      50.9 |
| E2E median (ms)           |        580.5 | **270.2** |     351.1 |
| Throughput median (tok/s) |          8.4 |  **18.3** |      13.3 |
| Correctness               |          98% |       98% |       98% |
