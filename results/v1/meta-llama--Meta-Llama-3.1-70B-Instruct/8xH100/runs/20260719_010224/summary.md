# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.2s (0.7m)** | `96adc9d` |
| vllm         |    336.9s (5.6m) | `9243e01` |
| sglang       |    189.1s (3.2m) | `99f5a6f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.2 |  **77.4** |   95.2 |
| TPOT median (ms)          |     **31.4** |      36.4 |   68.1 |
| E2E median (ms)           |        164.7 | **104.2** |  152.6 |
| Throughput median (tok/s) |          7.0 |  **12.6** |    8.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **53.9** |  88.4 |  155.9 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **70.1** | 107.0 |  236.1 |
| Throughput median (tok/s) |     **14.3** |   9.3 |    4.2 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.0 |  **86.4** |   89.5 |
| TPOT median (ms)          |         35.4 |  **34.6** |   76.9 |
| E2E median (ms)           |        217.2 | **111.3** |  152.2 |
| Throughput median (tok/s) |          5.2 |  **12.1** |    8.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         51.4 | **36.5** |   59.6 |
| TPOT median (ms)          |         34.6 | **23.8** |  405.7 |
| E2E median (ms)           |         72.9 | **55.1** |  456.0 |
| Throughput median (tok/s) |         20.0 | **24.1** |    3.2 |
| Correctness               |          96% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.3 |  **46.6** |   55.6 |
| TPOT median (ms)          |         19.5 |  **15.4** |   28.1 |
| E2E median (ms)           |        897.5 | **583.5** | 1094.6 |
| Throughput median (tok/s) |         40.6 |  **60.8** |   34.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.2 |  **67.0** |   91.2 |
| TPOT median (ms)          |         24.2 |  **22.0** |  115.8 |
| E2E median (ms)           |        284.5 | **192.2** |  418.3 |
| Throughput median (tok/s) |         17.4 |  **23.8** |   11.9 |
| Correctness               |          99% |       98% |    99% |
