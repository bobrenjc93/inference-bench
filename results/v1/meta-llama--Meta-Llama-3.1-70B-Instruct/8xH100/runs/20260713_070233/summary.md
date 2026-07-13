# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.8s (0.8m)** | `96adc9d` |
| vllm         |    399.8s (6.7m) | `75fe92a` |
| sglang       |    161.2s (2.7m) | `2225817` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.0 |  **77.8** |   81.0 |
| TPOT median (ms)          |     **31.9** |      39.0 |   65.7 |
| E2E median (ms)           |        165.6 | **108.7** |  137.1 |
| Throughput median (tok/s) |          6.9 |  **12.3** |    9.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **56.9** |  82.5 |  115.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **75.3** | 100.3 |  197.0 |
| Throughput median (tok/s) |     **13.3** |  10.0 |    5.1 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        190.5 |      84.7 | **82.5** |
| TPOT median (ms)          |     **35.5** |      35.8 |     80.6 |
| E2E median (ms)           |        218.8 | **117.9** |    147.6 |
| Throughput median (tok/s) |          5.1 |  **11.2** |      9.1 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         51.6 | **37.4** |   52.7 |
| TPOT median (ms)          |         34.4 | **27.3** |  406.5 |
| E2E median (ms)           |         73.2 | **56.8** |  484.7 |
| Throughput median (tok/s) |         19.7 | **23.2** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.4 |  **47.7** |   51.9 |
| TPOT median (ms)          |         19.2 |  **15.7** |   24.5 |
| E2E median (ms)           |        863.0 | **585.0** |  955.4 |
| Throughput median (tok/s) |         41.5 |  **59.9** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.9 |  **66.0** |   76.8 |
| TPOT median (ms)          |         24.2 |  **23.6** |  115.5 |
| E2E median (ms)           |        279.2 | **193.7** |  384.4 |
| Throughput median (tok/s) |         17.3 |  **23.3** |   13.3 |
| Correctness               |          99% |       99% |    99% |
