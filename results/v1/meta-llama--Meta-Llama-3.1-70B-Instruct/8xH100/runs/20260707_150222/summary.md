# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.7s (0.7m)** | `372227c` |
| vllm         |    281.9s (4.7m) | `21b396a` |
| sglang       |    207.6s (3.5m) | `11cea29` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        152.9 | **118.1** |  131.1 |
| TPOT median (ms)          |         46.4 |  **40.2** |   77.4 |
| E2E median (ms)           |        193.4 | **146.9** |  207.1 |
| Throughput median (tok/s) |          6.1 |   **9.7** |    6.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **107.0** | 131.9 |  205.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **114.8** | 153.9 |  356.8 |
| Throughput median (tok/s) |      **8.7** |   6.5 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        258.2 | **151.4** |  161.5 |
| TPOT median (ms)          |         60.4 |  **46.1** |  119.2 |
| E2E median (ms)           |        316.3 | **193.2** |  281.2 |
| Throughput median (tok/s) |          4.5 |   **6.9** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         63.4 | **32.7** |   48.9 |
| TPOT median (ms)          |         43.5 | **21.8** |  350.7 |
| E2E median (ms)           |         96.8 | **48.0** |  416.4 |
| Throughput median (tok/s) |         14.8 | **25.6** |    3.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        248.5 |      74.3 | **72.0** |
| TPOT median (ms)          |         20.4 |  **14.7** |     22.2 |
| E2E median (ms)           |       1007.2 | **598.6** |    895.0 |
| Throughput median (tok/s) |         35.8 |  **60.3** |     41.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        166.0 | **101.7** |  123.7 |
| TPOT median (ms)          |         34.1 |  **24.6** |  113.9 |
| E2E median (ms)           |        345.7 | **228.1** |  431.3 |
| Throughput median (tok/s) |         14.0 |  **21.8** |   11.6 |
| Correctness               |          99% |       99% |    99% |
