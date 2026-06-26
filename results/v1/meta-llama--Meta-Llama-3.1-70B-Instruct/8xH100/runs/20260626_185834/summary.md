# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:58 AM PT, Jun 26 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/4** |    0/4 |          1/4 |
| self_consistency |   **2/4** |    0/4 |          1/4 |
| multi_turn       |   **3/4** |    1/4 |          0/4 |
| tree_of_thought  |   **4/4** |    0/4 |          0/4 |
| long_output      |   **4/4** |    0/4 |          0/4 |
| **Total**        | **16/20** |   1/20 |         2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `9222148` |
| sglang       |     0.0s (0.0m) | `bc15017` |
| torchinferno |     0.0s (0.0m) | `876c18c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **152.3** |  162.7 |        167.3 |
| TPOT median (ms)          |      57.0 |   88.2 |     **55.2** |
| E2E median (ms)           | **199.6** |  246.6 |        214.8 |
| Throughput median (tok/s) |   **6.9** |    4.9 |          5.3 |
| Correctness               |       98% |    98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |     182.5 |  324.9 |    **161.4** |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **316.3** |  626.6 |        325.7 |
| Throughput median (tok/s) |   **3.2** |    1.6 |          3.1 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     197.6 | **187.9** |        477.7 |
| TPOT median (ms)          |  **60.2** |     109.0 |         67.1 |
| E2E median (ms)           | **249.5** |     302.4 |        535.4 |
| Throughput median (tok/s) |   **5.5** |       4.2 |          2.2 |
| Correctness               |       98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **74.9** |   77.5 |        281.2 |
| TPOT median (ms)          |  **36.1** |   82.8 |         56.4 |
| E2E median (ms)           | **102.1** |  165.9 |        377.2 |
| Throughput median (tok/s) |  **12.2** |    8.6 |          4.1 |
| Correctness               |       97% |    97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **82.2** |   85.1 |        350.0 |
| TPOT median (ms)          |  **18.8** |   27.0 |         27.8 |
| E2E median (ms)           | **759.3** | 1004.8 |       1446.4 |
| Throughput median (tok/s) |  **47.6** |   34.5 |         26.2 |
| Correctness               |      100% |   100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **137.9** |  167.6 |        287.5 |
| TPOT median (ms)          |  **34.4** |   61.4 |         41.3 |
| E2E median (ms)           | **325.3** |  469.3 |        579.9 |
| Throughput median (tok/s) |  **15.1** |   10.8 |          8.2 |
| Correctness               |       98% |    98% |          98% |
