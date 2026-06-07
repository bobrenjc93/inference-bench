# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 PM PT, Jun 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     343.9s (5.7m) | `51a6f22` |
| vllm         |   1274.1s (21.2m) | `4dcd10e` |
| sglang       | **220.1s (3.7m)** | `02be2e7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        318.5 |     161.8 | **158.3** |
| TPOT median (ms)          |         97.4 |  **55.5** |      69.0 |
| E2E median (ms)           |        412.5 | **216.4** |     226.9 |
| Throughput median (tok/s) |          3.0 |   **7.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        458.1 | **208.7** |  210.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        619.7 | **232.2** |  338.6 |
| Throughput median (tok/s) |          1.6 |   **4.3** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        841.2 |     176.0 | **166.6** |
| TPOT median (ms)          |        134.5 |  **67.1** |     104.3 |
| E2E median (ms)           |        968.5 | **235.0** |     265.0 |
| Throughput median (tok/s) |          1.5 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        452.0 | **61.8** |   91.7 |
| TPOT median (ms)          |         61.9 | **29.5** |   43.1 |
| E2E median (ms)           |        490.6 | **83.9** |  148.2 |
| Throughput median (tok/s) |          2.9 | **14.6** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        542.3 |      79.9 | **78.7** |
| TPOT median (ms)          |         22.8 |  **15.1** |     24.1 |
| E2E median (ms)           |       1342.0 | **630.2** |    887.9 |
| Throughput median (tok/s) |         26.6 |  **57.9** |     38.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        522.4 | **137.7** |  141.1 |
| TPOT median (ms)          |         63.3 |  **33.4** |   48.1 |
| E2E median (ms)           |        766.7 | **279.6** |  373.3 |
| Throughput median (tok/s) |          7.1 |  **18.0** |   12.3 |
| Correctness               |          99% |       99% |    99% |
