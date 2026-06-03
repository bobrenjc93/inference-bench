# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, Jun 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     422.4s (7.0m) | `254f74b` |
| vllm         |   1374.3s (22.9m) | `e523267` |
| sglang       | **225.6s (3.8m)** | `f65aae8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        366.0 |     163.3 | **155.1** |
| TPOT median (ms)          |     **55.5** |      58.0 |      75.7 |
| E2E median (ms)           |        412.0 | **214.9** |     223.8 |
| Throughput median (tok/s) |          3.0 |   **6.9** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        260.7 |     267.9 | **211.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        362.8 | **298.6** |     350.8 |
| Throughput median (tok/s) |          2.8 |   **3.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        846.9 |     178.9 | **163.1** |
| TPOT median (ms)          |        149.5 |  **63.3** |     101.1 |
| E2E median (ms)           |        973.5 | **232.2** |     258.6 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        346.1 | **60.2** |   83.1 |
| TPOT median (ms)          |         30.3 | **28.3** |   50.5 |
| E2E median (ms)           |        376.9 | **81.7** |  145.1 |
| Throughput median (tok/s) |          3.9 | **15.2** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        426.9 |  **70.4** |   79.9 |
| TPOT median (ms)          |         37.1 |  **14.8** |   23.3 |
| E2E median (ms)           |       1687.1 | **617.0** |  878.7 |
| Throughput median (tok/s) |         20.8 |  **58.9** |   40.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        449.3 |     148.1 | **138.6** |
| TPOT median (ms)          |         54.5 |  **32.9** |      50.1 |
| E2E median (ms)           |        762.5 | **288.9** |     371.4 |
| Throughput median (tok/s) |          6.4 |  **18.1** |      12.6 |
| Correctness               |          99% |       98% |       99% |
