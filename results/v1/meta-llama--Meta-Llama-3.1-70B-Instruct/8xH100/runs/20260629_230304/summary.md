# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    678.4s (11.3m) | `4237fa4` |
| vllm         |    624.1s (10.4m) | `75698e6` |
| sglang       | **293.8s (4.9m)** | `a6bc432` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        164.9 | **142.2** |  152.0 |
| TPOT median (ms)          |         49.2 |  **46.2** |   75.7 |
| E2E median (ms)           |        205.5 | **175.0** |  229.1 |
| Throughput median (tok/s) |          5.5 |   **7.8** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        238.3 | **199.3** |  218.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        254.9 | **220.3** |  357.3 |
| Throughput median (tok/s) |          3.9 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.5 | **153.1** |  171.9 |
| TPOT median (ms)          |         56.7 |  **53.2** |  103.2 |
| E2E median (ms)           |        344.6 | **197.0** |  277.2 |
| Throughput median (tok/s) |          4.1 |   **6.7** |    4.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        201.3 | **61.0** |   80.3 |
| TPOT median (ms)          |         57.3 | **30.4** |   54.0 |
| E2E median (ms)           |        248.1 | **83.8** |  144.6 |
| Throughput median (tok/s) |          5.5 | **14.5** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        343.0 |      79.4 | **69.3** |
| TPOT median (ms)          |         22.1 |  **15.1** |     22.6 |
| E2E median (ms)           |       1143.6 | **623.8** |    814.3 |
| Throughput median (tok/s) |         32.5 |  **57.4** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        247.8 | **127.0** |  138.3 |
| TPOT median (ms)          |         37.1 |  **29.0** |   51.1 |
| E2E median (ms)           |        439.4 | **260.0** |  364.5 |
| Throughput median (tok/s) |         10.3 |  **18.2** |   12.8 |
| Correctness               |          98% |       99% |    99% |
