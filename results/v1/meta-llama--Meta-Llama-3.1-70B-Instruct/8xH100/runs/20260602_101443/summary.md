# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     338.0s (5.6m) | `1cbe525` |
| vllm         |   1279.1s (21.3m) | `f8e9c56` |
| sglang       | **217.5s (3.6m)** | `84e1108` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        234.6 |     168.8 | **147.5** |
| TPOT median (ms)          |     **43.7** |      57.0 |      77.6 |
| E2E median (ms)           |        270.4 | **217.2** |     220.5 |
| Throughput median (tok/s) |          5.3 |   **6.7** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1038.0 | **186.0** |  207.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |       1138.4 | **210.4** |  341.9 |
| Throughput median (tok/s) |          0.9 |   **4.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2359.7 |     176.7 | **164.9** |
| TPOT median (ms)          |        419.9 |  **61.9** |     101.5 |
| E2E median (ms)           |       2813.5 | **234.3** |     270.5 |
| Throughput median (tok/s) |          0.5 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        775.8 | **59.0** |   82.1 |
| TPOT median (ms)          |     **27.3** |     27.8 |   47.1 |
| E2E median (ms)           |        800.3 | **80.0** |  140.4 |
| Throughput median (tok/s) |          1.6 | **15.4** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       2857.3 |      84.2 | **79.2** |
| TPOT median (ms)          |         89.8 |  **15.1** |     23.8 |
| E2E median (ms)           |       5613.4 | **639.2** |    925.0 |
| Throughput median (tok/s) |          5.9 |  **57.1** |     39.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1453.1 | **134.9** |  136.3 |
| TPOT median (ms)          |        116.1 |  **32.4** |   50.0 |
| E2E median (ms)           |       2127.2 | **276.2** |  379.7 |
| Throughput median (tok/s) |          2.8 |  **18.0** |   12.5 |
| Correctness               |          99% |       99% |    99% |
