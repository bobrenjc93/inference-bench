# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:43 PM PT, Jul 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.4s (0.7m)** | `96adc9d` |
| vllm         |    330.9s (5.5m) | `ab0a20d` |
| sglang       |    175.0s (2.9m) | `7cd55c6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.0 |  **74.4** |   82.4 |
| TPOT median (ms)          |     **32.3** |      37.5 |   66.9 |
| E2E median (ms)           |        166.2 | **100.5** |  136.6 |
| Throughput median (tok/s) |          7.1 |  **13.5** |    9.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **52.5** | 66.6 |  128.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **69.7** | 84.0 |  210.4 |
| Throughput median (tok/s) |     **14.3** | 11.9 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.2 |  **75.2** |   86.6 |
| TPOT median (ms)          |     **35.7** |      36.9 |   81.2 |
| E2E median (ms)           |        217.9 | **103.3** |  147.5 |
| Throughput median (tok/s) |          5.1 |  **12.4** |    8.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.8 | **36.3** |   54.0 |
| TPOT median (ms)          |         34.6 | **24.5** |  417.1 |
| E2E median (ms)           |         75.5 | **54.6** |  435.9 |
| Throughput median (tok/s) |         19.4 | **23.7** |    3.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.5 |  **47.3** |   54.1 |
| TPOT median (ms)          |         18.8 |  **15.6** |   25.1 |
| E2E median (ms)           |        854.7 | **581.8** |  968.7 |
| Throughput median (tok/s) |         41.5 |  **60.1** |   38.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.0 |  **60.0** |   81.2 |
| TPOT median (ms)          |         24.3 |  **22.9** |  118.1 |
| E2E median (ms)           |        276.8 | **184.8** |  379.8 |
| Throughput median (tok/s) |         17.5 |  **24.3** |   13.0 |
| Correctness               |          99% |       99% |    99% |
