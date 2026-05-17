# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:09 PM PT, May 16 2026

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
| torchinferno |     366.6s (6.1m) | `db749af` |
| vllm         |   1123.7s (18.7m) | `504a26c` |
| sglang       | **166.7s (2.8m)** | `229cade` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.6 |     156.3 | **146.4** |
| TPOT median (ms)          |        147.6 |  **53.9** |      70.7 |
| E2E median (ms)           |        367.3 | **210.7** |     213.3 |
| Throughput median (tok/s) |          4.0 |   **6.8** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        271.0 | **185.9** |  202.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        306.5 | **207.0** |  342.1 |
| Throughput median (tok/s) |          3.3 |   **4.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        538.3 |     166.0 | **157.9** |
| TPOT median (ms)          |        142.8 |  **58.7** |     104.9 |
| E2E median (ms)           |        660.6 | **208.6** |     256.2 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        387.4 | **58.3** |   77.7 |
| TPOT median (ms)          |        127.4 | **26.7** |   48.0 |
| E2E median (ms)           |        492.3 | **78.7** |  143.2 |
| Throughput median (tok/s) |          2.6 | **15.6** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      69.3 | **67.6** |
| TPOT median (ms)          |            - |  **14.9** |     21.9 |
| E2E median (ms)           |            - | **622.1** |    811.2 |
| Throughput median (tok/s) |            - |  **58.8** |     42.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        369.1 | **127.2** |  130.5 |
| TPOT median (ms)          |        104.4 |  **30.9** |   49.1 |
| E2E median (ms)           |        456.7 | **265.4** |  353.2 |
| Throughput median (tok/s) |          3.0 |  **18.5** |   13.3 |
| Correctness               |          98% |       98% |    99% |
