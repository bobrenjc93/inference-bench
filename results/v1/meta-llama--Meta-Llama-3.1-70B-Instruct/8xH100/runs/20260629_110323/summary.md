# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **16/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     494.7s (8.2m) | `03677fd` |
| vllm         |    676.2s (11.3m) | `3483240` |
| sglang       | **279.4s (4.7m)** | `bb7d344` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        160.8 | **139.5** |  150.4 |
| TPOT median (ms)          |     **46.7** |      49.6 |   75.7 |
| E2E median (ms)           |        198.3 | **178.6** |  226.0 |
| Throughput median (tok/s) |          5.8 |   **7.9** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        249.2 | **210.4** |  220.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        269.6 | **231.9** |  360.2 |
| Throughput median (tok/s) |          3.7 |   **4.3** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        316.4 | **155.2** |  161.2 |
| TPOT median (ms)          |     **57.8** |      58.5 |  101.5 |
| E2E median (ms)           |        371.9 | **201.1** |  253.5 |
| Throughput median (tok/s) |          3.6 |   **7.0** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        208.2 | **63.0** |   78.7 |
| TPOT median (ms)          |         59.1 | **31.5** |   52.5 |
| E2E median (ms)           |        257.5 | **85.5** |  138.5 |
| Throughput median (tok/s) |          5.4 | **14.1** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        317.7 |      76.4 | **68.6** |
| TPOT median (ms)          |         22.9 |  **15.0** |     22.1 |
| E2E median (ms)           |       1119.8 | **629.6** |    844.1 |
| Throughput median (tok/s) |         32.5 |  **57.6** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        250.5 | **128.9** |  135.8 |
| TPOT median (ms)          |         37.3 |  **30.9** |   50.4 |
| E2E median (ms)           |        443.4 | **265.4** |  364.5 |
| Throughput median (tok/s) |         10.2 |  **18.2** |   13.1 |
| Correctness               |          99% |       99% |    99% |
