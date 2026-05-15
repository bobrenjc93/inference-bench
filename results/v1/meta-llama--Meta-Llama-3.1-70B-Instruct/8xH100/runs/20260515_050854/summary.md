# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:08 PM PT, May 14 2026

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
| torchinferno |     375.7s (6.3m) | `d648af4` |
| vllm         |   1058.2s (17.6m) | `faa4b76` |
| sglang       | **166.2s (2.8m)** | `897587b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        308.9 |    163.2 | **135.0** |
| TPOT median (ms)          |        158.1 | **53.5** |      72.6 |
| E2E median (ms)           |        398.0 |    216.4 | **201.5** |
| Throughput median (tok/s) |          3.7 |  **6.9** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        286.8 | **188.3** |  214.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        361.5 | **210.8** |  356.1 |
| Throughput median (tok/s) |          2.8 |   **4.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        586.8 |     170.8 | **158.5** |
| TPOT median (ms)          |        189.0 |  **67.2** |     110.4 |
| E2E median (ms)           |        698.6 | **231.1** |     260.0 |
| Throughput median (tok/s) |          1.9 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.8 | **57.3** |   73.8 |
| TPOT median (ms)          |        130.3 | **26.6** |   67.8 |
| E2E median (ms)           |        451.4 | **77.9** |  154.6 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        730.1 |      67.7 | **64.3** |
| TPOT median (ms)          |         16.0 |  **15.0** |     22.1 |
| E2E median (ms)           |       1395.6 | **612.5** |    832.7 |
| Throughput median (tok/s) |         23.1 |  **58.9** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        452.9 |     129.5 | **129.3** |
| TPOT median (ms)          |         98.7 |  **32.5** |      54.6 |
| E2E median (ms)           |        661.0 | **269.8** |     361.0 |
| Throughput median (tok/s) |          6.9 |  **18.5** |      13.1 |
| Correctness               |          99% |       99% |       99% |
