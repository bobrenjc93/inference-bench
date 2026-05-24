# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     402.1s (6.7m) | `9f91b40` |
| vllm         |   1310.5s (21.8m) | `33d7cbe` |
| sglang       | **197.7s (3.3m)** | `d6d9f12` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        271.9 |     153.9 | **139.7** |
| TPOT median (ms)          |        154.5 |  **50.6** |      75.1 |
| E2E median (ms)           |        366.2 | **195.8** |     208.8 |
| Throughput median (tok/s) |          4.1 |   **7.5** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        264.5 | **191.7** |  206.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        282.6 | **223.1** |  347.0 |
| Throughput median (tok/s) |          3.5 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        767.2 |     173.4 | **159.0** |
| TPOT median (ms)          |        114.3 |  **55.4** |     105.7 |
| E2E median (ms)           |        847.0 | **224.5** |     257.8 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        369.8 | **57.9** |   78.5 |
| TPOT median (ms)          |        133.6 | **27.1** |   58.8 |
| E2E median (ms)           |        479.2 | **78.2** |  151.5 |
| Throughput median (tok/s) |          2.8 | **15.5** |    9.5 |
| Correctness               |          97% |      96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        837.3 |      70.0 | **67.2** |
| TPOT median (ms)          |         15.6 |  **15.1** |     22.6 |
| E2E median (ms)           |       1495.6 | **616.5** |    855.8 |
| Throughput median (tok/s) |         23.5 |  **58.6** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        502.2 | **129.4** |  130.2 |
| TPOT median (ms)          |         83.6 |  **29.6** |   52.4 |
| E2E median (ms)           |        694.1 | **267.6** |  364.2 |
| Throughput median (tok/s) |          7.1 |  **18.5** |   12.9 |
| Correctness               |          98% |       98% |    98% |
