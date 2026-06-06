# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:30 PM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     321.7s (5.4m) | `75bbe35` |
| vllm         |   1320.9s (22.0m) | `2f27c9a` |
| sglang       | **199.0s (3.3m)** | `e866850` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        322.8 |     163.0 | **155.5** |
| TPOT median (ms)          |     **53.5** |      61.7 |      75.8 |
| E2E median (ms)           |        376.9 | **218.3** |     223.0 |
| Throughput median (tok/s) |          3.4 |   **6.9** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        309.8 | **198.7** |  205.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        493.1 | **222.8** |  349.3 |
| Throughput median (tok/s) |          2.0 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        733.2 |     176.2 | **169.3** |
| TPOT median (ms)          |     **61.2** |      65.9 |      99.9 |
| E2E median (ms)           |        788.1 | **233.8** |     267.5 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        414.6 | **62.7** |   80.3 |
| TPOT median (ms)          |         32.4 | **28.4** |   47.0 |
| E2E median (ms)           |        467.0 | **85.3** |  140.3 |
| Throughput median (tok/s) |          3.2 | **14.1** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        513.7 |  **69.5** |   75.5 |
| TPOT median (ms)          |         31.3 |  **15.1** |   24.0 |
| E2E median (ms)           |       1718.9 | **619.6** |  889.9 |
| Throughput median (tok/s) |         21.7 |  **57.7** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        458.8 | **134.0** |  137.1 |
| TPOT median (ms)          |         35.7 |  **34.2** |   49.3 |
| E2E median (ms)           |        768.8 | **276.0** |  374.0 |
| Throughput median (tok/s) |          6.4 |  **17.8** |   12.5 |
| Correctness               |          98% |       99% |    99% |
