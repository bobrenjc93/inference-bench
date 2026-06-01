# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 PM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     365.1s (6.1m) | `69b6447` |
| vllm         |   1295.3s (21.6m) | `8b8546d` |
| sglang       | **193.6s (3.2m)** | `4b0453f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        259.8 |     150.2 | **143.4** |
| TPOT median (ms)          |     **45.6** |      54.2 |      72.3 |
| E2E median (ms)           |        311.7 | **205.9** |     209.4 |
| Throughput median (tok/s) |          4.1 |   **7.3** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        557.7 | **191.0** |  209.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        653.2 | **213.6** |  347.3 |
| Throughput median (tok/s) |          1.5 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        812.6 |     171.0 | **156.7** |
| TPOT median (ms)          |        113.4 |  **62.9** |      97.2 |
| E2E median (ms)           |        877.5 | **229.8** |     253.3 |
| Throughput median (tok/s) |          1.3 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        408.0 | **57.4** |   78.6 |
| TPOT median (ms)          |         29.9 | **28.2** |   42.1 |
| E2E median (ms)           |        441.7 | **78.3** |  129.6 |
| Throughput median (tok/s) |          2.8 | **15.6** |   10.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        428.0 |  **75.1** |   76.0 |
| TPOT median (ms)          |         22.4 |  **15.0** |   23.2 |
| E2E median (ms)           |       1612.6 | **611.6** |  851.3 |
| Throughput median (tok/s) |         15.9 |  **58.6** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        493.2 | **128.9** |  132.8 |
| TPOT median (ms)          |         42.3 |  **32.1** |   46.9 |
| E2E median (ms)           |        779.4 | **267.9** |  358.2 |
| Throughput median (tok/s) |          5.1 |  **18.5** |   13.0 |
| Correctness               |          98% |       98% |    98% |
