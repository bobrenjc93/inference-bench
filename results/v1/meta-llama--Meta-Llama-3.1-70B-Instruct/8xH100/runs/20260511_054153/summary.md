# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **4/5** |    1/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **5/5** |    0/5 |          0/5 |
| **Total**        | **22/25** |   3/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1038.2s (17.3m) | `5536fc0` |
| sglang       |    275.1s (4.6m) | `a623ee4` |
| torchinferno | **79.0s (1.3m)** | `103395c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    166.8 | **156.1** |        564.9 |
| TPOT median (ms)          | **66.7** |      75.0 |        343.4 |
| E2E median (ms)           |    228.5 | **226.7** |        881.1 |
| Throughput median (tok/s) |  **6.3** |       5.2 |          1.5 |
| Correctness               |  **98%** |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **189.2** |  212.7 |        464.1 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **211.2** |  368.1 |        584.0 |
| Throughput median (tok/s) |   **4.7** |    2.7 |          1.7 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     181.9 | **161.0** |       2589.1 |
| TPOT median (ms)          |  **59.6** |      96.8 |        404.3 |
| E2E median (ms)           | **231.6** |     267.1 |       2947.2 |
| Throughput median (tok/s) |   **5.9** |       4.9 |          0.5 |
| Correctness               |   **98%** |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **68.6** |   81.8 |        615.5 |
| TPOT median (ms)          | **31.0** |   51.6 |        292.0 |
| E2E median (ms)           | **94.9** |  142.3 |        901.3 |
| Throughput median (tok/s) | **13.4** |    9.1 |          1.4 |
| Correctness               |  **97%** |    97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **75.5** |   77.3 |       2623.2 |
| TPOT median (ms)          |  **15.2** |   22.0 |         82.6 |
| E2E median (ms)           | **613.5** |  828.8 |       6788.1 |
| Throughput median (tok/s) |  **57.7** |   41.9 |          6.1 |
| Correctness               |  **100%** |   100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **136.4** |  137.8 |       1371.3 |
| TPOT median (ms)          |  **34.5** |   49.1 |        224.4 |
| E2E median (ms)           | **275.9** |  366.6 |       2420.3 |
| Throughput median (tok/s) |  **17.6** |   12.8 |          2.2 |
| Correctness               |   **98%** |    98% |          98% |
