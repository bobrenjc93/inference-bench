# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:09 PM PT, Jul 8 2026

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
| torchinferno | **41.4s (0.7m)** | `c65061f` |
| vllm         |    274.9s (4.6m) | `56da398` |
| sglang       |    215.7s (3.6m) | `bc607ff` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        174.4 | **133.8** |  136.1 |
| TPOT median (ms)          |         45.1 |  **43.9** |   82.0 |
| E2E median (ms)           |        210.4 | **172.3** |  212.1 |
| Throughput median (tok/s) |          5.9 |   **8.4** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **126.1** | 137.2 |  223.4 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **135.7** | 162.3 |  364.8 |
| Throughput median (tok/s) |      **7.4** |   6.2 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        323.6 | **151.1** |  164.7 |
| TPOT median (ms)          |         56.4 |  **46.4** |  107.3 |
| E2E median (ms)           |        377.5 | **196.5** |  278.8 |
| Throughput median (tok/s) |          3.5 |   **6.9** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         46.2 | **33.4** |   49.6 |
| TPOT median (ms)          |         30.4 | **22.0** |  405.7 |
| E2E median (ms)           |         74.5 | **49.4** |  430.5 |
| Throughput median (tok/s) |         19.8 | **25.2** |    3.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        405.9 |      80.3 | **68.2** |
| TPOT median (ms)          |         17.3 |  **15.1** |     22.6 |
| E2E median (ms)           |       1042.7 | **692.6** |    913.7 |
| Throughput median (tok/s) |         35.1 |  **56.2** |     41.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        215.2 | **107.2** |  128.4 |
| TPOT median (ms)          |         29.8 |  **25.5** |  123.5 |
| E2E median (ms)           |        368.1 | **254.6** |  440.0 |
| Throughput median (tok/s) |         14.3 |  **20.6** |   11.5 |
| Correctness               |          98% |       99% |    99% |
