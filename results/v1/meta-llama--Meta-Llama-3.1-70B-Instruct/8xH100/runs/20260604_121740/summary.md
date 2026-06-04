# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, Jun 4 2026

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
| torchinferno |     405.1s (6.8m) | `a9e2f5a` |
| vllm         |   1395.3s (23.3m) | `4b87b3e` |
| sglang       | **216.7s (3.6m)** | `8933ec8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        426.1 |     161.8 | **152.7** |
| TPOT median (ms)          |     **56.1** |      60.5 |      80.8 |
| E2E median (ms)           |        478.6 | **215.6** |     228.2 |
| Throughput median (tok/s) |          3.1 |   **7.0** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.8 | **204.8** |  211.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        393.9 | **238.0** |  349.2 |
| Throughput median (tok/s) |          2.5 |   **4.2** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        803.2 |     182.9 | **161.9** |
| TPOT median (ms)          |        123.0 |  **64.1** |      98.4 |
| E2E median (ms)           |        931.5 | **232.2** |     264.7 |
| Throughput median (tok/s) |          1.4 |   **5.9** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        329.0 | **60.4** |   78.1 |
| TPOT median (ms)          |         32.6 | **27.9** |   43.0 |
| E2E median (ms)           |        357.8 | **82.4** |  132.7 |
| Throughput median (tok/s) |          3.9 | **14.7** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        481.8 |  **73.0** |   78.5 |
| TPOT median (ms)          |         28.0 |  **14.9** |   22.7 |
| E2E median (ms)           |       1487.6 | **615.0** |  889.8 |
| Throughput median (tok/s) |         24.0 |  **58.6** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        466.6 |     136.6 | **136.5** |
| TPOT median (ms)          |         47.9 |  **33.5** |      49.0 |
| E2E median (ms)           |        729.9 | **276.6** |     372.9 |
| Throughput median (tok/s) |          7.0 |  **18.1** |      12.8 |
| Correctness               |          98% |       98% |       98% |
