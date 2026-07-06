# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **14/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.4s (0.7m)** | `0d6ab82` |
| vllm         |    243.9s (4.1m) | `90ce3a0` |
| sglang       |    163.5s (2.7m) | `80decc7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        146.5 | **124.9** |  135.2 |
| TPOT median (ms)          |     **44.1** |      46.0 |   81.3 |
| E2E median (ms)           |        189.4 | **158.2** |  212.9 |
| Throughput median (tok/s) |          6.1 |   **8.5** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **94.5** | 125.8 |  212.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **101.8** | 150.4 |  371.3 |
| Throughput median (tok/s) |      **9.8** |   6.6 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        236.4 | **151.3** |  162.7 |
| TPOT median (ms)          |         59.1 |  **46.6** |  103.8 |
| E2E median (ms)           |        289.8 | **197.8** |  276.8 |
| Throughput median (tok/s) |          4.6 |   **7.1** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         79.7 | **32.4** |   48.6 |
| TPOT median (ms)          |         63.4 | **21.7** |  411.8 |
| E2E median (ms)           |        110.4 | **47.9** |  433.2 |
| Throughput median (tok/s) |         12.5 | **25.7** |    3.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        266.9 |      76.4 | **67.6** |
| TPOT median (ms)          |         19.4 |  **14.8** |     22.4 |
| E2E median (ms)           |        924.5 | **673.2** |    972.2 |
| Throughput median (tok/s) |         36.7 |  **58.6** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        164.8 | **102.2** |  125.2 |
| TPOT median (ms)          |         37.2 |  **25.8** |  123.8 |
| E2E median (ms)           |        323.2 | **245.5** |  453.3 |
| Throughput median (tok/s) |         14.0 |  **21.3** |   11.7 |
| Correctness               |          99% |       99% |    98% |
