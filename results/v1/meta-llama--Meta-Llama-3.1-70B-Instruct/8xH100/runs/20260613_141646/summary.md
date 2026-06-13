# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     438.5s (7.3m) | `4611869` |
| vllm         |   1298.9s (21.6m) | `470229c` |
| sglang       | **200.3s (3.3m)** | `0e59239` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        291.9 |     154.6 | **142.9** |
| TPOT median (ms)          |         96.5 |  **50.7** |      76.7 |
| E2E median (ms)           |        381.1 | **205.7** |     209.9 |
| Throughput median (tok/s) |          3.2 |   **7.2** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        337.2 |     204.7 | **204.7** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        451.4 | **227.5** |     338.3 |
| Throughput median (tok/s) |          2.2 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        699.8 | **172.9** |  172.9 |
| TPOT median (ms)          |         66.6 |  **63.3** |  100.9 |
| E2E median (ms)           |        755.0 | **220.1** |  277.5 |
| Throughput median (tok/s) |          1.9 |   **6.1** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        283.1 | **60.5** |   83.2 |
| TPOT median (ms)          |         61.0 | **28.0** |   45.3 |
| E2E median (ms)           |        325.2 | **82.4** |  145.6 |
| Throughput median (tok/s) |          3.8 | **14.9** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        332.5 |  **65.4** |   70.4 |
| TPOT median (ms)          |         21.6 |  **14.8** |   22.1 |
| E2E median (ms)           |       1160.7 | **596.5** |  813.1 |
| Throughput median (tok/s) |         32.7 |  **60.3** |   42.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        388.9 | **131.6** |  134.8 |
| TPOT median (ms)          |         49.1 |  **31.4** |   49.0 |
| E2E median (ms)           |        614.7 | **266.4** |  356.9 |
| Throughput median (tok/s) |          8.8 |  **18.6** |   13.1 |
| Correctness               |          99% |       99% |    98% |
