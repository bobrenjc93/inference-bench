# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, Jun 1 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     358.6s (6.0m) | `1557ba6` |
| vllm         |   1359.5s (22.7m) | `de21863` |
| sglang       | **223.7s (3.7m)** | `89410b3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        142.7 |   166.5 | **141.9** |
| TPOT median (ms)          |     **45.3** |    61.2 |      74.7 |
| E2E median (ms)           |    **185.0** |   225.7 |     211.1 |
| Throughput median (tok/s) |          6.4 | **6.7** |       5.8 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        356.4 | **196.1** |  206.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        451.6 | **224.0** |  346.1 |
| Throughput median (tok/s) |          2.2 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        641.4 |     170.3 | **158.2** |
| TPOT median (ms)          |         70.6 |  **57.7** |     101.8 |
| E2E median (ms)           |        765.4 | **222.6** |     255.3 |
| Throughput median (tok/s) |          1.9 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        363.1 | **59.4** |   78.5 |
| TPOT median (ms)          |         29.3 | **27.8** |   54.5 |
| E2E median (ms)           |        389.6 | **79.8** |  141.8 |
| Throughput median (tok/s) |          3.7 | **15.4** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1139.3 |  **74.7** |   78.2 |
| TPOT median (ms)          |         32.2 |  **14.9** |   23.9 |
| E2E median (ms)           |       2144.5 | **636.3** |  891.4 |
| Throughput median (tok/s) |         17.2 |  **58.9** |   38.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        528.6 |     133.4 | **132.7** |
| TPOT median (ms)          |         35.5 |  **32.3** |      51.0 |
| E2E median (ms)           |        787.2 | **277.7** |     369.1 |
| Throughput median (tok/s) |          6.3 |  **18.4** |      12.4 |
| Correctness               |          99% |       99% |       99% |
