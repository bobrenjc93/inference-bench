# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:01 AM PT, May 16 2026

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
| torchinferno | **104.2s (1.7m)** | `db749af` |
| vllm         |   1241.2s (20.7m) | `8a56da3` |
| sglang       |     176.4s (2.9m) | `2fc217d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        320.2 |    167.5 | **150.3** |
| TPOT median (ms)          |        161.3 | **59.2** |      73.6 |
| E2E median (ms)           |        423.5 |    229.2 | **220.8** |
| Throughput median (tok/s) |          3.3 |  **6.3** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.6 | **203.5** |  222.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        321.6 | **234.0** |  362.1 |
| Throughput median (tok/s) |          3.1 |   **4.3** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1023.2 |     187.3 | **163.6** |
| TPOT median (ms)          |        162.4 |  **60.5** |     113.9 |
| E2E median (ms)           |       1122.1 | **239.3** |     286.4 |
| Throughput median (tok/s) |          1.2 |   **5.8** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        381.0 | **61.9** |   78.4 |
| TPOT median (ms)          |        138.2 | **27.8** |   53.1 |
| E2E median (ms)           |        499.6 | **82.8** |  142.0 |
| Throughput median (tok/s) |          2.8 | **15.1** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.1 | **75.8** |
| TPOT median (ms)          |            - |  **15.0** |     22.2 |
| E2E median (ms)           |            - | **632.0** |    834.8 |
| Throughput median (tok/s) |            - |  **57.8** |     41.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        503.8 |     139.2 | **138.0** |
| TPOT median (ms)          |        115.4 |  **32.5** |      52.6 |
| E2E median (ms)           |        591.7 | **283.4** |     369.2 |
| Throughput median (tok/s) |          2.6 |  **17.8** |      12.8 |
| Correctness               |          98% |       99% |       99% |
