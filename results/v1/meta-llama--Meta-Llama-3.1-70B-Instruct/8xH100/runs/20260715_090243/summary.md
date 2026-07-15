# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.9s (0.7m)** | `96adc9d` |
| vllm         |    258.1s (4.3m) | `7aab6e2` |
| sglang       |    178.2s (3.0m) | `f2c875d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        140.6 |      94.1 | **81.0** |
| TPOT median (ms)          |     **31.0** |      37.0 |     65.9 |
| E2E median (ms)           |        164.9 | **121.5** |    138.7 |
| Throughput median (tok/s) |          7.0 |  **11.1** |      9.7 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **57.9** |  84.2 |  124.6 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **76.5** | 102.3 |  198.0 |
| Throughput median (tok/s) |     **13.1** |   9.8 |    5.1 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.1 |  **80.6** |   81.3 |
| TPOT median (ms)          |     **34.5** |      37.9 |   73.0 |
| E2E median (ms)           |        218.7 | **109.9** |  140.6 |
| Throughput median (tok/s) |          5.1 |  **11.5** |    9.5 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.2 | **36.3** |   52.8 |
| TPOT median (ms)          |         34.6 | **23.9** |  387.6 |
| E2E median (ms)           |         75.4 | **54.3** |  446.4 |
| Throughput median (tok/s) |         19.5 | **23.7** |    3.2 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.4 |  **46.7** |   51.6 |
| TPOT median (ms)          |         19.0 |  **15.4** |   24.5 |
| E2E median (ms)           |        856.8 | **580.2** |  940.7 |
| Throughput median (tok/s) |         41.3 |  **60.7** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.6 |  **68.4** |   78.3 |
| TPOT median (ms)          |         23.8 |  **22.8** |  110.2 |
| E2E median (ms)           |        278.5 | **193.6** |  372.9 |
| Throughput median (tok/s) |         17.2 |  **23.3** |   13.3 |
| Correctness               |          98% |       98% |    99% |
