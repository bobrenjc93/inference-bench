# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:09 AM PT, Jul 2 2026

## Scorecard

| Benchmark        | vllm |    sglang | torchinferno |
| :--------------- | ---: | --------: | -----------: |
| few_shot         |  0/4 |   **3/4** |          1/4 |
| self_consistency |  0/4 |       1/4 |      **2/4** |
| multi_turn       |  0/4 |   **3/4** |          1/4 |
| tree_of_thought  |  0/4 |   **3/4** |          1/4 |
| long_output      |  0/4 |   **4/4** |          0/4 |
| **Total**        | 0/20 | **14/20** |         5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `2a16ece` |
| sglang       |     0.0s (0.0m) | `a375e9f` |
| torchinferno |     0.0s (0.0m) | `0c3edef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 239.1 | **114.0** |        172.3 |
| TPOT median (ms)          |  86.4 |      88.5 |     **50.1** |
| E2E median (ms)           | 319.8 | **202.7** |        214.3 |
| Throughput median (tok/s) |   4.6 |   **5.8** |          5.5 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 216.4 | **195.7** |        216.4 |
| TPOT median (ms)          |   0.0 |       0.0 |          0.0 |
| E2E median (ms)           | 304.4 |     388.3 |    **234.3** |
| Throughput median (tok/s) |   3.3 |       2.6 |      **4.3** |
| Correctness               |  100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 284.7 | **144.5** |        341.2 |
| TPOT median (ms)          |  97.0 |     124.8 |     **66.6** |
| E2E median (ms)           | 379.4 | **273.7** |        399.3 |
| Throughput median (tok/s) |   3.9 |   **4.7** |          3.3 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 125.4 |  **55.9** |        156.1 |
| TPOT median (ms)          |  82.8 |      84.9 |     **42.3** |
| E2E median (ms)           | 186.4 | **147.7** |        195.4 |
| Throughput median (tok/s) |   6.8 |   **9.1** |          6.7 |
| Correctness               |   97% |       97% |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   94.6 |  **60.5** |        274.0 |
| TPOT median (ms)          |   27.4 |  **24.7** |         25.1 |
| E2E median (ms)           | 1115.2 | **889.8** |       1283.8 |
| Throughput median (tok/s) |   33.0 |  **38.6** |         30.5 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 192.0 | **114.1** |        232.0 |
| TPOT median (ms)          |  58.7 |      64.6 |     **36.8** |
| E2E median (ms)           | 461.0 | **380.4** |        465.4 |
| Throughput median (tok/s) |  10.3 |  **12.2** |         10.0 |
| Correctness               |   99% |       98% |          98% |
