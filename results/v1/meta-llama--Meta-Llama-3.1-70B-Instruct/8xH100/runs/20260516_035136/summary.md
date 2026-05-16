# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:19 PM PT, May 15 2026

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
| torchinferno |     284.8s (4.7m) | `cbfd345` |
| vllm         |    965.2s (16.1m) | `32b7177` |
| sglang       | **162.4s (2.7m)** | `a741d0c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        282.9 |    163.7 | **133.7** |
| TPOT median (ms)          |        150.5 | **57.6** |      73.0 |
| E2E median (ms)           |        373.8 |    214.8 | **200.3** |
| Throughput median (tok/s) |          3.8 |  **6.6** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        293.3 | **196.2** |  197.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        334.4 | **227.7** |  328.6 |
| Throughput median (tok/s) |          3.0 |   **4.4** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        525.5 |     172.0 | **161.9** |
| TPOT median (ms)          |        149.4 |  **56.7** |      96.7 |
| E2E median (ms)           |        627.6 | **227.3** |     257.6 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        338.8 | **58.4** |   74.7 |
| TPOT median (ms)          |        131.9 | **27.9** |   56.1 |
| E2E median (ms)           |        439.0 | **79.2** |  140.5 |
| Throughput median (tok/s) |          3.5 | **15.4** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.7 | **66.0** |
| TPOT median (ms)          |            - |  **15.0** |     22.1 |
| E2E median (ms)           |            - | **617.1** |    819.4 |
| Throughput median (tok/s) |            - |  **58.6** |     42.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        360.1 |     132.2 | **126.8** |
| TPOT median (ms)          |        108.0 |  **31.4** |      49.6 |
| E2E median (ms)           |        443.7 | **273.2** |     349.3 |
| Throughput median (tok/s) |          3.1 |  **18.3** |      13.4 |
| Correctness               |          98% |       99% |       99% |
