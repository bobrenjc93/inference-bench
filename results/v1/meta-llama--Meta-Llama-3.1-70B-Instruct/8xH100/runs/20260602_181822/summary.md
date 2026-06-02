# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          1/4 |   **3/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         2/20 | **13/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     403.0s (6.7m) | `1cbe525` |
| vllm         |   1362.4s (22.7m) | `afcb580` |
| sglang       | **229.4s (3.8m)** | `9e717ca` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        183.2 |   159.4 | **146.0** |
| TPOT median (ms)          |     **45.7** |    60.6 |      74.6 |
| E2E median (ms)           |        220.4 |   220.4 | **216.4** |
| Throughput median (tok/s) |          5.7 | **6.7** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1054.9 | **194.7** |  204.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |       1155.7 | **221.8** |  344.6 |
| Throughput median (tok/s) |          0.9 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2420.9 |     163.3 | **157.7** |
| TPOT median (ms)          |        424.2 |  **56.6** |     103.3 |
| E2E median (ms)           |       2750.1 | **216.4** |     261.0 |
| Throughput median (tok/s) |          0.5 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        725.3 | **60.5** |   79.2 |
| TPOT median (ms)          |     **27.5** |     27.7 |   50.2 |
| E2E median (ms)           |        748.0 | **81.6** |  141.0 |
| Throughput median (tok/s) |          1.7 | **14.7** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       2868.0 |      76.8 | **75.0** |
| TPOT median (ms)          |         89.4 |  **14.9** |     23.5 |
| E2E median (ms)           |       5608.7 | **624.6** |    879.4 |
| Throughput median (tok/s) |          5.8 |  **57.7** |     39.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1450.5 | **130.9** |  132.5 |
| TPOT median (ms)          |        117.3 |  **32.0** |   50.3 |
| E2E median (ms)           |       2096.6 | **273.0** |  368.5 |
| Throughput median (tok/s) |          2.9 |  **18.0** |   12.6 |
| Correctness               |          99% |       98% |    98% |
