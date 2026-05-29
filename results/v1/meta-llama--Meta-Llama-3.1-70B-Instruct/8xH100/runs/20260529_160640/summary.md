# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 AM PT, May 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         3/20 | **12/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     311.1s (5.2m) | `b619d24` |
| vllm         |   1295.4s (21.6m) | `4ff865c` |
| sglang       | **192.9s (3.2m)** | `ec075d8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        261.7 |    163.1 | **146.0** |
| TPOT median (ms)          |         69.0 | **57.9** |      73.8 |
| E2E median (ms)           |        330.5 |    218.7 | **218.3** |
| Throughput median (tok/s) |          3.7 |  **6.8** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        291.8 |     206.7 | **205.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        332.2 | **233.4** |     336.0 |
| Throughput median (tok/s) |          3.0 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        705.2 |     171.6 | **166.2** |
| TPOT median (ms)          |     **57.4** |      60.6 |      94.3 |
| E2E median (ms)           |        754.9 | **226.2** |     266.1 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        170.7 | **59.8** |   82.6 |
| TPOT median (ms)          |     **28.8** |     29.0 |   39.2 |
| E2E median (ms)           |        194.7 | **80.9** |  130.4 |
| Throughput median (tok/s) |          6.6 | **15.1** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        634.3 |  **71.1** |   76.1 |
| TPOT median (ms)          |     **14.9** |      15.1 |   23.2 |
| E2E median (ms)           |       1218.4 | **631.4** |  872.9 |
| Throughput median (tok/s) |         26.4 |  **58.4** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        412.7 | **134.4** |  135.4 |
| TPOT median (ms)          |         34.0 |  **32.5** |   46.1 |
| E2E median (ms)           |        566.1 | **278.1** |  364.7 |
| Throughput median (tok/s) |          8.4 |  **18.2** |   12.8 |
| Correctness               |          99% |       99% |    99% |
