# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 16 2026

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
| torchinferno | **43.6s (0.7m)** | `96adc9d` |
| vllm         |    381.6s (6.4m) | `ea1d65f` |
| sglang       |    170.0s (2.8m) | `e2d021d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.9 |  **74.7** |   80.1 |
| TPOT median (ms)          |     **31.4** |      37.8 |   65.7 |
| E2E median (ms)           |        166.6 | **101.5** |  135.7 |
| Throughput median (tok/s) |          7.0 |  **12.7** |    9.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.7** | 71.8 |  129.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.6** | 90.2 |  212.1 |
| Throughput median (tok/s) |     **13.4** | 11.1 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.3 |  **82.7** |   83.1 |
| TPOT median (ms)          |     **34.6** |      35.6 |   78.1 |
| E2E median (ms)           |        222.0 | **112.6** |  147.4 |
| Throughput median (tok/s) |          5.0 |  **12.6** |    9.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         54.0 | **37.5** |   52.3 |
| TPOT median (ms)          |         35.1 | **27.5** |  409.9 |
| E2E median (ms)           |         76.2 | **56.2** |  448.5 |
| Throughput median (tok/s) |         19.3 | **22.9** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        182.7 |  **47.2** |   52.3 |
| TPOT median (ms)          |         19.5 |  **15.4** |   24.7 |
| E2E median (ms)           |        876.6 | **581.9** |  918.2 |
| Throughput median (tok/s) |         41.0 |  **60.4** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.7 |  **62.8** |   79.5 |
| TPOT median (ms)          |         24.1 |  **23.2** |  115.7 |
| E2E median (ms)           |        283.2 | **188.5** |  372.4 |
| Throughput median (tok/s) |         17.1 |  **24.0** |   13.2 |
| Correctness               |          98% |       99% |    98% |
