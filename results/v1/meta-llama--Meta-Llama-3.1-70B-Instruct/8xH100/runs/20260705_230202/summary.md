# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.4s (0.7m)** | `cddde7e` |
| vllm         |    244.0s (4.1m) | `b712181` |
| sglang       |    217.7s (3.6m) | `8673e85` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        164.3 | **114.7** |  136.4 |
| TPOT median (ms)          |         46.0 |  **41.5** |   80.6 |
| E2E median (ms)           |        213.1 | **153.9** |  212.6 |
| Throughput median (tok/s) |          6.0 |   **9.6** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        157.4 | **122.8** |  206.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        166.1 | **148.7** |  364.8 |
| Throughput median (tok/s) |          6.0 |   **6.7** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.2 | **150.8** |  156.2 |
| TPOT median (ms)          |         62.5 |  **50.1** |  117.4 |
| E2E median (ms)           |        381.2 | **190.2** |  269.4 |
| Throughput median (tok/s) |          3.8 |   **7.0** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         76.6 | **33.0** |   47.0 |
| TPOT median (ms)          |         63.0 | **21.9** |  346.0 |
| E2E median (ms)           |        106.5 | **48.7** |  380.0 |
| Throughput median (tok/s) |         12.9 | **25.3** |    3.8 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        282.6 |      76.8 | **70.7** |
| TPOT median (ms)          |         20.1 |  **15.0** |     22.4 |
| E2E median (ms)           |        989.8 | **690.8** |    880.1 |
| Throughput median (tok/s) |         37.0 |  **57.7** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        200.6 |  **99.6** |  123.3 |
| TPOT median (ms)          |         38.3 |  **25.7** |  113.3 |
| E2E median (ms)           |        371.3 | **246.5** |  421.4 |
| Throughput median (tok/s) |         13.1 |  **21.3** |   11.7 |
| Correctness               |          98% |       98% |    99% |
