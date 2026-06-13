# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:13 PM PT, Jun 12 2026

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
| torchinferno |     464.7s (7.7m) | `065275c` |
| vllm         |   1391.4s (23.2m) | `1a36978` |
| sglang       | **224.0s (3.7m)** | `335a9c7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        380.8 |    167.0 | **145.5** |
| TPOT median (ms)          |        100.7 | **59.9** |      75.4 |
| E2E median (ms)           |        508.1 |    221.0 | **220.2** |
| Throughput median (tok/s) |          2.6 |  **6.7** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        404.0 | **189.9** |  216.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        535.1 | **212.2** |  351.4 |
| Throughput median (tok/s) |          1.9 |   **4.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        652.0 |     176.4 | **159.9** |
| TPOT median (ms)          |         66.7 |  **63.1** |     100.2 |
| E2E median (ms)           |        722.0 | **235.1** |     250.0 |
| Throughput median (tok/s) |          1.8 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        431.5 | **61.7** |   83.6 |
| TPOT median (ms)          |         61.5 | **29.1** |   58.8 |
| E2E median (ms)           |        486.0 | **83.0** |  149.9 |
| Throughput median (tok/s) |          3.0 | **14.2** |    9.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        197.5 |  **73.6** |   80.8 |
| TPOT median (ms)          |         27.2 |  **14.8** |   23.8 |
| E2E median (ms)           |       1290.7 | **609.0** |  883.3 |
| Throughput median (tok/s) |         29.5 |  **59.1** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        413.2 | **133.7** |  137.2 |
| TPOT median (ms)          |         51.2 |  **33.4** |   51.6 |
| E2E median (ms)           |        708.4 | **272.1** |  370.9 |
| Throughput median (tok/s) |          7.8 |  **18.2** |   12.4 |
| Correctness               |          98% |       99% |    98% |
