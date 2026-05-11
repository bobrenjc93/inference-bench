# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **4/5** |    1/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **3/5** |    1/5 |          1/5 |
| tree_of_thought  |   **4/5** |    1/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **20/25** |   4/25 |         1/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1016.3s (16.9m) | `27ae676` |
| sglang       |    287.2s (4.8m) | `6b6963f` |
| torchinferno | **81.0s (1.4m)** | `22960e6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     164.8 | **151.0** |        438.9 |
| TPOT median (ms)          |  **62.0** |      73.4 |        406.3 |
| E2E median (ms)           | **221.2** |     224.1 |        839.9 |
| Throughput median (tok/s) |   **6.9** |       5.3 |          1.5 |
| Correctness               |   **98%** |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **163.8** |  231.0 |        427.3 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **203.0** |  380.1 |        547.6 |
| Throughput median (tok/s) |   **4.9** |    2.6 |          1.8 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     181.4 | **166.0** |       1267.6 |
| TPOT median (ms)          |  **60.1** |     116.8 |        351.1 |
| E2E median (ms)           | **231.1** |     273.2 |       1544.9 |
| Throughput median (tok/s) |   **6.0** |       4.9 |          0.8 |
| Correctness               |       98% |       98% |      **98%** |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **62.1** |    80.7 |            - |
| TPOT median (ms)          | **27.1** |    64.2 |            - |
| E2E median (ms)           | **83.3** |   152.3 |            - |
| Throughput median (tok/s) | **14.9** |     9.2 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      76.8 | **75.7** |            - |
| TPOT median (ms)          |  **15.0** |     22.1 |            - |
| E2E median (ms)           | **621.0** |    819.5 |            - |
| Throughput median (tok/s) |  **58.2** |     42.1 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **129.8** |  140.9 |        711.3 |
| TPOT median (ms)          |  **32.9** |   55.3 |        252.4 |
| E2E median (ms)           | **271.9** |  369.8 |        977.5 |
| Throughput median (tok/s) |  **18.2** |   12.8 |          1.4 |
| Correctness               |       99% |    99% |      **99%** |
