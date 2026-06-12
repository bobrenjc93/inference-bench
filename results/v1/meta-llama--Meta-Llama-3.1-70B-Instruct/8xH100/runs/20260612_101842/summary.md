# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     439.4s (7.3m) | `065275c` |
| vllm         |   1359.9s (22.7m) | `462ef83` |
| sglang       | **211.5s (3.5m)** | `f308abc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        301.4 | **154.4** |  161.2 |
| TPOT median (ms)          |         98.0 |  **58.5** |   73.9 |
| E2E median (ms)           |        395.1 | **209.7** |  230.2 |
| Throughput median (tok/s) |          3.1 |   **7.0** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        411.2 | **174.9** |  207.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        555.6 | **199.8** |  339.5 |
| Throughput median (tok/s) |          1.8 |   **5.0** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        683.6 |     172.7 | **167.3** |
| TPOT median (ms)          |         67.2 |  **63.7** |      98.4 |
| E2E median (ms)           |        755.3 | **226.9** |     267.2 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        409.2 | **59.2** |   83.5 |
| TPOT median (ms)          |         52.6 | **29.3** |   44.2 |
| E2E median (ms)           |        471.3 | **82.2** |  144.2 |
| Throughput median (tok/s) |          3.1 | **14.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.2 |  **65.4** |   81.6 |
| TPOT median (ms)          |         26.6 |  **15.1** |   23.2 |
| E2E median (ms)           |       1268.5 | **606.7** |  895.6 |
| Throughput median (tok/s) |         29.5 |  **59.2** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        399.9 | **125.3** |  140.1 |
| TPOT median (ms)          |         48.9 |  **33.3** |   47.9 |
| E2E median (ms)           |        689.2 | **265.1** |  375.4 |
| Throughput median (tok/s) |          7.8 |  **18.4** |   12.5 |
| Correctness               |          99% |       98% |    98% |
