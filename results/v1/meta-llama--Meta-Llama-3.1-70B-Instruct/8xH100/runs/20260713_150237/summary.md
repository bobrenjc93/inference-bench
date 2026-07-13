# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 13 2026

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
| torchinferno | **42.3s (0.7m)** | `96adc9d` |
| vllm         |    328.3s (5.5m) | `93e3bc8` |
| sglang       |    157.0s (2.6m) | `2cf2920` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        143.0 | **69.9** |   85.5 |
| TPOT median (ms)          |     **31.2** |     37.5 |   59.9 |
| E2E median (ms)           |        167.0 | **94.9** |  137.7 |
| Throughput median (tok/s) |          6.8 | **13.7** |    9.8 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **64.6** | 78.2 |  124.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **84.2** | 98.2 |  220.6 |
| Throughput median (tok/s) |     **11.9** | 10.2 |    4.5 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        191.8 | **72.0** |   85.6 |
| TPOT median (ms)          |     **34.5** |     37.8 |   72.8 |
| E2E median (ms)           |        221.4 | **98.1** |  143.3 |
| Throughput median (tok/s) |          5.0 | **13.3** |    9.2 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.3 | **36.1** |   53.2 |
| TPOT median (ms)          |         34.9 | **23.9** |  387.4 |
| E2E median (ms)           |         74.0 | **54.6** |  431.3 |
| Throughput median (tok/s) |         19.3 | **24.2** |    3.3 |
| Correctness               |          98% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.6 |  **47.0** |   51.9 |
| TPOT median (ms)          |         19.4 |  **15.6** |   24.6 |
| E2E median (ms)           |        862.9 | **574.4** |  946.6 |
| Throughput median (tok/s) |         41.0 |  **60.6** |   39.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.2 |  **60.6** |   80.1 |
| TPOT median (ms)          |         24.0 |  **23.0** |  108.9 |
| E2E median (ms)           |        281.9 | **184.0** |  375.9 |
| Throughput median (tok/s) |         16.8 |  **24.4** |   13.2 |
| Correctness               |          99% |       99% |    99% |
