# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 AM PT, May 24 2026

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
| torchinferno |     273.1s (4.6m) | `9f91b40` |
| vllm         |   1183.0s (19.7m) | `d56285c` |
| sglang       | **182.5s (3.0m)** | `7f45bcd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        261.1 |    162.0 | **144.4** |
| TPOT median (ms)          |        155.1 | **59.0** |      70.2 |
| E2E median (ms)           |        369.1 |    212.8 | **211.8** |
| Throughput median (tok/s) |          4.1 |  **6.9** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        268.7 |     211.0 | **203.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        300.8 | **234.7** |     335.6 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        639.2 |     173.1 | **158.1** |
| TPOT median (ms)          |        109.1 |  **61.5** |     108.8 |
| E2E median (ms)           |        724.7 | **220.3** |     258.3 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        295.7 | **58.5** |   76.5 |
| TPOT median (ms)          |        133.0 | **27.1** |   58.6 |
| E2E median (ms)           |        386.0 | **79.3** |  142.6 |
| Throughput median (tok/s) |          3.9 | **15.7** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      74.8 | **67.2** |
| TPOT median (ms)          |            - |  **15.0** |     22.1 |
| E2E median (ms)           |            - | **624.5** |    834.8 |
| Throughput median (tok/s) |            - |  **58.2** |     42.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        366.2 |     135.9 | **129.9** |
| TPOT median (ms)          |         99.3 |  **32.5** |      51.9 |
| E2E median (ms)           |        445.2 | **274.3** |     356.6 |
| Throughput median (tok/s) |          3.3 |  **18.2** |      13.2 |
| Correctness               |          98% |       98% |       99% |
