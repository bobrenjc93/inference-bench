# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 PM PT, May 19 2026

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
| torchinferno |     404.2s (6.7m) | `9f91b40` |
| vllm         |   1219.0s (20.3m) | `a65093c` |
| sglang       | **190.9s (3.2m)** | `fab097d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        305.5 |     149.1 | **138.1** |
| TPOT median (ms)          |        151.1 |  **55.1** |      75.3 |
| E2E median (ms)           |        420.6 | **198.8** |     208.7 |
| Throughput median (tok/s) |          3.5 |   **7.5** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.8 | **196.4** |  198.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        322.8 | **218.1** |  332.8 |
| Throughput median (tok/s) |          3.1 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        543.1 |     181.3 | **157.0** |
| TPOT median (ms)          |        122.3 |  **60.5** |      99.7 |
| E2E median (ms)           |        627.6 | **233.8** |     261.4 |
| Throughput median (tok/s) |          2.0 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        368.3 | **57.1** |   75.3 |
| TPOT median (ms)          |        128.7 | **27.1** |   54.9 |
| E2E median (ms)           |        473.6 | **78.0** |  144.6 |
| Throughput median (tok/s) |          2.8 | **15.8** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        774.0 |      67.4 | **65.6** |
| TPOT median (ms)          |         17.0 |  **15.0** |     22.5 |
| E2E median (ms)           |       1482.7 | **608.2** |    827.4 |
| Throughput median (tok/s) |         21.4 |  **59.5** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        455.9 |     130.3 | **127.0** |
| TPOT median (ms)          |         83.8 |  **31.5** |      50.5 |
| E2E median (ms)           |        665.5 | **267.4** |     355.0 |
| Throughput median (tok/s) |          6.6 |  **18.7** |      13.2 |
| Correctness               |          99% |       98% |       98% |
