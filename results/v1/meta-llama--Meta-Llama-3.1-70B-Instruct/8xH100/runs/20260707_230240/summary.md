# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.0s (0.7m)** | `49c2f1b` |
| vllm         |    342.2s (5.7m) | `aad0fb7` |
| sglang       |    209.3s (3.5m) | `b363249` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        155.9 | **123.8** |  130.6 |
| TPOT median (ms)          |         43.2 |  **41.5** |   80.4 |
| E2E median (ms)           |        195.5 | **151.6** |  208.8 |
| Throughput median (tok/s) |          6.1 |   **8.7** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **104.8** | 126.5 |  207.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **112.1** | 150.0 |  354.9 |
| Throughput median (tok/s) |      **8.9** |   6.7 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        239.8 | **149.9** |  160.1 |
| TPOT median (ms)          |         58.7 |  **40.0** |  110.8 |
| E2E median (ms)           |        283.5 | **189.0** |  276.2 |
| Throughput median (tok/s) |          4.4 |   **7.2** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         60.0 | **32.7** |   46.7 |
| TPOT median (ms)          |         43.1 | **21.7** |  352.5 |
| E2E median (ms)           |         91.5 | **48.2** |  393.0 |
| Throughput median (tok/s) |         15.6 | **25.5** |    3.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        254.1 |      79.5 | **66.9** |
| TPOT median (ms)          |         20.8 |  **14.7** |     23.1 |
| E2E median (ms)           |        991.2 | **645.2** |    932.7 |
| Throughput median (tok/s) |         36.1 |  **58.7** |     40.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        162.9 | **102.5** |  122.3 |
| TPOT median (ms)          |         33.1 |  **23.6** |  113.4 |
| E2E median (ms)           |        334.8 | **236.8** |  433.1 |
| Throughput median (tok/s) |         14.2 |  **21.3** |   11.6 |
| Correctness               |          99% |       99% |    99% |
