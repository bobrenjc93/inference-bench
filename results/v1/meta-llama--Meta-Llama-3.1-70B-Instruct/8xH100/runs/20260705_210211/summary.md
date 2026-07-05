# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 5 2026

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
| torchinferno | **37.2s (0.6m)** | `79bd32e` |
| vllm         |    295.1s (4.9m) | `cc1d020` |
| sglang       |    222.1s (3.7m) | `8673e85` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        175.1 | **115.7** |  139.6 |
| TPOT median (ms)          |         44.4 |  **39.9** |   74.7 |
| E2E median (ms)           |        212.3 | **145.3** |  214.9 |
| Throughput median (tok/s) |          6.0 |   **9.5** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **106.6** | 136.7 |  226.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **115.1** | 161.6 |  361.1 |
| Throughput median (tok/s) |      **8.7** |   6.2 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        245.4 | **153.7** |  164.4 |
| TPOT median (ms)          |         56.9 |  **45.3** |  105.8 |
| E2E median (ms)           |        297.0 | **196.7** |  275.1 |
| Throughput median (tok/s) |          4.5 |   **6.8** |    4.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         79.6 | **33.1** |   47.9 |
| TPOT median (ms)          |         64.9 | **21.7** |  382.9 |
| E2E median (ms)           |        114.5 | **49.0** |  404.6 |
| Throughput median (tok/s) |         12.1 | **25.5** |    3.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        255.0 |     101.0 | **68.8** |
| TPOT median (ms)          |         20.6 |  **14.5** |     22.3 |
| E2E median (ms)           |        959.5 | **701.4** |    931.9 |
| Throughput median (tok/s) |         36.4 |  **55.9** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        172.3 | **108.1** |  129.5 |
| TPOT median (ms)          |         37.3 |  **24.3** |  117.1 |
| E2E median (ms)           |        339.7 | **250.8** |  437.5 |
| Throughput median (tok/s) |         13.5 |  **20.8** |   11.6 |
| Correctness               |          99% |       99% |    98% |
