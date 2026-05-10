# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 6:36 AM PT, May 8 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **3/5** |     2/5 |          0/5 |
| tree_of_thought  |       1/5 | **4/5** |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **13/25** |   12/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |   807.8s (13.5m) |
| sglang       |     87.5s (1.5m) |
| torchinferno | **38.9s (0.6m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     31.2 | **30.6** |         92.6 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     44.7 | **41.6** |        171.7 |
| Throughput median (tok/s) |     22.4 | **24.0** |          5.8 |
| Correctness               | **100%** |     100% |         100% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **65.9** |  427.2 |       1165.3 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **88.3** |  437.8 |       1485.0 |
| Throughput median (tok/s) | **11.3** |    2.3 |          0.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **30.1** |     31.0 |        346.3 |
| TPOT median (ms)          |  **0.0** |      0.0 |          0.0 |
| E2E median (ms)           |     43.3 | **41.8** |        602.6 |
| Throughput median (tok/s) |     23.1 | **23.9** |          1.7 |
| Correctness               | **100%** |     100% |         100% |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     43.9 | **40.2** |        266.4 |
| TPOT median (ms)          |     28.5 | **23.9** |        256.5 |
| E2E median (ms)           |     58.2 | **54.6** |        349.3 |
| Throughput median (tok/s) |     17.6 | **18.4** |          2.9 |
| Correctness               | **100%** |     100% |         100% |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **31.3** |      32.6 |        328.2 |
| TPOT median (ms)          |     14.0 |  **12.1** |        279.7 |
| E2E median (ms)           |    550.7 | **480.0** |      10322.5 |
| Throughput median (tok/s) |     69.0 |  **79.1** |          3.6 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **40.5** |    112.3 |        439.8 |
| TPOT median (ms)          |       8.5 |  **7.2** |        107.2 |
| E2E median (ms)           | **157.0** |    211.2 |       2586.2 |
| Throughput median (tok/s) |      28.7 | **29.5** |          2.9 |
| Correctness               |  **100%** |     100% |         100% |
