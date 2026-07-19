# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 19 2026

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
| torchinferno | **46.9s (0.8m)** | `96adc9d` |
| vllm         |    416.6s (6.9m) | `b6ff8a2` |
| sglang       |    224.2s (3.7m) | `7a03d30` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.6 |  **77.6** |   84.0 |
| TPOT median (ms)          |     **30.7** |      39.0 |   68.4 |
| E2E median (ms)           |        166.8 | **105.3** |  140.6 |
| Throughput median (tok/s) |          6.8 |  **12.6** |    9.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.0** | 76.8 |  144.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.1** | 96.6 |  216.7 |
| Throughput median (tok/s) |     **13.3** | 10.4 |    4.6 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.6 |  **84.6** |   93.9 |
| TPOT median (ms)          |     **34.3** |      35.8 |   78.6 |
| E2E median (ms)           |        218.7 | **115.3** |  161.9 |
| Throughput median (tok/s) |          5.2 |  **12.3** |    8.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.4 | **37.1** |   67.9 |
| TPOT median (ms)          |         34.7 | **27.1** |  399.3 |
| E2E median (ms)           |         74.7 | **56.8** |  484.6 |
| Throughput median (tok/s) |         19.9 | **23.0** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.5 |  **47.4** |   55.6 |
| TPOT median (ms)          |         19.6 |  **15.7** |   29.3 |
| E2E median (ms)           |        889.6 | **591.5** | 1089.3 |
| Throughput median (tok/s) |         40.0 |  **59.6** |   33.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.8 |  **64.7** |   89.2 |
| TPOT median (ms)          |         23.9 |  **23.5** |  115.1 |
| E2E median (ms)           |        285.0 | **193.1** |  418.6 |
| Throughput median (tok/s) |         17.0 |  **23.6** |   11.7 |
| Correctness               |          99% |       99% |    99% |
