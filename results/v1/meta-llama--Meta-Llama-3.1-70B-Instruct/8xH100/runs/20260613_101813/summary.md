# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     377.8s (6.3m) | `f4af255` |
| vllm         |   1376.0s (22.9m) | `96fa5cd` |
| sglang       | **211.6s (3.5m)** | `f7041c9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.0 | **159.3** |  162.9 |
| TPOT median (ms)          |         98.0 |  **56.4** |   77.7 |
| E2E median (ms)           |        389.6 | **213.0** |  235.4 |
| Throughput median (tok/s) |          3.3 |   **7.0** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        305.1 | **210.8** |  240.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        423.1 | **237.7** |  395.5 |
| Throughput median (tok/s) |          2.4 |   **4.2** |    2.5 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        761.5 |     179.5 | **157.9** |
| TPOT median (ms)          |         64.3 |  **58.9** |     101.3 |
| E2E median (ms)           |        841.0 | **232.5** |     255.1 |
| Throughput median (tok/s) |          1.6 |   **5.9** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        313.2 | **60.6** |   82.4 |
| TPOT median (ms)          |         64.7 | **28.1** |   39.5 |
| E2E median (ms)           |        363.7 | **82.2** |  134.3 |
| Throughput median (tok/s) |          4.2 | **14.5** |   10.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        195.0 |      76.8 | **69.4** |
| TPOT median (ms)          |         26.5 |  **15.0** |     22.5 |
| E2E median (ms)           |       1285.1 | **634.3** |    843.2 |
| Throughput median (tok/s) |         29.8 |  **57.8** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        373.3 | **137.4** |  142.5 |
| TPOT median (ms)          |         50.7 |  **31.7** |   48.2 |
| E2E median (ms)           |        660.5 | **279.9** |  372.7 |
| Throughput median (tok/s) |          8.2 |  **17.9** |   13.0 |
| Correctness               |          98% |       98% |    99% |
