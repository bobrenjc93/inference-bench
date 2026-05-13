# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **85.7s (1.4m)** | `9d5290c` |
| vllm         |  1221.9s (20.4m) | `07534b8` |
| sglang       |    171.9s (2.9m) | `642ac9c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        426.2 |    171.8 | **146.5** |
| TPOT median (ms)          |        503.8 | **55.4** |      76.8 |
| E2E median (ms)           |        866.8 |    228.4 | **214.8** |
| Throughput median (tok/s) |          1.6 |  **6.1** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        754.9 | **181.4** |  221.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        787.9 | **213.7** |  367.8 |
| Throughput median (tok/s) |          1.3 |   **4.7** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1260.9 |     188.2 | **167.4** |
| TPOT median (ms)          |        212.6 |  **50.1** |     105.1 |
| E2E median (ms)           |       1417.9 | **237.8** |     268.0 |
| Throughput median (tok/s) |          0.9 |   **5.7** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        561.9 | **61.2** |   79.5 |
| TPOT median (ms)          |        490.6 | **27.8** |   52.3 |
| E2E median (ms)           |        934.4 | **82.6** |  139.3 |
| Throughput median (tok/s) |          1.5 | **14.9** |    9.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1048.8 |  **73.2** |   74.9 |
| TPOT median (ms)          |         31.1 |  **14.9** |   21.8 |
| E2E median (ms)           |       2250.3 | **618.0** |  855.6 |
| Throughput median (tok/s) |         15.9 |  **58.6** |   42.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        810.5 | **135.1** |  138.0 |
| TPOT median (ms)          |        247.6 |  **29.7** |   51.2 |
| E2E median (ms)           |       1251.4 | **276.1** |  369.1 |
| Throughput median (tok/s) |          4.3 |  **18.0** |   13.0 |
| Correctness               |          98% |       99% |    99% |
