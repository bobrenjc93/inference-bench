# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **2/4** |     1/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **14/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     400.2s (6.7m) | `254f74b` |
| vllm         |   1343.4s (22.4m) | `7268457` |
| sglang       | **220.1s (3.7m)** | `f790674` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        337.1 |   162.8 | **142.7** |
| TPOT median (ms)          |     **52.9** |    57.2 |      73.7 |
| E2E median (ms)           |        383.2 |   211.8 | **209.8** |
| Throughput median (tok/s) |          3.1 | **6.9** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        254.8 |     257.0 | **199.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        355.3 | **280.3** |     335.0 |
| Throughput median (tok/s) |          2.8 |   **3.6** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        870.8 |     178.3 | **160.1** |
| TPOT median (ms)          |        123.3 |  **52.1** |     103.1 |
| E2E median (ms)           |        964.5 | **222.3** |     251.4 |
| Throughput median (tok/s) |          1.4 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        362.2 | **62.5** |   81.7 |
| TPOT median (ms)          |         31.4 | **28.0** |   42.8 |
| E2E median (ms)           |        390.0 | **83.8** |  140.8 |
| Throughput median (tok/s) |          3.5 | **14.7** |    9.9 |
| Correctness               |          97% |      97% |    98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        424.5 |  **71.3** |   76.2 |
| TPOT median (ms)          |         36.7 |  **15.0** |   23.6 |
| E2E median (ms)           |       1687.7 | **607.1** |  886.4 |
| Throughput median (tok/s) |         21.1 |  **58.8** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        449.9 |     146.4 | **132.0** |
| TPOT median (ms)          |         48.8 |  **30.4** |      48.6 |
| E2E median (ms)           |        756.1 | **281.1** |     364.7 |
| Throughput median (tok/s) |          6.4 |  **18.0** |      12.7 |
| Correctness               |          99% |       98% |       99% |
