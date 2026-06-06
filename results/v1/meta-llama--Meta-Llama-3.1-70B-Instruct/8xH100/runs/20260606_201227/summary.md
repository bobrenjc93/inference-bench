# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **2/4** |     1/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **14/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     408.9s (6.8m) | `25260c0` |
| vllm         |   1284.2s (21.4m) | `fa27d4e` |
| sglang       | **206.6s (3.4m)** | `84ca0ff` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        373.5 |   163.3 | **141.5** |
| TPOT median (ms)          |     **57.2** |    57.9 |      71.9 |
| E2E median (ms)           |        424.7 |   216.8 | **208.7** |
| Throughput median (tok/s) |          3.0 | **6.8** |       5.8 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        269.7 |     204.1 | **203.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        398.1 | **229.0** |     344.8 |
| Throughput median (tok/s) |          2.5 |   **4.4** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        708.6 |     173.0 | **166.9** |
| TPOT median (ms)          |         62.8 |  **61.0** |     112.3 |
| E2E median (ms)           |        760.8 | **228.1** |     272.4 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        407.7 | **62.2** |   81.6 |
| TPOT median (ms)          |         32.5 | **28.0** |   45.5 |
| E2E median (ms)           |        438.7 | **83.0** |  143.8 |
| Throughput median (tok/s) |          3.2 | **14.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        512.1 |  **75.4** |   77.3 |
| TPOT median (ms)          |         30.7 |  **15.1** |   23.6 |
| E2E median (ms)           |       1578.6 | **627.9** |  884.6 |
| Throughput median (tok/s) |         22.3 |  **58.3** |   39.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        454.3 |     135.6 | **134.2** |
| TPOT median (ms)          |         36.6 |  **32.4** |      50.7 |
| E2E median (ms)           |        720.2 | **277.0** |     370.9 |
| Throughput median (tok/s) |          6.5 |  **18.1** |      12.5 |
| Correctness               |          99% |       99% |       99% |
