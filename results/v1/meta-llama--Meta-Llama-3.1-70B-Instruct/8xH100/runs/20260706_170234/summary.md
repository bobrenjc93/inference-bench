# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **14/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **42.8s (0.7m)** | `b488218` |
| vllm         |    391.5s (6.5m) | `9fde043` |
| sglang       |    262.2s (4.4m) | `3abdbab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        153.7 | **124.5** |  135.3 |
| TPOT median (ms)          |         45.4 |  **37.1** |   85.3 |
| E2E median (ms)           |        196.7 | **153.9** |  216.8 |
| Throughput median (tok/s) |          6.1 |   **9.1** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **102.4** | 135.5 |  214.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **109.0** | 159.2 |  356.4 |
| Throughput median (tok/s) |      **9.2** |   6.3 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        215.6 |     165.3 | **159.3** |
| TPOT median (ms)          |         62.7 |  **46.4** |     117.4 |
| E2E median (ms)           |        277.6 | **207.9** |     273.4 |
| Throughput median (tok/s) |          4.5 |   **6.4** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         77.9 | **33.4** |   50.2 |
| TPOT median (ms)          |         63.3 | **21.7** |  379.5 |
| E2E median (ms)           |        108.3 | **49.1** |  432.9 |
| Throughput median (tok/s) |         12.5 | **25.4** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        261.9 |      85.6 | **67.0** |
| TPOT median (ms)          |         20.6 |  **14.7** |     22.8 |
| E2E median (ms)           |       1023.9 | **636.4** |    878.1 |
| Throughput median (tok/s) |         34.5 |  **57.8** |     40.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        162.3 | **108.9** |  125.2 |
| TPOT median (ms)          |         38.4 |  **24.0** |  121.0 |
| E2E median (ms)           |        343.1 | **241.3** |  431.5 |
| Throughput median (tok/s) |         13.3 |  **21.0** |   11.5 |
| Correctness               |          98% |       99% |    98% |
