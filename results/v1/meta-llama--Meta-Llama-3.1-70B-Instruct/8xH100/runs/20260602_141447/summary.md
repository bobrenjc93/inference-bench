# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          1/4 |   **3/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         2/20 | **14/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     396.3s (6.6m) | `1cbe525` |
| vllm         |   1303.0s (21.7m) | `b623f7e` |
| sglang       | **218.6s (3.6m)** | `b5e154d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        191.3 |   177.1 | **142.6** |
| TPOT median (ms)          |     **44.8** |    53.6 |      80.7 |
| E2E median (ms)           |        229.3 |   232.3 | **217.3** |
| Throughput median (tok/s) |          5.7 | **5.8** |       5.5 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1039.9 | **201.2** |  211.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |       1140.1 | **224.8** |  358.1 |
| Throughput median (tok/s) |          0.9 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2452.5 |     181.4 | **161.5** |
| TPOT median (ms)          |        423.4 |  **66.4** |      95.4 |
| E2E median (ms)           |       2959.4 | **242.0** |     263.6 |
| Throughput median (tok/s) |          0.4 |   **5.9** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        747.2 | **59.7** |   82.7 |
| TPOT median (ms)          |     **27.5** |     28.4 |   45.9 |
| E2E median (ms)           |        767.6 | **81.4** |  139.4 |
| Throughput median (tok/s) |          1.9 | **15.2** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       2836.2 |  **72.2** |   75.1 |
| TPOT median (ms)          |         90.6 |  **15.0** |   23.5 |
| E2E median (ms)           |       5589.8 | **613.2** |  891.4 |
| Throughput median (tok/s) |          5.7 |  **58.6** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1453.4 |     138.3 | **134.7** |
| TPOT median (ms)          |        117.2 |  **32.7** |      49.1 |
| E2E median (ms)           |       2137.3 | **278.7** |     374.0 |
| Throughput median (tok/s) |          2.9 |  **18.0** |      12.6 |
| Correctness               |          99% |       99% |       99% |
