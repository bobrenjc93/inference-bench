# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:09 PM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     327.8s (5.5m) | `13d21ac` |
| vllm         |   1116.5s (18.6m) | `599e75f` |
| sglang       | **166.6s (2.8m)** | `89e501c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.4 |     151.6 | **138.9** |
| TPOT median (ms)          |        154.1 |  **54.3** |      77.4 |
| E2E median (ms)           |        378.1 | **203.6** |     211.7 |
| Throughput median (tok/s) |          4.0 |   **7.2** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        299.2 |     204.2 | **201.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        324.5 | **226.6** |     339.5 |
| Throughput median (tok/s) |          3.1 |   **4.4** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        533.7 |     165.1 | **155.1** |
| TPOT median (ms)          |        193.2 |  **67.2** |     108.1 |
| E2E median (ms)           |        620.7 | **220.2** |     258.3 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        363.2 | **57.6** |   75.9 |
| TPOT median (ms)          |        132.7 | **26.8** |   65.2 |
| E2E median (ms)           |        464.2 | **78.2** |  151.8 |
| Throughput median (tok/s) |          3.0 | **15.9** |    9.4 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        808.6 |      69.5 | **69.4** |
| TPOT median (ms)          |         16.9 |  **14.9** |     21.9 |
| E2E median (ms)           |       1502.9 | **612.8** |    821.0 |
| Throughput median (tok/s) |         21.3 |  **59.3** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        456.8 |     129.6 | **128.1** |
| TPOT median (ms)          |         99.4 |  **32.6** |      54.5 |
| E2E median (ms)           |        658.1 | **268.3** |     356.4 |
| Throughput median (tok/s) |          6.7 |  **18.6** |      13.2 |
| Correctness               |          98% |       98% |       99% |
