# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jun 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     327.4s (5.5m) | `3c33281` |
| vllm         |   1353.0s (22.5m) | `53b88d1` |
| sglang       | **229.2s (3.8m)** | `3e681d7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        339.9 |     166.8 | **148.0** |
| TPOT median (ms)          |     **51.3** |      61.7 |      79.1 |
| E2E median (ms)           |        396.0 | **218.4** |     224.3 |
| Throughput median (tok/s) |          3.2 |   **6.7** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        251.6 |     307.6 | **215.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        353.2 | **339.2** |     352.8 |
| Throughput median (tok/s) |          2.8 |   **2.9** |       2.8 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        838.8 |     180.9 | **161.2** |
| TPOT median (ms)          |         98.6 |  **64.8** |     100.9 |
| E2E median (ms)           |        948.6 | **241.9** |     261.0 |
| Throughput median (tok/s) |          1.5 |   **5.9** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        339.1 | **61.0** |   84.1 |
| TPOT median (ms)          |         32.4 | **28.0** |   45.0 |
| E2E median (ms)           |        369.4 | **82.3** |  144.2 |
| Throughput median (tok/s) |          3.8 | **14.9** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        412.7 |  **69.5** |   75.7 |
| TPOT median (ms)          |         35.7 |  **14.7** |   23.2 |
| E2E median (ms)           |       1639.0 | **601.0** |  879.7 |
| Throughput median (tok/s) |         21.7 |  **59.9** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        436.4 |     157.2 | **136.8** |
| TPOT median (ms)          |         43.6 |  **33.8** |      49.6 |
| E2E median (ms)           |        741.2 | **296.6** |     372.4 |
| Throughput median (tok/s) |          6.6 |  **18.1** |      12.6 |
| Correctness               |          99% |       99% |       99% |
