# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |      **2/4** |       0/4 |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **13/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     375.3s (6.3m) | `db749af` |
| vllm         |   1144.7s (19.1m) | `0867497` |
| sglang       | **167.6s (2.8m)** | `229cade` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        288.1 |     157.8 | **140.0** |
| TPOT median (ms)          |        151.0 |  **50.8** |      72.9 |
| E2E median (ms)           |        372.5 | **203.1** |     207.2 |
| Throughput median (tok/s) |          3.9 |   **7.4** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm |    sglang |
| :------------------------ | -----------: | ----: | --------: |
| TTFT median (ms)          |        272.0 | 221.7 | **204.9** |
| TPOT median (ms)          |          0.0 |   0.0 |       0.0 |
| E2E median (ms)           |    **296.0** | 308.7 |     341.7 |
| Throughput median (tok/s) |      **3.4** |   3.2 |       2.9 |
| Correctness               |         100% |  100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        550.8 |     169.6 | **157.7** |
| TPOT median (ms)          |        121.6 |  **52.5** |     103.8 |
| E2E median (ms)           |        639.6 | **213.7** |     254.3 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        324.3 | **58.2** |   75.8 |
| TPOT median (ms)          |        130.3 | **26.9** |   45.1 |
| E2E median (ms)           |        428.7 | **78.9** |  127.9 |
| Throughput median (tok/s) |          3.3 | **15.3** |   10.5 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        742.1 |      67.5 | **66.8** |
| TPOT median (ms)          |         18.9 |  **15.1** |     22.0 |
| E2E median (ms)           |       1470.2 | **602.8** |    819.7 |
| Throughput median (tok/s) |         23.1 |  **59.1** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        435.5 |     135.0 | **129.0** |
| TPOT median (ms)          |         84.4 |  **29.1** |      48.8 |
| E2E median (ms)           |        641.4 | **281.4** |     350.2 |
| Throughput median (tok/s) |          7.2 |  **18.3** |      13.4 |
| Correctness               |          99% |       99% |       98% |
