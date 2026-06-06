# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     348.7s (5.8m) | `75bbe35` |
| vllm         |   1283.2s (21.4m) | `00d1fb7` |
| sglang       | **222.6s (3.7m)** | `9a48bf7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.4 | **143.6** |  145.6 |
| TPOT median (ms)          |     **45.9** |      51.4 |   74.9 |
| E2E median (ms)           |        322.6 | **186.0** |  213.8 |
| Throughput median (tok/s) |          4.5 |   **7.4** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        251.6 | **187.6** |  207.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        351.5 | **211.2** |  343.0 |
| Throughput median (tok/s) |          2.8 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        677.8 |     178.5 | **160.2** |
| TPOT median (ms)          |         61.4 |  **60.0** |      93.5 |
| E2E median (ms)           |        746.2 | **236.4** |     254.7 |
| Throughput median (tok/s) |          1.6 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        365.8 | **59.8** |   79.0 |
| TPOT median (ms)          |         30.0 | **28.2** |   43.5 |
| E2E median (ms)           |        409.2 | **80.6** |  132.2 |
| Throughput median (tok/s) |          3.5 | **15.0** |   10.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        509.4 |  **73.4** |   74.3 |
| TPOT median (ms)          |         31.2 |  **15.1** |   23.2 |
| E2E median (ms)           |       1569.6 | **607.1** |  875.5 |
| Throughput median (tok/s) |         21.6 |  **58.5** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        416.6 | **128.6** |  133.4 |
| TPOT median (ms)          |         33.7 |  **31.0** |   47.0 |
| E2E median (ms)           |        679.8 | **264.3** |  363.8 |
| Throughput median (tok/s) |          6.8 |  **18.3** |   12.9 |
| Correctness               |          98% |       98% |    99% |
