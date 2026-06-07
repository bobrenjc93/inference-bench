# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, Jun 7 2026

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
| torchinferno |     329.9s (5.5m) | `e19c01f` |
| vllm         |   1255.7s (20.9m) | `4dcd10e` |
| sglang       | **188.2s (3.1m)** | `02be2e7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        338.9 |    161.1 | **146.8** |
| TPOT median (ms)          |         96.5 | **62.3** |      73.7 |
| E2E median (ms)           |        416.6 |    219.8 | **215.1** |
| Throughput median (tok/s) |          2.9 |  **6.7** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        368.4 | **191.9** |  199.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        516.8 | **244.7** |  339.0 |
| Throughput median (tok/s) |          1.9 |   **4.1** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        706.7 |     173.6 | **161.9** |
| TPOT median (ms)          |         67.0 |  **62.2** |     101.4 |
| E2E median (ms)           |        759.5 | **228.2** |     253.7 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        468.4 | **61.3** |   77.9 |
| TPOT median (ms)          |         60.2 | **27.9** |   45.9 |
| E2E median (ms)           |        518.5 | **83.0** |  137.3 |
| Throughput median (tok/s) |          2.7 | **14.7** |   10.1 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        513.1 |  **68.9** |   80.1 |
| TPOT median (ms)          |         21.5 |  **15.2** |   23.1 |
| E2E median (ms)           |       1247.8 | **610.1** |  866.9 |
| Throughput median (tok/s) |         27.3 |  **58.5** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        479.1 | **131.4** |  133.3 |
| TPOT median (ms)          |         49.0 |  **33.5** |   48.8 |
| E2E median (ms)           |        691.8 | **277.2** |  362.4 |
| Throughput median (tok/s) |          7.3 |  **18.0** |   12.8 |
| Correctness               |          98% |       98% |    98% |
