# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, May 27 2026

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
| torchinferno |     401.6s (6.7m) | `42db70d` |
| vllm         |   1315.2s (21.9m) | `33e94fc` |
| sglang       | **234.6s (3.9m)** | `b437a0d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |       4088.8 |    176.9 | **147.3** |
| TPOT median (ms)          |       2753.5 | **67.5** |      82.3 |
| E2E median (ms)           |       5696.4 |    232.5 | **221.0** |
| Throughput median (tok/s) |          0.2 |  **6.3** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **201.5** |  204.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **221.3** |  345.6 |
| Throughput median (tok/s) |            - |   **4.5** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 400 Bad Request\r\n')`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     174.9 | **162.1** |
| TPOT median (ms)          |            - |  **56.2** |      97.2 |
| E2E median (ms)           |            - | **225.4** |     261.2 |
| Throughput median (tok/s) |            - |   **6.3** |       5.0 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.4** |   79.6 |
| TPOT median (ms)          |            - | **27.7** |   43.1 |
| E2E median (ms)           |            - | **79.3** |  136.9 |
| Throughput median (tok/s) |            - | **15.4** |   10.2 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **67.3** |   74.0 |
| TPOT median (ms)          |            - |  **15.1** |   23.8 |
| E2E median (ms)           |            - | **602.2** |  888.2 |
| Throughput median (tok/s) |            - |  **59.2** |   39.3 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       4088.8 |     135.8 | **133.4** |
| TPOT median (ms)          |       2753.5 |  **33.3** |      49.3 |
| E2E median (ms)           |       5696.4 | **272.1** |     370.6 |
| Throughput median (tok/s) |          0.2 |  **18.4** |      12.6 |
| Correctness               |          98% |       99% |       99% |
