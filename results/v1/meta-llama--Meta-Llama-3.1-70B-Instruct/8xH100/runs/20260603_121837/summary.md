# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 3 2026

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
| torchinferno |     450.5s (7.5m) | `254f74b` |
| vllm         |   1416.8s (23.6m) | `309385a` |
| sglang       | **230.8s (3.8m)** | `03c77dc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    160.1 | **145.1** |
| TPOT median (ms)          |            - | **62.0** |      71.9 |
| E2E median (ms)           |            - |    223.4 | **213.9** |
| Throughput median (tok/s) |            - |  **6.7** |       5.5 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **221.7** |  222.7 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **278.5** |  376.5 |
| Throughput median (tok/s) |            - |   **3.6** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     181.4 | **159.9** |
| TPOT median (ms)          |            - |  **64.9** |     109.9 |
| E2E median (ms)           |            - | **243.0** |     264.6 |
| Throughput median (tok/s) |            - |   **5.8** |       5.3 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.0** |   80.0 |
| TPOT median (ms)          |            - | **27.9** |   49.9 |
| E2E median (ms)           |            - | **80.6** |  143.1 |
| Throughput median (tok/s) |            - | **15.4** |    9.8 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **74.4** |   78.0 |
| TPOT median (ms)          |            - |  **14.9** |   23.5 |
| E2E median (ms)           |            - | **626.9** |  886.5 |
| Throughput median (tok/s) |            - |  **58.9** |   39.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     139.5 | **137.1** |
| TPOT median (ms)          |            - |  **33.9** |      51.0 |
| E2E median (ms)           |            - | **290.5** |     376.9 |
| Throughput median (tok/s) |            - |  **18.1** |      12.6 |
| Correctness               |            - |       98% |       98% |
