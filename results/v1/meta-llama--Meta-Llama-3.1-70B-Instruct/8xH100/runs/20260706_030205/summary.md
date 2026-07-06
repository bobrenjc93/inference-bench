# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 5 2026

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
| torchinferno | **43.1s (0.7m)** | `2f33f36` |
| vllm         |    335.5s (5.6m) | `f2aaf59` |
| sglang       |    216.6s (3.6m) | `c016c6f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        178.9 | **125.7** |  137.0 |
| TPOT median (ms)          |         45.3 |  **43.8** |   76.4 |
| E2E median (ms)           |        217.5 | **159.5** |  213.1 |
| Throughput median (tok/s) |          5.8 |   **8.6** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **108.0** | 125.0 |  223.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **115.1** | 147.7 |  388.5 |
| Throughput median (tok/s) |      **8.7** |   6.8 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        246.3 | **151.6** |  159.0 |
| TPOT median (ms)          |         60.0 |  **47.1** |  109.6 |
| E2E median (ms)           |        303.3 | **194.6** |  275.6 |
| Throughput median (tok/s) |          4.3 |   **7.2** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         77.5 | **32.7** |   50.7 |
| TPOT median (ms)          |         63.5 | **21.8** |  371.8 |
| E2E median (ms)           |        110.9 | **48.1** |  424.8 |
| Throughput median (tok/s) |         12.5 | **25.4** |    3.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        277.2 |      74.3 | **69.8** |
| TPOT median (ms)          |         19.8 |  **14.8** |     22.7 |
| E2E median (ms)           |       1000.1 | **663.2** |    900.0 |
| Throughput median (tok/s) |         36.0 |  **58.5** |     40.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        177.6 | **101.9** |  127.9 |
| TPOT median (ms)          |         37.7 |  **25.5** |  116.1 |
| E2E median (ms)           |        349.4 | **242.6** |  440.4 |
| Throughput median (tok/s) |         13.5 |  **21.3** |   11.4 |
| Correctness               |          98% |       99% |    99% |
