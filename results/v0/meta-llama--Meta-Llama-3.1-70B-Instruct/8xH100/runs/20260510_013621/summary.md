# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:00 PM PT, May 9 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **5/5** |     0/5 |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **5/5** |     0/5 |          0/5 |
| tree_of_thought  |       1/5 | **3/5** |          1/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **18/25** |    6/25 |         1/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1037.6s (17.3m) |
| sglang       |    318.7s (5.3m) |
| torchinferno | **81.9s (1.4m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **25.1** |   30.3 |         37.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **36.2** |   39.5 |         49.5 |
| Throughput median (tok/s) | **27.6** |   25.3 |         20.2 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **74.7** |  513.5 |        293.0 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **89.4** |  523.4 |       1046.1 |
| Throughput median (tok/s) | **11.2** |    1.9 |          1.0 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.6** |   30.4 |         35.5 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.4** |   40.0 |         48.8 |
| Throughput median (tok/s) | **28.2** |   25.0 |         20.5 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          |     49.9 |     48.1 |     **46.3** |
| TPOT median (ms)          |     24.1 | **19.6** |         36.8 |
| E2E median (ms)           |     62.1 | **59.5** |         81.0 |
| Throughput median (tok/s) |     16.1 | **16.9** |         12.5 |
| Correctness               | **100%** |     100% |         100% |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **25.2** |      32.6 |        521.6 |
| TPOT median (ms)          |     11.3 |   **9.3** |         10.0 |
| E2E median (ms)           |    443.1 | **377.3** |        933.8 |
| Throughput median (tok/s) |     85.7 | **100.7** |         40.2 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |  **39.9** |    131.0 |        186.7 |
| TPOT median (ms)          |       7.1 |  **5.8** |          9.4 |
| E2E median (ms)           | **133.3** |    207.9 |        431.8 |
| Throughput median (tok/s) |      33.8 | **34.0** |         18.9 |
| Correctness               |  **100%** |     100% |         100% |
