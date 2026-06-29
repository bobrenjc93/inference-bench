# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 AM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **2/4** |       0/4 |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     580.1s (9.7m) | `bd17332` |
| vllm         |    600.7s (10.0m) | `bc8481a` |
| sglang       | **305.1s (5.1m)** | `bb7d344` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        166.5 | **137.3** |  147.7 |
| TPOT median (ms)          |         49.3 |  **46.9** |   74.2 |
| E2E median (ms)           |        208.2 | **177.1** |  220.7 |
| Throughput median (tok/s) |          5.5 |   **8.0** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        261.3 | 219.9 | **212.5** |
| TPOT median (ms)          |          0.0 |   0.0 |       0.0 |
| E2E median (ms)           |    **282.8** | 306.3 |     381.3 |
| Throughput median (tok/s) |      **3.5** |   3.3 |       2.6 |
| Correctness               |         100% |  100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        319.0 |     161.2 | **158.5** |
| TPOT median (ms)          |         57.2 |  **55.5** |      99.8 |
| E2E median (ms)           |        376.1 | **204.3** |     257.8 |
| Throughput median (tok/s) |          3.5 |   **6.6** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        190.7 | **65.1** |   85.8 |
| TPOT median (ms)          |         57.3 | **31.8** |   37.1 |
| E2E median (ms)           |        235.3 | **90.4** |  131.3 |
| Throughput median (tok/s) |          5.7 | **13.4** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        340.1 |  **75.3** |   82.0 |
| TPOT median (ms)          |         22.8 |  **15.0** |   22.0 |
| E2E median (ms)           |       1207.4 | **621.4** |  853.4 |
| Throughput median (tok/s) |         30.7 |  **58.6** |   41.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        255.5 | **131.8** |  137.3 |
| TPOT median (ms)          |         37.3 |  **29.8** |   46.6 |
| E2E median (ms)           |        462.0 | **279.9** |  368.9 |
| Throughput median (tok/s) |          9.8 |  **18.0** |   13.0 |
| Correctness               |          98% |       99% |    99% |
