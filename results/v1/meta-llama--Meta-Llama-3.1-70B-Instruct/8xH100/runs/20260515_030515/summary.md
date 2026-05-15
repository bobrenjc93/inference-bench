# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:07 PM PT, May 14 2026

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
| torchinferno |     325.3s (5.4m) | `d648af4` |
| vllm         |   1075.6s (17.9m) | `0d4d334` |
| sglang       | **167.5s (2.8m)** | `8d5b347` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        316.1 |    161.1 | **133.5** |
| TPOT median (ms)          |        160.3 | **56.6** |      78.4 |
| E2E median (ms)           |        407.7 |    213.9 | **202.7** |
| Throughput median (tok/s) |          3.5 |  **6.9** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.5 | **184.6** |  206.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        323.4 | **206.1** |  354.0 |
| Throughput median (tok/s) |          3.1 |   **4.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        560.3 |     166.9 | **149.9** |
| TPOT median (ms)          |        155.9 |  **51.0** |      99.5 |
| E2E median (ms)           |        640.0 | **209.3** |     249.3 |
| Throughput median (tok/s) |          2.1 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        343.7 | **57.7** |   73.0 |
| TPOT median (ms)          |        133.9 | **27.3** |   48.5 |
| E2E median (ms)           |        437.3 | **78.1** |  129.2 |
| Throughput median (tok/s) |          3.1 | **15.7** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        646.9 |      73.9 | **68.5** |
| TPOT median (ms)          |         15.8 |  **15.0** |     22.2 |
| E2E median (ms)           |       1298.4 | **630.8** |    833.9 |
| Throughput median (tok/s) |         26.2 |  **58.3** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        432.7 |     128.9 | **126.2** |
| TPOT median (ms)          |         93.2 |  **30.0** |      49.7 |
| E2E median (ms)           |        621.4 | **267.6** |     353.8 |
| Throughput median (tok/s) |          7.6 |  **18.4** |      13.2 |
| Correctness               |          98% |       99% |       99% |
