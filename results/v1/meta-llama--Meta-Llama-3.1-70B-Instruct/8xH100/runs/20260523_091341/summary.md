# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 AM PT, May 23 2026

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
| torchinferno |     325.4s (5.4m) | `9f91b40` |
| vllm         |   1223.8s (20.4m) | `3f3e862` |
| sglang       | **188.0s (3.1m)** | `774b29d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        294.9 |    161.9 | **139.1** |
| TPOT median (ms)          |        154.6 | **54.0** |      75.1 |
| E2E median (ms)           |        388.4 |    219.4 | **208.5** |
| Throughput median (tok/s) |          3.8 |  **6.7** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        238.5 |     209.9 | **197.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        306.9 | **300.0** |     333.7 |
| Throughput median (tok/s) |          3.3 |   **3.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        798.1 |     165.7 | **161.8** |
| TPOT median (ms)          |        149.7 |  **55.3** |      99.3 |
| E2E median (ms)           |        899.9 | **216.4** |     262.0 |
| Throughput median (tok/s) |          1.6 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.6** |   73.6 |
| TPOT median (ms)          |            - | **26.9** |   59.3 |
| E2E median (ms)           |            - | **77.6** |  140.8 |
| Throughput median (tok/s) |            - | **15.6** |    9.9 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.9 | **67.2** |
| TPOT median (ms)          |            - |  **15.0** |     22.0 |
| E2E median (ms)           |            - | **627.9** |    823.0 |
| Throughput median (tok/s) |            - |  **58.7** |     42.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        443.8 |     133.2 | **127.9** |
| TPOT median (ms)          |        101.4 |  **30.2** |      51.1 |
| E2E median (ms)           |        531.7 | **288.3** |     353.6 |
| Throughput median (tok/s) |          2.9 |  **18.2** |      13.2 |
| Correctness               |          99% |       98% |       99% |
