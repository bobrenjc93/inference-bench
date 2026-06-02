# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     423.8s (7.1m) | `1cbe525` |
| vllm         |   1330.2s (22.2m) | `e9e08c4` |
| sglang       | **244.3s (4.1m)** | `9e717ca` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.8 | **138.3** |  152.0 |
| TPOT median (ms)          |         44.8 |  **44.2** |   71.6 |
| E2E median (ms)           |        183.9 | **179.2** |  222.1 |
| Throughput median (tok/s) |          6.3 |   **7.5** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1050.6 |     239.8 | **213.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |       1151.0 | **267.9** |     347.9 |
| Throughput median (tok/s) |          0.9 |   **3.7** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2366.8 |     178.4 | **163.2** |
| TPOT median (ms)          |        380.1 |  **61.0** |     106.8 |
| E2E median (ms)           |       2723.8 | **234.5** |     266.7 |
| Throughput median (tok/s) |          0.5 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        738.3 | **60.4** |   78.7 |
| TPOT median (ms)          |     **27.4** |     29.3 |   51.2 |
| E2E median (ms)           |        759.4 | **82.1** |  137.1 |
| Throughput median (tok/s) |          1.8 | **15.1** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       2894.3 |  **68.6** |   78.6 |
| TPOT median (ms)          |         89.1 |  **14.8** |   23.5 |
| E2E median (ms)           |       5728.6 | **606.2** |  886.6 |
| Throughput median (tok/s) |          5.8 |  **59.7** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1438.7 | **137.1** |  137.3 |
| TPOT median (ms)          |        108.3 |  **29.9** |   50.6 |
| E2E median (ms)           |       2109.3 | **274.0** |  372.1 |
| Throughput median (tok/s) |          3.0 |  **18.4** |   12.7 |
| Correctness               |          99% |       99% |    99% |
