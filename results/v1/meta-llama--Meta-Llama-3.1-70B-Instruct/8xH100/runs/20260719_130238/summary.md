# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 19 2026

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
| torchinferno | **44.8s (0.7m)** | `96adc9d` |
| vllm         |    341.8s (5.7m) | `e6d1310` |
| sglang       |    182.2s (3.0m) | `a03ca46` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        143.7 | **70.7** |   98.1 |
| TPOT median (ms)          |     **31.0** |     38.0 |   71.4 |
| E2E median (ms)           |        167.2 | **97.8** |  161.5 |
| Throughput median (tok/s) |          6.8 | **13.5** |    7.9 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.6** | 71.6 |  172.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **78.0** | 89.3 |  239.6 |
| Throughput median (tok/s) |     **12.8** | 11.2 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.5 |  **81.1** |   91.3 |
| TPOT median (ms)          |     **34.3** |      34.4 |   77.3 |
| E2E median (ms)           |        221.0 | **106.6** |  152.8 |
| Throughput median (tok/s) |          5.0 |  **12.3** |    8.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.8 | **36.3** |   69.0 |
| TPOT median (ms)          |         35.1 | **24.1** |  395.9 |
| E2E median (ms)           |         74.7 | **54.6** |  497.7 |
| Throughput median (tok/s) |         19.4 | **23.3** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.2 |  **46.9** |   57.7 |
| TPOT median (ms)          |         19.2 |  **15.4** |   27.6 |
| E2E median (ms)           |        885.1 | **581.5** | 1064.0 |
| Throughput median (tok/s) |         41.4 |  **60.8** |   34.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.8 |  **61.3** |   97.8 |
| TPOT median (ms)          |         23.9 |  **22.4** |  114.4 |
| E2E median (ms)           |        285.2 | **186.0** |  423.1 |
| Throughput median (tok/s) |         17.1 |  **24.2** |   11.7 |
| Correctness               |          98% |       99% |    99% |
