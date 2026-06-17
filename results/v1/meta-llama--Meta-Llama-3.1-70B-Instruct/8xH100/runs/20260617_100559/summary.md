# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     408.4s (6.8m) | `ccca738` |
| vllm         |     557.3s (9.3m) | `68ff30d` |
| sglang       | **258.8s (4.3m)** | `21a9533` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.6 | **132.9** |  157.1 |
| TPOT median (ms)          |         51.3 |  **46.4** |   72.1 |
| E2E median (ms)           |        334.6 | **171.7** |  227.9 |
| Throughput median (tok/s) |          4.2 |   **8.0** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        303.3 |     211.6 | **207.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        414.9 | **237.6** |     344.5 |
| Throughput median (tok/s) |          2.4 |   **4.2** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        703.1 | **159.6** |  174.2 |
| TPOT median (ms)          |         60.2 |  **56.7** |   98.9 |
| E2E median (ms)           |        763.8 | **201.1** |  276.6 |
| Throughput median (tok/s) |          1.8 |   **6.6** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.1 | **57.5** |   85.1 |
| TPOT median (ms)          |         35.9 | **29.2** |   41.2 |
| E2E median (ms)           |        228.5 | **79.2** |  138.5 |
| Throughput median (tok/s) |          5.5 | **15.2** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        368.7 |      69.9 | **69.1** |
| TPOT median (ms)          |         21.6 |  **14.9** |     22.9 |
| E2E median (ms)           |       1108.9 | **599.4** |    829.3 |
| Throughput median (tok/s) |         31.9 |  **59.6** |     41.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        372.1 | **126.3** |  138.7 |
| TPOT median (ms)          |         33.8 |  **29.4** |   47.0 |
| E2E median (ms)           |        570.1 | **257.8** |  363.4 |
| Throughput median (tok/s) |          9.1 |  **18.7** |   12.8 |
| Correctness               |          99% |       99% |    99% |
