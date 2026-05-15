# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:08 AM PT, May 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     410.4s (6.8m) | `d648af4` |
| vllm         |   1118.1s (18.6m) | `ee58665` |
| sglang       | **174.1s (2.9m)** | `3f7e538` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        297.4 |    156.8 | **139.3** |
| TPOT median (ms)          |        156.9 | **57.8** |      74.9 |
| E2E median (ms)           |        392.2 |    209.0 | **206.5** |
| Throughput median (tok/s) |          3.7 |  **7.1** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        293.7 | **191.0** |  212.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        333.0 | **213.3** |  351.5 |
| Throughput median (tok/s) |          3.0 |   **4.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        555.7 |     174.5 | **159.2** |
| TPOT median (ms)          |        109.1 |  **65.7** |     104.7 |
| E2E median (ms)           |        643.2 | **232.4** |     259.1 |
| Throughput median (tok/s) |          2.0 |   **6.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        348.7 | **57.7** |   77.0 |
| TPOT median (ms)          |        131.9 | **27.6** |   58.7 |
| E2E median (ms)           |        447.2 | **78.6** |  150.5 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        507.1 |      67.1 | **66.7** |
| TPOT median (ms)          |         15.3 |  **15.0** |     22.2 |
| E2E median (ms)           |       1185.7 | **603.6** |    827.7 |
| Throughput median (tok/s) |         27.4 |  **59.2** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        400.5 | **129.4** |  130.9 |
| TPOT median (ms)          |         82.6 |  **33.2** |   52.1 |
| E2E median (ms)           |        600.2 | **267.4** |  359.0 |
| Throughput median (tok/s) |          7.8 |  **18.6** |   13.1 |
| Correctness               |          98% |       98% |    99% |
