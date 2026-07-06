# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, Jul 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.6s (0.8m)** | `b488218` |
| vllm         |    264.8s (4.4m) | `9fde043` |
| sglang       |    208.6s (3.5m) | `52c6e27` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        154.6 | **122.1** |  132.9 |
| TPOT median (ms)          |         46.5 |  **39.6** |   80.6 |
| E2E median (ms)           |        196.2 | **151.6** |  209.4 |
| Throughput median (tok/s) |          6.2 |   **9.2** |    5.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **99.6** | 144.6 |  210.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **105.0** | 167.4 |  352.7 |
| Throughput median (tok/s) |      **9.5** |   6.0 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.7 | **157.2** |  162.8 |
| TPOT median (ms)          |         57.4 |  **43.0** |  114.4 |
| E2E median (ms)           |        297.1 | **201.5** |  271.7 |
| Throughput median (tok/s) |          4.6 |   **6.8** |    4.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         77.1 | **32.9** |   48.3 |
| TPOT median (ms)          |         63.9 | **21.7** |  382.5 |
| E2E median (ms)           |        109.4 | **48.2** |  421.8 |
| Throughput median (tok/s) |         12.5 | **25.6** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        260.4 |      82.8 | **66.3** |
| TPOT median (ms)          |         20.8 |  **14.8** |     22.7 |
| E2E median (ms)           |        966.0 | **678.3** |    980.0 |
| Throughput median (tok/s) |         35.3 |  **57.8** |     40.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        168.1 | **107.9** |  124.2 |
| TPOT median (ms)          |         37.7 |  **23.8** |  120.0 |
| E2E median (ms)           |        334.7 | **249.4** |  447.1 |
| Throughput median (tok/s) |         13.6 |  **21.1** |   11.5 |
| Correctness               |          98% |       99% |    98% |
