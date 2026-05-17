# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:10 AM PT, May 17 2026

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
| torchinferno |     364.6s (6.1m) | `13d21ac` |
| vllm         |   1152.6s (19.2m) | `599e75f` |
| sglang       | **172.5s (2.9m)** | `89e501c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        292.5 |    159.2 | **137.7** |
| TPOT median (ms)          |        151.5 | **55.8** |      72.4 |
| E2E median (ms)           |        396.9 |    212.4 | **205.0** |
| Throughput median (tok/s) |          3.7 |  **6.9** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        289.6 |     217.1 | **208.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        314.5 | **305.4** |     341.4 |
| Throughput median (tok/s) |          3.2 |   **3.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        541.9 |     167.2 | **156.9** |
| TPOT median (ms)          |        112.5 |  **51.3** |      98.5 |
| E2E median (ms)           |        639.1 | **220.6** |     259.3 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        342.5 | **57.5** |   75.5 |
| TPOT median (ms)          |        132.7 | **26.8** |   63.7 |
| E2E median (ms)           |        441.0 | **77.6** |  153.4 |
| Throughput median (tok/s) |          3.2 | **15.7** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        728.8 |      71.5 | **66.5** |
| TPOT median (ms)          |         17.4 |  **15.0** |     22.3 |
| E2E median (ms)           |       1380.6 | **619.9** |    845.3 |
| Throughput median (tok/s) |         23.6 |  **58.5** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        439.1 |     134.5 | **129.1** |
| TPOT median (ms)          |         82.8 |  **29.8** |      51.4 |
| E2E median (ms)           |        634.4 | **287.2** |     360.9 |
| Throughput median (tok/s) |          7.2 |  **18.1** |      13.1 |
| Correctness               |          98% |       99% |       99% |
