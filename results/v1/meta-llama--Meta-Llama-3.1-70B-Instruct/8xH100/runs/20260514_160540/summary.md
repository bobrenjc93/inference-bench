# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:07 AM PT, May 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     284.7s (4.7m) | `0c3133f` |
| vllm         |   1101.1s (18.4m) | `24337fb` |
| sglang       | **164.4s (2.7m)** | `50f4058` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        315.5 |    162.3 | **140.9** |
| TPOT median (ms)          |        169.0 | **62.9** |      81.1 |
| E2E median (ms)           |        408.6 |    217.8 | **214.3** |
| Throughput median (tok/s) |          3.5 |  **6.8** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        297.0 |     199.8 | **196.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        341.7 | **224.0** |     336.4 |
| Throughput median (tok/s) |          2.9 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        616.9 |     179.1 | **154.5** |
| TPOT median (ms)          |        183.2 |  **59.6** |     100.6 |
| E2E median (ms)           |        773.7 | **227.9** |     253.0 |
| Throughput median (tok/s) |          1.8 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        397.6 | **57.2** |   75.6 |
| TPOT median (ms)          |        237.8 | **27.1** |   46.2 |
| E2E median (ms)           |        603.6 | **77.7** |  132.1 |
| Throughput median (tok/s) |          2.4 | **15.7** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        486.4 |      71.8 | **64.4** |
| TPOT median (ms)          |         16.3 |  **15.1** |     22.8 |
| E2E median (ms)           |       1263.0 | **613.9** |    838.2 |
| Throughput median (tok/s) |         25.6 |  **58.4** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        422.7 |     134.0 | **126.4** |
| TPOT median (ms)          |        121.3 |  **32.9** |      50.1 |
| E2E median (ms)           |        678.1 | **272.2** |     354.8 |
| Throughput median (tok/s) |          7.2 |  **18.3** |      13.1 |
| Correctness               |          99% |       98% |       99% |
