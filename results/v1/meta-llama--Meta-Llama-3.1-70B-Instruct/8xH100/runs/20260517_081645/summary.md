# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:09 AM PT, May 17 2026

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
| torchinferno |     332.5s (5.5m) | `26df1b4` |
| vllm         |   1053.8s (17.6m) | `ff712f6` |
| sglang       | **162.1s (2.7m)** | `e547f3f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        276.0 |    153.5 | **133.7** |
| TPOT median (ms)          |        149.3 | **53.0** |      71.0 |
| E2E median (ms)           |        365.5 |    201.0 | **199.5** |
| Throughput median (tok/s) |          3.9 |  **7.4** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.9 | **184.6** |  202.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        318.7 | **207.9** |  338.6 |
| Throughput median (tok/s) |          3.1 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        524.5 |     177.6 | **162.5** |
| TPOT median (ms)          |        119.3 |  **56.4** |      98.3 |
| E2E median (ms)           |        619.7 | **225.0** |     250.9 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        341.4 | **57.6** |   74.7 |
| TPOT median (ms)          |        131.0 | **26.9** |   62.1 |
| E2E median (ms)           |        458.9 | **78.2** |  148.7 |
| Throughput median (tok/s) |          3.0 | **15.6** |    9.5 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.0 | **65.5** |
| TPOT median (ms)          |            - |  **14.9** |     22.1 |
| E2E median (ms)           |            - | **607.0** |    816.7 |
| Throughput median (tok/s) |            - |  **59.2** |     42.7 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        358.4 |     128.3 | **127.7** |
| TPOT median (ms)          |         99.9 |  **30.2** |      50.7 |
| E2E median (ms)           |        440.7 | **263.8** |     350.9 |
| Throughput median (tok/s) |          3.0 |  **18.6** |      13.3 |
| Correctness               |          98% |       99% |       98% |
