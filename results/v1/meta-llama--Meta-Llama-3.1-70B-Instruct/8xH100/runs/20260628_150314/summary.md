# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **3/4** |       1/4 |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     373.1s (6.2m) | `3f37307` |
| vllm         |     519.8s (8.7m) | `4b643c4` |
| sglang       | **264.2s (4.4m)** | `aaa31eb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm | sglang |
| :------------------------ | -----------: | ------: | -----: |
| TTFT median (ms)          |    **139.0** |   141.9 |  156.6 |
| TPOT median (ms)          |     **46.2** |    50.1 |   75.3 |
| E2E median (ms)           |    **178.1** |   183.7 |  225.3 |
| Throughput median (tok/s) |          6.4 | **7.9** |    5.3 |
| Correctness               |          98% |     98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.2 | **190.3** |  216.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        267.6 | **228.8** |  353.2 |
| Throughput median (tok/s) |          3.7 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        387.0 | **161.5** |  178.3 |
| TPOT median (ms)          |         56.7 |  **52.1** |   98.2 |
| E2E median (ms)           |        453.2 | **203.1** |  281.2 |
| Throughput median (tok/s) |          2.9 |   **6.5** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        278.6 | **63.1** |   81.9 |
| TPOT median (ms)          |         41.5 | **31.6** |   46.2 |
| E2E median (ms)           |        318.2 | **86.4** |  142.8 |
| Throughput median (tok/s) |          4.0 | **13.9** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        256.9 |      70.1 | **69.4** |
| TPOT median (ms)          |         21.6 |  **14.8** |     22.1 |
| E2E median (ms)           |       1102.9 | **590.7** |    834.0 |
| Throughput median (tok/s) |         35.5 |  **60.3** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        261.9 | **125.4** |  140.6 |
| TPOT median (ms)          |         33.2 |  **29.7** |   48.4 |
| E2E median (ms)           |        464.0 | **258.5** |  367.3 |
| Throughput median (tok/s) |         10.5 |  **18.6** |   13.0 |
| Correctness               |          99% |       98% |    99% |
