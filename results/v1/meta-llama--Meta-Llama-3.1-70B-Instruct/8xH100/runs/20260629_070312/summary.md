# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 AM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **18/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     583.4s (9.7m) | `a37dfc0` |
| vllm         |    637.8s (10.6m) | `4559c43` |
| sglang       | **298.2s (5.0m)** | `91cf159` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        161.6 | **138.9** |  143.1 |
| TPOT median (ms)          |     **46.4** |      47.2 |   74.1 |
| E2E median (ms)           |        202.6 | **178.7** |  217.8 |
| Throughput median (tok/s) |          5.9 |   **7.6** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        247.6 | **189.6** |  229.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        265.0 | **222.8** |  384.2 |
| Throughput median (tok/s) |          3.8 |   **4.5** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        314.1 | **163.1** |  164.8 |
| TPOT median (ms)          |         55.3 |  **52.1** |  106.1 |
| E2E median (ms)           |        369.5 | **205.7** |  262.5 |
| Throughput median (tok/s) |          3.8 |   **6.7** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        201.4 | **63.2** |   81.7 |
| TPOT median (ms)          |         56.7 | **32.0** |   56.9 |
| E2E median (ms)           |        248.5 | **86.7** |  142.7 |
| Throughput median (tok/s) |          5.6 | **14.0** |    9.7 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        319.5 |  **72.0** |   74.0 |
| TPOT median (ms)          |         23.3 |  **14.9** |   22.0 |
| E2E median (ms)           |       1158.3 | **599.3** |  842.3 |
| Throughput median (tok/s) |         32.6 |  **59.7** |   42.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.8 | **125.4** |  138.6 |
| TPOT median (ms)          |         36.3 |  **29.3** |   51.8 |
| E2E median (ms)           |        448.8 | **258.6** |  369.9 |
| Throughput median (tok/s) |         10.3 |  **18.5** |   13.0 |
| Correctness               |          98% |       99% |    99% |
