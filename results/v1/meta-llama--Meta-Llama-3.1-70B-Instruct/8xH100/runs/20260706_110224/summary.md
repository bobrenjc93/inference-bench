# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 6 2026

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
| torchinferno | **35.9s (0.6m)** | `0d6ab82` |
| vllm         |    265.0s (4.4m) | `ba22152` |
| sglang       |    172.0s (2.9m) | `80decc7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        147.1 | **128.0** |  131.0 |
| TPOT median (ms)          |         44.8 |  **42.5** |   82.8 |
| E2E median (ms)           |        186.5 | **162.0** |  214.1 |
| Throughput median (tok/s) |          6.5 |   **8.8** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **100.8** | 120.3 |  209.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **105.8** | 145.8 |  360.2 |
| Throughput median (tok/s) |      **9.4** |   6.9 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        258.1 | **145.5** |  161.9 |
| TPOT median (ms)          |         58.5 |  **39.5** |  113.8 |
| E2E median (ms)           |        312.5 | **184.9** |  282.2 |
| Throughput median (tok/s) |          4.3 |   **7.8** |    4.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         81.4 | **32.7** |   50.9 |
| TPOT median (ms)          |         63.8 | **21.8** |  427.1 |
| E2E median (ms)           |        117.6 | **48.2** |  459.2 |
| Throughput median (tok/s) |         11.9 | **25.5** |    3.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        255.8 |      76.3 | **69.3** |
| TPOT median (ms)          |         20.2 |  **14.6** |     22.3 |
| E2E median (ms)           |        934.8 | **591.1** |    931.2 |
| Throughput median (tok/s) |         37.1 |  **60.4** |     41.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        168.6 | **100.6** |  124.4 |
| TPOT median (ms)          |         37.5 |  **23.7** |  129.2 |
| E2E median (ms)           |        331.5 | **226.4** |  449.4 |
| Throughput median (tok/s) |         13.9 |  **21.9** |   11.5 |
| Correctness               |          99% |       98% |    99% |
