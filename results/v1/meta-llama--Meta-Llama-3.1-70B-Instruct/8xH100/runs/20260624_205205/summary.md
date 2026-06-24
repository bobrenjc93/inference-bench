# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:52 PM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **3/4** |       1/4 |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.9s (0.1m)** | `2af6f8f` |
| vllm         |    86.2s (1.4m) | `1cd3e0e` |
| sglang       |     9.0s (0.1m) | `4a4f063` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm | sglang |
| :------------------------ | -----------: | ------: | -----: |
| TTFT median (ms)          |    **154.6** |   159.1 |  155.3 |
| TPOT median (ms)          |     **51.2** |    55.6 |   89.2 |
| E2E median (ms)           |    **197.6** |   209.1 |  248.2 |
| Throughput median (tok/s) |          6.0 | **6.6** |    4.8 |
| Correctness               |          98% |     98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        339.7 | **181.0** |  238.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        370.4 | **352.5** |  437.0 |
| Throughput median (tok/s) |          2.7 |   **2.8** |    2.3 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        468.7 | **163.5** |  180.7 |
| TPOT median (ms)          |     **67.5** |      87.1 |  122.5 |
| E2E median (ms)           |        573.5 | **247.5** |  306.0 |
| Throughput median (tok/s) |          2.1 |   **5.2** |    4.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        285.4 |  **73.9** |   81.2 |
| TPOT median (ms)          |         51.4 |  **34.8** |   71.1 |
| E2E median (ms)           |        330.4 | **101.2** |  165.8 |
| Throughput median (tok/s) |          4.5 |  **12.1** |    8.2 |
| Correctness               |          97% |       97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        375.4 |  **85.7** |   95.3 |
| TPOT median (ms)          |         24.8 |  **18.8** |   26.5 |
| E2E median (ms)           |       1387.3 | **768.1** |  977.0 |
| Throughput median (tok/s) |         27.9 |  **47.1** |   34.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        324.7 | **132.6** |  150.2 |
| TPOT median (ms)          |     **39.0** |      39.3 |   61.8 |
| E2E median (ms)           |        571.8 | **335.7** |  426.8 |
| Throughput median (tok/s) |          8.6 |  **14.8** |   10.8 |
| Correctness               |          98% |       98% |    99% |
