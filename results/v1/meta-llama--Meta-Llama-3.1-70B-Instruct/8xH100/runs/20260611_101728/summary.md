# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 11 2026

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
| torchinferno |     385.9s (6.4m) | `065275c` |
| vllm         |   1346.2s (22.4m) | `0d657e4` |
| sglang       | **191.7s (3.2m)** | `22c7285` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        313.5 |     160.0 | **156.6** |
| TPOT median (ms)          |         94.4 |  **55.4** |      74.7 |
| E2E median (ms)           |        401.6 | **211.2** |     227.3 |
| Throughput median (tok/s) |          3.1 |   **7.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        407.9 | **202.7** |  207.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        556.0 | **234.1** |  341.3 |
| Throughput median (tok/s) |          1.8 |   **4.3** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        728.2 |     177.3 | **165.2** |
| TPOT median (ms)          |         66.7 |  **42.8** |      99.9 |
| E2E median (ms)           |        785.5 | **217.4** |     270.0 |
| Throughput median (tok/s) |          1.8 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        367.1 | **60.8** |   83.2 |
| TPOT median (ms)          |         58.2 | **28.5** |   42.7 |
| E2E median (ms)           |        432.2 | **83.4** |  135.7 |
| Throughput median (tok/s) |          3.4 | **14.4** |    9.7 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.4 |  **70.1** |   76.1 |
| TPOT median (ms)          |         26.2 |  **15.2** |   24.2 |
| E2E median (ms)           |       1242.5 | **611.9** |  909.5 |
| Throughput median (tok/s) |         30.8 |  **59.0** |   38.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        401.4 | **134.2** |  137.8 |
| TPOT median (ms)          |         49.1 |  **28.4** |   48.3 |
| E2E median (ms)           |        683.6 | **271.6** |  376.8 |
| Throughput median (tok/s) |          8.2 |  **18.2** |   12.2 |
| Correctness               |          98% |       98% |    98% |
