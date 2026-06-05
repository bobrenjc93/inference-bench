# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, Jun 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     399.7s (6.7m) | `89edcfc` |
| vllm         |   1363.1s (22.7m) | `c505cd9` |
| sglang       | **193.7s (3.2m)** | `4df1ccd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        358.7 |     154.8 | **147.9** |
| TPOT median (ms)          |         59.7 |  **53.9** |      76.0 |
| E2E median (ms)           |        424.1 | **208.7** |     219.2 |
| Throughput median (tok/s) |          3.1 |   **7.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        295.4 | **199.6** |  204.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        411.9 | **251.8** |  337.7 |
| Throughput median (tok/s) |          2.4 |   **4.0** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        769.4 |     170.5 | **166.8** |
| TPOT median (ms)          |         66.5 |  **55.6** |      97.7 |
| E2E median (ms)           |        832.1 | **222.3** |     259.6 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        352.8 | **60.6** |   89.1 |
| TPOT median (ms)          |         32.4 | **29.1** |   39.1 |
| E2E median (ms)           |        381.1 | **82.4** |  142.2 |
| Throughput median (tok/s) |          3.6 | **14.7** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        543.9 |  **69.0** |   79.1 |
| TPOT median (ms)          |         32.9 |  **14.8** |   24.3 |
| E2E median (ms)           |       1574.1 | **597.4** |  914.8 |
| Throughput median (tok/s) |         21.6 |  **59.5** |   38.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        464.0 | **130.9** |  137.5 |
| TPOT median (ms)          |         38.3 |  **30.7** |   47.4 |
| E2E median (ms)           |        724.7 | **272.5** |  374.7 |
| Throughput median (tok/s) |          6.5 |  **18.3** |   12.3 |
| Correctness               |          98% |       98% |    99% |
