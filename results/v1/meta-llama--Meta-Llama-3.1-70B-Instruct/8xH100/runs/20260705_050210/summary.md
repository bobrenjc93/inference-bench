# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **14/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.8s (0.7m)** | `390fed4` |
| vllm         |    273.4s (4.6m) | `34b560b` |
| sglang       |    213.6s (3.6m) | `67361ff` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        152.6 | **136.5** |  143.3 |
| TPOT median (ms)          |         50.0 |  **43.4** |   76.7 |
| E2E median (ms)           |        200.3 | **174.2** |  218.8 |
| Throughput median (tok/s) |          6.0 |   **8.3** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **169.2** | 201.7 |  216.7 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **180.8** | 226.8 |  367.8 |
| Throughput median (tok/s) |      **5.5** |   4.4 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        336.5 |     186.3 | **168.2** |
| TPOT median (ms)          |         60.8 |  **58.3** |     100.4 |
| E2E median (ms)           |        396.8 | **240.1** |     272.8 |
| Throughput median (tok/s) |          3.5 |   **5.8** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        116.9 | **61.8** |   75.7 |
| TPOT median (ms)          |         74.1 | **29.5** |   64.8 |
| E2E median (ms)           |        147.3 | **84.5** |  144.8 |
| Throughput median (tok/s) |          9.0 | **14.7** |    9.8 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        262.4 |      78.0 | **72.6** |
| TPOT median (ms)          |         20.0 |  **14.8** |     21.9 |
| E2E median (ms)           |       1016.4 | **621.9** |    838.4 |
| Throughput median (tok/s) |         35.9 |  **58.9** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        207.5 | **132.9** |  135.3 |
| TPOT median (ms)          |         41.0 |  **29.2** |   52.8 |
| E2E median (ms)           |        388.3 | **269.5** |  368.5 |
| Throughput median (tok/s) |         12.0 |  **18.4** |   13.0 |
| Correctness               |          99% |       98% |    99% |
