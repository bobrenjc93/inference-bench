# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:37 PM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **3/5** |    2/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **20/25** |   5/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1259.8s (21.0m) | `21943d4` |
| sglang       |    182.7s (3.0m) | `2473659` |
| torchinferno | **43.2s (0.7m)** | `432e970` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    161.9 | **136.0** |        627.4 |
| TPOT median (ms)          | **52.5** |      74.0 |        391.9 |
| E2E median (ms)           |    215.8 | **205.1** |       1031.5 |
| Throughput median (tok/s) |  **7.1** |       5.7 |          1.1 |
| Correctness               |  **98%** |       98% |          98% |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **177.3** |  209.5 |        308.0 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **198.1** |  344.5 |        445.1 |
| Throughput median (tok/s) |   **5.0** |    2.9 |          2.2 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     177.4 | **159.2** |       1642.3 |
| TPOT median (ms)          |  **52.7** |     106.5 |       1522.8 |
| E2E median (ms)           | **225.3** |     262.8 |       3110.6 |
| Throughput median (tok/s) |   **6.3** |       5.1 |          0.5 |
| Correctness               |       98% |   **98%** |          98% |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **58.0** |   74.3 |        502.1 |
| TPOT median (ms)          | **26.9** |   73.4 |        470.5 |
| E2E median (ms)           | **77.9** |  164.3 |        996.1 |
| Throughput median (tok/s) | **15.6** |    8.9 |          1.3 |
| Correctness               |  **97%** |    97% |          97% |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      73.8 | **66.3** |       4537.9 |
| TPOT median (ms)          |  **15.0** |     22.2 |       1493.6 |
| E2E median (ms)           | **620.8** |    840.5 |      53806.6 |
| Throughput median (tok/s) |  **58.7** |     42.4 |          0.6 |
| Correctness               |  **100%** |     100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     129.7 | **129.1** |       1523.5 |
| TPOT median (ms)          |  **29.4** |      55.2 |        775.7 |
| E2E median (ms)           | **267.6** |     363.5 |      11878.0 |
| Throughput median (tok/s) |  **18.5** |      13.0 |          1.2 |
| Correctness               |   **98%** |       98% |          98% |
