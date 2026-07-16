# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 16 2026

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
| torchinferno | **45.1s (0.8m)** | `96adc9d` |
| vllm         |    391.7s (6.5m) | `dc9f845` |
| sglang       |    205.7s (3.4m) | `5cbea10` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        142.4 |  **84.1** |   85.5 |
| TPOT median (ms)          |     **32.0** |      41.9 |   65.8 |
| E2E median (ms)           |        167.8 | **121.8** |  141.8 |
| Throughput median (tok/s) |          6.9 |  **11.1** |    9.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.5** | 71.7 |  136.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.9** | 90.8 |  209.8 |
| Throughput median (tok/s) |     **13.3** | 11.0 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.6 |  **83.7** |   88.0 |
| TPOT median (ms)          |     **35.4** |      36.8 |   78.0 |
| E2E median (ms)           |        219.9 | **110.6** |  155.8 |
| Throughput median (tok/s) |          5.2 |  **12.3** |    8.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         54.3 | **35.5** |   52.9 |
| TPOT median (ms)          |         35.4 | **23.0** |  386.7 |
| E2E median (ms)           |         75.6 | **53.5** |  456.5 |
| Throughput median (tok/s) |         18.8 | **24.3** |    3.2 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.8 |  **45.7** |   52.2 |
| TPOT median (ms)          |         19.1 |  **15.1** |   25.0 |
| E2E median (ms)           |        842.4 | **570.9** |  965.2 |
| Throughput median (tok/s) |         41.4 |  **62.0** |   38.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.9 |  **64.1** |   83.1 |
| TPOT median (ms)          |         24.4 |  **23.4** |  111.1 |
| E2E median (ms)           |        276.1 | **189.5** |  385.8 |
| Throughput median (tok/s) |         17.1 |  **24.1** |   12.9 |
| Correctness               |          98% |       99% |    98% |
