# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, May 22 2026

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
| torchinferno |     308.0s (5.1m) | `9f91b40` |
| vllm         |   1277.8s (21.3m) | `91f5b92` |
| sglang       | **192.6s (3.2m)** | `b801a27` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        297.3 |    163.9 | **138.4** |
| TPOT median (ms)          |        148.2 | **55.6** |      79.0 |
| E2E median (ms)           |        404.5 |    216.4 | **211.1** |
| Throughput median (tok/s) |          3.4 |  **6.7** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.6 | **195.1** |  199.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        320.2 | **219.1** |  339.1 |
| Throughput median (tok/s) |          3.1 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        711.8 |     164.1 | **159.7** |
| TPOT median (ms)          |        106.3 |  **58.8** |     102.3 |
| E2E median (ms)           |        816.3 | **209.8** |     261.3 |
| Throughput median (tok/s) |          1.5 |   **6.5** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        328.9 | **58.4** |   77.3 |
| TPOT median (ms)          |        130.0 | **26.4** |   60.5 |
| E2E median (ms)           |        420.9 | **78.4** |  149.1 |
| Throughput median (tok/s) |          3.3 | **15.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      69.6 | **65.1** |
| TPOT median (ms)          |            - |  **14.9** |     22.7 |
| E2E median (ms)           |            - | **592.2** |    843.9 |
| Throughput median (tok/s) |            - |  **59.8** |     41.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        408.1 |     130.2 | **127.9** |
| TPOT median (ms)          |         96.1 |  **31.2** |      52.9 |
| E2E median (ms)           |        490.5 | **263.2** |     360.9 |
| Throughput median (tok/s) |          2.8 |  **18.6** |      13.0 |
| Correctness               |          98% |       98% |       98% |
