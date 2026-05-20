# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:02 AM PT, May 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     269.6s (4.5m) | `9f91b40` |
| vllm         |   1079.7s (18.0m) | `87e3145` |
| sglang       | **192.4s (3.2m)** | `1bd4f94` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        294.2 |    160.1 | **141.2** |
| TPOT median (ms)          |        150.4 | **55.6** |      71.8 |
| E2E median (ms)           |        405.4 |    211.2 | **204.9** |
| Throughput median (tok/s) |          3.9 |  **7.2** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.8 | **196.0** |  202.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        313.8 | **228.0** |  329.0 |
| Throughput median (tok/s) |          3.2 |   **4.4** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        541.6 |     169.7 | **156.1** |
| TPOT median (ms)          |        110.7 |  **59.2** |      94.6 |
| E2E median (ms)           |        627.8 | **214.9** |     255.0 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        342.5 | **58.4** |   77.6 |
| TPOT median (ms)          |        129.1 | **26.9** |   48.4 |
| E2E median (ms)           |        444.6 | **78.8** |  133.4 |
| Throughput median (tok/s) |          3.0 | **15.5** |    9.9 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **64.6** |   66.1 |
| TPOT median (ms)          |            - |  **15.0** |   21.9 |
| E2E median (ms)           |            - | **597.9** |  818.2 |
| Throughput median (tok/s) |            - |  **59.4** |   43.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        366.8 |     129.8 | **128.6** |
| TPOT median (ms)          |         97.5 |  **31.3** |      47.4 |
| E2E median (ms)           |        447.9 | **266.2** |     348.1 |
| Throughput median (tok/s) |          3.0 |  **18.5** |      13.4 |
| Correctness               |          98% |       99% |       99% |
