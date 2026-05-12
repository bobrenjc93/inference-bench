# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 AM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **85.5s (1.4m)** | `b468ebb` |
| vllm         |  1194.6s (19.9m) | `d37e25f` |
| sglang       |    169.6s (2.8m) | `8d27ce7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        572.1 |    169.5 | **144.7** |
| TPOT median (ms)          |        453.2 | **58.8** |      82.7 |
| E2E median (ms)           |        885.6 |    233.1 | **219.8** |
| Throughput median (tok/s) |          1.6 |  **6.3** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        458.1 | **180.0** |  213.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        558.9 | **206.2** |  366.5 |
| Throughput median (tok/s) |          1.8 |   **4.8** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1193.6 |     183.5 | **161.8** |
| TPOT median (ms)          |        781.2 |  **64.0** |     112.0 |
| E2E median (ms)           |       1941.2 | **239.2** |     267.8 |
| Throughput median (tok/s) |          0.7 |   **5.9** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        582.8 | **61.3** |   79.4 |
| TPOT median (ms)          |        501.9 | **27.2** |   62.8 |
| E2E median (ms)           |        978.7 | **82.5** |  157.1 |
| Throughput median (tok/s) |          1.6 | **14.9** |    8.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1348.4 |  **75.1** |   75.4 |
| TPOT median (ms)          |         29.7 |  **15.1** |   21.7 |
| E2E median (ms)           |       2435.3 | **672.6** |  842.3 |
| Throughput median (tok/s) |         13.7 |  **57.8** |   42.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        831.0 | **133.9** |  135.1 |
| TPOT median (ms)          |        353.2 |  **33.0** |   55.9 |
| E2E median (ms)           |       1360.0 | **286.7** |  370.7 |
| Throughput median (tok/s) |          3.9 |  **18.0** |   12.9 |
| Correctness               |          98% |       99% |    99% |
