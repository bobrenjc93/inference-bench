# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **2/4** |       1/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.2s (0.7m)** | `372227c` |
| vllm         |    217.3s (3.6m) | `2f3f441` |
| sglang       |    192.5s (3.2m) | `d88644b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        181.3 | **131.1** |  140.7 |
| TPOT median (ms)          |     **46.0** |      47.2 |   75.0 |
| E2E median (ms)           |        217.2 | **172.2** |  215.9 |
| Throughput median (tok/s) |          5.9 |   **8.0** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        121.1 | **114.1** |  213.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |    **130.1** |     136.7 |  348.3 |
| Throughput median (tok/s) |      **7.7** |       7.3 |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        227.6 | **152.5** |  163.2 |
| TPOT median (ms)          |         58.0 |  **56.4** |  118.4 |
| E2E median (ms)           |        288.0 | **199.2** |  284.9 |
| Throughput median (tok/s) |          4.5 |   **7.0** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         67.3 | **32.7** |   49.6 |
| TPOT median (ms)          |         44.3 | **21.7** |  410.5 |
| E2E median (ms)           |        102.3 | **48.4** |  430.7 |
| Throughput median (tok/s) |         14.3 | **25.8** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        292.2 |      79.5 | **68.8** |
| TPOT median (ms)          |         19.3 |  **14.8** |     22.1 |
| E2E median (ms)           |       1059.0 | **695.0** |    898.5 |
| Throughput median (tok/s) |         35.8 |  **58.4** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        177.9 | **102.0** |  127.3 |
| TPOT median (ms)          |         33.5 |  **28.0** |  125.2 |
| E2E median (ms)           |        359.3 | **250.3** |  435.7 |
| Throughput median (tok/s) |         13.6 |  **21.3** |   11.7 |
| Correctness               |          98% |       99% |    98% |
