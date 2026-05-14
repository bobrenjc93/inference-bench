# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, May 14 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **91.2s (1.5m)** | `58e4246` |
| vllm         |  1222.7s (20.4m) | `ae4f59f` |
| sglang       |    177.1s (3.0m) | `3fc60e5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        345.1 |    168.0 | **143.1** |
| TPOT median (ms)          |        177.2 | **55.3** |      77.2 |
| E2E median (ms)           |        448.3 |    224.0 | **216.6** |
| Throughput median (tok/s) |          3.1 |  **6.5** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        316.9 | **193.0** |  215.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        371.2 | **221.9** |  361.8 |
| Throughput median (tok/s) |          2.7 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1396.0 |     180.7 | **168.4** |
| TPOT median (ms)          |        224.0 |  **51.9** |     107.3 |
| E2E median (ms)           |       1585.6 | **232.8** |     282.0 |
| Throughput median (tok/s) |          0.9 |   **6.0** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        434.3 | **61.2** |   79.7 |
| TPOT median (ms)          |        254.7 | **27.5** |   51.7 |
| E2E median (ms)           |        662.2 | **82.2** |  140.5 |
| Throughput median (tok/s) |          2.3 | **14.8** |    9.4 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      88.9 | **72.8** |
| TPOT median (ms)          |            - |  **15.0** |     21.9 |
| E2E median (ms)           |            - | **651.8** |    879.1 |
| Throughput median (tok/s) |            - |  **56.2** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        623.1 |     138.4 | **135.9** |
| TPOT median (ms)          |        164.0 |  **29.9** |      51.6 |
| E2E median (ms)           |        766.8 | **282.6** |     376.0 |
| Throughput median (tok/s) |          2.3 |  **17.6** |      12.9 |
| Correctness               |          98% |       99% |       98% |
