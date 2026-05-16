# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:07 PM PT, May 15 2026

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
| torchinferno |     337.4s (5.6m) | `cbfd345` |
| vllm         |   1072.8s (17.9m) | `39c67d7` |
| sglang       | **159.5s (2.7m)** | `b674007` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        284.0 |    165.5 | **137.9** |
| TPOT median (ms)          |        146.2 | **56.4** |      75.4 |
| E2E median (ms)           |        367.9 |    219.9 | **207.4** |
| Throughput median (tok/s) |          4.0 |  **6.2** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        281.7 |     216.0 | **201.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        314.2 | **300.3** |     336.1 |
| Throughput median (tok/s) |          3.2 |   **3.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        528.9 |     174.7 | **160.8** |
| TPOT median (ms)          |        117.6 |  **59.2** |      98.0 |
| E2E median (ms)           |        634.1 | **231.2** |     260.1 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        294.3 | **57.7** |   75.3 |
| TPOT median (ms)          |        128.9 | **26.4** |   60.4 |
| E2E median (ms)           |        381.3 | **77.9** |  147.2 |
| Throughput median (tok/s) |          3.7 | **15.8** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      78.5 | **63.9** |
| TPOT median (ms)          |            - |  **14.9** |     22.8 |
| E2E median (ms)           |            - | **611.0** |    831.5 |
| Throughput median (tok/s) |            - |  **58.5** |     41.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        347.2 |     138.5 | **127.9** |
| TPOT median (ms)          |         98.2 |  **31.4** |      51.3 |
| E2E median (ms)           |        424.4 | **288.1** |     356.5 |
| Throughput median (tok/s) |          3.2 |  **18.0** |      13.1 |
| Correctness               |          98% |       99% |       99% |
