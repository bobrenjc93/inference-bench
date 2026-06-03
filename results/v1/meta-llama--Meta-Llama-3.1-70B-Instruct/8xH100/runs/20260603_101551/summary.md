# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, Jun 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     378.7s (6.3m) | `254f74b` |
| vllm         |   1329.4s (22.2m) | `0e2b131` |
| sglang       | **217.0s (3.6m)** | `d7013b6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        519.9 |     157.2 | **142.5** |
| TPOT median (ms)          |         55.3 |  **49.6** |      68.9 |
| E2E median (ms)           |        574.0 | **203.1** |     209.7 |
| Throughput median (tok/s) |          2.5 |   **7.3** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        294.3 |     249.0 | **214.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        394.4 | **274.0** |     346.6 |
| Throughput median (tok/s) |          2.5 |   **3.6** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        805.5 |     181.0 | **164.7** |
| TPOT median (ms)          |        114.6 |  **72.7** |      97.8 |
| E2E median (ms)           |        951.1 | **242.7** |     259.0 |
| Throughput median (tok/s) |          1.4 |   **5.8** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        425.7 | **57.9** |   81.9 |
| TPOT median (ms)          |         33.2 | **27.4** |   42.3 |
| E2E median (ms)           |        457.0 | **78.3** |  135.1 |
| Throughput median (tok/s) |          3.2 | **15.8** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        414.0 |  **70.5** |   77.6 |
| TPOT median (ms)          |         36.0 |  **14.9** |   23.9 |
| E2E median (ms)           |       1669.2 | **605.3** |  902.7 |
| Throughput median (tok/s) |         21.3 |  **59.1** |   38.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        491.9 |     143.1 | **136.2** |
| TPOT median (ms)          |         47.8 |  **32.9** |      46.6 |
| E2E median (ms)           |        809.1 | **280.7** |     370.6 |
| Throughput median (tok/s) |          6.2 |  **18.3** |      12.5 |
| Correctness               |          99% |       99% |       99% |
