# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:03 PM PT, May 24 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **89.3s (1.5m)** | `9f91b40` |
| vllm         |  1204.8s (20.1m) | `b06813e` |
| sglang       |    179.9s (3.0m) | `821d5f4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        298.1 |    175.3 | **150.2** |
| TPOT median (ms)          |        160.1 | **65.3** |      76.0 |
| E2E median (ms)           |        395.1 |    231.9 | **220.5** |
| Throughput median (tok/s) |          3.8 |  **6.5** |       5.3 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        273.7 | **186.4** |  216.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        335.5 | **209.4** |  366.2 |
| Throughput median (tok/s) |          3.0 |   **4.8** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1099.3 |     188.8 | **173.7** |
| TPOT median (ms)          |        116.9 |  **63.6** |     105.9 |
| E2E median (ms)           |       1194.3 | **245.1** |     285.1 |
| Throughput median (tok/s) |          1.0 |   **5.6** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        367.5 | **62.7** |   81.7 |
| TPOT median (ms)          |        137.2 | **27.9** |   55.7 |
| E2E median (ms)           |        479.5 | **84.6** |  147.8 |
| Throughput median (tok/s) |          2.7 | **14.8** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      83.2 | **79.4** |
| TPOT median (ms)          |            - |  **15.0** |     22.1 |
| E2E median (ms)           |            - | **621.1** |    830.8 |
| Throughput median (tok/s) |            - |  **57.7** |     41.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        509.7 | **139.3** |  140.3 |
| TPOT median (ms)          |        103.5 |  **34.4** |   51.9 |
| E2E median (ms)           |        601.1 | **278.4** |  370.1 |
| Throughput median (tok/s) |          2.6 |  **17.9** |   12.7 |
| Correctness               |          98% |       99% |    98% |
