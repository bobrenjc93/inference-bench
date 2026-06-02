# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 AM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     403.8s (6.7m) | `1cbe525` |
| vllm         |   1361.7s (22.7m) | `53fa09d` |
| sglang       | **200.5s (3.3m)** | `28f9c1f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        185.3 |     157.4 | **147.2** |
| TPOT median (ms)          |     **44.5** |      52.5 |      72.5 |
| E2E median (ms)           |        227.5 | **211.0** |     215.2 |
| Throughput median (tok/s) |          6.0 |   **6.8** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1047.7 | **197.0** |  207.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |       1149.1 | **234.2** |  348.1 |
| Throughput median (tok/s) |          0.9 |   **4.3** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2556.5 |     172.6 | **160.6** |
| TPOT median (ms)          |        430.1 |  **61.5** |      97.8 |
| E2E median (ms)           |       2804.5 | **224.1** |     258.3 |
| Throughput median (tok/s) |          0.4 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        786.8 | **57.5** |   80.0 |
| TPOT median (ms)          |     **27.5** |     27.7 |   43.4 |
| E2E median (ms)           |        811.1 | **77.9** |  136.5 |
| Throughput median (tok/s) |          1.7 | **15.5** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       2856.1 |      77.7 | **76.5** |
| TPOT median (ms)          |         93.7 |  **15.0** |     23.7 |
| E2E median (ms)           |       5661.9 | **607.9** |    885.9 |
| Throughput median (tok/s) |          5.5 |  **58.2** |     39.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1486.5 | **132.4** |  134.4 |
| TPOT median (ms)          |        119.2 |  **31.3** |   47.5 |
| E2E median (ms)           |       2130.8 | **271.0** |  368.8 |
| Throughput median (tok/s) |          2.9 |  **18.2** |   12.7 |
| Correctness               |          99% |       99% |    98% |
