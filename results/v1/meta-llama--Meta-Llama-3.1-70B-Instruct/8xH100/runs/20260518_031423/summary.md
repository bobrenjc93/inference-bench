# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:10 PM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     311.5s (5.2m) | `3f0f3bc` |
| vllm         |   1104.9s (18.4m) | `1072104` |
| sglang       | **177.6s (3.0m)** | `784fe7e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        261.1 |    156.1 | **137.8** |
| TPOT median (ms)          |        152.7 | **58.0** |      71.6 |
| E2E median (ms)           |        361.4 |    211.5 | **205.0** |
| Throughput median (tok/s) |          4.1 |  **7.0** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        269.3 | **190.7** |  205.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        298.7 | **218.4** |  333.2 |
| Throughput median (tok/s) |          3.3 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        511.9 |     176.4 | **161.6** |
| TPOT median (ms)          |         96.8 |  **57.2** |     100.5 |
| E2E median (ms)           |        622.3 | **232.4** |     257.8 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        326.0 | **58.6** |   73.2 |
| TPOT median (ms)          |        132.6 | **27.1** |   60.2 |
| E2E median (ms)           |        442.6 | **79.1** |  141.8 |
| Throughput median (tok/s) |          3.0 | **15.5** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        735.7 |  **66.1** |   66.8 |
| TPOT median (ms)          |         15.5 |  **15.2** |   21.9 |
| E2E median (ms)           |       1310.5 | **611.1** |  824.1 |
| Throughput median (tok/s) |         25.9 |  **59.2** |   43.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        420.8 |     129.6 | **128.9** |
| TPOT median (ms)          |         79.5 |  **31.5** |      50.8 |
| E2E median (ms)           |        607.1 | **270.5** |     352.4 |
| Throughput median (tok/s) |          7.7 |  **18.5** |      13.4 |
| Correctness               |          98% |       99% |       99% |
