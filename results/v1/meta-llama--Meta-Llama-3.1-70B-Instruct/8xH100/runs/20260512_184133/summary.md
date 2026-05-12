# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:01 AM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **91.0s (1.5m)** | `708195d` |
| vllm         |  1217.0s (20.3m) | `4d591db` |
| sglang       |    164.6s (2.7m) | `e86fb42` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        429.9 |    175.1 | **143.6** |
| TPOT median (ms)          |        494.4 | **57.0** |      77.8 |
| E2E median (ms)           |        840.1 |    226.2 | **215.5** |
| Throughput median (tok/s) |          1.6 |  **6.3** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        364.7 | **212.2** |  213.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        405.2 | **237.0** |  351.7 |
| Throughput median (tok/s) |          2.5 |   **4.2** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1379.7 |     181.7 | **168.9** |
| TPOT median (ms)          |        205.6 |  **67.7** |     107.0 |
| E2E median (ms)           |       1572.4 | **242.4** |     272.2 |
| Throughput median (tok/s) |          0.9 |   **5.8** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        436.3 | **61.2** |   79.4 |
| TPOT median (ms)          |        424.4 | **27.2** |   61.7 |
| E2E median (ms)           |        802.7 | **81.8** |  152.6 |
| Throughput median (tok/s) |          1.9 | **15.2** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1019.8 |      84.5 | **76.0** |
| TPOT median (ms)          |         32.4 |  **14.8** |     22.0 |
| E2E median (ms)           |       2285.7 | **625.2** |    812.5 |
| Throughput median (tok/s) |         17.2 |  **57.3** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        726.1 |     142.9 | **136.3** |
| TPOT median (ms)          |        231.4 |  **33.3** |      53.7 |
| E2E median (ms)           |       1181.2 | **282.5** |     360.9 |
| Throughput median (tok/s) |          4.8 |  **17.8** |      12.8 |
| Correctness               |          99% |       99% |       99% |
