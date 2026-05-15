# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:08 AM PT, May 15 2026

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
| torchinferno |     273.2s (4.6m) | `d648af4` |
| vllm         |   1129.1s (18.8m) | `95cfe10` |
| sglang       | **164.6s (2.7m)** | `fd95254` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        302.1 |    164.0 | **133.3** |
| TPOT median (ms)          |        160.7 | **57.7** |      69.6 |
| E2E median (ms)           |        398.5 |    216.3 | **195.9** |
| Throughput median (tok/s) |          3.6 |  **6.6** |       6.2 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.8 | **189.5** |  197.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        352.1 | **213.1** |  332.8 |
| Throughput median (tok/s) |          2.8 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        561.3 |     169.8 | **156.2** |
| TPOT median (ms)          |        153.3 |  **60.2** |      97.0 |
| E2E median (ms)           |        654.1 | **222.2** |     250.9 |
| Throughput median (tok/s) |          2.0 |   **6.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        382.3 | **58.1** |   72.9 |
| TPOT median (ms)          |        135.5 | **27.1** |   58.3 |
| E2E median (ms)           |        496.9 | **78.4** |  143.4 |
| Throughput median (tok/s) |          2.6 | **15.5** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        624.4 |      70.1 | **66.3** |
| TPOT median (ms)          |         15.4 |  **15.1** |     22.1 |
| E2E median (ms)           |       1203.5 | **612.3** |    833.5 |
| Throughput median (tok/s) |         26.7 |  **58.9** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        432.2 |     130.3 | **125.1** |
| TPOT median (ms)          |         93.0 |  **32.0** |      49.4 |
| E2E median (ms)           |        621.0 | **268.5** |     351.3 |
| Throughput median (tok/s) |          7.6 |  **18.4** |      13.4 |
| Correctness               |          98% |       99% |       98% |
