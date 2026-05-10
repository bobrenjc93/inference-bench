# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **4/5** |    1/5 |          0/5 |
| tree_of_thought  |   **4/5** |    1/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **20/25** |   5/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |
| :----------- | ---------------: |
| vllm         |  1297.4s (21.6m) |
| sglang       |    177.9s (3.0m) |
| torchinferno | **44.1s (0.7m)** |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     147.4 | **135.2** |            - |
| TPOT median (ms)          |  **53.8** |      75.2 |            - |
| E2E median (ms)           | **194.6** |     206.5 |            - |
| Throughput median (tok/s) |   **7.5** |       5.9 |            - |
| Correctness               |       98% |   **98%** |            - |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **198.5** |  198.8 |            - |
| TPOT median (ms)          |   **0.0** |    0.0 |            - |
| E2E median (ms)           | **267.2** |  349.0 |            - |
| Throughput median (tok/s) |   **3.7** |    2.9 |            - |
| Correctness               |  **100%** |   100% |            - |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     186.6 | **158.8** |            - |
| TPOT median (ms)          |  **71.3** |     103.6 |            - |
| E2E median (ms)           | **250.8** |     258.0 |            - |
| Throughput median (tok/s) |   **5.8** |       5.1 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **57.7** |    75.2 |            - |
| TPOT median (ms)          | **26.8** |    62.9 |            - |
| E2E median (ms)           | **78.4** |   145.7 |            - |
| Throughput median (tok/s) | **16.0** |     9.7 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      69.0 | **64.0** |            - |
| TPOT median (ms)          |  **14.6** |     22.2 |            - |
| E2E median (ms)           | **630.9** |    891.5 |            - |
| Throughput median (tok/s) |  **60.9** |     42.5 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     131.8 | **126.4** |            - |
| TPOT median (ms)          |  **33.3** |      52.8 |            - |
| E2E median (ms)           | **284.4** |     370.1 |            - |
| Throughput median (tok/s) |  **18.8** |      13.2 |            - |
| Correctness               |   **99%** |       99% |            - |
