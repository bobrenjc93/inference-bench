# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:27 PM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **2/5** | **2/5** |          1/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **4/5** |     1/5 |          0/5 |
| tree_of_thought  |   **4/5** |     1/5 |          0/5 |
| long_output      |   **4/5** |     1/5 |          0/5 |
| **Total**        | **19/25** |    5/25 |         1/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1282.3s (21.4m) | `5536fc0` |
| sglang       |    176.3s (2.9m) | `d5e707f` |
| torchinferno | **41.6s (0.7m)** | `d403fcb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    166.4 | **139.8** |        462.6 |
| TPOT median (ms)          | **56.0** |      72.5 |        325.8 |
| E2E median (ms)           |    221.4 | **208.5** |        785.5 |
| Throughput median (tok/s) |  **6.6** |       5.8 |          1.6 |
| Correctness               |      98% |       98% |      **98%** |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **179.7** |  218.6 |        511.4 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **200.7** |  364.7 |        625.3 |
| Throughput median (tok/s) |   **5.0** |    2.7 |          1.6 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          | **151.2** |   157.3 |       1414.1 |
| TPOT median (ms)          |  **46.8** |   109.9 |        372.6 |
| E2E median (ms)           | **193.9** |   267.1 |       1867.7 |
| Throughput median (tok/s) |   **6.6** |     5.0 |          0.7 |
| Correctness               |       98% | **98%** |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **57.6** |    73.0 |        604.0 |
| TPOT median (ms)          | **26.7** |    76.0 |        301.0 |
| E2E median (ms)           | **77.6** |   155.6 |        860.8 |
| Throughput median (tok/s) | **15.8** |     9.4 |          1.6 |
| Correctness               |      97% | **97%** |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      73.1 | **64.3** |       2463.7 |
| TPOT median (ms)          |  **15.0** |     22.4 |         77.3 |
| E2E median (ms)           | **630.5** |    827.2 |       5700.2 |
| Throughput median (tok/s) |  **59.1** |     42.1 |          6.9 |
| Correctness               |  **100%** |     100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          | **125.6** |   130.6 |       1091.2 |
| TPOT median (ms)          |  **28.9** |    56.2 |        215.3 |
| E2E median (ms)           | **264.8** |   364.6 |       1967.9 |
| Throughput median (tok/s) |  **18.6** |    13.0 |          2.5 |
| Correctness               |       99% | **99%** |          98% |
