# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:08 AM PT, Jun 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     412.1s (6.9m) | `065275c` |
| vllm         |   1407.3s (23.5m) | `d6fd7ce` |
| sglang       | **230.1s (3.8m)** | `75998d0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    170.9 | **141.6** |
| TPOT median (ms)          |            - | **56.9** |      75.0 |
| E2E median (ms)           |            - |    228.2 | **209.9** |
| Throughput median (tok/s) |            - |  **6.6** |       5.7 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     206.6 | **205.8** |
| TPOT median (ms)          |            - |       0.0 |       0.0 |
| E2E median (ms)           |            - | **228.8** |     345.3 |
| Throughput median (tok/s) |            - |   **4.4** |       2.9 |
| Correctness               |            - |      100% |      100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     173.9 | **168.4** |
| TPOT median (ms)          |            - |  **64.5** |     103.5 |
| E2E median (ms)           |            - | **228.6** |     267.0 |
| Throughput median (tok/s) |            - |   **6.2** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **64.9** |   82.5 |
| TPOT median (ms)          |            - | **30.2** |   52.9 |
| E2E median (ms)           |            - | **87.4** |  141.4 |
| Throughput median (tok/s) |            - | **13.8** |    9.7 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **71.9** |   79.4 |
| TPOT median (ms)          |            - |  **14.9** |   23.8 |
| E2E median (ms)           |            - | **610.0** |  872.2 |
| Throughput median (tok/s) |            - |  **58.6** |   39.4 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[torchinferno] Server did not become ready within 1800s`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     137.6 | **135.5** |
| TPOT median (ms)          |            - |  **33.3** |      51.0 |
| E2E median (ms)           |            - | **276.6** |     367.1 |
| Throughput median (tok/s) |            - |  **17.9** |      12.5 |
| Correctness               |            - |       99% |       99% |
