# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:30 AM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |    vllm |    sglang |
| :--------------- | -----------: | ------: | --------: |
| few_shot         |          1/4 |     0/4 |   **3/4** |
| self_consistency |          0/4 | **2/4** |       1/4 |
| multi_turn       |          1/4 |     0/4 |   **3/4** |
| tree_of_thought  |          1/4 |     0/4 |   **3/4** |
| long_output      |          0/4 |     0/4 |   **4/4** |
| **Total**        |         3/20 |    2/20 | **14/20** |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **0.0s (0.0m)** | `467c3c3` |
| vllm         |     0.0s (0.0m) |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        165.3 | 232.7 | **122.8** |
| TPOT median (ms)          |     **51.1** |  84.6 |      79.0 |
| E2E median (ms)           |        207.1 | 302.8 | **198.1** |
| Throughput median (tok/s) |          5.6 |   5.1 |   **6.1** |
| Correctness               |          98% |   98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        245.0 |     274.2 | **206.4** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        329.0 | **321.8** |     389.0 |
| Throughput median (tok/s) |          3.0 |   **3.1** |       2.6 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        348.1 | 271.7 | **163.3** |
| TPOT median (ms)          |     **61.2** | 103.4 |     106.2 |
| E2E median (ms)           |        408.1 | 361.3 | **280.9** |
| Throughput median (tok/s) |          3.1 |   4.0 |   **4.7** |
| Correctness               |          98% |   98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        238.2 | 119.2 |  **62.5** |
| TPOT median (ms)          |     **48.6** |  81.8 |      73.4 |
| E2E median (ms)           |        281.2 | 186.3 | **149.7** |
| Throughput median (tok/s) |          4.5 |   6.7 |   **9.5** |
| Correctness               |          96% |   97% |       97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |   vllm |    sglang |
| :------------------------ | -----------: | -----: | --------: |
| TTFT median (ms)          |        301.9 |   92.3 |  **61.8** |
| TPOT median (ms)          |         25.5 |   26.0 |  **24.1** |
| E2E median (ms)           |       1154.4 | 1113.7 | **905.3** |
| Throughput median (tok/s) |         30.5 |   34.1 |  **39.6** |
| Correctness               |         100% |   100% |      100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        259.7 | 198.0 | **123.4** |
| TPOT median (ms)          |     **37.3** |  59.2 |      56.5 |
| E2E median (ms)           |        476.0 | 457.2 | **384.6** |
| Throughput median (tok/s) |          9.3 |  10.6 |  **12.5** |
| Correctness               |          98% |   98% |       98% |
