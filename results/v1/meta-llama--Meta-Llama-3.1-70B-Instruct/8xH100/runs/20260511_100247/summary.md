# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **4/5** |    1/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **3/5** |    2/5 |          0/5 |
| tree_of_thought  |   **4/5** |    1/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **20/25** |   5/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1045.7s (17.4m) | `b1b5972` |
| sglang       |    281.2s (4.7m) | `c027ae6` |
| torchinferno | **81.2s (1.4m)** | `69d140e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     163.7 | **150.2** |        743.9 |
| TPOT median (ms)          |  **57.6** |      76.1 |        403.7 |
| E2E median (ms)           | **216.7** |     224.1 |       1131.0 |
| Throughput median (tok/s) |   **6.7** |       5.4 |          1.4 |
| Correctness               |   **98%** |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **179.8** |  227.5 |        429.8 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **203.9** |  391.7 |        552.5 |
| Throughput median (tok/s) |   **4.9** |    2.6 |          1.8 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     179.4 | **164.0** |       1271.5 |
| TPOT median (ms)          |  **53.4** |     112.1 |        323.9 |
| E2E median (ms)           | **229.4** |     271.1 |       1542.3 |
| Throughput median (tok/s) |   **6.0** |       4.9 |          0.8 |
| Correctness               |       98% |   **98%** |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **60.7** |    78.0 |            - |
| TPOT median (ms)          | **26.9** |    57.0 |            - |
| E2E median (ms)           | **81.4** |   142.7 |            - |
| Throughput median (tok/s) | **15.2** |     9.3 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      80.7 | **72.2** |            - |
| TPOT median (ms)          |  **15.1** |     22.2 |            - |
| E2E median (ms)           | **643.5** |    822.7 |            - |
| Throughput median (tok/s) |  **57.6** |     42.2 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **132.9** |  138.4 |        815.1 |
| TPOT median (ms)          |  **30.6** |   53.5 |        242.5 |
| E2E median (ms)           | **275.0** |  370.5 |       1075.3 |
| Throughput median (tok/s) |  **18.1** |   12.9 |          1.3 |
| Correctness               |       98% |    99% |      **99%** |
