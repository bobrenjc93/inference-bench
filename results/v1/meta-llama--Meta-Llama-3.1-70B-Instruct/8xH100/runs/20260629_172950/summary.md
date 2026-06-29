# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:29 AM PT, Jun 29 2026

## Scorecard

| Benchmark        |    vllm |    sglang | torchinferno |
| :--------------- | ------: | --------: | -----------: |
| few_shot         |     0/4 |       2/4 |          2/4 |
| self_consistency | **2/4** |       1/4 |          0/4 |
| multi_turn       |     0/4 |   **3/4** |          1/4 |
| tree_of_thought  |     0/4 |   **3/4** |          1/4 |
| long_output      |     0/4 |   **4/4** |          0/4 |
| **Total**        |    2/20 | **13/20** |         4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** |         - |
| sglang       |     0.0s (0.0m) | `643e1cc` |
| torchinferno |     0.0s (0.0m) | `3bff181` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 242.2 | **128.1** |        165.8 |
| TPOT median (ms)          |  90.3 |      76.5 |     **48.1** |
| E2E median (ms)           | 323.9 |     205.9 |    **205.6** |
| Throughput median (tok/s) |   4.3 |   **5.9** |          5.5 |
| Correctness               |   98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     233.7 | **201.1** |        315.3 |
| TPOT median (ms)          |       0.0 |       0.0 |          0.0 |
| E2E median (ms)           | **289.1** |     390.9 |        352.8 |
| Throughput median (tok/s) |   **3.5** |       2.6 |          2.8 |
| Correctness               |      100% |      100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 281.4 | **143.0** |        314.7 |
| TPOT median (ms)          | 103.9 |     117.6 |     **64.8** |
| E2E median (ms)           | 373.2 | **267.6** |        373.5 |
| Throughput median (tok/s) |   3.9 |   **4.9** |          3.3 |
| Correctness               |   98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 125.0 |  **64.0** |        272.3 |
| TPOT median (ms)          |  83.2 |      69.6 |     **48.2** |
| E2E median (ms)           | 185.3 | **140.0** |        313.6 |
| Throughput median (tok/s) |   6.8 |   **9.8** |          4.6 |
| Correctness               |   97% |       97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |   vllm |    sglang | torchinferno |
| :------------------------ | -----: | --------: | -----------: |
| TTFT median (ms)          |   93.0 |  **61.0** |        283.5 |
| TPOT median (ms)          |   26.8 |  **24.7** |         24.9 |
| E2E median (ms)           | 1118.2 | **932.8** |       1207.8 |
| Throughput median (tok/s) |   34.0 |  **38.0** |         30.8 |
| Correctness               |   100% |      100% |         100% |

## Cross-Benchmark Averages

| Metric                    |  vllm |    sglang | torchinferno |
| :------------------------ | ----: | --------: | -----------: |
| TTFT median (ms)          | 195.1 | **119.4** |        270.3 |
| TPOT median (ms)          |  60.9 |      57.7 |     **37.2** |
| E2E median (ms)           | 458.0 | **387.4** |        490.7 |
| Throughput median (tok/s) |  10.5 |  **12.2** |          9.4 |
| Correctness               |   99% |       98% |          99% |
