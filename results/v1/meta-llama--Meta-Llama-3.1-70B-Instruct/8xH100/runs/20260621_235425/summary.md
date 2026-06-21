# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **13/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     288.3s (4.8m) | `28d7c7c` |
| vllm         |     401.2s (6.7m) | `a19ff22` |
| sglang       | **254.4s (4.2m)** | `4f5ff39` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        150.6 |   152.4 | **147.7** |
| TPOT median (ms)          |     **44.1** |    53.5 |      73.5 |
| E2E median (ms)           |    **197.3** |   203.9 |     217.3 |
| Throughput median (tok/s) |          6.3 | **7.1** |       5.4 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.1 | **208.9** |  214.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        388.6 | **235.6** |  367.9 |
| Throughput median (tok/s) |          2.6 |   **4.2** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        601.7 |     162.9 | **162.5** |
| TPOT median (ms)          |     **37.5** |      58.9 |     100.4 |
| E2E median (ms)           |        632.1 | **208.6** |     258.3 |
| Throughput median (tok/s) |          2.1 |   **6.6** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        238.7 | **58.3** |   80.8 |
| TPOT median (ms)          |         32.1 | **28.8** |   40.1 |
| E2E median (ms)           |        274.1 | **79.7** |  128.7 |
| Throughput median (tok/s) |          5.0 | **15.3** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        348.7 |      71.5 | **66.4** |
| TPOT median (ms)          |         21.0 |  **15.0** |     22.5 |
| E2E median (ms)           |       1168.7 | **620.5** |    856.2 |
| Throughput median (tok/s) |         31.9 |  **58.9** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.7 | **130.8** |  134.3 |
| TPOT median (ms)          |     **26.9** |      31.2 |   47.3 |
| E2E median (ms)           |        532.2 | **269.7** |  365.7 |
| Throughput median (tok/s) |          9.6 |  **18.4** |   13.1 |
| Correctness               |          98% |       99% |    99% |
