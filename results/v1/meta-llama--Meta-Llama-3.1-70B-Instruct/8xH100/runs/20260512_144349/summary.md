# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:01 AM PT, May 12 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **91.1s (1.5m)** | `708195d` |
| vllm         |  1127.2s (18.8m) | `dd6b3a5` |
| sglang       |    163.8s (2.7m) | `6be1a45` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        492.8 |    176.8 | **144.9** |
| TPOT median (ms)          |        489.8 | **63.7** |      81.5 |
| E2E median (ms)           |        931.9 |    237.9 | **222.7** |
| Throughput median (tok/s) |          1.6 |  **6.4** |       5.3 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        341.0 | **174.3** |  219.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        405.5 | **196.7** |  359.2 |
| Throughput median (tok/s) |          2.5 |   **5.1** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1261.2 |     181.1 | **160.1** |
| TPOT median (ms)          |        226.5 |  **59.9** |     114.3 |
| E2E median (ms)           |       1458.0 | **232.9** |     261.0 |
| Throughput median (tok/s) |          0.9 |   **5.9** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        314.4 | **60.0** |   78.9 |
| TPOT median (ms)          |        355.5 | **27.3** |   46.5 |
| E2E median (ms)           |        591.9 | **80.5** |  140.2 |
| Throughput median (tok/s) |          2.4 | **15.3** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        859.4 |      80.8 | **72.7** |
| TPOT median (ms)          |         33.0 |  **15.0** |     22.2 |
| E2E median (ms)           |       2129.5 | **664.8** |    854.3 |
| Throughput median (tok/s) |         17.3 |  **57.3** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        653.7 | **134.6** |  135.1 |
| TPOT median (ms)          |        220.9 |  **33.2** |   52.9 |
| E2E median (ms)           |       1103.4 | **282.5** |  367.5 |
| Throughput median (tok/s) |          4.9 |  **18.0** |   12.9 |
| Correctness               |          99% |       98% |    99% |
