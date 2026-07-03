# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         5/20 | **12/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **81.3s (1.4m)** | `cbbd77d` |
| vllm         |    375.9s (6.3m) | `4875b44` |
| sglang       |    158.5s (2.6m) | `430418e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        146.6 | **135.1** |  142.5 |
| TPOT median (ms)          |     **47.3** |      51.9 |   79.4 |
| E2E median (ms)           |        185.5 | **180.5** |  220.9 |
| Throughput median (tok/s) |          6.5 |   **7.8** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **143.0** | 216.0 |  225.3 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **151.0** | 239.2 |  386.1 |
| Throughput median (tok/s) |      **6.6** |   4.2 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        302.2 |     171.5 | **161.2** |
| TPOT median (ms)          |         59.9 |  **57.1** |     111.4 |
| E2E median (ms)           |        360.3 | **219.1** |     268.3 |
| Throughput median (tok/s) |          4.1 |   **6.3** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        129.9 | **67.0** |   74.0 |
| TPOT median (ms)          |     **32.0** |     33.2 |   68.4 |
| E2E median (ms)           |        151.5 | **93.5** |  145.0 |
| Throughput median (tok/s) |          8.7 | **13.1** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        245.2 |      76.5 | **75.2** |
| TPOT median (ms)          |         20.7 |  **15.2** |     22.0 |
| E2E median (ms)           |        952.7 | **614.9** |    821.2 |
| Throughput median (tok/s) |         37.6 |  **57.3** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.4 | **133.2** |  135.6 |
| TPOT median (ms)          |         32.0 |  **31.5** |   56.2 |
| E2E median (ms)           |        360.2 | **269.5** |  368.3 |
| Throughput median (tok/s) |         12.7 |  **17.7** |   12.9 |
| Correctness               |          99% |       98% |    99% |
