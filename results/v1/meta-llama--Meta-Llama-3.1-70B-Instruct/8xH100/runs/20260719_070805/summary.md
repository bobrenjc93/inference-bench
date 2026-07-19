# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 AM PT, Jul 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **50.0s (0.8m)** | `96adc9d` |
| vllm         |    344.0s (5.7m) | `b6ff8a2` |
| sglang       |    187.6s (3.1m) | `942bf04` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        142.0 |      83.1 | **80.9** |
| TPOT median (ms)          |     **31.6** |      43.1 |     65.3 |
| E2E median (ms)           |        165.2 | **120.3** |    135.7 |
| Throughput median (tok/s) |          6.9 |  **11.8** |      9.7 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.6** | 71.6 |  149.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.1** | 90.0 |  227.0 |
| Throughput median (tok/s) |     **13.5** | 11.1 |    4.4 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.0 |  **77.4** |   91.0 |
| TPOT median (ms)          |     **34.8** |      35.8 |   76.2 |
| E2E median (ms)           |        218.0 | **102.5** |  156.7 |
| Throughput median (tok/s) |          5.2 |  **12.5** |    8.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.3 | **35.1** |   57.0 |
| TPOT median (ms)          |         34.5 | **23.5** |  396.6 |
| E2E median (ms)           |         72.2 | **53.2** |  431.6 |
| Throughput median (tok/s) |         20.0 | **24.4** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.3 |  **46.5** |   56.0 |
| TPOT median (ms)          |         19.3 |  **15.4** |   27.3 |
| E2E median (ms)           |        839.3 | **588.3** | 1056.8 |
| Throughput median (tok/s) |         41.0 |  **60.6** |   35.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.8 |  **62.7** |   86.9 |
| TPOT median (ms)          |         24.0 |  **23.6** |  113.1 |
| E2E median (ms)           |        273.8 | **190.9** |  401.6 |
| Throughput median (tok/s) |         17.3 |  **24.1** |   12.2 |
| Correctness               |          99% |       99% |    99% |
