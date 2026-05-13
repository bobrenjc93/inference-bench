# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:01 PM PT, May 12 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **90.7s (1.5m)** | `9d5290c` |
| vllm         |  1191.3s (19.9m) | `dcacdf9` |
| sglang       |    178.1s (3.0m) | `3f048c8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        430.1 |    170.2 | **143.8** |
| TPOT median (ms)          |        510.1 | **62.0** |      81.2 |
| E2E median (ms)           |        868.4 |    228.8 | **217.9** |
| Throughput median (tok/s) |          1.6 |  **6.5** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        769.1 | **189.9** |  214.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        801.5 | **216.1** |  360.6 |
| Throughput median (tok/s) |          1.2 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1297.4 |     188.3 | **167.3** |
| TPOT median (ms)          |        227.6 |  **57.1** |     110.4 |
| E2E median (ms)           |       1476.5 | **244.0** |     264.9 |
| Throughput median (tok/s) |          0.9 |   **5.8** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        631.0 | **61.7** |   78.4 |
| TPOT median (ms)          |        467.5 | **28.1** |   53.4 |
| E2E median (ms)           |        992.4 | **83.2** |  144.4 |
| Throughput median (tok/s) |          1.5 | **14.9** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1053.0 |  **73.9** |   79.1 |
| TPOT median (ms)          |         32.9 |  **14.9** |   21.9 |
| E2E median (ms)           |       2203.7 | **608.3** |  826.6 |
| Throughput median (tok/s) |         15.1 |  **58.2** |   42.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        836.1 |     136.8 | **136.6** |
| TPOT median (ms)          |        247.6 |  **32.4** |      53.4 |
| E2E median (ms)           |       1268.5 | **276.1** |     362.9 |
| Throughput median (tok/s) |          4.1 |  **18.0** |      12.9 |
| Correctness               |          99% |       99% |       98% |
