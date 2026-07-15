# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 15 2026

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
| torchinferno | **41.2s (0.7m)** | `96adc9d` |
| vllm         |    313.2s (5.2m) | `615834e` |
| sglang       |    171.5s (2.9m) | `495ae9a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.2 |  **73.9** |   79.7 |
| TPOT median (ms)          |     **30.9** |      35.4 |   65.5 |
| E2E median (ms)           |        166.3 | **101.6** |  136.0 |
| Throughput median (tok/s) |          6.8 |  **13.5** |    9.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.7** | 71.2 |  121.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **78.1** | 88.3 |  203.0 |
| Throughput median (tok/s) |     **12.8** | 11.3 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.9 |  **75.9** |   85.9 |
| TPOT median (ms)          |     **34.4** |      35.0 |   83.6 |
| E2E median (ms)           |        217.8 | **106.6** |  149.3 |
| Throughput median (tok/s) |          5.1 |  **12.4** |    9.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.6 | **34.5** |   52.9 |
| TPOT median (ms)          |         34.9 | **22.7** |  394.1 |
| E2E median (ms)           |         72.0 | **52.6** |  452.6 |
| Throughput median (tok/s) |         19.7 | **24.8** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        177.6 |  **46.7** |   50.6 |
| TPOT median (ms)          |         19.1 |  **15.2** |   24.8 |
| E2E median (ms)           |        895.1 | **576.8** |  925.0 |
| Throughput median (tok/s) |         41.9 |  **61.2** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.4 |  **60.5** |   78.1 |
| TPOT median (ms)          |         23.8 |  **21.7** |  113.6 |
| E2E median (ms)           |        285.9 | **185.2** |  373.2 |
| Throughput median (tok/s) |         17.3 |  **24.7** |   13.2 |
| Correctness               |          99% |       99% |    99% |
