# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **44.3s (0.7m)** | `96adc9d` |
| vllm         |    336.1s (5.6m) | `7c2acd3` |
| sglang       |    167.0s (2.8m) | `b3a0185` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.9 | **69.6** |   87.1 |
| TPOT median (ms)          |     **32.6** |     38.2 |   71.8 |
| E2E median (ms)           |        166.2 | **96.3** |  146.8 |
| Throughput median (tok/s) |          6.9 | **13.6** |    9.0 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **60.0** | 73.0 |  164.3 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **76.6** | 90.4 |  230.2 |
| Throughput median (tok/s) |     **13.0** | 11.1 |    4.3 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.7 |  **81.6** |   95.8 |
| TPOT median (ms)          |         35.1 |  **34.3** |   73.7 |
| E2E median (ms)           |        219.8 | **109.8** |  159.9 |
| Throughput median (tok/s) |          5.1 |  **12.2** |    8.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         51.8 | **36.2** |   68.0 |
| TPOT median (ms)          |         34.5 | **24.4** |  376.4 |
| E2E median (ms)           |         73.4 | **54.7** |  462.7 |
| Throughput median (tok/s) |         20.0 | **24.1** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.2 |  **46.7** |   57.0 |
| TPOT median (ms)          |         19.1 |  **15.4** |   28.1 |
| E2E median (ms)           |        857.3 | **579.4** | 1050.7 |
| Throughput median (tok/s) |         41.1 |  **60.7** |   34.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.9 |  **61.4** |   94.4 |
| TPOT median (ms)          |         24.3 |  **22.5** |  110.0 |
| E2E median (ms)           |        278.7 | **186.1** |  410.1 |
| Throughput median (tok/s) |         17.2 |  **24.3** |   11.9 |
| Correctness               |          99% |       99% |    98% |
