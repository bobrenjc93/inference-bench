# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     367.1s (6.1m) | `db749af` |
| vllm         |   1110.1s (18.5m) | `ff712f6` |
| sglang       | **159.7s (2.7m)** | `6dcacb1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        282.4 |     151.4 | **137.3** |
| TPOT median (ms)          |        147.7 |  **51.5** |      72.9 |
| E2E median (ms)           |        366.1 | **198.8** |     205.0 |
| Throughput median (tok/s) |          4.1 |   **7.1** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        284.4 |     215.1 | **200.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        313.2 | **301.4** |     341.9 |
| Throughput median (tok/s) |          3.2 |   **3.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        568.1 |     175.6 | **152.9** |
| TPOT median (ms)          |        137.0 |  **64.6** |     102.4 |
| E2E median (ms)           |        653.8 | **224.7** |     251.3 |
| Throughput median (tok/s) |          2.0 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        316.8 | **57.2** |   77.6 |
| TPOT median (ms)          |        128.3 | **26.4** |   66.8 |
| E2E median (ms)           |        417.7 | **77.8** |  156.5 |
| Throughput median (tok/s) |          3.4 | **15.8** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      78.4 | **68.1** |
| TPOT median (ms)          |            - |  **15.0** |     22.1 |
| E2E median (ms)           |            - | **637.7** |    826.6 |
| Throughput median (tok/s) |            - |  **57.6** |     42.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        362.9 |     135.5 | **127.2** |
| TPOT median (ms)          |        103.2 |  **31.5** |      52.8 |
| E2E median (ms)           |        437.7 | **288.1** |     356.3 |
| Throughput median (tok/s) |          3.2 |  **18.0** |      13.2 |
| Correctness               |          98% |       99% |       98% |
