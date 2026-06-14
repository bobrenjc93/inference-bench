# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     376.0s (6.3m) | `a102128` |
| vllm         |   1326.2s (22.1m) | `cf027b8` |
| sglang       | **229.7s (3.8m)** | `a3fd5c2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.8 |     164.1 | **151.6** |
| TPOT median (ms)          |         92.2 |  **58.4** |      76.4 |
| E2E median (ms)           |        374.9 | **216.2** |     219.4 |
| Throughput median (tok/s) |          3.4 |   **6.9** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        301.8 | **196.2** |  218.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        419.8 | **258.9** |  352.1 |
| Throughput median (tok/s) |          2.4 |   **3.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        710.5 |     183.2 | **159.8** |
| TPOT median (ms)          |     **69.6** |      70.9 |     102.7 |
| E2E median (ms)           |        774.4 | **243.2** |     257.7 |
| Throughput median (tok/s) |          1.7 |   **5.7** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        256.0 | **65.7** |   84.3 |
| TPOT median (ms)          |         58.1 | **30.6** |   60.8 |
| E2E median (ms)           |        373.4 | **90.4** |  149.9 |
| Throughput median (tok/s) |          4.1 | **13.6** |    9.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        358.6 |      78.3 | **67.9** |
| TPOT median (ms)          |         21.3 |  **15.1** |     22.4 |
| E2E median (ms)           |       1136.0 | **635.6** |    832.7 |
| Throughput median (tok/s) |         31.4 |  **57.6** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        383.1 |     137.5 | **136.5** |
| TPOT median (ms)          |         48.2 |  **35.0** |      52.4 |
| E2E median (ms)           |        615.7 | **288.9** |     362.4 |
| Throughput median (tok/s) |          8.6 |  **17.5** |      13.0 |
| Correctness               |          98% |       99% |       99% |
