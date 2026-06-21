# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **18/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     379.5s (6.3m) | `a7e5516` |
| vllm         |     523.6s (8.7m) | `b91b772` |
| sglang       | **266.5s (4.4m)** | `a51d56d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        135.0 | **132.2** |  147.5 |
| TPOT median (ms)          |         45.4 |  **42.7** |   76.5 |
| E2E median (ms)           |        175.2 | **164.2** |  216.9 |
| Throughput median (tok/s) |          6.7 |   **8.6** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        317.1 | **203.8** |  225.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        429.1 | **233.3** |  378.3 |
| Throughput median (tok/s) |          2.3 |   **4.3** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        548.4 | **158.7** |  163.5 |
| TPOT median (ms)          |     **37.2** |      47.0 |  105.6 |
| E2E median (ms)           |        581.4 | **196.7** |  259.3 |
| Throughput median (tok/s) |          2.2 |   **6.5** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        225.2 | **58.6** |   84.7 |
| TPOT median (ms)          |         31.3 | **28.3** |   45.1 |
| E2E median (ms)           |        260.4 | **79.6** |  134.5 |
| Throughput median (tok/s) |          5.2 | **15.1** |    9.9 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        337.5 |  **67.5** |   74.6 |
| TPOT median (ms)          |         21.5 |  **14.8** |   22.5 |
| E2E median (ms)           |       1078.8 | **600.3** |  851.9 |
| Throughput median (tok/s) |         32.4 |  **59.4** |   41.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        312.6 | **124.2** |  139.1 |
| TPOT median (ms)          |         27.1 |  **26.6** |   49.9 |
| E2E median (ms)           |        505.0 | **254.8** |  368.2 |
| Throughput median (tok/s) |          9.7 |  **18.8** |   13.0 |
| Correctness               |          98% |       99% |    98% |
