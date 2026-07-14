# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 14 2026

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
| torchinferno | **39.9s (0.7m)** | `96adc9d` |
| vllm         |    338.0s (5.6m) | `05d4f8b` |
| sglang       |    174.7s (2.9m) | `08c46e1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.8 |  **71.9** |   88.0 |
| TPOT median (ms)          |     **31.7** |      38.6 |   61.8 |
| E2E median (ms)           |        164.8 | **100.4** |  143.9 |
| Throughput median (tok/s) |          7.0 |  **12.8** |    9.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.3** | 77.1 |  122.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **77.2** | 95.2 |  213.7 |
| Throughput median (tok/s) |     **13.0** | 10.5 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        189.2 | **72.6** |   83.5 |
| TPOT median (ms)          |     **35.5** |     36.5 |   76.5 |
| E2E median (ms)           |        218.3 | **98.0** |  142.1 |
| Throughput median (tok/s) |          5.2 | **13.8** |    9.4 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.5 | **38.1** |   52.5 |
| TPOT median (ms)          |         34.6 | **28.4** |  391.7 |
| E2E median (ms)           |         73.7 | **58.6** |  428.0 |
| Throughput median (tok/s) |         20.1 | **22.2** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.4 |  **47.4** |   51.6 |
| TPOT median (ms)          |         19.3 |  **15.5** |   24.7 |
| E2E median (ms)           |        877.1 | **583.3** |  963.0 |
| Throughput median (tok/s) |         40.4 |  **60.6** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.6 |  **61.4** |   79.6 |
| TPOT median (ms)          |         24.2 |  **23.8** |  110.9 |
| E2E median (ms)           |        282.2 | **187.1** |  378.1 |
| Throughput median (tok/s) |         17.1 |  **24.0** |   13.1 |
| Correctness               |          99% |       98% |    98% |
