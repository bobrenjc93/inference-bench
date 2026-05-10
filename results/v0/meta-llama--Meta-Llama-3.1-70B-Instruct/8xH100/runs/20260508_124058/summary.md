# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 5:34 AM PT, May 8 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **3/5** |     2/5 |          0/5 |
| tree_of_thought  |       2/5 | **3/5** |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **14/25** |   11/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |   807.8s (13.5m) |
| sglang       |     87.5s (1.5m) |
| torchinferno | **39.2s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.0 | **30.7** |         94.5 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.6 | **41.7** |        173.3 |
| Throughput median (tok/s) |     22.4 | **24.0** |          5.8 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **66.1** |  427.1 |       1134.6 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **90.3** |  436.3 |       1451.0 |
| Throughput median (tok/s) | **11.1** |    2.3 |          0.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **30.4** |     31.0 |        343.5 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     43.7 | **41.7** |        594.5 |
| Throughput median (tok/s) |     22.9 | **24.0** |          1.7 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     45.3 | **40.3** |        104.1 |
| TPOT median (ms)          | **26.0** |     28.0 |        251.5 |
| E2E median (ms)           |     59.3 | **55.6** |        422.8 |
| Throughput median (tok/s) |     16.9 | **18.0** |          2.9 |
| Correctness               | **100%** |     100% |         100% |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **30.9** |      32.3 |        331.9 |
| TPOT median (ms)          |     14.0 |  **12.1** |        265.7 |
| E2E median (ms)           |    550.7 | **479.4** |      10196.7 |
| Throughput median (tok/s) |     69.0 |  **79.2** |          3.7 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **40.7** |    112.3 |        401.7 |
| TPOT median (ms)          |   **8.0** |      8.0 |        103.4 |
| E2E median (ms)           | **157.7** |    210.9 |       2567.7 |
| Throughput median (tok/s) |      28.5 | **29.5** |          3.0 |
| Correctness               |  **100%** |     100% |         100% |
