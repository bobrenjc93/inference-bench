# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:08 PM PT, May 17 2026

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
| torchinferno |     326.2s (5.4m) | `13d21ac` |
| vllm         |   1055.4s (17.6m) | `966903e` |
| sglang       | **159.5s (2.7m)** | `c67b287` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        274.5 |    163.0 | **136.8** |
| TPOT median (ms)          |        153.3 | **56.4** |      71.4 |
| E2E median (ms)           |        371.1 |    214.9 | **204.2** |
| Throughput median (tok/s) |          4.1 |  **7.1** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        276.5 | **204.1** |  210.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        311.6 | **281.4** |  353.4 |
| Throughput median (tok/s) |          3.2 |   **3.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        524.2 |     171.1 | **164.7** |
| TPOT median (ms)          |        139.4 |  **60.4** |     104.2 |
| E2E median (ms)           |        642.8 | **215.3** |     267.1 |
| Throughput median (tok/s) |          2.0 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        344.4 | **57.5** |   74.8 |
| TPOT median (ms)          |        130.2 | **27.1** |   65.6 |
| E2E median (ms)           |        438.9 | **78.7** |  155.8 |
| Throughput median (tok/s) |          2.9 | **15.9** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        760.3 |  **69.3** |   69.5 |
| TPOT median (ms)          |         17.1 |  **15.1** |   22.1 |
| E2E median (ms)           |       1363.0 | **612.7** |  819.3 |
| Throughput median (tok/s) |         25.0 |  **58.8** |   42.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        436.0 |     133.0 | **131.3** |
| TPOT median (ms)          |         88.0 |  **31.8** |      52.7 |
| E2E median (ms)           |        625.5 | **280.6** |     360.0 |
| Throughput median (tok/s) |          7.5 |  **18.3** |      13.1 |
| Correctness               |          98% |       99% |       99% |
