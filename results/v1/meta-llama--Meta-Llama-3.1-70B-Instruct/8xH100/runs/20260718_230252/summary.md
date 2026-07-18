# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 18 2026

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
| torchinferno | **41.8s (0.7m)** | `96adc9d` |
| vllm         |    284.7s (4.7m) | `9243e01` |
| sglang       |    170.6s (2.8m) | `99f5a6f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        139.8 |  **85.9** |   87.7 |
| TPOT median (ms)          |     **32.1** |      39.0 |   69.4 |
| E2E median (ms)           |        164.2 | **123.2** |  149.9 |
| Throughput median (tok/s) |          7.1 |  **11.5** |    8.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **76.0** |  86.9 |  158.7 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **93.1** | 105.6 |  244.5 |
| Throughput median (tok/s) |     **10.7** |   9.5 |    4.1 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.7 |  **73.9** |  100.7 |
| TPOT median (ms)          |     **35.5** |      36.2 |   80.9 |
| E2E median (ms)           |        217.5 | **101.2** |  168.1 |
| Throughput median (tok/s) |          5.2 |  **13.1** |    7.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.3 | **37.8** |   65.8 |
| TPOT median (ms)          |         34.7 | **28.0** |  452.7 |
| E2E median (ms)           |         72.4 | **58.2** |  495.3 |
| Throughput median (tok/s) |         19.9 | **22.4** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.7 |  **46.8** |   62.9 |
| TPOT median (ms)          |         19.4 |  **15.4** |   29.4 |
| E2E median (ms)           |        885.9 | **578.0** | 1097.9 |
| Throughput median (tok/s) |         39.3 |  **60.7** |   32.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.3 |  **66.3** |   95.2 |
| TPOT median (ms)          |         24.3 |  **23.7** |  126.5 |
| E2E median (ms)           |        286.6 | **193.2** |  431.1 |
| Throughput median (tok/s) |         16.4 |  **23.4** |   11.3 |
| Correctness               |          99% |       99% |    98% |
