# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:59 AM PT, Jul 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **17/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.8s (0.7m)** | `96adc9d` |
| vllm         |    353.4s (5.9m) | `c233d90` |
| sglang       |    196.6s (3.3m) | `d7b9425` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        142.3 |  **80.5** |   93.2 |
| TPOT median (ms)          |     **31.5** |      36.8 |   73.3 |
| E2E median (ms)           |        166.4 | **111.1** |  154.9 |
| Throughput median (tok/s) |          6.9 |  **12.0** |    8.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         76.7 | **74.1** |  162.3 |
| TPOT median (ms)          |          0.0 |      0.0 |    0.0 |
| E2E median (ms)           |         95.8 | **90.7** |  235.0 |
| Throughput median (tok/s) |         10.4 | **11.0** |    4.3 |
| Correctness               |         100% |     100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        192.2 | **71.7** |   94.2 |
| TPOT median (ms)          |     **34.2** |     34.7 |   82.0 |
| E2E median (ms)           |        220.8 | **95.8** |  160.2 |
| Throughput median (tok/s) |          5.2 | **13.7** |    8.3 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.4 | **35.7** |   66.4 |
| TPOT median (ms)          |         34.9 | **23.4** |  387.6 |
| E2E median (ms)           |         73.4 | **54.0** |  447.4 |
| Throughput median (tok/s) |         19.4 | **23.8** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.4 |  **46.2** |   57.8 |
| TPOT median (ms)          |         19.1 |  **15.1** |   28.0 |
| E2E median (ms)           |        904.6 | **570.3** | 1097.9 |
| Throughput median (tok/s) |         40.9 |  **61.7** |   34.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        131.4 |  **61.7** |   94.8 |
| TPOT median (ms)          |         23.9 |  **22.0** |  114.2 |
| E2E median (ms)           |        292.2 | **184.4** |  419.1 |
| Throughput median (tok/s) |         16.6 |  **24.5** |   11.7 |
| Correctness               |          99% |       98% |    99% |
