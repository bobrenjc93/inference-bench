# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jun 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     399.7s (6.7m) | `065275c` |
| vllm         |   1341.0s (22.3m) | `42ae5e7` |
| sglang       | **199.6s (3.3m)** | `e1164a6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        311.4 |    173.3 | **142.3** |
| TPOT median (ms)          |         91.8 | **64.5** |      78.0 |
| E2E median (ms)           |        398.6 |    231.5 | **213.4** |
| Throughput median (tok/s) |          3.1 |  **6.3** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        355.1 | **194.5** |  210.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        472.5 | **217.9** |  350.1 |
| Throughput median (tok/s) |          2.1 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        653.7 |     180.7 | **167.3** |
| TPOT median (ms)          |     **63.6** |      64.2 |      93.9 |
| E2E median (ms)           |        711.7 | **241.7** |     266.6 |
| Throughput median (tok/s) |          1.8 |   **5.9** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        402.8 | **64.9** |   82.2 |
| TPOT median (ms)          |         63.0 | **30.4** |   46.6 |
| E2E median (ms)           |        452.6 | **89.4** |  140.1 |
| Throughput median (tok/s) |          3.2 | **13.6** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.4 |  **70.6** |   79.0 |
| TPOT median (ms)          |         26.9 |  **15.1** |   23.4 |
| E2E median (ms)           |       1270.9 | **608.6** |  893.8 |
| Throughput median (tok/s) |         30.0 |  **58.7** |   39.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        383.1 |     136.8 | **136.3** |
| TPOT median (ms)          |         49.1 |  **34.8** |      48.4 |
| E2E median (ms)           |        661.3 | **277.8** |     372.8 |
| Throughput median (tok/s) |          8.0 |  **17.8** |      12.7 |
| Correctness               |          99% |       98% |       99% |
