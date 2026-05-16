# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     292.0s (4.9m) | `db749af` |
| vllm         |   1082.0s (18.0m) | `36e74c9` |
| sglang       | **166.6s (2.8m)** | `9869ef0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        280.9 |     155.1 | **142.0** |
| TPOT median (ms)          |        149.9 |  **51.0** |      76.2 |
| E2E median (ms)           |        370.0 | **200.3** |     209.9 |
| Throughput median (tok/s) |          3.8 |   **7.1** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        264.3 | **187.0** |  202.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        284.4 | **207.7** |  337.6 |
| Throughput median (tok/s) |          3.5 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        548.1 |     164.9 | **160.6** |
| TPOT median (ms)          |        152.6 |  **57.4** |     103.4 |
| E2E median (ms)           |        638.8 | **216.9** |     261.3 |
| Throughput median (tok/s) |          2.1 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        325.6 | **58.2** |   73.7 |
| TPOT median (ms)          |        129.1 | **26.7** |   66.0 |
| E2E median (ms)           |        424.4 | **78.8** |  155.7 |
| Throughput median (tok/s) |          3.3 | **15.6** |    9.3 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        672.4 |      70.1 | **66.3** |
| TPOT median (ms)          |         15.6 |  **15.0** |     22.6 |
| E2E median (ms)           |       1237.8 | **617.8** |    810.4 |
| Throughput median (tok/s) |         27.1 |  **58.4** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        418.3 | **127.0** |  129.0 |
| TPOT median (ms)          |         89.4 |  **30.0** |   53.7 |
| E2E median (ms)           |        591.1 | **264.3** |  355.0 |
| Throughput median (tok/s) |          8.0 |  **18.5** |   13.0 |
| Correctness               |          99% |       99% |    98% |
