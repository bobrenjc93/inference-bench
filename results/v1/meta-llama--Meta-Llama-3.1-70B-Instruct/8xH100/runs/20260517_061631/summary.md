# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:10 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     343.2s (5.7m) | `db749af` |
| vllm         |   1138.9s (19.0m) | `ff712f6` |
| sglang       | **169.5s (2.8m)** | `52875ab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        287.3 |    162.8 | **140.0** |
| TPOT median (ms)          |        147.5 | **61.4** |      71.4 |
| E2E median (ms)           |        369.1 |    217.2 | **204.5** |
| Throughput median (tok/s) |          4.0 |  **6.7** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        273.1 | **201.0** |  205.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        294.7 | **224.4** |  344.3 |
| Throughput median (tok/s) |          3.4 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        525.1 |     166.7 | **155.9** |
| TPOT median (ms)          |        123.2 |  **63.7** |     111.2 |
| E2E median (ms)           |        628.2 | **221.3** |     259.3 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        378.4 | **57.7** |   78.4 |
| TPOT median (ms)          |        127.5 | **27.2** |   59.4 |
| E2E median (ms)           |        473.0 | **78.1** |  156.2 |
| Throughput median (tok/s) |          3.1 | **15.8** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        684.8 |      70.3 | **62.2** |
| TPOT median (ms)          |         16.2 |  **14.9** |     22.3 |
| E2E median (ms)           |       1425.5 | **613.8** |    823.7 |
| Throughput median (tok/s) |         26.8 |  **58.5** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        429.7 |     131.7 | **128.4** |
| TPOT median (ms)          |         82.9 |  **33.4** |      52.8 |
| E2E median (ms)           |        638.1 | **270.9** |     357.6 |
| Throughput median (tok/s) |          7.9 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       98% |
