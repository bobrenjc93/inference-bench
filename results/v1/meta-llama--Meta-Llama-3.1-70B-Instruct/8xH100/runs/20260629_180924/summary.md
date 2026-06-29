# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:09 AM PT, Jun 29 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     0/4 |   **3/4** |          1/4 |
| self_consistency | **2/4** |       1/4 |          0/4 |
| multi_turn       |     0/4 |   **3/4** |          1/4 |
| tree_of_thought  |     0/4 |   **3/4** |          1/4 |
| long_output      |     0/4 |   **3/4** |          1/4 |
| **Total**        |    2/20 | **13/20** |         4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |
| torchinferno |     0.0s (0.0m) | `7110c60` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 274.1 | **121.0** |        164.2 |
| TPOT median (ms)          | 134.7 |      82.4 |     **49.7** |
| E2E median (ms)           | 324.1 | **203.8** |        205.0 |
| Throughput median (tok/s) |   4.2 |   **6.0** |          5.6 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     259.4 | **243.9** |        281.8 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **312.0** |     403.0 |        349.0 |
| Throughput median (tok/s) |   **3.2** |       2.5 |          2.9 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 274.7 | **166.3** |        323.7 |
| TPOT median (ms)          |  95.4 |     107.0 |     **61.6** |
| E2E median (ms)           | 371.2 | **290.8** |        383.0 |
| Throughput median (tok/s) |   4.1 |   **4.6** |          3.2 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 126.5 |  **61.8** |        283.9 |
| TPOT median (ms)          |  83.7 |      68.2 |     **47.0** |
| E2E median (ms)           | 189.0 | **142.2** |        308.1 |
| Throughput median (tok/s) |   6.6 |   **9.5** |          4.5 |
| Correctness               |   97% |       97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   95.9 |  **63.0** |        273.9 |
| TPOT median (ms)          |   27.8 |      24.8 |     **24.4** |
| E2E median (ms)           | 1025.0 | **912.0** |       1204.6 |
| Throughput median (tok/s) |   32.4 |  **37.6** |         31.6 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 206.1 | **131.2** |        265.5 |
| TPOT median (ms)          |  68.3 |      56.5 |     **36.6** |
| E2E median (ms)           | 444.3 | **390.4** |        490.0 |
| Throughput median (tok/s) |  10.1 |  **12.0** |          9.5 |
| Correctness               |   99% |       99% |          99% |
