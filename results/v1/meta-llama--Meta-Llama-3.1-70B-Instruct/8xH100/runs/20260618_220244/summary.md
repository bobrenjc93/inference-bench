# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:08 PM PT, Jun 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     336.2s (5.6m) | `8fff803` |
| vllm         |     397.4s (6.6m) | `4ce2d01` |
| sglang       | **265.9s (4.4m)** | `bea282c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        279.1 | **126.1** |  141.5 |
| TPOT median (ms)          |         50.2 |  **43.5** |   70.1 |
| E2E median (ms)           |        325.0 | **157.2** |  211.7 |
| Throughput median (tok/s) |          3.8 |   **8.4** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.6 | **190.9** |  204.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        404.8 | **220.5** |  352.2 |
| Throughput median (tok/s) |          2.5 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        640.8 | **156.3** |  166.0 |
| TPOT median (ms)          |         63.1 |  **48.5** |  104.4 |
| E2E median (ms)           |        701.2 | **198.0** |  263.8 |
| Throughput median (tok/s) |          1.9 |   **6.8** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        219.3 | **56.9** |   85.1 |
| TPOT median (ms)          |         32.1 | **27.4** |   41.9 |
| E2E median (ms)           |        267.4 | **77.7** |  137.9 |
| Throughput median (tok/s) |          5.5 | **15.4** |   10.1 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        324.0 |  **69.3** |   71.0 |
| TPOT median (ms)          |         22.0 |  **15.2** |   22.4 |
| E2E median (ms)           |       1084.9 | **611.9** |  848.0 |
| Throughput median (tok/s) |         31.8 |  **58.4** |   41.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        352.0 | **119.9** |  133.6 |
| TPOT median (ms)          |         33.5 |  **26.9** |   47.8 |
| E2E median (ms)           |        556.7 | **253.1** |  362.7 |
| Throughput median (tok/s) |          9.1 |  **18.7** |   13.0 |
| Correctness               |          99% |       99% |    98% |
