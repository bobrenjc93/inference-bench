# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **4/5** |    1/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **21/25** |   4/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1383.4s (23.1m) | `4b64fc2` |
| sglang       |    203.7s (3.4m) | `2e69266` |
| torchinferno | **44.3s (0.7m)** | `af56747` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    164.6 | **136.3** |        271.7 |
| TPOT median (ms)          | **57.2** |      70.2 |        238.3 |
| E2E median (ms)           |    217.8 | **202.3** |        504.2 |
| Throughput median (tok/s) |  **6.4** |       6.1 |          2.7 |
| Correctness               |  **98%** |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **181.2** |  198.7 |        403.6 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **203.8** |  339.3 |        515.5 |
| Throughput median (tok/s) |   **4.9** |    2.9 |          1.9 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     171.0 | **162.3** |            - |
| TPOT median (ms)          |  **54.4** |      97.5 |            - |
| E2E median (ms)           | **216.7** |     260.4 |            - |
| Throughput median (tok/s) |   **6.4** |       4.9 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **58.9** |   71.8 |            - |
| TPOT median (ms)          | **27.3** |   67.8 |            - |
| E2E median (ms)           | **79.5** |  161.0 |            - |
| Throughput median (tok/s) | **15.6** |    9.2 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      72.9 | **65.4** |            - |
| TPOT median (ms)          |  **15.0** |     22.1 |            - |
| E2E median (ms)           | **641.4** |    835.2 |            - |
| Throughput median (tok/s) |  **58.0** |     42.8 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     129.7 | **126.9** |        337.7 |
| TPOT median (ms)          |  **30.8** |      51.5 |        119.1 |
| E2E median (ms)           | **271.8** |     359.7 |        509.8 |
| Throughput median (tok/s) |  **18.2** |      13.2 |          2.3 |
| Correctness               |       99% |       99% |      **99%** |
