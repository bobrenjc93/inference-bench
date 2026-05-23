# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, May 22 2026

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
| torchinferno |     330.4s (5.5m) | `9f91b40` |
| vllm         |   1262.6s (21.0m) | `367cb81` |
| sglang       | **182.4s (3.0m)** | `d226f75` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.9 |     158.5 | **146.4** |
| TPOT median (ms)          |        155.0 |  **55.2** |      74.7 |
| E2E median (ms)           |        382.9 | **209.7** |     216.2 |
| Throughput median (tok/s) |          3.9 |   **6.9** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        283.5 | **191.4** |  202.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        308.2 | **214.1** |  341.0 |
| Throughput median (tok/s) |          3.2 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        751.1 |     172.2 | **158.2** |
| TPOT median (ms)          |        131.0 |  **57.7** |     102.3 |
| E2E median (ms)           |        850.6 | **219.1** |     263.3 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        341.8 | **59.4** |   79.3 |
| TPOT median (ms)          |        133.6 | **27.0** |   53.8 |
| E2E median (ms)           |        456.8 | **80.5** |  148.8 |
| Throughput median (tok/s) |          3.1 | **15.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        917.5 |      70.9 | **68.8** |
| TPOT median (ms)          |         15.9 |  **15.0** |     22.2 |
| E2E median (ms)           |       1569.1 | **612.8** |    830.0 |
| Throughput median (tok/s) |         20.6 |  **58.9** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        515.9 | **130.5** |  131.1 |
| TPOT median (ms)          |         87.1 |  **31.0** |   50.6 |
| E2E median (ms)           |        713.5 | **267.2** |  359.9 |
| Throughput median (tok/s) |          6.5 |  **18.5** |   13.1 |
| Correctness               |          98% |       98% |    99% |
