# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:07 PM PT, May 14 2026

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
| torchinferno |     323.3s (5.4m) | `58e4246` |
| vllm         |   1090.0s (18.2m) | `f887aa1` |
| sglang       | **166.2s (2.8m)** | `88d3ed7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        313.8 |    159.2 | **136.2** |
| TPOT median (ms)          |        169.3 | **57.0** |      76.0 |
| E2E median (ms)           |        413.7 |    217.7 | **205.5** |
| Throughput median (tok/s) |          3.3 |  **6.7** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        304.4 | **189.1** |  200.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        366.0 | **215.9** |  334.8 |
| Throughput median (tok/s) |          2.7 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        573.0 |     167.2 | **158.3** |
| TPOT median (ms)          |        151.3 |  **65.9** |     100.5 |
| E2E median (ms)           |        753.3 | **222.6** |     257.0 |
| Throughput median (tok/s) |          1.9 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        431.5 | **58.4** |   73.3 |
| TPOT median (ms)          |        209.9 | **26.8** |   61.6 |
| E2E median (ms)           |        609.0 | **79.1** |  155.1 |
| Throughput median (tok/s) |          2.1 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        555.7 |      74.7 | **67.5** |
| TPOT median (ms)          |         16.5 |  **14.9** |     22.1 |
| E2E median (ms)           |       1267.4 | **650.2** |    809.7 |
| Throughput median (tok/s) |         25.6 |  **58.1** |     43.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        435.7 |     129.7 | **127.1** |
| TPOT median (ms)          |        109.4 |  **32.9** |      52.0 |
| E2E median (ms)           |        681.9 | **277.1** |     352.4 |
| Throughput median (tok/s) |          7.1 |  **18.3** |      13.3 |
| Correctness               |          98% |       99% |       98% |
