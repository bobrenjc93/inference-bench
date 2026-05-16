# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:09 AM PT, May 16 2026

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
| torchinferno |     366.4s (6.1m) | `db749af` |
| vllm         |   1129.3s (18.8m) | `8a56da3` |
| sglang       | **175.7s (2.9m)** | `0be5390` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        285.8 |    165.2 | **143.8** |
| TPOT median (ms)          |        150.0 | **58.2** |      73.8 |
| E2E median (ms)           |        370.9 |    218.9 | **213.5** |
| Throughput median (tok/s) |          3.9 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.0 | **203.2** |  207.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        317.1 | **227.6** |  340.6 |
| Throughput median (tok/s) |          3.2 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        514.3 |     175.8 | **153.5** |
| TPOT median (ms)          |        106.3 |  **65.4** |     100.0 |
| E2E median (ms)           |        619.3 | **238.0** |     250.7 |
| Throughput median (tok/s) |          2.2 |   **6.0** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        366.2 | **58.3** |   73.4 |
| TPOT median (ms)          |        133.9 | **27.0** |   65.8 |
| E2E median (ms)           |        460.6 | **78.5** |  151.0 |
| Throughput median (tok/s) |          3.1 | **15.6** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.0 | **66.8** |
| TPOT median (ms)          |            - |  **15.0** |     22.4 |
| E2E median (ms)           |            - | **608.2** |    846.2 |
| Throughput median (tok/s) |            - |  **58.9** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        364.3 |     134.5 | **129.0** |
| TPOT median (ms)          |         97.6 |  **33.1** |      52.4 |
| E2E median (ms)           |        442.0 | **274.2** |     360.4 |
| Throughput median (tok/s) |          3.1 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       98% |
