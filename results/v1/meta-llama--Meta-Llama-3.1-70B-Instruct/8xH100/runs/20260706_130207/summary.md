# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.1s (0.6m)** | `3558018` |
| vllm         |    339.5s (5.7m) | `07f9baf` |
| sglang       |    183.6s (3.1m) | `80decc7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        150.2 | **131.5** |  133.9 |
| TPOT median (ms)          |     **44.2** |      45.9 |   85.1 |
| E2E median (ms)           |        192.1 | **168.1** |  215.8 |
| Throughput median (tok/s) |          6.3 |   **8.5** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **101.5** | 119.9 |  202.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **108.6** | 143.5 |  353.9 |
| Throughput median (tok/s) |      **9.2** |   7.0 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        311.1 |     161.1 | **158.9** |
| TPOT median (ms)          |         59.0 |  **45.0** |     107.4 |
| E2E median (ms)           |        367.2 | **202.5** |     276.0 |
| Throughput median (tok/s) |          4.0 |   **6.7** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         80.3 | **32.9** |   44.2 |
| TPOT median (ms)          |         64.0 | **21.6** |  274.8 |
| E2E median (ms)           |        114.4 | **48.4** |  292.7 |
| Throughput median (tok/s) |         12.1 | **25.6** |    4.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        276.4 |      75.9 | **70.4** |
| TPOT median (ms)          |         20.0 |  **14.9** |     22.0 |
| E2E median (ms)           |        987.5 | **596.1** |    883.7 |
| Throughput median (tok/s) |         36.1 |  **58.3** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        183.9 | **104.2** |  121.9 |
| TPOT median (ms)          |         37.4 |  **25.5** |   97.9 |
| E2E median (ms)           |        354.0 | **231.7** |  404.4 |
| Throughput median (tok/s) |         13.5 |  **21.2** |   12.0 |
| Correctness               |          99% |       99% |    99% |
