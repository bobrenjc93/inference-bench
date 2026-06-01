# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:05 AM PT, Jun 1 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **4/4** |       0/4 |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     331.7s (5.5m) | `1557ba6` |
| vllm         |   1247.2s (20.8m) | `023808c` |
| sglang       | **210.7s (3.5m)** | `f59bbef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **147.1** | 177.3 |  154.9 |
| TPOT median (ms)          |     **46.5** |  60.5 |   74.0 |
| E2E median (ms)           |    **193.7** | 237.8 |  224.8 |
| Throughput median (tok/s) |      **6.2** |   5.9 |    5.2 |
| Correctness               |          98% |   98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        356.5 |     219.3 | **206.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        450.2 | **321.3** |     340.5 |
| Throughput median (tok/s) |          2.2 |   **3.1** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        632.4 |     177.1 | **162.5** |
| TPOT median (ms)          |         72.7 |  **55.9** |     106.9 |
| E2E median (ms)           |        748.6 | **225.1** |     267.1 |
| Throughput median (tok/s) |          1.8 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.8 | **58.9** |   82.4 |
| TPOT median (ms)          |         28.7 | **28.2** |   54.7 |
| E2E median (ms)           |        378.0 | **80.2** |  145.3 |
| Throughput median (tok/s) |          3.7 | **15.5** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1103.2 |  **71.7** |   73.6 |
| TPOT median (ms)          |         31.7 |  **15.0** |   23.0 |
| E2E median (ms)           |       2107.8 | **621.6** |  879.0 |
| Throughput median (tok/s) |         17.3 |  **58.3** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        518.2 |     140.8 | **136.0** |
| TPOT median (ms)          |         35.9 |  **31.9** |      51.7 |
| E2E median (ms)           |        775.7 | **297.2** |     371.3 |
| Throughput median (tok/s) |          6.2 |  **17.8** |      12.6 |
| Correctness               |          98% |       99% |       99% |
