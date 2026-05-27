# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:02 AM PT, May 27 2026

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
| torchinferno |     372.9s (6.2m) | `89c74c2` |
| vllm         |   1299.9s (21.7m) | `52a31cc` |
| sglang       | **161.8s (2.7m)** | `a95b4e2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    171.2 | **152.6** |
| TPOT median (ms)          |            - | **63.9** |      75.9 |
| E2E median (ms)           |            - |    233.2 | **219.0** |
| Throughput median (tok/s) |            - |  **6.6** |       5.6 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `timed out`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     202.0 | **193.4** |
| TPOT median (ms)          |            - |       0.0 |       0.0 |
| E2E median (ms)           |            - | **224.4** |     329.9 |
| Throughput median (tok/s) |            - |   **4.5** |       3.0 |
| Correctness               |            - |      100% |      100% |

> **torchinferno error:** `Connection error.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     176.8 | **162.9** |
| TPOT median (ms)          |            - |  **60.7** |     111.7 |
| E2E median (ms)           |            - | **228.0** |     265.2 |
| Throughput median (tok/s) |            - |   **6.3** |       5.0 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **59.8** |   84.3 |
| TPOT median (ms)          |            - | **26.6** |   43.8 |
| E2E median (ms)           |            - | **81.1** |  146.2 |
| Throughput median (tok/s) |            - | **15.4** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **71.1** |   75.9 |
| TPOT median (ms)          |            - |  **15.0** |   23.7 |
| E2E median (ms)           |            - | **614.3** |  887.9 |
| Throughput median (tok/s) |            - |  **58.5** |   39.3 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     136.2 | **133.8** |
| TPOT median (ms)          |            - |  **33.3** |      51.0 |
| E2E median (ms)           |            - | **276.2** |     369.7 |
| Throughput median (tok/s) |            - |  **18.2** |      12.5 |
| Correctness               |            - |       99% |       98% |
