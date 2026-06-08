# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jun 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     417.5s (7.0m) | `6efe640` |
| vllm         |   1339.8s (22.3m) | `2ed0a96` |
| sglang       | **207.2s (3.5m)** | `303757c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        313.5 |     167.2 | **151.1** |
| TPOT median (ms)          |         94.2 |  **55.7** |      69.9 |
| E2E median (ms)           |        390.4 | **215.9** |     219.7 |
| Throughput median (tok/s) |          3.1 |   **6.8** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        416.0 | **193.6** |  211.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        553.6 | **216.3** |  346.9 |
| Throughput median (tok/s) |          1.8 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        867.4 |     179.3 | **170.6** |
| TPOT median (ms)          |         65.5 |  **59.5** |      96.5 |
| E2E median (ms)           |        919.1 | **232.3** |     264.4 |
| Throughput median (tok/s) |          1.5 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        466.9 | **59.1** |   81.6 |
| TPOT median (ms)          |         62.4 | **27.6** |   59.9 |
| E2E median (ms)           |        527.3 | **80.4** |  143.9 |
| Throughput median (tok/s) |          2.8 | **15.1** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        499.1 |  **72.8** |   79.2 |
| TPOT median (ms)          |         21.9 |  **14.8** |   23.4 |
| E2E median (ms)           |       1308.4 | **611.7** |  881.2 |
| Throughput median (tok/s) |         27.5 |  **59.2** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        512.6 | **134.4** |  138.8 |
| TPOT median (ms)          |         48.8 |  **31.5** |   49.9 |
| E2E median (ms)           |        739.8 | **271.3** |  371.2 |
| Throughput median (tok/s) |          7.3 |  **18.4** |   12.5 |
| Correctness               |          99% |       99% |    99% |
