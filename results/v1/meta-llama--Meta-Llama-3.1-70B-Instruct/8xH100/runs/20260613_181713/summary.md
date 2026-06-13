# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     397.7s (6.6m) | `054d670` |
| vllm         |   1325.3s (22.1m) | `b3f0a0a` |
| sglang       | **204.4s (3.4m)** | `29128f3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        363.2 |     158.7 | **153.6** |
| TPOT median (ms)          |         99.7 |  **57.5** |      73.4 |
| E2E median (ms)           |        428.7 | **211.9** |     222.1 |
| Throughput median (tok/s) |          3.0 |   **6.8** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        342.0 | **203.5** |  212.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        473.8 | **223.0** |  350.4 |
| Throughput median (tok/s) |          2.1 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        711.9 |     174.1 | **163.7** |
| TPOT median (ms)          |         68.0 |  **64.5** |      97.8 |
| E2E median (ms)           |        791.5 | **227.8** |     254.2 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        278.7 | **62.2** |   80.7 |
| TPOT median (ms)          |         60.0 | **28.2** |   58.4 |
| E2E median (ms)           |        348.5 | **84.4** |  150.5 |
| Throughput median (tok/s) |          3.7 | **14.7** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        311.3 |  **69.7** |   70.3 |
| TPOT median (ms)          |         21.7 |  **14.8** |   22.4 |
| E2E median (ms)           |       1131.6 | **598.8** |  813.2 |
| Throughput median (tok/s) |         33.3 |  **59.2** |   42.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        401.4 | **133.6** |  136.1 |
| TPOT median (ms)          |         49.9 |  **33.0** |   50.4 |
| E2E median (ms)           |        634.8 | **269.2** |  358.1 |
| Throughput median (tok/s) |          8.7 |  **18.3** |   13.0 |
| Correctness               |          99% |       98% |    99% |
