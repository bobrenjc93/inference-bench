# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:07 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     305.4s (5.1m) | `9d5290c` |
| vllm         |    977.2s (16.3m) | `3d635c5` |
| sglang       | **162.0s (2.7m)** | `4fb40bf` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        404.1 |    160.0 | **140.2** |
| TPOT median (ms)          |        483.9 | **55.8** |      76.5 |
| E2E median (ms)           |        805.9 |    212.6 | **210.2** |
| Throughput median (tok/s) |          1.7 |  **7.0** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        713.5 | **181.3** |  199.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        744.4 | **202.1** |  335.0 |
| Throughput median (tok/s) |          1.3 |   **4.9** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        618.4 |     172.8 | **161.8** |
| TPOT median (ms)          |        198.6 |  **62.3** |      95.1 |
| E2E median (ms)           |        798.0 | **226.0** |     254.0 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        439.7 | **57.5** |   72.9 |
| TPOT median (ms)          |        451.7 | **26.7** |   52.5 |
| E2E median (ms)           |        832.5 | **77.0** |  133.9 |
| Throughput median (tok/s) |          1.6 | **15.7** |   10.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        611.7 |      75.4 | **64.5** |
| TPOT median (ms)          |         30.6 |  **14.9** |     22.4 |
| E2E median (ms)           |       1967.5 | **628.9** |    832.6 |
| Throughput median (tok/s) |         18.7 |  **58.1** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        557.5 |     129.4 | **127.8** |
| TPOT median (ms)          |        233.0 |  **32.0** |      49.3 |
| E2E median (ms)           |       1029.6 | **269.3** |     353.2 |
| Throughput median (tok/s) |          5.0 |  **18.4** |      13.3 |
| Correctness               |          98% |       99% |       99% |
