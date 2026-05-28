# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 PM PT, May 27 2026

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
| torchinferno |     404.5s (6.7m) | `18b17f4` |
| vllm         |   1252.0s (20.9m) | `c87f62c` |
| sglang       | **159.1s (2.7m)** | `14c1bb2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    181.0 | **146.6** |
| TPOT median (ms)          |            - | **66.5** |      78.3 |
| E2E median (ms)           |            - |    240.7 | **218.2** |
| Throughput median (tok/s) |            - |  **6.1** |       5.3 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `timed out`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **205.3** |  230.8 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **240.6** |  391.1 |
| Throughput median (tok/s) |            - |   **4.2** |    2.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     176.4 | **166.9** |
| TPOT median (ms)          |            - |  **46.1** |     110.9 |
| E2E median (ms)           |            - | **223.0** |     281.4 |
| Throughput median (tok/s) |            - |   **6.1** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **60.5** |   78.8 |
| TPOT median (ms)          |            - | **27.4** |   64.7 |
| E2E median (ms)           |            - | **81.9** |  150.3 |
| Throughput median (tok/s) |            - | **15.1** |    9.5 |
| Correctness               |            - |      97% |    96% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **77.9** |   81.0 |
| TPOT median (ms)          |            - |  **15.1** |   23.8 |
| E2E median (ms)           |            - | **617.6** |  913.5 |
| Throughput median (tok/s) |            - |  **57.9** |   39.0 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **140.2** |  140.8 |
| TPOT median (ms)          |            - |  **31.0** |   55.5 |
| E2E median (ms)           |            - | **280.7** |  390.9 |
| Throughput median (tok/s) |            - |  **17.9** |   12.2 |
| Correctness               |            - |       99% |    98% |
