# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jun 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     363.4s (6.1m) | `a870596` |
| vllm         |   1321.7s (22.0m) | `2c9c07c` |
| sglang       | **205.5s (3.4m)** | `047e5df` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        317.0 |     157.3 | **150.2** |
| TPOT median (ms)          |         83.8 |  **55.8** |      73.2 |
| E2E median (ms)           |        391.9 | **205.5** |     219.9 |
| Throughput median (tok/s) |          3.1 |   **7.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        382.9 | **185.2** |  211.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        536.6 | **208.5** |  347.5 |
| Throughput median (tok/s) |          1.9 |   **4.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        754.8 |     174.5 | **160.7** |
| TPOT median (ms)          |         67.0 |  **61.7** |      98.6 |
| E2E median (ms)           |        823.0 | **231.7** |     263.5 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        364.8 | **61.1** |   78.2 |
| TPOT median (ms)          |         65.1 | **28.6** |   64.3 |
| E2E median (ms)           |        450.6 | **83.0** |  151.8 |
| Throughput median (tok/s) |          3.2 | **14.3** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.9 |  **68.5** |   85.1 |
| TPOT median (ms)          |         26.5 |  **15.1** |   23.5 |
| E2E median (ms)           |       1254.9 | **608.0** |  909.7 |
| Throughput median (tok/s) |         31.1 |  **59.0** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        401.9 | **129.3** |  137.1 |
| TPOT median (ms)          |         48.5 |  **32.2** |   51.9 |
| E2E median (ms)           |        691.4 | **267.3** |  378.5 |
| Throughput median (tok/s) |          8.2 |  **18.3** |   12.4 |
| Correctness               |          98% |       99% |    98% |
