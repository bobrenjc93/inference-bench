# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, May 22 2026

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
| torchinferno |     343.9s (5.7m) | `9f91b40` |
| vllm         |   1326.9s (22.1m) | `7e1b45a` |
| sglang       | **197.5s (3.3m)** | `10751a4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        291.1 |    165.6 | **138.8** |
| TPOT median (ms)          |        155.3 | **58.4** |      73.5 |
| E2E median (ms)           |        390.8 |    223.6 | **205.4** |
| Throughput median (tok/s) |          3.8 |  **6.4** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        272.3 | **183.1** |  205.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        303.2 | **206.9** |  333.2 |
| Throughput median (tok/s) |          3.3 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        698.8 |     167.9 | **151.4** |
| TPOT median (ms)          |        114.4 |  **54.2** |     102.4 |
| E2E median (ms)           |        829.3 | **214.5** |     251.9 |
| Throughput median (tok/s) |          1.5 |   **6.5** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        357.6 | **57.3** |   74.5 |
| TPOT median (ms)          |        131.3 | **26.9** |   54.4 |
| E2E median (ms)           |        460.5 | **78.1** |  135.8 |
| Throughput median (tok/s) |          3.0 | **15.7** |   10.1 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        782.6 |  **66.0** |   70.1 |
| TPOT median (ms)          |         16.0 |  **15.0** |   22.4 |
| E2E median (ms)           |       1388.5 | **597.5** |  821.7 |
| Throughput median (tok/s) |         26.7 |  **59.4** |   42.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        480.5 | **128.0** |  128.1 |
| TPOT median (ms)          |         83.4 |  **30.9** |   50.5 |
| E2E median (ms)           |        674.5 | **264.1** |  349.6 |
| Throughput median (tok/s) |          7.7 |  **18.6** |   13.3 |
| Correctness               |          99% |       98% |    98% |
