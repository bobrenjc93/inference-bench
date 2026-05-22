# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, May 21 2026

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
| torchinferno |     331.4s (5.5m) | `9f91b40` |
| vllm         |   1307.9s (21.8m) | `39910f2` |
| sglang       | **184.1s (3.1m)** | `b2631a9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        291.8 |    161.1 | **141.3** |
| TPOT median (ms)          |        154.3 | **61.9** |      78.1 |
| E2E median (ms)           |        403.5 |    216.7 | **211.0** |
| Throughput median (tok/s) |          3.8 |  **6.8** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        258.4 |     195.7 | **195.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        328.2 | **221.3** |     329.6 |
| Throughput median (tok/s) |          3.0 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        682.4 |     175.5 | **158.0** |
| TPOT median (ms)          |        112.8 |  **60.0** |     101.7 |
| E2E median (ms)           |        781.3 | **229.6** |     253.9 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        379.1 | **57.9** |   75.2 |
| TPOT median (ms)          |        131.9 | **26.7** |   49.7 |
| E2E median (ms)           |        491.0 | **79.0** |  132.5 |
| Throughput median (tok/s) |          2.8 | **15.9** |    9.8 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        863.3 |      79.8 | **64.7** |
| TPOT median (ms)          |         16.5 |  **14.9** |     22.5 |
| E2E median (ms)           |       1522.8 | **624.7** |    827.2 |
| Throughput median (tok/s) |         20.0 |  **58.0** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        495.0 |     134.0 | **126.8** |
| TPOT median (ms)          |         83.1 |  **32.7** |      50.4 |
| E2E median (ms)           |        705.4 | **274.3** |     350.8 |
| Throughput median (tok/s) |          6.3 |  **18.3** |      13.2 |
| Correctness               |          98% |       98% |       99% |
