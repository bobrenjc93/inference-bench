# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 8 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.6s (0.7m)** | `1ec045c` |
| vllm         |    316.5s (5.3m) | `4400025` |
| sglang       |    162.8s (2.7m) | `042228a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        157.0 | **125.9** |  136.9 |
| TPOT median (ms)          |     **45.9** |      46.2 |   78.8 |
| E2E median (ms)           |        198.3 | **162.8** |  215.7 |
| Throughput median (tok/s) |          6.1 |   **8.7** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **121.0** | 126.2 |  214.6 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **127.7** | 150.0 |  355.9 |
| Throughput median (tok/s) |      **7.8** |   6.7 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        284.2 | **140.0** |  164.9 |
| TPOT median (ms)          |         58.4 |  **50.7** |  113.7 |
| E2E median (ms)           |        337.7 | **186.1** |  282.7 |
| Throughput median (tok/s) |          4.0 |   **7.4** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         59.0 | **32.7** |   49.8 |
| TPOT median (ms)          |         42.0 | **21.7** |  364.7 |
| E2E median (ms)           |         87.9 | **48.3** |  416.1 |
| Throughput median (tok/s) |         16.5 | **25.7** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        282.0 |  **71.3** |   71.8 |
| TPOT median (ms)          |         19.8 |  **14.7** |   21.6 |
| E2E median (ms)           |       1051.0 | **586.3** |  904.5 |
| Throughput median (tok/s) |         36.9 |  **59.6** |   41.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        180.6 |  **99.2** |  127.6 |
| TPOT median (ms)          |         33.2 |  **26.6** |  115.8 |
| E2E median (ms)           |        360.5 | **226.7** |  435.0 |
| Throughput median (tok/s) |         14.3 |  **21.6** |   11.6 |
| Correctness               |          98% |       99% |    99% |
