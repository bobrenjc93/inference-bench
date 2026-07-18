# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 18 2026

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
| torchinferno | **50.9s (0.8m)** | `96adc9d` |
| vllm         |    367.3s (6.1m) | `c7ce03b` |
| sglang       |    190.7s (3.2m) | `d7b9425` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.7 | **70.7** |   97.5 |
| TPOT median (ms)          |     **32.9** |     36.3 |   76.6 |
| E2E median (ms)           |        167.2 | **97.3** |  163.5 |
| Throughput median (tok/s) |          6.9 | **13.5** |    8.1 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.2** | 68.8 |  150.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **73.5** | 85.2 |  230.8 |
| Throughput median (tok/s) |     **13.6** | 11.7 |    4.3 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.9 |  **81.9** |  101.5 |
| TPOT median (ms)          |     **34.8** |      36.6 |   80.5 |
| E2E median (ms)           |        218.5 | **114.4** |  166.9 |
| Throughput median (tok/s) |          5.1 |  **12.0** |    7.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         54.0 | **35.0** |   64.5 |
| TPOT median (ms)          |         35.1 | **23.1** |  433.4 |
| E2E median (ms)           |         75.2 | **53.0** |  516.8 |
| Throughput median (tok/s) |         19.2 | **24.6** |    2.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.7 |  **46.3** |   56.0 |
| TPOT median (ms)          |         19.5 |  **15.3** |   27.6 |
| E2E median (ms)           |        895.7 | **574.4** | 1045.2 |
| Throughput median (tok/s) |         41.0 |  **60.9** |   35.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.7 |  **60.5** |   94.0 |
| TPOT median (ms)          |         24.5 |  **22.3** |  123.6 |
| E2E median (ms)           |        286.0 | **184.9** |  424.6 |
| Throughput median (tok/s) |         17.2 |  **24.5** |   11.6 |
| Correctness               |          99% |       99% |    99% |
