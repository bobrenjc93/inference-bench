# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 14 2026

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
| torchinferno | **37.5s (0.6m)** | `96adc9d` |
| vllm         |    334.4s (5.6m) | `520a20b` |
| sglang       |    160.0s (2.7m) | `50d1eda` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        146.2 |  **76.4** |   80.4 |
| TPOT median (ms)          |     **30.7** |      37.8 |   66.1 |
| E2E median (ms)           |        170.3 | **103.1** |  137.4 |
| Throughput median (tok/s) |          6.7 |  **13.3** |   10.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **63.7** | 77.6 |  121.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **83.7** | 94.2 |  216.1 |
| Throughput median (tok/s) |     **11.9** | 10.6 |    4.6 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        190.2 | **71.1** |   83.7 |
| TPOT median (ms)          |     **34.0** |     36.9 |   71.0 |
| E2E median (ms)           |        217.6 | **97.4** |  144.1 |
| Throughput median (tok/s) |          5.1 | **13.2** |    9.3 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.0 | **36.8** |   52.3 |
| TPOT median (ms)          |         34.7 | **27.0** |  351.0 |
| E2E median (ms)           |         74.4 | **55.1** |  435.9 |
| Throughput median (tok/s) |         19.8 | **23.1** |    3.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.9 |  **47.3** |   51.8 |
| TPOT median (ms)          |         19.4 |  **15.6** |   25.0 |
| E2E median (ms)           |        876.9 | **581.3** |  956.7 |
| Throughput median (tok/s) |         40.8 |  **59.7** |   38.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.0 |  **61.9** |   78.0 |
| TPOT median (ms)          |         23.8 |  **23.5** |  102.6 |
| E2E median (ms)           |        284.6 | **186.2** |  378.0 |
| Throughput median (tok/s) |         16.9 |  **24.0** |   13.2 |
| Correctness               |          98% |       99% |    98% |
