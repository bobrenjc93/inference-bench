# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **16/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    665.6s (11.1m) | `20cb8e8` |
| vllm         |     546.2s (9.1m) | `72f6399` |
| sglang       | **337.7s (5.6m)** | `f480c5f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        160.1 | **144.3** |  151.9 |
| TPOT median (ms)          |     **46.2** |      53.2 |   65.1 |
| E2E median (ms)           |        199.9 | **192.4** |  220.6 |
| Throughput median (tok/s) |          5.9 |   **7.5** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        223.4 | **190.2** |  208.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        238.9 | **222.1** |  345.4 |
| Throughput median (tok/s) |          4.2 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.8 | **166.4** |  174.8 |
| TPOT median (ms)          |     **56.1** |      63.8 |   98.3 |
| E2E median (ms)           |        342.1 | **219.9** |  267.7 |
| Throughput median (tok/s) |          4.3 |   **6.4** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        186.7 | **61.2** |   87.2 |
| TPOT median (ms)          |         56.6 | **33.9** |   38.1 |
| E2E median (ms)           |        233.4 | **87.1** |  135.4 |
| Throughput median (tok/s) |          6.0 | **13.7** |    9.9 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        307.1 |      71.8 | **70.5** |
| TPOT median (ms)          |         22.3 |  **14.8** |     22.1 |
| E2E median (ms)           |       1127.7 | **607.4** |    822.6 |
| Throughput median (tok/s) |         33.3 |  **58.8** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        233.8 | **126.8** |  138.6 |
| TPOT median (ms)          |         36.2 |  **33.1** |   44.7 |
| E2E median (ms)           |        428.4 | **265.8** |  358.3 |
| Throughput median (tok/s) |         10.7 |  **18.2** |   13.0 |
| Correctness               |          98% |       99% |    98% |
