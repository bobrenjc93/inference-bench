# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:07 PM PT, May 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     319.2s (5.3m) | `d648af4` |
| vllm         |   1100.7s (18.3m) | `0d4d334` |
| sglang       | **160.6s (2.7m)** | `dca9ba6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        305.7 |    171.4 | **134.2** |
| TPOT median (ms)          |        156.9 | **55.0** |      74.3 |
| E2E median (ms)           |        389.2 |    227.5 | **205.2** |
| Throughput median (tok/s) |          3.8 |  **6.3** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        306.8 |     215.6 | **213.1** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        376.3 | **257.5** |     349.6 |
| Throughput median (tok/s) |          2.7 |   **3.9** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        518.8 |     175.8 | **151.9** |
| TPOT median (ms)          |        103.0 |  **59.9** |     101.8 |
| E2E median (ms)           |        630.9 | **230.5** |     251.5 |
| Throughput median (tok/s) |          2.2 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        330.2 | **59.2** |   73.5 |
| TPOT median (ms)          |        132.7 | **27.6** |   68.4 |
| E2E median (ms)           |        425.9 | **80.2** |  159.2 |
| Throughput median (tok/s) |          3.7 | **15.4** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        582.3 |      72.6 | **64.4** |
| TPOT median (ms)          |         15.3 |  **15.0** |     22.6 |
| E2E median (ms)           |       1226.5 | **622.1** |    816.2 |
| Throughput median (tok/s) |         27.7 |  **58.3** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        408.8 |     138.9 | **127.4** |
| TPOT median (ms)          |         81.6 |  **31.5** |      53.4 |
| E2E median (ms)           |        609.7 | **283.6** |     356.3 |
| Throughput median (tok/s) |          8.0 |  **18.0** |      13.0 |
| Correctness               |          99% |       99% |       99% |
