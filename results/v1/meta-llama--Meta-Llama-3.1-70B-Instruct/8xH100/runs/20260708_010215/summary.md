# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.5s (0.7m)** | `4892cad` |
| vllm         |    192.7s (3.2m) | `f7fc0ca` |
| sglang       |    174.1s (2.9m) | `9bf122a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **122.2** |  135.1 |
| TPOT median (ms)          |            - |  **45.2** |   80.9 |
| E2E median (ms)           |            - | **157.8** |  214.5 |
| Throughput median (tok/s) |            - |   **8.6** |    5.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **126.4** |  208.6 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **148.8** |  356.9 |
| Throughput median (tok/s) |            - |   **6.7** |    2.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **150.2** |  164.6 |
| TPOT median (ms)          |            - |  **43.7** |  102.1 |
| E2E median (ms)           |            - | **196.6** |  276.9 |
| Throughput median (tok/s) |            - |   **6.9** |    4.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.6** |   47.8 |
| TPOT median (ms)          |            - | **21.7** |  391.8 |
| E2E median (ms)           |            - | **47.9** |  422.3 |
| Throughput median (tok/s) |            - | **25.7** |    3.4 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      78.6 | **71.6** |
| TPOT median (ms)          |            - |  **14.8** |     22.1 |
| E2E median (ms)           |            - | **616.0** |    927.8 |
| Throughput median (tok/s) |            - |  **58.6** |     41.0 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **102.0** |  125.5 |
| TPOT median (ms)          |            - |  **25.1** |  119.4 |
| E2E median (ms)           |            - | **233.4** |  439.7 |
| Throughput median (tok/s) |            - |  **21.3** |   11.5 |
| Correctness               |            - |       99% |    98% |
