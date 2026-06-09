# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 PM PT, Jun 9 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     307.1s (5.1m) | `a870596` |
| vllm         |   1359.8s (22.7m) | `e1ed89d` |
| sglang       | **203.2s (3.4m)** | `fde4004` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        308.7 |    167.8 | **149.0** |
| TPOT median (ms)          |         94.8 | **61.9** |      72.3 |
| E2E median (ms)           |        383.3 |    218.9 | **213.4** |
| Throughput median (tok/s) |          3.1 |  **6.6** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        377.8 | **208.7** |  217.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        509.3 | **233.8** |  368.2 |
| Throughput median (tok/s) |          2.0 |   **4.3** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        635.3 |     179.9 | **162.5** |
| TPOT median (ms)          |         65.7 |  **53.3** |     104.3 |
| E2E median (ms)           |        706.3 | **236.6** |     263.0 |
| Throughput median (tok/s) |          1.7 |   **5.8** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        385.5 | **60.7** |   83.5 |
| TPOT median (ms)          |         56.0 | **27.2** |   51.5 |
| E2E median (ms)           |        435.4 | **82.6** |  151.3 |
| Throughput median (tok/s) |          3.3 | **14.9** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.6 |  **74.5** |   80.8 |
| TPOT median (ms)          |         26.6 |  **15.2** |   23.6 |
| E2E median (ms)           |       1260.0 | **620.7** |  900.4 |
| Throughput median (tok/s) |         30.7 |  **58.2** |   39.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        380.4 | **138.3** |  138.6 |
| TPOT median (ms)          |         48.6 |  **31.5** |   50.3 |
| E2E median (ms)           |        658.9 | **278.5** |  379.3 |
| Throughput median (tok/s) |          8.2 |  **18.0** |   12.5 |
| Correctness               |          98% |       99% |    99% |
