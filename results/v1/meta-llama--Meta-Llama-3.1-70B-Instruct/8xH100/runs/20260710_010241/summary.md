# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **39.6s (0.7m)** | `75387c9` |
| vllm         |    202.6s (3.4m) | `feb384a` |
| sglang       |    255.6s (4.3m) | `073b368` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        147.3 | **125.2** |  136.0 |
| TPOT median (ms)          |     **42.6** |      45.4 |   81.8 |
| E2E median (ms)           |        187.0 | **163.6** |  214.8 |
| Throughput median (tok/s) |          6.5 |   **8.6** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        145.2 | **106.9** |  207.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        155.5 | **129.4** |  352.1 |
| Throughput median (tok/s) |          6.4 |   **7.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     166.8 | **164.5** |
| TPOT median (ms)          |            - |  **51.2** |     118.6 |
| E2E median (ms)           |            - | **214.7** |     291.7 |
| Throughput median (tok/s) |            - |   **6.4** |       4.4 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **33.0** |   50.5 |
| TPOT median (ms)          |            - | **22.1** |  407.0 |
| E2E median (ms)           |            - | **49.6** |  472.9 |
| Throughput median (tok/s) |            - | **25.6** |    3.0 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      79.5 | **66.9** |
| TPOT median (ms)          |            - |  **14.7** |     22.7 |
| E2E median (ms)           |            - | **610.2** |    899.7 |
| Throughput median (tok/s) |            - |  **58.7** |     41.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        146.3 | **102.3** |  125.1 |
| TPOT median (ms)          |     **21.3** |      26.7 |  126.0 |
| E2E median (ms)           |    **171.2** |     233.5 |  446.2 |
| Throughput median (tok/s) |          6.5 |  **21.4** |   11.4 |
| Correctness               |          99% |       99% |    99% |
