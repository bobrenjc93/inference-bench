# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:01 PM PT, May 9 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **5/5** |     0/5 |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **5/5** |     0/5 |          0/5 |
| tree_of_thought  |   **5/5** |     0/5 |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **22/25** |    3/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1346.6s (22.4m) |
| sglang       |    188.5s (3.1m) |
| torchinferno | **47.4s (0.8m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **23.6** |   31.2 |         25.3 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **33.4** |   40.4 |         37.4 |
| Throughput median (tok/s) | **30.0** |   24.7 |         26.8 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **53.2** |  509.1 |        280.2 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **73.7** |  519.4 |        363.7 |
| Throughput median (tok/s) | **13.6** |    1.9 |          2.7 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **23.1** |   29.6 |         24.9 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **32.9** |   38.1 |         37.6 |
| Throughput median (tok/s) | **30.4** |   26.2 |         26.6 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **38.1** |   49.8 |         45.8 |
| TPOT median (ms)          | **20.2** |   21.1 |         36.9 |
| E2E median (ms)           | **51.1** |   60.1 |         81.1 |
| Throughput median (tok/s) | **20.0** |   16.7 |         12.6 |
| Correctness               | **100%** |   100% |         100% |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **23.9** |      31.4 |         24.8 |
| TPOT median (ms)          |     10.2 |   **9.4** |         10.1 |
| E2E median (ms)           |    400.2 | **377.6** |        397.3 |
| Throughput median (tok/s) |     94.9 | **100.6** |         95.6 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **32.4** |  130.2 |         80.2 |
| TPOT median (ms)          |   **6.1** |    6.1 |          9.4 |
| E2E median (ms)           | **118.2** |  207.1 |        183.4 |
| Throughput median (tok/s) |  **37.8** |   34.0 |         32.9 |
| Correctness               |  **100%** |   100% |         100% |
