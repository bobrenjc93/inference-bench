# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, May 31 2026

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
| torchinferno |     383.9s (6.4m) | `28e2983` |
| vllm         |   1313.9s (21.9m) | `29d6933` |
| sglang       | **233.3s (3.9m)** | `53b8378` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        343.9 |     163.8 | **150.1** |
| TPOT median (ms)          |         65.5 |  **60.5** |      75.4 |
| E2E median (ms)           |        403.5 | **217.8** |     220.4 |
| Throughput median (tok/s) |          3.2 |   **6.8** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        403.3 |     202.8 | **199.1** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        534.6 | **225.7** |     338.1 |
| Throughput median (tok/s) |          1.9 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        727.1 |     177.1 | **164.3** |
| TPOT median (ms)          |         92.7 |  **67.1** |     106.5 |
| E2E median (ms)           |        972.3 | **234.8** |     264.3 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        472.9 | **60.2** |   79.5 |
| TPOT median (ms)          |         38.8 | **27.2** |   42.1 |
| E2E median (ms)           |        510.5 | **80.9** |  132.9 |
| Throughput median (tok/s) |          2.7 | **14.9** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        471.3 |  **71.5** |   78.0 |
| TPOT median (ms)          |         29.9 |  **15.1** |   24.0 |
| E2E median (ms)           |       1471.7 | **608.7** |  902.7 |
| Throughput median (tok/s) |         23.1 |  **58.2** |   38.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        483.7 |     135.1 | **134.2** |
| TPOT median (ms)          |         45.4 |  **34.0** |      49.6 |
| E2E median (ms)           |        778.5 | **273.6** |     371.7 |
| Throughput median (tok/s) |          6.5 |  **18.1** |      12.4 |
| Correctness               |          99% |       98% |       99% |
