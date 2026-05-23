# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:02 PM PT, May 22 2026

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
| torchinferno | **95.5s (1.6m)** | `9f91b40` |
| vllm         |  1359.2s (22.7m) | `367cb81` |
| sglang       |    179.5s (3.0m) | `7b7f106` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        282.6 |    170.2 | **146.0** |
| TPOT median (ms)          |        161.0 | **61.3** |      82.5 |
| E2E median (ms)           |        381.4 |    229.2 | **221.0** |
| Throughput median (tok/s) |          3.9 |  **6.4** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.0 | **195.5** |  223.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        337.2 | **219.0** |  374.9 |
| Throughput median (tok/s) |          3.0 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        997.2 |     183.0 | **170.5** |
| TPOT median (ms)          |        125.2 |  **57.6** |     101.3 |
| E2E median (ms)           |       1149.5 | **237.2** |     274.1 |
| Throughput median (tok/s) |          1.2 |   **5.9** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        415.9 | **61.7** |   76.7 |
| TPOT median (ms)          |        134.8 | **27.8** |   57.4 |
| E2E median (ms)           |        508.7 | **83.6** |  147.8 |
| Throughput median (tok/s) |          2.7 | **14.9** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      79.1 | **73.8** |
| TPOT median (ms)          |            - |  **15.0** |     22.1 |
| E2E median (ms)           |            - | **621.6** |    810.1 |
| Throughput median (tok/s) |            - |  **58.5** |     41.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        494.2 | **137.9** |  138.0 |
| TPOT median (ms)          |        105.3 |  **32.3** |   52.7 |
| E2E median (ms)           |        594.2 | **278.1** |  365.6 |
| Throughput median (tok/s) |          2.7 |  **18.0** |   12.8 |
| Correctness               |          98% |       99% |    99% |
