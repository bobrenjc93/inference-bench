# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, May 23 2026

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
| torchinferno |     417.0s (7.0m) | `9f91b40` |
| vllm         |   1314.1s (21.9m) | `4438b6e` |
| sglang       | **207.7s (3.5m)** | `2de7403` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        291.7 |     159.3 | **143.8** |
| TPOT median (ms)          |        154.9 |  **48.9** |      75.8 |
| E2E median (ms)           |        393.3 | **202.9** |     214.8 |
| Throughput median (tok/s) |          3.7 |   **7.2** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.1 | **184.7** |  198.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        311.1 | **202.3** |  346.4 |
| Throughput median (tok/s) |          3.2 |   **4.9** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        981.7 |     167.4 | **160.9** |
| TPOT median (ms)          |        116.1 |  **60.7** |      93.1 |
| E2E median (ms)           |       1060.3 | **212.2** |     251.6 |
| Throughput median (tok/s) |          1.3 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        315.1 | **57.6** |   78.4 |
| TPOT median (ms)          |        133.3 | **26.4** |   60.3 |
| E2E median (ms)           |        412.6 | **77.5** |  148.4 |
| Throughput median (tok/s) |          3.7 | **15.7** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        907.6 |      74.6 | **67.0** |
| TPOT median (ms)          |         15.7 |  **14.9** |     22.5 |
| E2E median (ms)           |       1623.0 | **618.1** |    830.3 |
| Throughput median (tok/s) |         22.5 |  **58.8** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        555.4 | **128.7** |  129.7 |
| TPOT median (ms)          |         84.0 |  **30.2** |   50.4 |
| E2E median (ms)           |        760.1 | **262.6** |  358.3 |
| Throughput median (tok/s) |          6.9 |  **18.6** |   13.1 |
| Correctness               |          98% |       99% |    98% |
