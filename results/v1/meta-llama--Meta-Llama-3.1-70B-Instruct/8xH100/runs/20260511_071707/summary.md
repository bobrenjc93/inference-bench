# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:01 PM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm |  sglang | torchinferno |
| :--------------- | --------: | ------: | -----------: |
| few_shot         |       2/5 | **3/5** |          0/5 |
| self_consistency |   **5/5** |     0/5 |          0/5 |
| multi_turn       |   **4/5** |     1/5 |          0/5 |
| tree_of_thought  |   **5/5** |     0/5 |          0/5 |
| long_output      |   **4/5** |     1/5 |          0/5 |
| **Total**        | **20/25** |    5/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1328.1s (22.1m) | `581b5e9` |
| sglang       |    174.7s (2.9m) | `d102b0c` |
| torchinferno | **43.1s (0.7m)** | `f38bf91` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    166.7 | **136.7** |        540.6 |
| TPOT median (ms)          | **56.6** |      74.7 |        571.4 |
| E2E median (ms)           |    224.9 | **205.3** |       1093.9 |
| Throughput median (tok/s) |  **6.5** |       5.8 |          1.1 |
| Correctness               |      98% |   **98%** |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **179.8** |  223.9 |        429.7 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **201.3** |  358.8 |        520.9 |
| Throughput median (tok/s) |   **5.0** |    2.8 |          1.9 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     172.5 | **161.4** |            - |
| TPOT median (ms)          |  **52.3** |      98.0 |            - |
| E2E median (ms)           | **218.0** |     262.0 |            - |
| Throughput median (tok/s) |   **6.4** |       5.2 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **57.0** |   73.1 |            - |
| TPOT median (ms)          | **26.2** |   73.0 |            - |
| E2E median (ms)           | **76.2** |  157.8 |            - |
| Throughput median (tok/s) | **15.8** |    9.4 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      70.0 | **67.9** |            - |
| TPOT median (ms)          |  **14.9** |     22.6 |            - |
| E2E median (ms)           | **622.1** |    842.8 |            - |
| Throughput median (tok/s) |  **58.4** |     41.8 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **129.2** |  132.6 |        485.2 |
| TPOT median (ms)          |  **30.0** |   53.7 |        285.7 |
| E2E median (ms)           | **268.5** |  365.3 |        807.4 |
| Throughput median (tok/s) |  **18.4** |   13.0 |          1.5 |
| Correctness               |       99% |    99% |      **99%** |
