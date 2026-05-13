# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:08 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     318.7s (5.3m) | `9d5290c` |
| vllm         |    978.8s (16.3m) | `18f6bf5` |
| sglang       | **158.4s (2.6m)** | `409d350` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        413.3 |    162.0 | **131.8** |
| TPOT median (ms)          |        480.8 | **60.4** |      74.4 |
| E2E median (ms)           |        814.6 |    224.6 | **199.3** |
| Throughput median (tok/s) |          1.7 |  **6.5** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        740.0 | **191.3** |      - |
| TPOT median (ms)          |          0.0 |       0.0 |      - |
| E2E median (ms)           |        770.1 | **221.4** |      - |
| Throughput median (tok/s) |          1.3 |   **4.5** |      - |
| Correctness               |         100% |      100% |      - |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        635.8 | **170.5** |      - |
| TPOT median (ms)          |        209.8 |  **57.7** |      - |
| E2E median (ms)           |        814.1 | **216.3** |      - |
| Throughput median (tok/s) |          1.6 |   **6.3** |      - |
| Correctness               |          98% |       98% |      - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        462.2 | **58.3** |      - |
| TPOT median (ms)          |        493.8 | **27.5** |      - |
| E2E median (ms)           |        865.3 | **78.6** |      - |
| Throughput median (tok/s) |          1.6 | **15.5** |      - |
| Correctness               |          97% |      97% |      - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        625.7 |  **74.1** |      - |
| TPOT median (ms)          |         31.4 |  **14.9** |      - |
| E2E median (ms)           |       2015.8 | **614.3** |      - |
| Throughput median (tok/s) |         18.3 |  **58.4** |      - |
| Correctness               |         100% |      100% |      - |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        575.4 | **131.3** |     131.8 |
| TPOT median (ms)          |        243.2 |  **32.1** |      74.4 |
| E2E median (ms)           |       1056.0 |     271.0 | **199.3** |
| Throughput median (tok/s) |          4.9 |  **18.3** |       6.1 |
| Correctness               |          99% |       99% |       98% |
