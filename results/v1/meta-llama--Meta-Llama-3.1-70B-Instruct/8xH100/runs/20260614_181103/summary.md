# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     361.1s (6.0m) | `a102128` |
| vllm         |   1274.9s (21.2m) | `c621af1` |
| sglang       | **202.8s (3.4m)** | `3cb29f6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        317.9 |     155.3 | **140.5** |
| TPOT median (ms)          |        100.5 |  **55.7** |      77.3 |
| E2E median (ms)           |        413.7 | **203.3** |     211.2 |
| Throughput median (tok/s) |          3.0 |   **7.2** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        305.7 | **166.9** |  203.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        426.3 | **188.4** |  338.8 |
| Throughput median (tok/s) |          2.3 |   **5.3** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        685.7 |     174.9 | **163.8** |
| TPOT median (ms)          |     **63.6** |      65.2 |      97.0 |
| E2E median (ms)           |        760.6 | **231.0** |     259.8 |
| Throughput median (tok/s) |          1.6 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        287.0 | **59.6** |   82.2 |
| TPOT median (ms)          |         53.9 | **29.2** |   45.5 |
| E2E median (ms)           |        338.6 | **80.9** |  136.8 |
| Throughput median (tok/s) |          4.0 | **14.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        368.7 |      76.3 | **68.0** |
| TPOT median (ms)          |         22.3 |  **14.9** |     22.9 |
| E2E median (ms)           |       1125.8 | **626.4** |    840.2 |
| Throughput median (tok/s) |         30.8 |  **58.2** |     41.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        393.0 | **126.6** |  131.5 |
| TPOT median (ms)          |         48.1 |  **33.0** |   48.6 |
| E2E median (ms)           |        613.0 | **266.0** |  357.4 |
| Throughput median (tok/s) |          8.4 |  **18.3** |   12.9 |
| Correctness               |          98% |       99% |    99% |
