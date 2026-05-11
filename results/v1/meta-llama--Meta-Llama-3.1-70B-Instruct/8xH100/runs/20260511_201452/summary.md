# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:54 AM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/5 |   **2/5** | **2/5** |
| self_consistency |          2/5 |   **3/5** |     0/5 |
| multi_turn       |          0/5 |   **4/5** |     1/5 |
| tree_of_thought  |          0/5 |   **5/5** |     0/5 |
| long_output      |          0/5 |   **4/5** |     1/5 |
| **Total**        |         3/25 | **18/25** |    4/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     342.0s (5.7m) | `9e501e8` |
| vllm         |    971.1s (16.2m) | `56e5810` |
| sglang       | **163.4s (2.7m)** | `c7e53e6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        407.4 |    163.1 | **136.4** |
| TPOT median (ms)          |        290.0 | **60.1** |      73.6 |
| E2E median (ms)           |        657.8 |    222.1 | **204.0** |
| Throughput median (tok/s) |          2.0 |  **6.7** |       6.0 |
| Correctness               |      **98%** |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        470.5 | **190.4** |  195.1 |
| TPOT median (ms)          |      **0.0** |       0.0 |    0.0 |
| E2E median (ms)           |        560.6 | **213.0** |  343.8 |
| Throughput median (tok/s) |          1.8 |   **4.7** |    2.9 |
| Correctness               |     **100%** |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     169.4 | **154.3** |
| TPOT median (ms)          |            - |  **61.2** |     102.1 |
| E2E median (ms)           |            - | **219.6** |     249.7 |
| Throughput median (tok/s) |            - |   **6.4** |       5.1 |
| Correctness               |            - |   **98%** |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **58.1** |   78.1 |
| TPOT median (ms)          |            - | **26.8** |   43.7 |
| E2E median (ms)           |            - | **78.2** |  141.7 |
| Throughput median (tok/s) |            - | **15.8** |    9.9 |
| Correctness               |            - |  **97%** |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.9 | **64.9** |
| TPOT median (ms)          |            - |  **15.0** |     22.4 |
| E2E median (ms)           |            - | **619.5** |    832.1 |
| Throughput median (tok/s) |            - |  **58.7** |     42.1 |
| Correctness               |            - |  **100%** |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        438.9 |     130.4 | **125.8** |
| TPOT median (ms)          |        145.0 |  **32.6** |      48.4 |
| E2E median (ms)           |        609.2 | **270.5** |     354.2 |
| Throughput median (tok/s) |          1.9 |  **18.5** |      13.2 |
| Correctness               |      **99%** |       99% |       99% |
