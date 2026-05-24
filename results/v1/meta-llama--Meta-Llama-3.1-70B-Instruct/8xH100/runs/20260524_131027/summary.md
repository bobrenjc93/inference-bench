# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:03 AM PT, May 24 2026

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
| torchinferno |     328.2s (5.5m) | `9f91b40` |
| vllm         |   1220.6s (20.3m) | `1806d1a` |
| sglang       | **181.4s (3.0m)** | `b6f71d5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        291.1 |    157.2 | **142.6** |
| TPOT median (ms)          |        155.3 | **60.2** |      72.7 |
| E2E median (ms)           |        383.4 |    212.1 | **211.6** |
| Throughput median (tok/s) |          3.9 |  **7.1** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.5 | **192.1** |  198.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        287.3 | **251.1** |  327.3 |
| Throughput median (tok/s) |          3.5 |   **4.0** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        830.2 |     171.7 | **154.5** |
| TPOT median (ms)          |        123.1 |  **61.1** |     103.1 |
| E2E median (ms)           |        931.7 | **226.7** |     251.1 |
| Throughput median (tok/s) |          1.4 |   **6.3** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        341.2 | **57.5** |   78.3 |
| TPOT median (ms)          |        133.2 | **26.7** |   58.8 |
| E2E median (ms)           |        439.4 | **77.9** |  161.8 |
| Throughput median (tok/s) |          2.9 | **15.9** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        751.5 |      72.0 | **66.4** |
| TPOT median (ms)          |         15.2 |  **14.9** |     22.1 |
| E2E median (ms)           |       1435.7 | **610.1** |    836.6 |
| Throughput median (tok/s) |         26.8 |  **59.1** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        496.5 |     130.1 | **128.0** |
| TPOT median (ms)          |         85.3 |  **32.6** |      51.3 |
| E2E median (ms)           |        695.5 | **275.6** |     357.7 |
| Throughput median (tok/s) |          7.7 |  **18.5** |      13.2 |
| Correctness               |          99% |       98% |       99% |
