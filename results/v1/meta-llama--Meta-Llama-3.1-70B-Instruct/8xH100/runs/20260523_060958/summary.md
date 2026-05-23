# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 PM PT, May 22 2026

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
| torchinferno |     377.6s (6.3m) | `9f91b40` |
| vllm         |   1288.7s (21.5m) | `3a1c062` |
| sglang       | **201.8s (3.4m)** | `c69844f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        283.9 |    157.9 | **140.0** |
| TPOT median (ms)          |        152.0 | **52.8** |      72.6 |
| E2E median (ms)           |        373.1 |    212.6 | **211.0** |
| Throughput median (tok/s) |          4.0 |  **7.2** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        272.9 | **197.4** |  201.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        293.5 | **227.5** |  337.6 |
| Throughput median (tok/s) |          3.4 |   **4.4** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        654.6 |     171.0 | **159.0** |
| TPOT median (ms)          |        109.1 |  **60.5** |     102.9 |
| E2E median (ms)           |        769.2 | **221.3** |     253.3 |
| Throughput median (tok/s) |          1.7 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        324.3 | **57.9** |   72.8 |
| TPOT median (ms)          |        130.4 | **27.0** |   66.3 |
| E2E median (ms)           |        434.3 | **78.7** |  147.4 |
| Throughput median (tok/s) |          3.4 | **15.8** |    9.5 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        749.6 |      70.2 | **65.7** |
| TPOT median (ms)          |         15.1 |  **15.0** |     22.5 |
| E2E median (ms)           |       1399.9 | **617.6** |    842.4 |
| Throughput median (tok/s) |         25.3 |  **58.6** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        457.1 |     130.9 | **127.7** |
| TPOT median (ms)          |         81.3 |  **31.1** |      52.9 |
| E2E median (ms)           |        654.0 | **271.5** |     358.4 |
| Throughput median (tok/s) |          7.6 |  **18.5** |      13.1 |
| Correctness               |          98% |       99% |       98% |
