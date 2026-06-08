# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 PM PT, Jun 8 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     355.9s (5.9m) | `a80b89c` |
| vllm         |   1299.9s (21.7m) | `2c27c29` |
| sglang       | **213.2s (3.6m)** | `ea1d190` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        293.2 |     151.7 | **148.6** |
| TPOT median (ms)          |         80.9 |  **52.8** |      72.6 |
| E2E median (ms)           |        373.3 | **200.6** |     215.8 |
| Throughput median (tok/s) |          3.2 |   **7.6** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        391.8 | **189.4** |  205.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        540.7 | **247.0** |  336.8 |
| Throughput median (tok/s) |          1.8 |   **4.0** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        767.1 |     177.2 | **163.0** |
| TPOT median (ms)          |         71.0 |  **62.8** |     100.5 |
| E2E median (ms)           |        825.2 | **236.9** |     262.0 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        495.2 | **58.6** |   78.7 |
| TPOT median (ms)          |         60.8 | **28.8** |   51.6 |
| E2E median (ms)           |        550.8 | **80.5** |  143.0 |
| Throughput median (tok/s) |          2.5 | **14.8** |    9.9 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        518.1 |  **64.9** |   78.4 |
| TPOT median (ms)          |         22.0 |  **15.1** |   24.0 |
| E2E median (ms)           |       1356.3 | **609.3** |  899.9 |
| Throughput median (tok/s) |         27.5 |  **59.4** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        493.1 | **128.4** |  134.7 |
| TPOT median (ms)          |         46.9 |  **31.9** |   49.8 |
| E2E median (ms)           |        729.3 | **274.9** |  371.5 |
| Throughput median (tok/s) |          7.3 |  **18.4** |   12.5 |
| Correctness               |          99% |       98% |    99% |
