# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, Jun 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     392.8s (6.5m) | `065275c` |
| vllm         |   1353.1s (22.6m) | `8a91228` |
| sglang       | **218.1s (3.6m)** | `cd075d1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        315.5 |     156.5 | **145.1** |
| TPOT median (ms)          |         95.4 |  **46.2** |      68.3 |
| E2E median (ms)           |        394.7 | **206.3** |     216.7 |
| Throughput median (tok/s) |          3.3 |   **7.3** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        396.2 | **201.3** |  204.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        532.7 | **224.9** |  343.2 |
| Throughput median (tok/s) |          1.9 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        695.8 | **168.9** |  173.7 |
| TPOT median (ms)          |         65.8 |  **58.1** |   98.4 |
| E2E median (ms)           |        766.0 | **222.0** |  275.4 |
| Throughput median (tok/s) |          1.6 |   **6.4** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        453.7 | **61.0** |   87.2 |
| TPOT median (ms)          |         58.9 | **28.4** |   43.7 |
| E2E median (ms)           |        501.3 | **82.4** |  145.9 |
| Throughput median (tok/s) |          3.4 | **14.3** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        201.5 |      78.2 | **77.3** |
| TPOT median (ms)          |         26.4 |  **15.1** |     24.1 |
| E2E median (ms)           |       1223.7 | **642.9** |    892.9 |
| Throughput median (tok/s) |         30.8 |  **57.8** |     38.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        412.5 | **133.2** |  137.6 |
| TPOT median (ms)          |         49.3 |  **29.6** |   46.9 |
| E2E median (ms)           |        683.7 | **275.7** |  374.8 |
| Throughput median (tok/s) |          8.2 |  **18.1** |   12.2 |
| Correctness               |          99% |       99% |    99% |
