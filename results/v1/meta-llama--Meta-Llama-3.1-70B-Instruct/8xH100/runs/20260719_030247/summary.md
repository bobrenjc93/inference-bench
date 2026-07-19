# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 18 2026

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
| torchinferno | **49.0s (0.8m)** | `96adc9d` |
| vllm         |    386.4s (6.4m) | `b6ff8a2` |
| sglang       |    190.7s (3.2m) | `cce5fe7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        147.1 |  **78.9** |   89.5 |
| TPOT median (ms)          |     **31.2** |      40.1 |   67.2 |
| E2E median (ms)           |        172.1 | **110.5** |  148.2 |
| Throughput median (tok/s) |          6.8 |  **12.4** |    9.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.5** | 68.4 |  162.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **73.7** | 84.8 |  238.8 |
| Throughput median (tok/s) |     **13.6** | 11.8 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.1 |  **78.8** |   88.7 |
| TPOT median (ms)          |     **34.0** |      40.9 |   83.2 |
| E2E median (ms)           |        221.2 | **110.9** |  151.2 |
| Throughput median (tok/s) |          5.1 |  **12.1** |    8.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.3 | **35.0** |   62.5 |
| TPOT median (ms)          |         34.6 | **22.8** |  374.3 |
| E2E median (ms)           |         75.4 | **52.7** |  426.9 |
| Throughput median (tok/s) |         19.9 | **24.6** |    3.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.6 |  **46.2** |   58.2 |
| TPOT median (ms)          |         19.2 |  **15.3** |   28.2 |
| E2E median (ms)           |        854.8 | **589.5** | 1052.6 |
| Throughput median (tok/s) |         41.1 |  **61.0** |   34.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.9 |  **61.5** |   92.4 |
| TPOT median (ms)          |         23.8 |  **23.8** |  110.6 |
| E2E median (ms)           |        279.5 | **189.7** |  403.5 |
| Throughput median (tok/s) |         17.3 |  **24.4** |   11.9 |
| Correctness               |          98% |       99% |    99% |
