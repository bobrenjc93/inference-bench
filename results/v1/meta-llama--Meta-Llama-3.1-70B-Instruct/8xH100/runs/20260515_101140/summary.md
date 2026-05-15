# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 AM PT, May 15 2026

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
| torchinferno |     343.3s (5.7m) | `d648af4` |
| vllm         |   1087.5s (18.1m) | `1dc3fe0` |
| sglang       | **164.0s (2.7m)** | `eec5ba2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        304.0 |    156.2 | **136.2** |
| TPOT median (ms)          |        157.6 | **57.3** |      72.6 |
| E2E median (ms)           |        393.4 |    208.4 | **204.9** |
| Throughput median (tok/s) |          3.7 |  **7.0** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        302.2 | **201.4** |  203.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        350.0 | **224.3** |  341.1 |
| Throughput median (tok/s) |          2.9 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        549.2 |     170.1 | **154.2** |
| TPOT median (ms)          |        187.5 |  **61.4** |      96.8 |
| E2E median (ms)           |        647.0 | **222.8** |     255.7 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        357.8 | **58.4** |   73.9 |
| TPOT median (ms)          |        132.9 | **26.5** |   58.9 |
| E2E median (ms)           |        468.9 | **79.8** |  144.6 |
| Throughput median (tok/s) |          2.9 | **15.8** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.7 | **65.2** |
| TPOT median (ms)          |            - |  **14.9** |     22.6 |
| E2E median (ms)           |            - | **607.3** |    838.1 |
| Throughput median (tok/s) |            - |  **59.1** |     41.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        378.3 |     131.0 | **126.5** |
| TPOT median (ms)          |        119.5 |  **32.0** |      50.2 |
| E2E median (ms)           |        464.8 | **268.5** |     356.9 |
| Throughput median (tok/s) |          2.8 |  **18.5** |      13.2 |
| Correctness               |          98% |       98% |       99% |
