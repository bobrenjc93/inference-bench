# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, May 11 2026

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
| vllm         |  1375.7s (22.9m) | `8415bf2` |
| sglang       |    199.7s (3.3m) | `62edbc3` |
| torchinferno | **44.3s (0.7m)** | `57745fd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    159.4 | **134.9** |        288.6 |
| TPOT median (ms)          | **52.8** |      75.8 |        257.3 |
| E2E median (ms)           |    208.9 | **206.1** |        531.8 |
| Throughput median (tok/s) |  **7.1** |       6.0 |          2.3 |
| Correctness               |      98% |   **98%** |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **182.1** |  219.5 |        458.1 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **203.6** |  359.4 |        560.3 |
| Throughput median (tok/s) |   **4.9** |    2.8 |          1.8 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     172.1 | **165.0** |        629.9 |
| TPOT median (ms)          |  **65.9** |      92.0 |        311.4 |
| E2E median (ms)           | **231.3** |     262.9 |        936.3 |
| Throughput median (tok/s) |   **6.0** |       5.0 |          1.5 |
| Correctness               |   **98%** |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **58.0** |   76.3 |            - |
| TPOT median (ms)          | **26.7** |   77.6 |            - |
| E2E median (ms)           | **78.4** |  167.6 |            - |
| Throughput median (tok/s) | **15.9** |    8.8 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      74.1 | **66.9** |            - |
| TPOT median (ms)          |  **14.9** |     21.8 |            - |
| E2E median (ms)           | **636.9** |    814.0 |            - |
| Throughput median (tok/s) |  **58.2** |     43.1 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **129.1** |  132.5 |        458.9 |
| TPOT median (ms)          |  **32.1** |   53.4 |        189.6 |
| E2E median (ms)           | **271.8** |  362.0 |        676.2 |
| Throughput median (tok/s) |  **18.4** |   13.1 |          1.9 |
| Correctness               |       99% |    99% |      **99%** |
