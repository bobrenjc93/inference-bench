# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.6s (0.7m)** | `70fbe31` |
| vllm         |    323.5s (5.4m) | `cc1d020` |
| sglang       |    213.7s (3.6m) | `92a1f6e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        156.0 | **124.4** |  133.3 |
| TPOT median (ms)          |         45.0 |  **43.1** |   84.2 |
| E2E median (ms)           |        199.6 | **164.2** |  209.5 |
| Throughput median (tok/s) |          6.2 |   **8.7** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **105.9** | 133.3 |  214.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **114.3** | 155.1 |  371.3 |
| Throughput median (tok/s) |      **8.8** |   6.4 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        329.8 | **141.6** |  161.0 |
| TPOT median (ms)          |         59.4 |  **51.1** |  113.2 |
| E2E median (ms)           |        395.7 | **186.2** |  273.8 |
| Throughput median (tok/s) |          3.7 |   **7.3** |    4.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         79.7 | **32.6** |   51.0 |
| TPOT median (ms)          |         63.2 | **21.7** |  396.3 |
| E2E median (ms)           |        111.7 | **47.9** |  439.9 |
| Throughput median (tok/s) |         12.4 | **25.6** |    3.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        288.6 |      76.8 | **68.3** |
| TPOT median (ms)          |         20.3 |  **14.7** |     22.7 |
| E2E median (ms)           |       1009.2 | **670.4** |    943.5 |
| Throughput median (tok/s) |         35.0 |  **58.7** |     41.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.0 | **101.8** |  125.7 |
| TPOT median (ms)          |         37.6 |  **26.1** |  123.3 |
| E2E median (ms)           |        366.1 | **244.7** |  447.6 |
| Throughput median (tok/s) |         13.2 |  **21.3** |   11.5 |
| Correctness               |          98% |       99% |    99% |
