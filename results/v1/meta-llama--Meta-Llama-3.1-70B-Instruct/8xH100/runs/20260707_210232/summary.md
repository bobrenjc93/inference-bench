# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **44.4s (0.7m)** | `027a6d8` |
| vllm         |    323.2s (5.4m) | `3f99883` |
| sglang       |    229.6s (3.8m) | `bbc5370` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        175.3 | **130.6** |  131.9 |
| TPOT median (ms)          |         47.0 |  **42.1** |   78.2 |
| E2E median (ms)           |        214.9 | **167.8** |  208.6 |
| Throughput median (tok/s) |          5.8 |   **8.4** |    6.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **120.5** | 134.4 |  207.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **128.7** | 154.7 |  354.3 |
| Throughput median (tok/s) |      **7.8** |   6.5 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        272.1 | **157.0** |  160.5 |
| TPOT median (ms)          |         58.6 |  **46.3** |  107.9 |
| E2E median (ms)           |        327.0 | **201.3** |  277.8 |
| Throughput median (tok/s) |          4.1 |   **6.6** |    4.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         65.8 | **33.1** |   49.9 |
| TPOT median (ms)          |         43.5 | **21.8** |  389.2 |
| E2E median (ms)           |         99.1 | **48.8** |  448.2 |
| Throughput median (tok/s) |         14.2 | **25.6** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        267.4 |      82.4 | **68.6** |
| TPOT median (ms)          |         20.5 |  **14.7** |     22.4 |
| E2E median (ms)           |       1005.5 | **656.3** |    893.3 |
| Throughput median (tok/s) |         36.7 |  **59.3** |     41.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        180.2 | **107.5** |  123.7 |
| TPOT median (ms)          |         33.9 |  **25.0** |  119.6 |
| E2E median (ms)           |        355.0 | **245.8** |  436.4 |
| Throughput median (tok/s) |         13.7 |  **21.3** |   11.6 |
| Correctness               |          99% |       99% |    98% |
