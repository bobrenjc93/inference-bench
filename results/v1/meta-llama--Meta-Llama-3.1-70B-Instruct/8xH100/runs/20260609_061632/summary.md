# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 PM PT, Jun 8 2026

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
| torchinferno |     333.6s (5.6m) | `a80b89c` |
| vllm         |   1367.0s (22.8m) | `ebf53ba` |
| sglang       | **213.4s (3.6m)** | `dff695c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    163.3 | **150.2** |
| TPOT median (ms)          |            - | **59.6** |      72.9 |
| E2E median (ms)           |            - |    220.2 | **219.1** |
| Throughput median (tok/s) |            - |  **6.9** |       5.4 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **204.3** |  204.7 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **228.8** |  338.9 |
| Throughput median (tok/s) |            - |   **4.4** |    3.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     182.7 | **166.4** |
| TPOT median (ms)          |            - |  **70.4** |      96.4 |
| E2E median (ms)           |            - | **249.5** |     267.9 |
| Throughput median (tok/s) |            - |   **5.9** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.2** |   83.3 |
| TPOT median (ms)          |            - | **28.2** |   46.9 |
| E2E median (ms)           |            - | **82.2** |  142.9 |
| Throughput median (tok/s) |            - | **14.7** |    9.6 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **69.9** |   79.0 |
| TPOT median (ms)          |            - |  **14.8** |   23.3 |
| E2E median (ms)           |            - | **599.4** |  883.4 |
| Throughput median (tok/s) |            - |  **59.9** |   40.3 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **136.1** |  136.7 |
| TPOT median (ms)          |            - |  **34.6** |   47.9 |
| E2E median (ms)           |            - | **276.0** |  370.5 |
| Throughput median (tok/s) |            - |  **18.3** |   12.6 |
| Correctness               |            - |       98% |    99% |
