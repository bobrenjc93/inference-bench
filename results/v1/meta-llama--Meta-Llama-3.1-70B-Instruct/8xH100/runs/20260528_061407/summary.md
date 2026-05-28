# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, May 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     397.4s (6.6m) | `f4c65f7` |
| vllm         |   1332.3s (22.2m) | `7909f82` |
| sglang       | **206.7s (3.4m)** | `e60f799` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        292.9 |    170.9 | **159.2** |
| TPOT median (ms)          |         72.5 | **58.1** |      74.9 |
| E2E median (ms)           |        364.2 |    230.2 | **226.4** |
| Throughput median (tok/s) |          3.4 |  **6.0** |       5.2 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.7 | **188.3** |  200.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        334.3 | **208.1** |  327.2 |
| Throughput median (tok/s) |          3.0 |   **4.8** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        733.0 |     169.9 | **163.5** |
| TPOT median (ms)          |     **55.4** |      68.8 |      97.6 |
| E2E median (ms)           |        786.7 | **224.7** |     257.3 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        213.5 | **57.9** |   84.1 |
| TPOT median (ms)          |     **27.2** |     27.7 |   39.3 |
| E2E median (ms)           |        233.2 | **78.2** |  136.4 |
| Throughput median (tok/s) |          6.0 | **15.7** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        852.1 |  **67.4** |   79.2 |
| TPOT median (ms)          |         15.3 |  **15.0** |   23.0 |
| E2E median (ms)           |       1397.6 | **608.5** |  844.2 |
| Throughput median (tok/s) |         25.2 |  **59.5** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        476.1 | **130.9** |  137.4 |
| TPOT median (ms)          |         34.1 |  **33.9** |   46.9 |
| E2E median (ms)           |        623.2 | **269.9** |  358.3 |
| Throughput median (tok/s) |          7.9 |  **18.4** |   12.8 |
| Correctness               |          99% |       99% |    99% |
