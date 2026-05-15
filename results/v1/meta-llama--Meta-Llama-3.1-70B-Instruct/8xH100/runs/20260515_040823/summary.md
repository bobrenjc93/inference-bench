# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:08 PM PT, May 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     409.0s (6.8m) | `d648af4` |
| vllm         |   1110.0s (18.5m) | `0d4d334` |
| sglang       | **150.8s (2.5m)** | `897587b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        311.7 |    156.5 | **138.4** |
| TPOT median (ms)          |        159.3 | **54.1** |      75.6 |
| E2E median (ms)           |        399.2 |    207.8 | **206.4** |
| Throughput median (tok/s) |          3.7 |  **7.2** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.8 | **205.5** |  224.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        361.9 | **226.7** |  368.1 |
| Throughput median (tok/s) |          2.8 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        563.2 |     166.7 | **159.1** |
| TPOT median (ms)          |        158.0 |  **67.4** |     103.1 |
| E2E median (ms)           |        664.7 | **225.2** |     252.8 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        370.8 | **57.7** |   76.2 |
| TPOT median (ms)          |        138.0 | **27.0** |   56.0 |
| E2E median (ms)           |        476.2 | **77.8** |  146.2 |
| Throughput median (tok/s) |          2.8 | **15.7** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        605.7 |      69.8 | **66.0** |
| TPOT median (ms)          |         15.5 |  **15.1** |     22.5 |
| E2E median (ms)           |       1231.0 | **603.5** |    837.6 |
| Throughput median (tok/s) |         27.9 |  **59.1** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        426.6 | **131.2** |  132.8 |
| TPOT median (ms)          |         94.2 |  **32.7** |   51.5 |
| E2E median (ms)           |        626.6 | **268.2** |  362.2 |
| Throughput median (tok/s) |          7.8 |  **18.5** |   13.0 |
| Correctness               |          99% |       99% |    99% |
