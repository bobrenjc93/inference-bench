# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 PM PT, Jun 4 2026

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
| torchinferno |     426.2s (7.1m) | `9910350` |
| vllm         |   1207.2s (20.1m) | `063ce98` |
| sglang       | **167.7s (2.8m)** | `46c58b5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |            - |    170.0 | **149.5** |
| TPOT median (ms)          |            - | **60.7** |      74.2 |
| E2E median (ms)           |            - |    229.7 | **220.0** |
| Throughput median (tok/s) |            - |  **6.3** |       5.4 |
| Correctness               |            - |      98% |       98% |

> **torchinferno error:** `timed out`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     213.4 | **210.0** |
| TPOT median (ms)          |            - |       0.0 |       0.0 |
| E2E median (ms)           |            - | **238.8** |     344.3 |
| Throughput median (tok/s) |            - |   **4.2** |       2.9 |
| Correctness               |            - |      100% |      100% |

> **torchinferno error:** `Connection error.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     177.2 | **167.9** |
| TPOT median (ms)          |            - |  **60.1** |     103.3 |
| E2E median (ms)           |            - | **227.6** |     271.5 |
| Throughput median (tok/s) |            - |   **6.0** |       4.9 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **62.0** |   84.5 |
| TPOT median (ms)          |            - | **28.5** |   45.7 |
| E2E median (ms)           |            - | **84.2** |  146.5 |
| Throughput median (tok/s) |            - | **14.4** |    9.6 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **69.5** |   78.1 |
| TPOT median (ms)          |            - |  **14.8** |   23.3 |
| E2E median (ms)           |            - | **601.3** |  899.2 |
| Throughput median (tok/s) |            - |  **59.6** |   39.8 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     138.4 | **138.0** |
| TPOT median (ms)          |            - |  **32.8** |      49.3 |
| E2E median (ms)           |            - | **276.3** |     376.3 |
| Throughput median (tok/s) |            - |  **18.1** |      12.5 |
| Correctness               |            - |       99% |       99% |
