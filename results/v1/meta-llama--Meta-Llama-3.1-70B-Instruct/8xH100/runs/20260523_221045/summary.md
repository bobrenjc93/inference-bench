# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, May 23 2026

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
| torchinferno |     330.9s (5.5m) | `9f91b40` |
| vllm         |   1294.4s (21.6m) | `10d264a` |
| sglang       | **200.1s (3.3m)** | `982f67d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        282.6 |    157.9 | **137.9** |
| TPOT median (ms)          |        151.6 | **57.6** |      71.7 |
| E2E median (ms)           |        372.9 |    209.0 | **205.7** |
| Throughput median (tok/s) |          4.0 |  **7.1** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        276.9 |     207.9 | **202.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        312.8 | **233.1** |     340.5 |
| Throughput median (tok/s) |          3.2 |   **4.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        747.5 |     173.1 | **155.2** |
| TPOT median (ms)          |        121.1 |  **65.2** |     108.0 |
| E2E median (ms)           |        840.0 | **227.0** |     256.8 |
| Throughput median (tok/s) |          1.5 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        314.1 | **57.9** |   78.5 |
| TPOT median (ms)          |        131.8 | **26.2** |   66.6 |
| E2E median (ms)           |        417.5 | **77.9** |  160.4 |
| Throughput median (tok/s) |          3.3 | **15.9** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        900.8 |      67.3 | **66.3** |
| TPOT median (ms)          |         18.3 |  **14.9** |     22.1 |
| E2E median (ms)           |       1499.0 | **612.3** |    811.2 |
| Throughput median (tok/s) |         22.6 |  **59.3** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        504.4 |     132.8 | **128.2** |
| TPOT median (ms)          |         84.6 |  **32.8** |      53.7 |
| E2E median (ms)           |        688.4 | **271.9** |     354.9 |
| Throughput median (tok/s) |          6.9 |  **18.5** |      13.2 |
| Correctness               |          99% |       99% |       99% |
