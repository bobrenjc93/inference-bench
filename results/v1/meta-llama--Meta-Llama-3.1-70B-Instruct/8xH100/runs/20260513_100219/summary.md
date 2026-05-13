# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:06 AM PT, May 13 2026

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
| torchinferno |     301.8s (5.0m) | `9d5290c` |
| vllm         |    976.3s (16.3m) | `97c4317` |
| sglang       | **164.7s (2.7m)** | `a935970` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        407.4 |    163.2 | **143.2** |
| TPOT median (ms)          |        487.8 | **54.9** |      75.4 |
| E2E median (ms)           |        811.2 |    222.6 | **213.8** |
| Throughput median (tok/s) |          1.7 |  **6.6** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        722.8 | **187.8** |  200.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        753.1 | **226.5** |  337.4 |
| Throughput median (tok/s) |          1.3 |   **4.4** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        616.8 |     178.7 | **154.1** |
| TPOT median (ms)          |        188.8 |  **49.9** |      99.8 |
| E2E median (ms)           |        809.2 | **226.6** |     248.9 |
| Throughput median (tok/s) |          1.6 |   **6.0** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        532.6 | **57.3** |   73.6 |
| TPOT median (ms)          |        481.4 | **27.2** |   51.0 |
| E2E median (ms)           |        891.4 | **77.6** |  142.1 |
| Throughput median (tok/s) |          1.6 | **15.7** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        650.0 |      84.6 | **68.2** |
| TPOT median (ms)          |         31.8 |  **14.8** |     22.1 |
| E2E median (ms)           |       1936.3 | **638.0** |    812.4 |
| Throughput median (tok/s) |         17.8 |  **57.5** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        585.9 |     134.3 | **127.9** |
| TPOT median (ms)          |        238.0 |  **29.4** |      49.7 |
| E2E median (ms)           |       1040.2 | **278.3** |     350.9 |
| Throughput median (tok/s) |          4.8 |  **18.1** |      13.2 |
| Correctness               |          99% |       98% |       99% |
