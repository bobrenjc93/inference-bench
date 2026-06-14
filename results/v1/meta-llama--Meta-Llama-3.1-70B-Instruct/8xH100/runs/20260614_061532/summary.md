# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     420.2s (7.0m) | `a102128` |
| vllm         |   1346.6s (22.4m) | `78e7293` |
| sglang       | **210.8s (3.5m)** | `1747b88` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        341.0 |     161.7 | **148.6** |
| TPOT median (ms)          |        100.0 |  **58.2** |      73.6 |
| E2E median (ms)           |        418.2 | **214.7** |     218.4 |
| Throughput median (tok/s) |          3.0 |   **6.9** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        325.6 | **192.4** |  206.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        442.9 | **212.8** |  345.2 |
| Throughput median (tok/s) |          2.3 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        744.7 | **171.9** |  178.6 |
| TPOT median (ms)          |         68.1 |  **61.5** |   98.4 |
| E2E median (ms)           |        837.9 | **228.6** |  276.8 |
| Throughput median (tok/s) |          1.7 |   **6.1** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        257.4 | **60.7** |   83.4 |
| TPOT median (ms)          |         34.0 | **30.4** |   43.2 |
| E2E median (ms)           |        290.9 | **82.7** |  140.7 |
| Throughput median (tok/s) |          4.7 | **14.6** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        352.4 |  **73.3** |   74.4 |
| TPOT median (ms)          |         21.4 |  **15.1** |   22.1 |
| E2E median (ms)           |       1074.0 | **620.8** |  810.7 |
| Throughput median (tok/s) |         31.7 |  **57.9** |   42.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        404.2 | **132.0** |  138.3 |
| TPOT median (ms)          |         44.7 |  **33.1** |   47.5 |
| E2E median (ms)           |        612.8 | **271.9** |  358.3 |
| Throughput median (tok/s) |          8.7 |  **18.0** |   13.1 |
| Correctness               |          98% |       99% |    99% |
