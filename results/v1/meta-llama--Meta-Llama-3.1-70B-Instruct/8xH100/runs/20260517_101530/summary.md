# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:08 AM PT, May 17 2026

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
| torchinferno |     329.2s (5.5m) | `1cdab3f` |
| vllm         |   1044.6s (17.4m) | `0fa8884` |
| sglang       | **163.7s (2.7m)** | `be3c425` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        283.5 |    160.0 | **135.2** |
| TPOT median (ms)          |        150.4 | **55.1** |      73.0 |
| E2E median (ms)           |        374.1 |    212.6 | **204.9** |
| Throughput median (tok/s) |          3.8 |  **7.0** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.3 |     202.1 | **199.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        308.1 | **225.8** |     328.0 |
| Throughput median (tok/s) |          3.2 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        532.2 |     176.9 | **152.4** |
| TPOT median (ms)          |         99.0 |  **62.2** |     109.5 |
| E2E median (ms)           |        623.2 | **230.7** |     247.4 |
| Throughput median (tok/s) |          2.2 |   **6.1** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        378.4 | **58.9** |   76.7 |
| TPOT median (ms)          |        130.5 | **27.5** |   51.8 |
| E2E median (ms)           |        479.9 | **79.3** |  136.6 |
| Throughput median (tok/s) |          3.0 | **15.3** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      65.9 | **65.7** |
| TPOT median (ms)          |            - |  **15.0** |     22.2 |
| E2E median (ms)           |            - | **599.3** |    844.5 |
| Throughput median (tok/s) |            - |  **59.4** |     42.3 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        370.6 |     132.7 | **125.9** |
| TPOT median (ms)          |         95.0 |  **32.0** |      51.3 |
| E2E median (ms)           |        446.3 | **269.5** |     352.3 |
| Throughput median (tok/s) |          3.0 |  **18.4** |      13.3 |
| Correctness               |          98% |       99% |       99% |
