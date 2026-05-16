# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, May 15 2026

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
| torchinferno | **87.4s (1.5m)** | `cbfd345` |
| vllm         |  1261.2s (21.0m) | `32b7177` |
| sglang       |    178.8s (3.0m) | `daade9c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        312.9 |    169.3 | **149.8** |
| TPOT median (ms)          |        155.0 | **61.0** |      72.2 |
| E2E median (ms)           |        405.3 |    230.1 | **221.3** |
| Throughput median (tok/s) |          3.5 |  **6.3** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        303.9 | **185.7** |  214.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        346.8 | **210.6** |  360.1 |
| Throughput median (tok/s) |          2.9 |   **4.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1068.4 |     188.0 | **172.2** |
| TPOT median (ms)          |        109.5 |  **52.4** |     117.4 |
| E2E median (ms)           |       1158.3 | **237.9** |     294.7 |
| Throughput median (tok/s) |          1.2 |   **6.0** |       4.5 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        368.7 | **61.5** |   83.3 |
| TPOT median (ms)          |        135.7 | **27.5** |   46.2 |
| E2E median (ms)           |        478.7 | **82.6** |  140.8 |
| Throughput median (tok/s) |          2.9 | **14.8** |    9.5 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.6 | **72.2** |
| TPOT median (ms)          |            - |  **14.9** |     22.1 |
| E2E median (ms)           |            - | **609.0** |    893.7 |
| Throughput median (tok/s) |            - |  **58.7** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        513.5 | **136.2** |  138.4 |
| TPOT median (ms)          |        100.0 |  **31.2** |   51.6 |
| E2E median (ms)           |        597.3 | **274.1** |  382.1 |
| Throughput median (tok/s) |          2.6 |  **18.1** |   12.9 |
| Correctness               |          98% |       99% |    98% |
