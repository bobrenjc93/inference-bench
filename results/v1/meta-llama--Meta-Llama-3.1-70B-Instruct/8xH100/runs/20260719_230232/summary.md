# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **36.1s (0.6m)** | `96adc9d` |
| vllm         |    336.4s (5.6m) | `ace9fda` |
| sglang       |    205.9s (3.4m) | `b3570a4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.0 |  **81.3** |   96.6 |
| TPOT median (ms)          |     **32.0** |      38.1 |   70.0 |
| E2E median (ms)           |        165.7 | **113.4** |  158.6 |
| Throughput median (tok/s) |          7.0 |  **12.3** |    8.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.6** | 73.2 |  153.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.6** | 90.3 |  236.9 |
| Throughput median (tok/s) |     **13.4** | 11.1 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.9 |  **83.3** |   91.8 |
| TPOT median (ms)          |     **35.2** |      35.2 |   79.4 |
| E2E median (ms)           |        224.1 | **109.6** |  158.1 |
| Throughput median (tok/s) |          5.1 |  **12.6** |    8.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.7 | **36.1** |   58.9 |
| TPOT median (ms)          |         34.8 | **23.4** |  396.8 |
| E2E median (ms)           |         74.4 | **54.0** |  479.7 |
| Throughput median (tok/s) |         19.5 | **24.2** |    3.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.9 |  **47.5** |   59.2 |
| TPOT median (ms)          |         19.4 |  **15.4** |   28.8 |
| E2E median (ms)           |        869.4 | **580.6** | 1096.3 |
| Throughput median (tok/s) |         41.7 |  **60.3** |   33.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.2 |  **64.3** |   92.0 |
| TPOT median (ms)          |         24.3 |  **22.4** |  115.0 |
| E2E median (ms)           |        281.6 | **189.6** |  425.9 |
| Throughput median (tok/s) |         17.3 |  **24.1** |   11.6 |
| Correctness               |          99% |       99% |    99% |
