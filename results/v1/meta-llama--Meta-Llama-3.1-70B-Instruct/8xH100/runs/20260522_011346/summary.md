# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:03 PM PT, May 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     377.7s (6.3m) | `9f91b40` |
| vllm         |   1314.1s (21.9m) | `39910f2` |
| sglang       | **193.7s (3.2m)** | `16b3edc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        313.0 |    161.1 | **134.2** |
| TPOT median (ms)          |        155.1 | **52.6** |      74.2 |
| E2E median (ms)           |        423.8 |    215.7 | **201.9** |
| Throughput median (tok/s) |          3.2 |  **6.7** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        293.3 |     198.4 | **195.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        313.5 | **222.6** |     332.0 |
| Throughput median (tok/s) |          3.2 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        680.6 |     173.9 | **154.9** |
| TPOT median (ms)          |        135.6 |  **62.2** |     108.0 |
| E2E median (ms)           |        774.2 | **223.2** |     253.1 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        335.5 | **59.0** |   73.5 |
| TPOT median (ms)          |        131.3 | **27.4** |   67.5 |
| E2E median (ms)           |        426.3 | **79.4** |  148.6 |
| Throughput median (tok/s) |          3.4 | **15.3** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        905.4 |      68.2 | **66.3** |
| TPOT median (ms)          |         15.6 |  **15.1** |     22.1 |
| E2E median (ms)           |       1577.5 | **608.3** |    800.5 |
| Throughput median (tok/s) |         20.2 |  **58.9** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        505.5 |     132.1 | **124.9** |
| TPOT median (ms)          |         87.5 |  **31.4** |      54.4 |
| E2E median (ms)           |        703.1 | **269.9** |     347.2 |
| Throughput median (tok/s) |          6.3 |  **18.3** |      13.4 |
| Correctness               |          98% |       98% |       99% |
