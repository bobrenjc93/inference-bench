# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 19 2026

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
| torchinferno | **58.0s (1.0m)** | `96adc9d` |
| vllm         |    331.8s (5.5m) | `2730b65` |
| sglang       |    191.0s (3.2m) | `9f8e916` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.7 |  **85.2** |   88.1 |
| TPOT median (ms)          |     **31.1** |      37.5 |   69.8 |
| E2E median (ms)           |        166.7 | **119.0** |  146.1 |
| Throughput median (tok/s) |          6.9 |  **11.6** |    9.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.3** | 73.9 |  155.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.2** | 90.5 |  232.7 |
| Throughput median (tok/s) |     **13.3** | 11.1 |    4.3 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.2 |  **74.9** |   85.1 |
| TPOT median (ms)          |     **34.2** |      42.0 |   79.3 |
| E2E median (ms)           |        219.4 | **105.0** |  146.1 |
| Throughput median (tok/s) |          5.1 |  **11.9** |    9.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.1 | **35.6** |   58.1 |
| TPOT median (ms)          |         34.5 | **24.6** |  374.2 |
| E2E median (ms)           |         73.3 | **54.1** |  437.1 |
| Throughput median (tok/s) |         19.7 | **24.3** |    3.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        180.8 |  **46.8** |   55.6 |
| TPOT median (ms)          |         19.0 |  **15.4** |   26.9 |
| E2E median (ms)           |        894.5 | **576.2** | 1051.4 |
| Throughput median (tok/s) |         42.0 |  **60.6** |   35.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.2 |  **63.3** |   88.5 |
| TPOT median (ms)          |     **23.8** |      23.9 |  110.1 |
| E2E median (ms)           |        285.8 | **188.9** |  402.7 |
| Throughput median (tok/s) |         17.4 |  **23.9** |   12.3 |
| Correctness               |          99% |       99% |    99% |
