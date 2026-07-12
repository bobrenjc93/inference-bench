# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 12 2026

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
| torchinferno | **40.2s (0.7m)** | `96adc9d` |
| vllm         |    361.6s (6.0m) | `8df14cf` |
| sglang       |    155.6s (2.6m) | `96a04cb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        143.3 | **72.8** |   76.9 |
| TPOT median (ms)          |     **31.1** |     36.7 |   63.4 |
| E2E median (ms)           |        167.5 | **98.1** |  129.8 |
| Throughput median (tok/s) |          6.8 | **13.1** |   10.5 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **62.5** | 73.4 |  119.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **82.2** | 90.5 |  208.5 |
| Throughput median (tok/s) |     **12.2** | 11.0 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.3 |  **76.0** |   82.3 |
| TPOT median (ms)          |     **34.4** |      41.3 |   81.1 |
| E2E median (ms)           |        217.3 | **103.7** |  141.7 |
| Throughput median (tok/s) |          5.1 |  **11.9** |    9.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.1 | **37.3** |   52.2 |
| TPOT median (ms)          |         34.9 | **27.1** |  419.6 |
| E2E median (ms)           |         73.8 | **57.4** |  490.6 |
| Throughput median (tok/s) |         19.7 | **23.8** |    3.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.2 |  **47.5** |   51.5 |
| TPOT median (ms)          |         19.1 |  **15.2** |   25.0 |
| E2E median (ms)           |        892.4 | **575.6** |  939.4 |
| Throughput median (tok/s) |         41.5 |  **61.5** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.5 |  **61.4** |   76.4 |
| TPOT median (ms)          |     **23.9** |      24.1 |  117.8 |
| E2E median (ms)           |        286.6 | **185.1** |  382.0 |
| Throughput median (tok/s) |         17.1 |  **24.3** |   13.2 |
| Correctness               |          98% |       99% |    99% |
