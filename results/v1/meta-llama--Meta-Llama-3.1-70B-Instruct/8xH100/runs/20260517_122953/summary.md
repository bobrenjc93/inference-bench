# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:09 AM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     347.3s (5.8m) | `1cdab3f` |
| vllm         |   1006.5s (16.8m) | `0fa8884` |
| sglang       | **161.5s (2.7m)** | `be3c425` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.0 |     157.8 | **136.9** |
| TPOT median (ms)          |        149.7 |  **55.7** |      73.0 |
| E2E median (ms)           |        369.4 | **201.8** |     203.6 |
| Throughput median (tok/s) |          4.1 |   **7.1** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        295.4 | **187.8** |  199.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        329.3 | **210.9** |  336.4 |
| Throughput median (tok/s) |          3.0 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        535.9 |     172.2 | **153.9** |
| TPOT median (ms)          |        123.3 |  **45.2** |     101.7 |
| E2E median (ms)           |        624.3 | **218.7** |     252.0 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        334.4 | **57.2** |   73.1 |
| TPOT median (ms)          |        130.6 | **27.1** |   62.9 |
| E2E median (ms)           |        430.2 | **77.9** |  154.3 |
| Throughput median (tok/s) |          3.0 | **15.9** |    9.4 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.0 | **68.7** |
| TPOT median (ms)          |            - |  **15.0** |     22.4 |
| E2E median (ms)           |            - | **619.5** |    824.0 |
| Throughput median (tok/s) |            - |  **58.5** |     42.0 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        362.7 |     129.0 | **126.4** |
| TPOT median (ms)          |        100.9 |  **28.6** |      52.0 |
| E2E median (ms)           |        438.3 | **265.8** |     354.1 |
| Throughput median (tok/s) |          3.0 |  **18.5** |      13.1 |
| Correctness               |          98% |       98% |       99% |
