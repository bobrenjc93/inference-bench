# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:10 AM PT, May 18 2026

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
| torchinferno |     341.5s (5.7m) | `c837893` |
| vllm         |   1151.1s (19.2m) | `f5d3dc7` |
| sglang       | **178.8s (3.0m)** | `d1acd62` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        263.9 |    158.3 | **136.7** |
| TPOT median (ms)          |        152.6 | **64.1** |      75.3 |
| E2E median (ms)           |        367.4 |    215.1 | **202.9** |
| Throughput median (tok/s) |          4.1 |  **6.9** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        269.4 | **199.0** |  200.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        296.4 | **220.3** |  334.5 |
| Throughput median (tok/s) |          3.4 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        521.4 |     177.3 | **156.2** |
| TPOT median (ms)          |        125.3 |  **66.7** |     107.4 |
| E2E median (ms)           |        613.6 | **238.1** |     256.5 |
| Throughput median (tok/s) |          2.2 |   **5.9** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        362.1 | **59.1** |   76.4 |
| TPOT median (ms)          |        130.8 | **28.0** |   61.6 |
| E2E median (ms)           |        472.1 | **80.1** |  152.7 |
| Throughput median (tok/s) |          2.8 | **15.3** |    9.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        723.3 |      73.1 | **65.1** |
| TPOT median (ms)          |         15.6 |  **14.9** |     22.0 |
| E2E median (ms)           |       1279.8 | **620.0** |    818.6 |
| Throughput median (tok/s) |         28.0 |  **58.6** |     42.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        428.0 |     133.4 | **126.9** |
| TPOT median (ms)          |         84.9 |  **34.7** |      53.3 |
| E2E median (ms)           |        605.9 | **274.7** |     353.0 |
| Throughput median (tok/s) |          8.1 |  **18.2** |      13.3 |
| Correctness               |          98% |       99% |       98% |
