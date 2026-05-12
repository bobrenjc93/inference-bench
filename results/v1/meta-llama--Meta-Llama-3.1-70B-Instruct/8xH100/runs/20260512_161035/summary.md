# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:07 AM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     444.3s (7.4m) | `708195d` |
| vllm         |   1006.7s (16.8m) | `c8a6e27` |
| sglang       | **152.7s (2.5m)** | `fd3eb77` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        414.0 |     153.6 | **136.0** |
| TPOT median (ms)          |        468.6 |  **52.3** |      73.9 |
| E2E median (ms)           |        797.6 | **204.5** |     205.4 |
| Throughput median (tok/s) |          1.7 |   **7.2** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        337.0 | **206.1** |  211.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        375.4 | **227.6** |  350.9 |
| Throughput median (tok/s) |          2.7 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        650.1 |     164.9 | **157.7** |
| TPOT median (ms)          |        280.8 |  **58.2** |     105.3 |
| E2E median (ms)           |        836.0 | **214.5** |     260.1 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        324.2 | **58.4** |   76.6 |
| TPOT median (ms)          |        380.0 | **26.8** |   63.3 |
| E2E median (ms)           |        677.1 | **78.8** |  149.8 |
| Throughput median (tok/s) |          2.1 | **15.6** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        559.3 |      68.7 | **66.1** |
| TPOT median (ms)          |         30.9 |  **14.9** |     22.3 |
| E2E median (ms)           |       1800.8 | **610.4** |    834.7 |
| Throughput median (tok/s) |         21.7 |  **58.8** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        456.9 |     130.4 | **129.6** |
| TPOT median (ms)          |        232.1 |  **30.4** |      52.9 |
| E2E median (ms)           |        897.4 | **267.2** |     360.2 |
| Throughput median (tok/s) |          5.9 |  **18.5** |      13.1 |
| Correctness               |          98% |       98% |       98% |
