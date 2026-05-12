# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:28 PM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          1/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **91.9s (1.5m)** | `75cf5d5` |
| vllm         |  1200.8s (20.0m) | `39dff5f` |
| sglang       |    167.9s (2.8m) | `34555ae` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        889.6 |     163.0 | **152.1** |
| TPOT median (ms)          |        634.1 |  **62.7** |      73.0 |
| E2E median (ms)           |       1552.5 | **222.8** |     225.9 |
| Throughput median (tok/s) |          0.9 |   **6.9** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        583.3 | **185.1** |  220.3 |
| TPOT median (ms)          |      **0.0** |       0.0 |    0.0 |
| E2E median (ms)           |        710.3 | **209.4** |  373.0 |
| Throughput median (tok/s) |          1.4 |   **4.8** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2619.0 |     187.6 | **170.7** |
| TPOT median (ms)          |       1560.6 |  **70.2** |     100.1 |
| E2E median (ms)           |       3845.2 | **242.9** |     271.9 |
| Throughput median (tok/s) |          0.3 |   **5.6** |       4.9 |
| Correctness               |          94% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        801.0 | **61.9** |   80.9 |
| TPOT median (ms)          |        614.0 | **27.9** |   58.2 |
| E2E median (ms)           |       1380.0 | **83.7** |  142.8 |
| Throughput median (tok/s) |          1.0 | **14.7** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1828.0 |      79.8 | **74.1** |
| TPOT median (ms)          |         67.6 |  **15.0** |     21.9 |
| E2E median (ms)           |       4440.9 | **627.0** |    880.5 |
| Throughput median (tok/s) |          8.8 |  **57.6** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1344.2 | **135.5** |  139.6 |
| TPOT median (ms)          |        575.3 |  **35.1** |   50.6 |
| E2E median (ms)           |       2385.8 | **277.2** |  378.8 |
| Throughput median (tok/s) |          2.5 |  **17.9** |   12.9 |
| Correctness               |          98% |       99% |    99% |
