# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          1/4 |   **2/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         2/20 | **14/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     360.4s (6.0m) | `1b6207c` |
| vllm         |   1367.5s (22.8m) | `15652a6` |
| sglang       | **208.4s (3.5m)** | `eab2e02` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        391.5 |   163.0 | **147.5** |
| TPOT median (ms)          |     **51.6** |    55.5 |      72.1 |
| E2E median (ms)           |        451.3 |   215.8 | **213.4** |
| Throughput median (tok/s) |          3.1 | **6.9** |       5.5 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        283.7 | **195.5** |  210.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        391.9 | **221.9** |  343.1 |
| Throughput median (tok/s) |          2.6 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        866.0 |     175.2 | **166.8** |
| TPOT median (ms)          |     **59.8** |      59.9 |      96.2 |
| E2E median (ms)           |        923.7 | **225.5** |     267.3 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        505.2 | **61.4** |   77.1 |
| TPOT median (ms)          |         33.4 | **27.8** |   61.2 |
| E2E median (ms)           |        543.5 | **82.9** |  146.0 |
| Throughput median (tok/s) |          2.6 | **14.4** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        581.7 |  **66.0** |   76.0 |
| TPOT median (ms)          |         33.0 |  **15.2** |   23.2 |
| E2E median (ms)           |       1704.9 | **612.2** |  868.2 |
| Throughput median (tok/s) |         20.2 |  **58.9** |   40.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        525.6 | **132.2** |  135.5 |
| TPOT median (ms)          |         35.5 |  **31.7** |   50.6 |
| E2E median (ms)           |        803.1 | **271.7** |  367.6 |
| Throughput median (tok/s) |          6.0 |  **18.2** |   12.6 |
| Correctness               |          99% |       99% |    99% |
