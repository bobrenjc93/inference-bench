# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:01 PM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/5 |   **2/5** | **2/5** |
| self_consistency |          2/5 |   **3/5** |     0/5 |
| multi_turn       |          0/5 |   **3/5** |     2/5 |
| tree_of_thought  |          0/5 |   **4/5** |     1/5 |
| long_output      |          0/5 |   **4/5** |     1/5 |
| **Total**        |         3/25 | **16/25** |    6/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **93.1s (1.6m)** | `7655aec` |
| vllm         |   965.5s (16.1m) | `5318138` |
| sglang       |    169.4s (2.8m) | `da0eeb8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        701.7 |    169.8 | **143.6** |
| TPOT median (ms)          |        449.6 | **62.6** |      78.2 |
| E2E median (ms)           |       1067.0 |    224.8 | **216.0** |
| Throughput median (tok/s) |          1.2 |  **6.6** |       5.5 |
| Correctness               |      **98%** |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        520.9 | **188.9** |  212.7 |
| TPOT median (ms)          |      **0.0** |       0.0 |    0.0 |
| E2E median (ms)           |        604.0 | **212.3** |  347.6 |
| Throughput median (tok/s) |          1.7 |   **4.7** |    2.9 |
| Correctness               |     **100%** |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     187.7 | **167.1** |
| TPOT median (ms)          |            - |  **64.7** |      97.9 |
| E2E median (ms)           |            - | **239.9** |     264.6 |
| Throughput median (tok/s) |            - |   **5.6** |       5.1 |
| Correctness               |            - |       98% |   **98%** |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm |  sglang |
| :------------------------ | -----------: | -------: | ------: |
| TTFT median (ms)          |            - | **61.6** |    77.8 |
| TPOT median (ms)          |            - | **28.2** |    60.4 |
| E2E median (ms)           |            - | **82.9** |   141.0 |
| Throughput median (tok/s) |            - | **15.0** |     9.6 |
| Correctness               |            - |      97% | **97%** |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      78.4 | **73.6** |
| TPOT median (ms)          |            - |  **15.0** |     22.5 |
| E2E median (ms)           |            - | **661.3** |    833.4 |
| Throughput median (tok/s) |            - |  **57.2** |     41.5 |
| Correctness               |            - |  **100%** |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        611.3 |     137.3 | **135.0** |
| TPOT median (ms)          |        224.8 |  **34.1** |      51.8 |
| E2E median (ms)           |        835.5 | **284.2** |     360.5 |
| Throughput median (tok/s) |          1.4 |  **17.8** |      12.9 |
| Correctness               |      **99%** |       99% |       99% |
