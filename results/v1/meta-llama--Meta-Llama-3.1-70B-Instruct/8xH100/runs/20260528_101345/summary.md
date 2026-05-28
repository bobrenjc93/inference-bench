# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, May 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     390.0s (6.5m) | `f4c65f7` |
| vllm         |   1363.7s (22.7m) | `a04afd7` |
| sglang       | **203.7s (3.4m)** | `f143d54` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        259.0 |    162.9 | **149.6** |
| TPOT median (ms)          |         65.1 | **57.3** |      69.5 |
| E2E median (ms)           |        319.9 |    219.2 | **215.7** |
| Throughput median (tok/s) |          4.1 |  **6.6** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        270.8 | **196.3** |  210.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        311.1 | **221.6** |  346.3 |
| Throughput median (tok/s) |          3.2 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        759.5 |     173.3 | **163.8** |
| TPOT median (ms)          |     **56.2** |      57.4 |      98.3 |
| E2E median (ms)           |        808.4 | **223.8** |     265.2 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        198.3 | **57.2** |   77.7 |
| TPOT median (ms)          |         29.0 | **27.4** |   45.7 |
| E2E median (ms)           |        236.9 | **77.1** |  133.0 |
| Throughput median (tok/s) |          5.7 | **15.8** |   10.4 |
| Correctness               |          96% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        549.7 |  **68.6** |   77.8 |
| TPOT median (ms)          |     **14.7** |      15.0 |   23.9 |
| E2E median (ms)           |       1259.7 | **607.2** |  927.1 |
| Throughput median (tok/s) |         27.8 |  **59.1** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        407.4 | **131.7** |  135.8 |
| TPOT median (ms)          |         33.0 |  **31.4** |   47.5 |
| E2E median (ms)           |        587.2 | **269.8** |  377.5 |
| Throughput median (tok/s) |          8.5 |  **18.4** |   12.6 |
| Correctness               |          98% |       98% |    98% |
