# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 PM PT, Jun 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     386.0s (6.4m) | `d5e2f1e` |
| vllm         |   1201.5s (20.0m) | `da1daf4` |
| sglang       | **181.3s (3.0m)** | `aed0808` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     166.0 | **164.6** |
| TPOT median (ms)          |            - |  **63.5** |      70.0 |
| E2E median (ms)           |            - | **224.1** |     234.0 |
| Throughput median (tok/s) |            - |   **6.6** |       5.1 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `timed out`

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **197.5** |  227.1 |
| TPOT median (ms)          |            - |       0.0 |    0.0 |
| E2E median (ms)           |            - | **221.1** |  365.3 |
| Throughput median (tok/s) |            - |   **4.5** |    2.7 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `Connection error.`

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     168.3 | **159.0** |
| TPOT median (ms)          |            - |  **55.1** |     103.5 |
| E2E median (ms)           |            - | **213.9** |     257.3 |
| Throughput median (tok/s) |            - |   **6.2** |       5.2 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `Connection error.`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **65.0** |   79.7 |
| TPOT median (ms)          |            - | **29.1** |   55.0 |
| E2E median (ms)           |            - | **88.3** |  142.4 |
| Throughput median (tok/s) |            - | **14.0** |    9.6 |
| Correctness               |            - |      96% |    97% |

> **torchinferno error:** `Connection error.`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      81.2 | **78.0** |
| TPOT median (ms)          |            - |  **14.9** |     23.1 |
| E2E median (ms)           |            - | **609.5** |    862.3 |
| Throughput median (tok/s) |            - |  **58.3** |     40.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `Connection error.`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **135.6** |  141.7 |
| TPOT median (ms)          |            - |  **32.5** |   50.3 |
| E2E median (ms)           |            - | **271.4** |  372.3 |
| Throughput median (tok/s) |            - |  **17.9** |   12.6 |
| Correctness               |            - |       98% |    99% |
