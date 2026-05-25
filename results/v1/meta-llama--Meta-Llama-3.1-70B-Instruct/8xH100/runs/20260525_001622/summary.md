# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     304.4s (5.1m) | `9f91b40` |
| vllm         |   1267.2s (21.1m) | `d0a100c` |
| sglang       | **208.4s (3.5m)** | `ed179bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.2 |     154.2 | **141.2** |
| TPOT median (ms)          |        153.7 |  **56.5** |      73.9 |
| E2E median (ms)           |        385.6 | **206.2** |     212.8 |
| Throughput median (tok/s) |          3.8 |   **7.2** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        273.1 |     217.1 | **211.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        308.6 | **238.5** |     352.0 |
| Throughput median (tok/s) |          3.2 |   **4.2** |       2.8 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        682.8 |     171.7 | **162.2** |
| TPOT median (ms)          |         99.2 |  **58.6** |     108.2 |
| E2E median (ms)           |        777.9 | **218.6** |     263.0 |
| Throughput median (tok/s) |          1.5 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.9** |   76.3 |
| TPOT median (ms)          |            - | **26.9** |   65.2 |
| E2E median (ms)           |            - | **78.3** |  159.8 |
| Throughput median (tok/s) |            - | **15.7** |    9.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.6 | **68.6** |
| TPOT median (ms)          |            - |  **15.0** |     22.3 |
| E2E median (ms)           |            - | **605.9** |    835.0 |
| Throughput median (tok/s) |            - |  **59.1** |     42.3 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        414.4 |     134.3 | **132.0** |
| TPOT median (ms)          |         84.3 |  **31.4** |      53.9 |
| E2E median (ms)           |        490.7 | **269.5** |     364.5 |
| Throughput median (tok/s) |          2.9 |  **18.5** |      13.0 |
| Correctness               |          99% |       99% |       99% |
