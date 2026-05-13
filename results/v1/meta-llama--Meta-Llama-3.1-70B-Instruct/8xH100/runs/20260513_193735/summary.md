# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:35 AM PT, May 13 2026

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
| torchinferno |     342.0s (5.7m) | `8684859` |
| vllm         |   1024.6s (17.1m) | `a505cf8` |
| sglang       | **158.2s (2.6m)** | `3178a70` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        267.4 |    156.7 | **137.9** |
| TPOT median (ms)          |        275.9 | **63.9** |      73.5 |
| E2E median (ms)           |        548.1 |    216.4 | **204.8** |
| Throughput median (tok/s) |          2.7 |  **7.1** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        432.6 |     203.3 | **201.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        526.2 | **224.8** |     335.5 |
| Throughput median (tok/s) |          1.9 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        653.4 |     179.4 | **155.9** |
| TPOT median (ms)          |        185.5 |  **65.8** |      98.3 |
| E2E median (ms)           |        828.7 | **231.9** |     256.1 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        333.2 | **58.5** |   75.8 |
| TPOT median (ms)          |        243.5 | **26.3** |   55.5 |
| E2E median (ms)           |        525.3 | **79.0** |  149.9 |
| Throughput median (tok/s) |          2.6 | **15.8** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.6 | **66.5** |
| TPOT median (ms)          |            - |  **15.0** |     22.5 |
| E2E median (ms)           |            - | **610.3** |    840.6 |
| Throughput median (tok/s) |            - |  **59.1** |     41.9 |
| Correctness               |            - |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        421.7 |     133.3 | **127.4** |
| TPOT median (ms)          |        176.2 |  **34.2** |      50.0 |
| E2E median (ms)           |        607.1 | **272.5** |     357.4 |
| Throughput median (tok/s) |          2.2 |  **18.5** |      13.1 |
| Correctness               |          98% |       99% |       99% |
