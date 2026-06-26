# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:14 AM PT, Jun 26 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **2/4** |    1/4 |          1/4 |
| self_consistency |   **2/4** |    0/4 |          1/4 |
| multi_turn       |   **3/4** |    0/4 |          1/4 |
| tree_of_thought  |   **4/4** |    0/4 |          0/4 |
| long_output      |   **4/4** |    0/4 |          0/4 |
| **Total**        | **15/20** |   1/20 |         3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `9222148` |
| sglang       |     0.0s (0.0m) | `bc15017` |
| torchinferno |     0.0s (0.0m) | `b068e8b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     158.9 | **144.7** |        171.8 |
| TPOT median (ms)          |      61.0 |      90.2 |     **54.2** |
| E2E median (ms)           | **209.0** |     230.5 |        220.6 |
| Throughput median (tok/s) |   **6.9** |       5.2 |          5.1 |
| Correctness               |       98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |     177.4 |  220.1 |    **155.5** |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **333.4** |  431.5 |        334.5 |
| Throughput median (tok/s) |   **3.0** |    2.3 |          3.0 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **131.7** |  177.1 |        484.7 |
| TPOT median (ms)          |      83.8 |  115.7 |     **68.5** |
| E2E median (ms)           | **214.6** |  289.9 |        541.5 |
| Throughput median (tok/s) |   **5.9** |    4.4 |          2.3 |
| Correctness               |       98% |    98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **73.4** |   77.6 |        309.3 |
| TPOT median (ms)          | **35.2** |   63.1 |         57.0 |
| E2E median (ms)           | **99.9** |  149.0 |        342.8 |
| Throughput median (tok/s) | **12.0** |    8.8 |          4.1 |
| Correctness               |      97% |    96% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **85.6** |  100.3 |        296.5 |
| TPOT median (ms)          |  **18.8** |   25.8 |         28.1 |
| E2E median (ms)           | **755.2** |  996.4 |       1466.5 |
| Throughput median (tok/s) |  **47.0** |   35.0 |         25.7 |
| Correctness               |      100% |   100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **125.4** |  143.9 |        283.6 |
| TPOT median (ms)          |  **39.8** |   59.0 |         41.6 |
| E2E median (ms)           | **322.4** |  419.4 |        581.2 |
| Throughput median (tok/s) |  **15.0** |   11.1 |          8.0 |
| Correctness               |       99% |    98% |          99% |
