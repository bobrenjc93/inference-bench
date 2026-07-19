# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 19 2026

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
| torchinferno | **49.9s (0.8m)** | `96adc9d` |
| vllm         |    435.8s (7.3m) | `b6ff8a2` |
| sglang       |    183.9s (3.1m) | `7a03d30` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.1 |  **73.4** |   94.3 |
| TPOT median (ms)          |     **30.6** |      38.0 |   72.4 |
| E2E median (ms)           |        166.8 | **103.3** |  157.6 |
| Throughput median (tok/s) |          6.9 |  **13.0** |    8.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.5** | 69.5 |  145.3 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **78.2** | 83.9 |  221.7 |
| Throughput median (tok/s) |     **12.8** | 11.9 |    4.5 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        192.0 | **74.6** |   89.2 |
| TPOT median (ms)          |         34.0 | **33.6** |   78.3 |
| E2E median (ms)           |        218.8 | **99.2** |  153.4 |
| Throughput median (tok/s) |          5.1 | **14.2** |    8.8 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.7 | **35.0** |   65.6 |
| TPOT median (ms)          |         34.7 | **22.5** |  392.0 |
| E2E median (ms)           |         73.7 | **52.4** |  449.2 |
| Throughput median (tok/s) |         19.5 | **24.8** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.9 |  **46.7** |   55.3 |
| TPOT median (ms)          |         18.9 |  **15.6** |   26.6 |
| E2E median (ms)           |        879.9 | **584.5** | 1036.0 |
| Throughput median (tok/s) |         41.8 |  **60.5** |   36.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.1 |  **59.9** |   89.9 |
| TPOT median (ms)          |         23.6 |  **21.9** |  113.9 |
| E2E median (ms)           |        283.5 | **184.7** |  403.6 |
| Throughput median (tok/s) |         17.2 |  **24.9** |   12.2 |
| Correctness               |          98% |       98% |    98% |
