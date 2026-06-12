# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 12 2026

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
| torchinferno |     411.9s (6.9m) | `065275c` |
| vllm         |   1383.8s (23.1m) | `f1e13f7` |
| sglang       | **243.6s (4.1m)** | `18989f3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        311.2 |     156.3 | **147.4** |
| TPOT median (ms)          |         95.2 |  **51.8** |      78.0 |
| E2E median (ms)           |        390.0 | **202.2** |     219.4 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        407.1 | **188.3** |  229.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        543.4 | **227.0** |  370.5 |
| Throughput median (tok/s) |          1.8 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        703.5 |     177.6 | **170.2** |
| TPOT median (ms)          |         71.8 |  **56.9** |      99.4 |
| E2E median (ms)           |        762.7 | **231.8** |     268.6 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        394.6 | **61.7** |   80.0 |
| TPOT median (ms)          |         64.3 | **28.2** |   59.7 |
| E2E median (ms)           |        443.9 | **83.3** |  151.1 |
| Throughput median (tok/s) |          3.2 | **14.4** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.7 |  **66.3** |   76.7 |
| TPOT median (ms)          |         26.8 |  **15.1** |   24.0 |
| E2E median (ms)           |       1255.1 | **604.7** |  903.8 |
| Throughput median (tok/s) |         30.3 |  **59.2** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        401.8 | **130.0** |  140.7 |
| TPOT median (ms)          |         51.6 |  **30.4** |   52.2 |
| E2E median (ms)           |        679.0 | **269.8** |  382.7 |
| Throughput median (tok/s) |          8.1 |  **18.3** |   12.4 |
| Correctness               |          99% |       98% |    98% |
