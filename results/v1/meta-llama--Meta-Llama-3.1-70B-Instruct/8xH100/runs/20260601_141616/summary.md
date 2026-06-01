# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, Jun 1 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     417.0s (7.0m) | `1557ba6` |
| vllm         |   1372.3s (22.9m) | `985c97a` |
| sglang       | **212.7s (3.5m)** | `693adab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        194.8 |     166.1 | **145.2** |
| TPOT median (ms)          |     **45.2** |      55.3 |      82.6 |
| E2E median (ms)           |        232.6 | **222.0** |     222.6 |
| Throughput median (tok/s) |          5.6 |   **6.8** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        356.5 | **192.8** |  206.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        446.3 | **213.6** |  344.2 |
| Throughput median (tok/s) |          2.2 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        616.6 |     177.5 | **164.4** |
| TPOT median (ms)          |         70.3 |  **67.2** |      97.8 |
| E2E median (ms)           |        719.8 | **235.0** |     261.8 |
| Throughput median (tok/s) |          2.0 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        415.9 | **59.4** |   82.1 |
| TPOT median (ms)          |         29.4 | **26.8** |   39.2 |
| E2E median (ms)           |        463.3 | **80.1** |  128.2 |
| Throughput median (tok/s) |          3.4 | **15.3** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1145.5 |  **76.8** |   77.1 |
| TPOT median (ms)          |         32.2 |  **15.0** |   22.9 |
| E2E median (ms)           |       2127.1 | **639.1** |  850.0 |
| Throughput median (tok/s) |         17.3 |  **58.3** |   40.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        545.9 | **134.5** |  135.0 |
| TPOT median (ms)          |         35.4 |  **32.8** |   48.5 |
| E2E median (ms)           |        797.8 | **278.0** |  361.4 |
| Throughput median (tok/s) |          6.1 |  **18.2** |   12.8 |
| Correctness               |          99% |       99% |    99% |
