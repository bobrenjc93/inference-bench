# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jul 19 2026

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
| torchinferno | **41.9s (0.7m)** | `96adc9d` |
| vllm         |    222.8s (3.7m) | `ace9fda` |
| sglang       |    173.6s (2.9m) | `d4801be` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.5 |  **78.1** |   96.0 |
| TPOT median (ms)          |     **31.9** |      36.9 |   73.2 |
| E2E median (ms)           |        165.7 | **104.4** |  160.3 |
| Throughput median (tok/s) |          7.0 |  **12.9** |    8.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.4** | 74.5 |  165.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **73.4** | 92.6 |  247.1 |
| Throughput median (tok/s) |     **13.6** | 10.8 |    4.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.8 |  **87.3** |   99.3 |
| TPOT median (ms)          |     **36.0** |      38.9 |   77.4 |
| E2E median (ms)           |        220.9 | **116.9** |  164.8 |
| Throughput median (tok/s) |          5.1 |  **11.4** |    7.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.7 | **37.2** |   69.7 |
| TPOT median (ms)          |         34.8 | **27.4** |  406.4 |
| E2E median (ms)           |         73.6 | **56.7** |  475.2 |
| Throughput median (tok/s) |         19.5 | **22.8** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.6 |  **46.7** |   61.2 |
| TPOT median (ms)          |         19.5 |  **15.5** |   29.2 |
| E2E median (ms)           |        891.0 | **582.0** | 1134.6 |
| Throughput median (tok/s) |         40.6 |  **60.6** |   33.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.8 |  **64.8** |   98.3 |
| TPOT median (ms)          |         24.4 |  **23.7** |  117.3 |
| E2E median (ms)           |        284.9 | **190.5** |  436.4 |
| Throughput median (tok/s) |         17.2 |  **23.7** |   11.2 |
| Correctness               |          99% |       99% |    99% |
