# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:02 PM PT, May 9 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |   **5/5** |     0/5 |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **5/5** |     0/5 |          0/5 |
| tree_of_thought  |   **4/5** |     1/5 |          0/5 |
| long_output      |       2/5 | **3/5** |          0/5 |
| **Total**        | **21/25** |    4/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1292.9s (21.5m) |
| sglang       |    175.5s (2.9m) |
| torchinferno | **40.9s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math equations — long input, short output, tests prefill speed ([source](../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.9** |   30.6 |         36.0 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.8** |   40.0 |         45.8 |
| Throughput median (tok/s) | **27.9** |   25.0 |         21.8 |
| Correctness               | **100%** |   100% |         100% |

### self_consistency
> N concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **71.8** |  508.7 |        284.7 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **85.7** |  519.9 |        660.1 |
| Throughput median (tok/s) | **11.7** |    1.9 |          1.5 |
| Correctness               | **100%** |   100% |         100% |

### multi_turn
> 8-turn growing conversation of math equations — tests KV cache management ([source](../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **24.6** |   29.1 |        350.1 |
| TPOT median (ms)          |  **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **35.3** |   38.0 |        430.0 |
| Throughput median (tok/s) | **28.3** |   26.3 |          2.4 |
| Correctness               | **100%** |   100% |         100% |

### tree_of_thought
> Branching concurrent math requests (4-wide x 3-deep) — tests scheduling ([source](../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |   sglang | torchinferno |
| :------------------------ | -------: | -------: | -----------: |
| TTFT median (ms)          | **38.8** |     46.0 |         46.5 |
| TPOT median (ms)          |     26.3 | **18.4** |         36.3 |
| E2E median (ms)           | **55.4** |     55.8 |         81.4 |
| Throughput median (tok/s) | **18.4** |     18.1 |         12.4 |
| Correctness               | **100%** |     100% |         100% |

### long_output
> 1 * <huge number> — forces long token output, tests decode throughput ([source](../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          | **24.7** |      28.9 |        207.5 |
| TPOT median (ms)          |     11.2 |   **9.3** |         10.0 |
| E2E median (ms)           |    440.6 | **376.4** |        580.9 |
| Throughput median (tok/s) |     86.2 | **100.9** |         65.3 |
| Correctness               | **100%** |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |  sglang | torchinferno |
| :------------------------ | --------: | ------: | -----------: |
| TTFT median (ms)          |  **36.9** |   128.7 |        184.9 |
| TPOT median (ms)          |       7.5 | **5.5** |          9.3 |
| E2E median (ms)           | **130.6** |   206.0 |        359.6 |
| Throughput median (tok/s) |  **34.5** |    34.5 |         20.7 |
| Correctness               |  **100%** |    100% |         100% |
