# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         5/20 | **11/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.3s (0.6m)** | `390fed4` |
| vllm         |    245.2s (4.1m) | `9226613` |
| sglang       |    238.1s (4.0m) | `8fb99bb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        161.1 |   160.4 | **141.8** |
| TPOT median (ms)          |     **46.6** |    66.1 |      75.1 |
| E2E median (ms)           |    **212.3** |   217.3 |     219.5 |
| Throughput median (tok/s) |          5.8 | **6.5** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **150.2** | 201.4 |  201.6 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **160.5** | 234.6 |  363.1 |
| Throughput median (tok/s) |      **6.2** |   4.3 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        328.0 |     181.1 | **158.7** |
| TPOT median (ms)          |         58.2 |  **46.1** |     109.6 |
| E2E median (ms)           |        383.3 | **227.5** |     267.5 |
| Throughput median (tok/s) |          3.7 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        123.1 | **64.1** |   75.6 |
| TPOT median (ms)          |         37.5 | **29.9** |   72.4 |
| E2E median (ms)           |        152.0 | **88.3** |  153.1 |
| Throughput median (tok/s) |          8.7 | **13.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        239.0 |      85.8 | **73.3** |
| TPOT median (ms)          |         20.6 |  **14.9** |     22.2 |
| E2E median (ms)           |        958.0 | **658.1** |    863.5 |
| Throughput median (tok/s) |         37.0 |  **56.3** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        200.3 |     138.6 | **130.2** |
| TPOT median (ms)          |         32.6 |  **31.4** |      55.9 |
| E2E median (ms)           |        373.2 | **285.2** |     373.3 |
| Throughput median (tok/s) |         12.3 |  **17.4** |      12.9 |
| Correctness               |          99% |       99% |       99% |
