# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jun 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     401.7s (6.7m) | `515261e` |
| vllm         |     501.1s (8.4m) | `0fbf42a` |
| sglang       | **258.9s (4.3m)** | `2cbe1e6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        325.0 |     143.6 | **139.5** |
| TPOT median (ms)          |         54.5 |  **52.9** |      74.9 |
| E2E median (ms)           |        386.9 | **196.0** |     208.6 |
| Throughput median (tok/s) |          3.4 |   **7.6** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        310.4 | **203.1** |  217.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        430.9 | **250.0** |  360.3 |
| Throughput median (tok/s) |          2.3 |   **4.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        737.4 | **156.2** |  161.6 |
| TPOT median (ms)          |         60.4 |  **53.2** |  105.1 |
| E2E median (ms)           |        802.0 | **200.2** |  260.2 |
| Throughput median (tok/s) |          1.6 |   **6.6** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        225.6 | **59.2** |   83.4 |
| TPOT median (ms)          |         31.2 | **29.6** |   58.0 |
| E2E median (ms)           |        258.2 | **80.9** |  153.5 |
| Throughput median (tok/s) |          5.4 | **15.0** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        347.3 |      79.9 | **66.9** |
| TPOT median (ms)          |         21.7 |  **14.8** |     22.5 |
| E2E median (ms)           |       1095.7 | **622.2** |    830.4 |
| Throughput median (tok/s) |         31.6 |  **58.4** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        389.2 | **128.4** |  133.7 |
| TPOT median (ms)          |         33.6 |  **30.1** |   52.1 |
| E2E median (ms)           |        594.7 | **269.8** |  362.6 |
| Throughput median (tok/s) |          8.9 |  **18.3** |   12.9 |
| Correctness               |          98% |       98% |    99% |
