# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:57 AM PT, Jun 29 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     0/4 |   **3/4** |          1/4 |
| self_consistency | **2/4** |       1/4 |          0/4 |
| multi_turn       |     0/4 |   **3/4** |          1/4 |
| tree_of_thought  |     0/4 |   **3/4** |          1/4 |
| long_output      |     0/4 |   **4/4** |          0/4 |
| **Total**        |    2/20 | **14/20** |         3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |
| torchinferno |     0.0s (0.0m) | `20cb8e8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 227.0 | **126.5** |        171.0 |
| TPOT median (ms)          |  85.7 |      80.6 |     **50.5** |
| E2E median (ms)           | 292.7 | **207.9** |        215.8 |
| Throughput median (tok/s) |   5.0 |   **5.8** |          5.3 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     210.9 | **206.2** |        319.3 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **285.3** |     361.4 |        398.6 |
| Throughput median (tok/s) |   **3.5** |       2.8 |          2.5 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 290.4 | **155.1** |        302.0 |
| TPOT median (ms)          | 100.9 |     122.9 |     **66.1** |
| E2E median (ms)           | 373.6 | **269.3** |        358.1 |
| Throughput median (tok/s) |   4.0 |   **4.7** |          3.8 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 129.0 |  **61.5** |        279.1 |
| TPOT median (ms)          |  82.8 |      68.4 |     **47.6** |
| E2E median (ms)           | 187.8 | **140.2** |        318.9 |
| Throughput median (tok/s) |   6.6 |   **9.4** |          4.5 |
| Correctness               |   97% |       97% |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   90.8 |  **62.9** |        281.0 |
| TPOT median (ms)          |   27.6 |  **24.6** |         24.7 |
| E2E median (ms)           | 1089.0 | **908.1** |       1200.5 |
| Throughput median (tok/s) |   33.6 |  **38.3** |         31.3 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 189.6 | **122.5** |        270.5 |
| TPOT median (ms)          |  59.4 |      59.3 |     **37.8** |
| E2E median (ms)           | 445.7 | **377.4** |        498.4 |
| Throughput median (tok/s) |  10.5 |  **12.2** |          9.5 |
| Correctness               |   99% |       99% |          98% |
