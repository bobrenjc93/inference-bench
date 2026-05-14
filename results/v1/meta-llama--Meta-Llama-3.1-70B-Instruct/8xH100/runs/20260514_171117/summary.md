# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:08 AM PT, May 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     332.6s (5.5m) | `0c3133f` |
| vllm         |   1125.4s (18.8m) | `f3d5360` |
| sglang       | **170.4s (2.8m)** | `3fc60e5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        316.2 |     154.2 | **141.3** |
| TPOT median (ms)          |        167.5 |  **55.6** |      77.3 |
| E2E median (ms)           |        406.3 | **204.0** |     212.8 |
| Throughput median (tok/s) |          3.6 |   **6.9** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        215.4 | **192.0** |  198.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        342.9 | **211.6** |  336.5 |
| Throughput median (tok/s) |          2.9 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        654.0 |     166.3 | **150.4** |
| TPOT median (ms)          |        211.6 |  **58.7** |     101.0 |
| E2E median (ms)           |        811.4 | **222.3** |     247.3 |
| Throughput median (tok/s) |          1.7 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        368.7 | **57.4** |   79.1 |
| TPOT median (ms)          |        234.2 | **26.9** |   63.7 |
| E2E median (ms)           |        581.1 | **77.6** |  155.7 |
| Throughput median (tok/s) |          2.6 | **15.9** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        577.2 |      70.5 | **64.8** |
| TPOT median (ms)          |         16.2 |  **15.0** |     22.2 |
| E2E median (ms)           |       1320.3 | **618.9** |    833.5 |
| Throughput median (tok/s) |         25.5 |  **58.7** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        426.3 |     128.1 | **126.8** |
| TPOT median (ms)          |        125.9 |  **31.2** |      52.8 |
| E2E median (ms)           |        692.4 | **266.9** |     357.2 |
| Throughput median (tok/s) |          7.3 |  **18.5** |      13.2 |
| Correctness               |          98% |       99% |       99% |
