# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, May 19 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     325.3s (5.4m) | `9f91b40` |
| vllm         |   1161.4s (19.4m) | `be16785` |
| sglang       | **175.0s (2.9m)** | `425dffb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        256.6 |    160.8 | **141.2** |
| TPOT median (ms)          |        153.4 | **58.6** |      80.9 |
| E2E median (ms)           |        360.7 |    215.9 | **213.7** |
| Throughput median (tok/s) |          4.2 |  **6.9** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        262.7 | **201.9** |  204.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        307.0 | **225.5** |  341.3 |
| Throughput median (tok/s) |          3.3 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        530.8 |     171.4 | **169.7** |
| TPOT median (ms)          |        190.3 |  **60.2** |     102.5 |
| E2E median (ms)           |        631.4 | **216.4** |     271.5 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        321.5 | **58.2** |   77.3 |
| TPOT median (ms)          |        132.4 | **26.9** |   55.0 |
| E2E median (ms)           |        416.9 | **79.9** |  147.0 |
| Throughput median (tok/s) |          3.6 | **15.3** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        693.9 |  **66.9** |   67.1 |
| TPOT median (ms)          |         15.4 |  **15.0** |   22.2 |
| E2E median (ms)           |       1228.0 | **597.3** |  824.5 |
| Throughput median (tok/s) |         26.9 |  **59.3** |   42.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        413.1 | **131.8** |  131.9 |
| TPOT median (ms)          |         98.3 |  **32.1** |   52.1 |
| E2E median (ms)           |        588.8 | **267.0** |  359.6 |
| Throughput median (tok/s) |          8.0 |  **18.4** |   13.1 |
| Correctness               |          98% |       99% |    98% |
