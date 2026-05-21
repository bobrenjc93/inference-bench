# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 AM PT, May 21 2026

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
| torchinferno |     249.6s (4.2m) | `9f91b40` |
| vllm         |   1118.2s (18.6m) | `1c78f76` |
| sglang       | **197.8s (3.3m)** | `b765fae` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        266.3 |    160.3 | **143.8** |
| TPOT median (ms)          |        151.4 | **58.3** |      74.7 |
| E2E median (ms)           |        361.1 |    215.0 | **214.9** |
| Throughput median (tok/s) |          4.2 |  **7.0** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        262.5 | **201.1** |  201.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        307.0 | **283.2** |  335.6 |
| Throughput median (tok/s) |          3.3 |   **3.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        672.3 |     171.6 | **161.1** |
| TPOT median (ms)          |        107.4 |  **58.3** |      97.3 |
| E2E median (ms)           |        789.9 | **219.1** |     257.8 |
| Throughput median (tok/s) |          1.6 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.1** |   74.8 |
| TPOT median (ms)          |            - | **26.8** |   61.7 |
| E2E median (ms)           |            - | **77.1** |  150.7 |
| Throughput median (tok/s) |            - | **16.0** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **64.8** |   69.0 |
| TPOT median (ms)          |            - |  **15.0** |   22.0 |
| E2E median (ms)           |            - | **596.0** |  815.1 |
| Throughput median (tok/s) |            - |  **59.9** |   42.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        400.4 |     131.0 | **130.1** |
| TPOT median (ms)          |         86.3 |  **31.7** |      51.1 |
| E2E median (ms)           |        486.0 | **278.1** |     354.8 |
| Throughput median (tok/s) |          3.0 |  **18.6** |      13.2 |
| Correctness               |          99% |       99% |       99% |
