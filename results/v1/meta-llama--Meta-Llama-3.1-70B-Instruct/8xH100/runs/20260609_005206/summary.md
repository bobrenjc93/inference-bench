# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:37 PM PT, Jun 8 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     317.9s (5.3m) | `a80b89c` |
| vllm         |   1359.8s (22.7m) | `05cb606` |
| sglang       | **194.9s (3.2m)** | `317fc6a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     160.3 | **147.2** |
| TPOT median (ms)          |            - |  **59.7** |      74.1 |
| E2E median (ms)           |            - | **214.7** |     217.6 |
| Throughput median (tok/s) |            - |   **6.9** |       5.4 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **208.7** |  210.2 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **232.9** |  344.0 |
| Throughput median (tok/s) |            - |   **4.3** |    2.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     184.3 | **161.6** |
| TPOT median (ms)          |            - |  **67.2** |      96.5 |
| E2E median (ms)           |            - | **240.2** |     264.6 |
| Throughput median (tok/s) |            - |   **5.8** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **61.2** |   79.8 |
| TPOT median (ms)          |            - | **27.8** |   67.7 |
| E2E median (ms)           |            - | **82.5** |  164.2 |
| Throughput median (tok/s) |            - | **14.5** |    8.9 |
| Correctness               |            - |      97% |    96% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **72.0** |   80.7 |
| TPOT median (ms)          |            - |  **14.8** |   23.0 |
| E2E median (ms)           |            - | **610.7** |  891.4 |
| Throughput median (tok/s) |            - |  **59.1** |   40.2 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     137.3 | **135.9** |
| TPOT median (ms)          |            - |  **33.9** |      52.3 |
| E2E median (ms)           |            - | **276.2** |     376.4 |
| Throughput median (tok/s) |            - |  **18.1** |      12.5 |
| Correctness               |            - |       98% |       98% |
