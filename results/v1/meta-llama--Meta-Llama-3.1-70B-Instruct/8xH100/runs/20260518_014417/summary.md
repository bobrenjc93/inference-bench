# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **89.6s (1.5m)** | `3f0f3bc` |
| vllm         |  1235.7s (20.6m) | `966903e` |
| sglang       |    177.0s (3.0m) | `5147de2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        280.6 |     173.2 | **163.6** |
| TPOT median (ms)          |        160.4 |  **61.1** |      75.0 |
| E2E median (ms)           |        383.2 | **232.6** |     236.7 |
| Throughput median (tok/s) |          3.9 |   **6.6** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.9 | **179.2** |  216.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        310.7 | **207.6** |  365.0 |
| Throughput median (tok/s) |          3.2 |   **4.8** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        964.8 |     180.6 | **168.7** |
| TPOT median (ms)          |        158.2 |  **58.0** |     111.5 |
| E2E median (ms)           |       1055.5 | **236.2** |     274.9 |
| Throughput median (tok/s) |          1.2 |   **5.8** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        363.1 | **60.6** |   77.7 |
| TPOT median (ms)          |        136.6 | **27.2** |   64.2 |
| E2E median (ms)           |        471.5 | **81.8** |  151.1 |
| Throughput median (tok/s) |          2.8 | **15.1** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1044.5 |  **73.1** |   77.2 |
| TPOT median (ms)          |         15.8 |  **15.1** |   21.8 |
| E2E median (ms)           |       1758.1 | **615.8** |  813.1 |
| Throughput median (tok/s) |         20.4 |  **58.5** |   42.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        589.0 | **133.3** |  140.7 |
| TPOT median (ms)          |         94.2 |  **32.3** |   54.5 |
| E2E median (ms)           |        795.8 | **274.8** |  368.2 |
| Throughput median (tok/s) |          6.3 |  **18.2** |   12.8 |
| Correctness               |          99% |       99% |    99% |
