# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 AM PT, May 22 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     250.7s (4.2m) | `9f91b40` |
| vllm         |   1253.3s (20.9m) | `694d9a8` |
| sglang       | **179.9s (3.0m)** | `4486a33` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        299.9 |    161.2 | **137.2** |
| TPOT median (ms)          |        150.9 | **55.5** |      75.7 |
| E2E median (ms)           |        419.8 |    215.9 | **205.8** |
| Throughput median (tok/s) |          3.5 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        284.6 | **191.5** |  201.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        308.6 | **215.3** |  342.3 |
| Throughput median (tok/s) |          3.2 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        766.1 |     176.6 | **157.0** |
| TPOT median (ms)          |        189.9 |  **59.1** |      99.4 |
| E2E median (ms)           |        912.1 | **228.5** |     254.1 |
| Throughput median (tok/s) |          1.4 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        348.1 | **58.0** |   75.7 |
| TPOT median (ms)          |        131.5 | **26.6** |   56.4 |
| E2E median (ms)           |        442.2 | **78.3** |  143.8 |
| Throughput median (tok/s) |          3.3 | **15.7** |    9.9 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        855.7 |      69.7 | **69.3** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.4 |
| E2E median (ms)           |       1544.7 | **604.3** |    831.9 |
| Throughput median (tok/s) |         21.4 |  **58.7** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        510.9 |     131.4 | **128.2** |
| TPOT median (ms)          |         97.7 |  **31.3** |      50.8 |
| E2E median (ms)           |        725.5 | **268.4** |     355.6 |
| Throughput median (tok/s) |          6.6 |  **18.4** |      13.1 |
| Correctness               |          98% |       98% |       99% |
