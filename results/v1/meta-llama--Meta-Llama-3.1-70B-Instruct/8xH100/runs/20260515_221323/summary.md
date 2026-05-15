# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 PM PT, May 15 2026

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
| torchinferno |     404.3s (6.7m) | `cbfd345` |
| vllm         |   1113.4s (18.6m) | `bd9dbe6` |
| sglang       | **161.3s (2.7m)** | `7cb4669` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.8 |     153.1 | **135.4** |
| TPOT median (ms)          |        145.9 |  **52.9** |      75.8 |
| E2E median (ms)           |        362.2 | **201.4** |     205.1 |
| Throughput median (tok/s) |          3.9 |   **7.2** |       6.0 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        305.6 | **192.4** |  200.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        347.6 | **213.8** |  335.2 |
| Throughput median (tok/s) |          2.9 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        525.2 |     174.7 | **160.0** |
| TPOT median (ms)          |        122.8 |  **45.5** |     100.9 |
| E2E median (ms)           |        603.9 | **214.4** |     258.7 |
| Throughput median (tok/s) |          2.1 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        314.9 | **57.1** |   72.8 |
| TPOT median (ms)          |        130.6 | **26.7** |   61.4 |
| E2E median (ms)           |        418.7 | **77.4** |  151.6 |
| Throughput median (tok/s) |          3.3 | **15.9** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.2 | **63.9** |
| TPOT median (ms)          |            - |  **14.9** |     22.2 |
| E2E median (ms)           |            - | **616.0** |    836.3 |
| Throughput median (tok/s) |            - |  **59.2** |     42.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        356.4 |     129.5 | **126.6** |
| TPOT median (ms)          |         99.8 |  **28.0** |      52.1 |
| E2E median (ms)           |        433.1 | **264.6** |     357.4 |
| Throughput median (tok/s) |          3.1 |  **18.7** |      13.3 |
| Correctness               |          98% |       99% |       99% |
