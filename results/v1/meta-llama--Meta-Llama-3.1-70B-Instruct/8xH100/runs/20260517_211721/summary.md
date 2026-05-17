# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:09 PM PT, May 17 2026

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
| torchinferno |     409.3s (6.8m) | `13d21ac` |
| vllm         |   1089.1s (18.2m) | `966903e` |
| sglang       | **166.7s (2.8m)** | `89e501c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        288.9 |    160.1 | **140.2** |
| TPOT median (ms)          |        149.6 | **57.1** |      74.7 |
| E2E median (ms)           |        392.7 |    214.9 | **206.8** |
| Throughput median (tok/s) |          3.9 |  **7.1** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        284.6 | **199.6** |  205.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        308.2 | **219.2** |  342.0 |
| Throughput median (tok/s) |          3.2 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        529.9 |     170.9 | **153.9** |
| TPOT median (ms)          |        118.6 |  **59.4** |     101.8 |
| E2E median (ms)           |        626.7 | **226.2** |     249.8 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        364.2 | **57.8** |   72.3 |
| TPOT median (ms)          |        127.6 | **27.3** |   67.9 |
| E2E median (ms)           |        462.2 | **78.6** |  154.7 |
| Throughput median (tok/s) |          2.9 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.9 | **63.5** |
| TPOT median (ms)          |            - |  **15.2** |     22.5 |
| E2E median (ms)           |            - | **622.0** |    843.5 |
| Throughput median (tok/s) |            - |  **58.5** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        366.9 |     131.4 | **127.1** |
| TPOT median (ms)          |         99.0 |  **31.8** |      53.4 |
| E2E median (ms)           |        447.4 | **272.2** |     359.3 |
| Throughput median (tok/s) |          3.0 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       98% |
