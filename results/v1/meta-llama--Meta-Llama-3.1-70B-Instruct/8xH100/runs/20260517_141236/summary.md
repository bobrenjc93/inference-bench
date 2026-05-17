# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:09 AM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     298.6s (5.0m) | `1cdab3f` |
| vllm         |   1119.8s (18.7m) | `0fa8884` |
| sglang       | **161.7s (2.7m)** | `eccfd6d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.0 |     156.6 | **140.6** |
| TPOT median (ms)          |        151.2 |  **56.8** |      72.2 |
| E2E median (ms)           |        371.3 | **211.2** |     212.1 |
| Throughput median (tok/s) |          3.8 |   **7.2** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        271.2 |     211.2 | **206.7** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        297.5 | **236.1** |     344.2 |
| Throughput median (tok/s) |          3.4 |   **4.2** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        518.0 |     170.8 | **154.4** |
| TPOT median (ms)          |        108.2 |  **47.6** |     106.6 |
| E2E median (ms)           |        609.3 | **211.8** |     255.3 |
| Throughput median (tok/s) |          2.2 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        324.0 | **57.5** |   73.7 |
| TPOT median (ms)          |        130.9 | **26.3** |   71.2 |
| E2E median (ms)           |        424.5 | **78.1** |  160.1 |
| Throughput median (tok/s) |          3.3 | **15.5** |    9.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        707.3 |      66.2 | **65.4** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.2 |
| E2E median (ms)           |       1378.0 | **603.6** |    820.3 |
| Throughput median (tok/s) |         26.1 |  **59.2** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        421.1 |     132.5 | **128.2** |
| TPOT median (ms)          |         81.3 |  **29.2** |      54.4 |
| E2E median (ms)           |        616.1 | **268.2** |     358.4 |
| Throughput median (tok/s) |          7.7 |  **18.5** |      13.1 |
| Correctness               |          98% |       99% |       99% |
