# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:10 AM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     332.6s (5.5m) | `1cdab3f` |
| vllm         |   1068.9s (17.8m) | `1c8e9c0` |
| sglang       | **164.4s (2.7m)** | `89e501c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        285.4 |    162.9 | **136.9** |
| TPOT median (ms)          |        151.4 | **58.1** |      73.1 |
| E2E median (ms)           |        370.3 |    218.5 | **206.0** |
| Throughput median (tok/s) |          3.8 |  **7.0** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        289.6 |     206.5 | **193.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        309.4 | **231.0** |     332.8 |
| Throughput median (tok/s) |          3.2 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        493.4 | **169.1** |  172.1 |
| TPOT median (ms)          |        107.7 |  **54.9** |   96.5 |
| E2E median (ms)           |        601.3 | **222.2** |  270.2 |
| Throughput median (tok/s) |          2.2 |   **6.3** |    4.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        378.8 | **57.2** |   77.5 |
| TPOT median (ms)          |        130.8 | **27.0** |   49.5 |
| E2E median (ms)           |        479.6 | **77.8** |  134.0 |
| Throughput median (tok/s) |          3.0 | **15.9** |    9.8 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      67.7 | **66.6** |
| TPOT median (ms)          |            - |  **15.0** |     22.1 |
| E2E median (ms)           |            - | **599.5** |    831.3 |
| Throughput median (tok/s) |            - |  **59.6** |     42.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        361.8 |     132.7 | **129.3** |
| TPOT median (ms)          |         97.5 |  **31.0** |      48.3 |
| E2E median (ms)           |        440.2 | **269.8** |     354.9 |
| Throughput median (tok/s) |          3.0 |  **18.6** |      13.2 |
| Correctness               |          98% |       99% |       98% |
