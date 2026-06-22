# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 PM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **18/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     394.4s (6.6m) | `bc3b9ea` |
| vllm         |     542.3s (9.0m) | `9037498` |
| sglang       | **246.6s (4.1m)** | `64e455d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.8 | **137.6** |  151.5 |
| TPOT median (ms)          |         45.7 |  **44.5** |   74.3 |
| E2E median (ms)           |        188.4 | **178.3** |  223.9 |
| Throughput median (tok/s) |          6.4 |   **7.9** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        272.6 | **206.2** |  224.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        376.5 | **230.8** |  378.2 |
| Throughput median (tok/s) |          2.7 |   **4.3** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        584.7 | **158.3** |  167.7 |
| TPOT median (ms)          |     **37.5** |      43.0 |   96.3 |
| E2E median (ms)           |        615.3 | **199.7** |  268.6 |
| Throughput median (tok/s) |          2.2 |   **6.9** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        243.8 | **57.9** |   81.2 |
| TPOT median (ms)          |         30.2 | **29.2** |   53.1 |
| E2E median (ms)           |        269.9 | **79.7** |  141.8 |
| Throughput median (tok/s) |          5.3 | **15.3** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        327.9 |  **65.9** |   68.8 |
| TPOT median (ms)          |         21.4 |  **14.8** |   22.2 |
| E2E median (ms)           |       1134.3 | **594.7** |  831.0 |
| Throughput median (tok/s) |         31.7 |  **59.9** |   42.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        314.1 | **125.2** |  138.7 |
| TPOT median (ms)          |         26.9 |  **26.3** |   49.2 |
| E2E median (ms)           |        516.9 | **256.6** |  368.7 |
| Throughput median (tok/s) |          9.7 |  **18.9** |   13.1 |
| Correctness               |          99% |       99% |    99% |
