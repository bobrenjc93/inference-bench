# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 8 2026

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
| torchinferno |     402.0s (6.7m) | `7ea9984` |
| vllm         |   1318.1s (22.0m) | `469f3dc` |
| sglang       | **195.2s (3.3m)** | `13dda3b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        309.6 |    167.1 | **146.7** |
| TPOT median (ms)          |         93.7 | **55.7** |      67.8 |
| E2E median (ms)           |        387.4 |    218.2 | **211.9** |
| Throughput median (tok/s) |          3.1 |  **6.8** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        401.8 | **210.7** |  238.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        558.7 | **233.1** |  377.1 |
| Throughput median (tok/s) |          1.8 |   **4.3** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        739.8 |     176.6 | **163.6** |
| TPOT median (ms)          |         61.4 |  **52.7** |     106.9 |
| E2E median (ms)           |        784.5 | **219.6** |     263.3 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        464.0 | **62.6** |   86.5 |
| TPOT median (ms)          |         62.6 | **28.9** |   45.8 |
| E2E median (ms)           |        502.4 | **84.6** |  143.9 |
| Throughput median (tok/s) |          2.7 | **14.0** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        502.0 |  **74.0** |   78.4 |
| TPOT median (ms)          |         21.7 |  **14.8** |   24.0 |
| E2E median (ms)           |       1276.3 | **605.8** |  896.9 |
| Throughput median (tok/s) |         27.4 |  **59.6** |   38.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        483.4 | **138.2** |  142.7 |
| TPOT median (ms)          |         47.9 |  **30.4** |   48.9 |
| E2E median (ms)           |        701.9 | **272.2** |  378.6 |
| Throughput median (tok/s) |          7.3 |  **18.2** |   12.3 |
| Correctness               |          99% |       99% |    99% |
