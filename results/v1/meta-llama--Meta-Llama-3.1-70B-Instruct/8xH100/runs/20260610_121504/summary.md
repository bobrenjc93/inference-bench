# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 10 2026

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
| torchinferno |     353.0s (5.9m) | `a870596` |
| vllm         |   1365.7s (22.8m) | `9ad08c4` |
| sglang       | **197.1s (3.3m)** | `4faaa9b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        274.1 |     169.1 | **156.4** |
| TPOT median (ms)          |         91.2 |  **60.2** |      71.3 |
| E2E median (ms)           |        367.1 | **223.4** |     223.7 |
| Throughput median (tok/s) |          3.2 |   **6.5** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        405.0 | **201.2** |  212.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        551.0 | **222.6** |  347.2 |
| Throughput median (tok/s) |          1.8 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        640.0 |     182.2 | **174.1** |
| TPOT median (ms)          |         63.8 |  **62.2** |     105.4 |
| E2E median (ms)           |        710.0 | **237.1** |     280.7 |
| Throughput median (tok/s) |          1.7 |   **5.8** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        415.7 | **60.8** |   85.9 |
| TPOT median (ms)          |         61.7 | **27.8** |   44.1 |
| E2E median (ms)           |        464.2 | **83.6** |  149.0 |
| Throughput median (tok/s) |          3.1 | **14.5** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        199.8 |  **80.3** |   82.4 |
| TPOT median (ms)          |         26.5 |  **15.2** |   24.2 |
| E2E median (ms)           |       1282.0 | **627.5** |  917.8 |
| Throughput median (tok/s) |         30.5 |  **57.8** |   38.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        386.9 | **138.7** |  142.2 |
| TPOT median (ms)          |         48.6 |  **33.1** |   49.0 |
| E2E median (ms)           |        674.9 | **278.9** |  383.7 |
| Throughput median (tok/s) |          8.1 |  **17.8** |   12.1 |
| Correctness               |          98% |       98% |    99% |
