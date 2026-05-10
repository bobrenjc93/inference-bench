# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:57 PM PT, May 9 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **4/5** |    1/5 |          0/5 |
| multi_turn       |   **3/5** |    2/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **19/25** |   6/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1312.9s (21.9m) |
| sglang       |    178.1s (3.0m) |
| torchinferno | **45.0s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     146.6 | **134.7** |        778.3 |
| TPOT median (ms)          |  **55.4** |      76.3 |        115.1 |
| E2E median (ms)           | **196.9** |     208.3 |        930.6 |
| Throughput median (tok/s) |   **7.5** |       5.8 |          1.3 |
| Correctness               |       98% |   **98%** |          98% |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     231.0 | **197.8** |        376.6 |
| TPOT median (ms)          |   **0.0** |       0.0 |          0.0 |
| E2E median (ms)           | **281.4** |     344.3 |        479.4 |
| Throughput median (tok/s) |   **3.6** |       2.9 |          2.1 |
| Correctness               |  **100%** |      100% |         100% |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     187.9 | **159.3** |            - |
| TPOT median (ms)          |  **68.0** |     102.8 |            - |
| E2E median (ms)           | **248.2** |     259.6 |            - |
| Throughput median (tok/s) |   **5.7** |       5.1 |            - |
| Correctness               |       98% |   **98%** |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **57.9** |   75.5 |            - |
| TPOT median (ms)          | **27.1** |   59.8 |            - |
| E2E median (ms)           | **78.4** |  141.2 |            - |
| Throughput median (tok/s) | **15.9** |    9.8 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      68.6 | **67.6** |            - |
| TPOT median (ms)          |  **14.6** |     22.0 |            - |
| E2E median (ms)           | **630.2** |    899.1 |            - |
| Throughput median (tok/s) |  **60.8** |     42.6 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     138.4 | **127.0** |        577.4 |
| TPOT median (ms)          |  **33.0** |      52.2 |         57.6 |
| E2E median (ms)           | **287.0** |     370.5 |        705.0 |
| Throughput median (tok/s) |  **18.7** |      13.2 |          1.7 |
| Correctness               |       99% |       99% |      **99%** |
