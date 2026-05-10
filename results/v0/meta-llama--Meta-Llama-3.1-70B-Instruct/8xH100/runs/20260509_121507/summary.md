# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Timestamp:** 4:05 AM PT, May 9 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **5/5** |     0/5 |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **5/5** |     0/5 |          0/5 |
| tree_of_thought  |   **3/5** |     2/5 |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **20/25** |    5/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1264.3s (21.1m) |
| sglang       |    185.1s (3.1m) |
| torchinferno | **41.0s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.8** |   31.7 |         89.2 |
| TPOT median (ms)          |  **0.0** |    0.0 |         10.2 |
| E2E median (ms)           | **35.8** |   41.0 |         98.8 |
| Throughput median (tok/s) | **28.0** |   24.4 |         10.7 |
| Correctness               | **100%** |   100% |          75% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **63.4** |  520.7 |      16027.0 |
| TPOT median (ms)          |  **0.0** |    0.0 |         57.4 |
| E2E median (ms)           | **84.1** |  537.9 |      16091.1 |
| Throughput median (tok/s) | **11.9** |    1.9 |          0.1 |
| Correctness               | **100%** |   100% |          94% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.5** |   30.4 |            - |
| TPOT median (ms)          |  **0.0** |    0.0 |            - |
| E2E median (ms)           | **35.2** |   38.6 |            - |
| Throughput median (tok/s) | **28.4** |   25.9 |            - |
| Correctness               | **100%** |   100% |            - |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **44.5** |     46.9 |            - |
| TPOT median (ms)          |     22.3 | **19.9** |            - |
| E2E median (ms)           |     60.8 | **56.1** |            - |
| Throughput median (tok/s) | **18.1** |     17.8 |            - |
| Correctness               | **100%** |     100% |            - |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **24.8** |      30.5 |            - |
| TPOT median (ms)          |     11.2 |   **9.4** |            - |
| E2E median (ms)           |    440.3 | **377.7** |            - |
| Throughput median (tok/s) |     86.3 | **100.6** |            - |
| Correctness               | **100%** |      100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          |  **36.4** |   132.0 |       8058.1 |
| TPOT median (ms)          |       6.7 | **5.8** |         33.8 |
| E2E median (ms)           | **131.2** |   210.3 |       8094.9 |
| Throughput median (tok/s) |  **34.5** |    34.1 |          5.4 |
| Correctness               |  **100%** |    100% |          84% |
