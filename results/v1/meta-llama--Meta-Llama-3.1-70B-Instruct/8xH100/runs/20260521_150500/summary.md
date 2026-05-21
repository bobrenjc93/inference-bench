# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:03 AM PT, May 21 2026

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
| torchinferno |     302.6s (5.0m) | `9f91b40` |
| vllm         |   1162.2s (19.4m) | `9b9d5db` |
| sglang       | **196.6s (3.3m)** | `32f996b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        290.0 |    161.1 | **138.9** |
| TPOT median (ms)          |        151.5 | **58.8** |      71.8 |
| E2E median (ms)           |        391.4 |    213.1 | **207.6** |
| Throughput median (tok/s) |          3.7 |  **7.0** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.1 | **194.7** |  216.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        310.1 | **228.8** |  362.0 |
| Throughput median (tok/s) |          3.2 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        679.9 |     177.5 | **163.3** |
| TPOT median (ms)          |        128.7 |  **66.3** |      98.5 |
| E2E median (ms)           |        779.9 | **236.3** |     260.3 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        327.9 | **58.9** |   77.5 |
| TPOT median (ms)          |        132.3 | **26.3** |   60.4 |
| E2E median (ms)           |        428.1 | **78.8** |  149.9 |
| Throughput median (tok/s) |          3.5 | **15.6** |    9.6 |
| Correctness               |          97% |      96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        859.7 |      72.9 | **68.8** |
| TPOT median (ms)          |         15.7 |  **14.9** |     22.4 |
| E2E median (ms)           |       1594.8 | **614.8** |    842.4 |
| Throughput median (tok/s) |         20.1 |  **58.2** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        489.5 | **133.0** |  133.1 |
| TPOT median (ms)          |         85.6 |  **33.3** |   50.6 |
| E2E median (ms)           |        700.9 | **274.4** |  364.5 |
| Throughput median (tok/s) |          6.4 |  **18.3** |   13.0 |
| Correctness               |          99% |       98% |    98% |
