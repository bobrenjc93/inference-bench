# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:09 PM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     321.3s (5.4m) | `e894602` |
| vllm         |    998.8s (16.6m) | `966903e` |
| sglang       | **170.8s (2.8m)** | `c67b287` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.4 | **135.6** |  140.8 |
| TPOT median (ms)          |        150.8 |  **49.2** |   70.9 |
| E2E median (ms)           |        366.3 | **177.4** |  209.0 |
| Throughput median (tok/s) |          4.2 |   **7.7** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        278.0 |     213.6 | **194.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        303.0 | **301.1** |     328.6 |
| Throughput median (tok/s) |          3.3 |   **3.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        537.3 |     173.8 | **161.4** |
| TPOT median (ms)          |        113.0 |  **56.3** |     101.1 |
| E2E median (ms)           |        635.4 | **222.4** |     261.2 |
| Throughput median (tok/s) |          2.2 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        342.9 | **58.2** |   75.7 |
| TPOT median (ms)          |        131.2 | **26.7** |   46.8 |
| E2E median (ms)           |        448.1 | **78.6** |  137.5 |
| Throughput median (tok/s) |          2.9 | **15.7** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      72.4 | **64.6** |
| TPOT median (ms)          |            - |  **15.1** |     22.2 |
| E2E median (ms)           |            - | **622.9** |    845.1 |
| Throughput median (tok/s) |            - |  **58.2** |     42.3 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        358.2 |     130.7 | **127.5** |
| TPOT median (ms)          |         98.7 |  **29.5** |      48.2 |
| E2E median (ms)           |        438.2 | **280.5** |     356.3 |
| Throughput median (tok/s) |          3.1 |  **18.2** |      13.3 |
| Correctness               |          98% |       99% |       98% |
