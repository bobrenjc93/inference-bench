# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 17 2026

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
| torchinferno | **44.4s (0.7m)** | `96adc9d` |
| vllm         |    358.3s (6.0m) | `4c6e2e4` |
| sglang       |    165.9s (2.8m) | `85ac56c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.6 |  **74.2** |   96.6 |
| TPOT median (ms)          |     **32.0** |      35.5 |   73.5 |
| E2E median (ms)           |        166.3 | **102.7** |  162.9 |
| Throughput median (tok/s) |          6.9 |  **13.5** |    8.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.1** | 71.9 |  134.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **73.0** | 90.3 |  212.1 |
| Throughput median (tok/s) |     **13.7** | 11.1 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.9 |  **88.0** |   88.9 |
| TPOT median (ms)          |         35.0 |  **34.2** |   82.2 |
| E2E median (ms)           |        219.7 | **116.0** |  158.3 |
| Throughput median (tok/s) |          5.1 |  **11.8** |    8.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.0 | **36.8** |   58.1 |
| TPOT median (ms)          |         34.7 | **27.1** |  470.4 |
| E2E median (ms)           |         75.8 | **55.5** |  483.8 |
| Throughput median (tok/s) |         19.5 | **23.4** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.9 |  **47.3** |   55.2 |
| TPOT median (ms)          |         19.5 |  **15.1** |   26.9 |
| E2E median (ms)           |        837.1 | **575.8** | 1019.0 |
| Throughput median (tok/s) |         41.6 |  **61.7** |   35.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.1 |  **63.6** |   86.7 |
| TPOT median (ms)          |         24.2 |  **22.4** |  130.6 |
| E2E median (ms)           |        274.4 | **188.1** |  407.2 |
| Throughput median (tok/s) |         17.4 |  **24.3** |   12.1 |
| Correctness               |          99% |       99% |    99% |
