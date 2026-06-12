# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:08 PM PT, Jun 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     385.2s (6.4m) | `065275c` |
| vllm         |   1285.2s (21.4m) | `e0871ad` |
| sglang       | **220.9s (3.7m)** | `7074704` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        303.3 |    168.4 | **145.0** |
| TPOT median (ms)          |         90.0 | **60.3** |      76.9 |
| E2E median (ms)           |        379.5 |    223.7 | **215.0** |
| Throughput median (tok/s) |          3.2 |  **6.7** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        387.0 | **196.0** |  215.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        542.3 | **219.7** |  359.6 |
| Throughput median (tok/s) |          1.8 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        734.9 |     183.5 | **166.8** |
| TPOT median (ms)          |     **67.5** |      69.6 |      97.3 |
| E2E median (ms)           |        806.2 | **238.1** |     269.0 |
| Throughput median (tok/s) |          1.6 |   **5.8** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        353.8 | **62.7** |   84.2 |
| TPOT median (ms)          |         61.8 | **29.1** |   60.9 |
| E2E median (ms)           |        420.8 | **84.1** |  151.0 |
| Throughput median (tok/s) |          3.2 | **14.3** |    9.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.0 |  **69.7** |   79.7 |
| TPOT median (ms)          |         26.5 |  **15.1** |   24.0 |
| E2E median (ms)           |       1219.3 | **627.4** |  916.7 |
| Throughput median (tok/s) |         31.2 |  **58.4** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        394.6 | **136.1** |  138.3 |
| TPOT median (ms)          |         49.2 |  **34.8** |   51.8 |
| E2E median (ms)           |        673.6 | **278.6** |  382.2 |
| Throughput median (tok/s) |          8.2 |  **17.9** |   12.3 |
| Correctness               |          99% |       98% |    99% |
