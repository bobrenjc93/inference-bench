# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     417.5s (7.0m) | `065275c` |
| vllm         |   1369.7s (22.8m) | `40e065e` |
| sglang       | **215.8s (3.6m)** | `2a51479` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        286.9 | **147.7** |  148.9 |
| TPOT median (ms)          |         92.9 |  **47.9** |   74.8 |
| E2E median (ms)           |        371.2 | **195.2** |  219.6 |
| Throughput median (tok/s) |          3.4 |   **7.6** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        366.1 | **205.3** |  210.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        493.2 | **227.8** |  357.0 |
| Throughput median (tok/s) |          2.0 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        726.5 |     180.8 | **160.6** |
| TPOT median (ms)          |     **65.9** |      69.9 |     101.6 |
| E2E median (ms)           |        780.7 | **244.3** |     258.7 |
| Throughput median (tok/s) |          1.7 |   **5.9** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        402.8 | **61.7** |   81.9 |
| TPOT median (ms)          |         60.0 | **29.1** |   48.2 |
| E2E median (ms)           |        452.2 | **84.2** |  149.1 |
| Throughput median (tok/s) |          3.4 | **14.4** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.9 |  **71.8** |   79.3 |
| TPOT median (ms)          |         26.1 |  **15.1** |   25.1 |
| E2E median (ms)           |       1177.4 | **626.7** |  933.2 |
| Throughput median (tok/s) |         31.7 |  **58.6** |   37.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        394.3 | **133.5** |  136.2 |
| TPOT median (ms)          |         49.0 |  **32.4** |   49.9 |
| E2E median (ms)           |        654.9 | **275.6** |  383.5 |
| Throughput median (tok/s) |          8.4 |  **18.2** |   12.0 |
| Correctness               |          99% |       99% |    99% |
