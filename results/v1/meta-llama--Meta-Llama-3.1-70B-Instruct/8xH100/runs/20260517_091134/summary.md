# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:09 AM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     321.8s (5.4m) | `26df1b4` |
| vllm         |   1098.5s (18.3m) | `ff712f6` |
| sglang       | **162.5s (2.7m)** | `e547f3f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        269.8 |    160.1 | **134.3** |
| TPOT median (ms)          |        146.8 | **57.9** |      73.4 |
| E2E median (ms)           |        363.9 |    209.9 | **203.6** |
| Throughput median (tok/s) |          4.0 |  **7.1** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.9 | **190.8** |  195.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        310.7 | **213.2** |  334.0 |
| Throughput median (tok/s) |          3.2 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        545.1 |     172.2 | **164.4** |
| TPOT median (ms)          |        115.3 |  **61.2** |     100.5 |
| E2E median (ms)           |        664.4 | **228.9** |     265.6 |
| Throughput median (tok/s) |          2.0 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        330.7 | **58.0** |   76.1 |
| TPOT median (ms)          |        127.1 | **27.0** |   63.2 |
| E2E median (ms)           |        422.9 | **78.5** |  148.5 |
| Throughput median (tok/s) |          3.1 | **15.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        765.7 |  **71.9** |   72.1 |
| TPOT median (ms)          |         17.5 |  **15.0** |   21.8 |
| E2E median (ms)           |       1472.1 | **620.0** |  828.0 |
| Throughput median (tok/s) |         24.3 |  **58.0** |   42.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        438.1 |     130.6 | **128.5** |
| TPOT median (ms)          |         81.3 |  **32.2** |      51.8 |
| E2E median (ms)           |        646.8 | **270.1** |     355.9 |
| Throughput median (tok/s) |          7.3 |  **18.3** |      13.2 |
| Correctness               |          98% |       98% |       99% |
