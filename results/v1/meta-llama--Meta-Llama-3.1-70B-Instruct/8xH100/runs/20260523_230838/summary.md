# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     299.6s (5.0m) | `9f91b40` |
| vllm         |   1274.8s (21.2m) | `10d264a` |
| sglang       | **194.6s (3.2m)** | `982f67d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        276.4 |    165.5 | **143.1** |
| TPOT median (ms)          |        156.4 | **56.9** |      72.8 |
| E2E median (ms)           |        372.9 |    216.0 | **210.7** |
| Throughput median (tok/s) |          4.1 |  **6.9** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        226.7 |     211.6 | **205.3** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        303.1 | **233.8** |     335.1 |
| Throughput median (tok/s) |          3.3 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        745.1 |     170.4 | **156.1** |
| TPOT median (ms)          |        126.1 |  **52.7** |     106.4 |
| E2E median (ms)           |        831.7 | **221.0** |     250.7 |
| Throughput median (tok/s) |          1.5 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        367.7 | **58.6** |   77.6 |
| TPOT median (ms)          |        133.9 | **26.5** |   60.8 |
| E2E median (ms)           |        461.3 | **79.1** |  152.7 |
| Throughput median (tok/s) |          3.0 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        722.7 |  **65.6** |   66.6 |
| TPOT median (ms)          |         15.1 |  **15.0** |   22.2 |
| E2E median (ms)           |       1372.3 | **603.3** |  819.6 |
| Throughput median (tok/s) |         24.6 |  **59.5** |   42.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        467.7 |     134.3 | **129.7** |
| TPOT median (ms)          |         86.3 |  **30.2** |      52.4 |
| E2E median (ms)           |        668.2 | **270.6** |     353.8 |
| Throughput median (tok/s) |          7.3 |  **18.5** |      13.2 |
| Correctness               |          99% |       99% |       99% |
