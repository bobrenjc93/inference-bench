# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, Jun 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     363.6s (6.1m) | `9ffdf20` |
| vllm         |   1391.7s (23.2m) | `5b2a2be` |
| sglang       | **253.8s (4.2m)** | `578f232` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        313.5 | **160.4** |  161.2 |
| TPOT median (ms)          |     **47.9** |      56.1 |   79.7 |
| E2E median (ms)           |        362.6 | **215.3** |  237.9 |
| Throughput median (tok/s) |          3.5 |   **7.0** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        287.0 | **216.3** |  220.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        397.5 | **242.7** |  372.5 |
| Throughput median (tok/s) |          2.5 |   **4.1** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        808.1 |     177.5 | **161.9** |
| TPOT median (ms)          |        166.4 |  **61.1** |     105.8 |
| E2E median (ms)           |       1034.7 | **235.4** |     264.8 |
| Throughput median (tok/s) |          1.3 |   **5.9** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.8 | **59.5** |   81.3 |
| TPOT median (ms)          |         33.3 | **27.8** |   44.5 |
| E2E median (ms)           |        419.0 | **80.6** |  140.9 |
| Throughput median (tok/s) |          3.5 | **14.8** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        428.9 |      82.1 | **79.1** |
| TPOT median (ms)          |         37.2 |  **14.8** |     23.4 |
| E2E median (ms)           |       1701.0 | **623.1** |    884.5 |
| Throughput median (tok/s) |         20.7 |  **58.0** |     39.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        443.1 | **139.2** |  140.8 |
| TPOT median (ms)          |         57.0 |  **32.0** |   50.7 |
| E2E median (ms)           |        782.9 | **279.4** |  380.1 |
| Throughput median (tok/s) |          6.3 |  **18.0** |   12.4 |
| Correctness               |          98% |       99% |    98% |
