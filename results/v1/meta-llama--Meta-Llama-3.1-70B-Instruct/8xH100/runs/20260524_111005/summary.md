# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     257.7s (4.3m) | `9f91b40` |
| vllm         |   1246.3s (20.8m) | `5940590` |
| sglang       | **193.7s (3.2m)** | `6447596` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        273.5 |    167.2 | **142.8** |
| TPOT median (ms)          |        155.5 | **63.8** |      69.2 |
| E2E median (ms)           |        371.7 |    227.5 | **207.0** |
| Throughput median (tok/s) |          4.1 |  **6.4** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.3 |     207.2 | **204.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        303.9 | **231.7** |     336.0 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        715.0 |     167.9 | **164.3** |
| TPOT median (ms)          |        103.0 |  **54.3** |     103.0 |
| E2E median (ms)           |        867.9 | **212.0** |     261.9 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        368.4 | **58.1** |   80.2 |
| TPOT median (ms)          |        133.0 | **26.6** |   57.4 |
| E2E median (ms)           |        469.5 | **78.8** |  154.6 |
| Throughput median (tok/s) |          2.8 | **15.8** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        729.2 |      68.6 | **66.9** |
| TPOT median (ms)          |         15.6 |  **15.0** |     22.7 |
| E2E median (ms)           |       1463.1 | **608.7** |    856.9 |
| Throughput median (tok/s) |         24.2 |  **59.2** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        473.1 |     133.8 | **131.8** |
| TPOT median (ms)          |         81.4 |  **31.9** |      50.4 |
| E2E median (ms)           |        695.2 | **271.8** |     363.3 |
| Throughput median (tok/s) |          7.2 |  **18.4** |      13.0 |
| Correctness               |          98% |       99% |       98% |
