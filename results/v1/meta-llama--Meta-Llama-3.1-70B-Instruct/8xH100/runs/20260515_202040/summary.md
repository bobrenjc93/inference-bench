# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:11 PM PT, May 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     356.0s (5.9m) | `33730f7` |
| vllm         |   1034.7s (17.2m) | `b2c58ee` |
| sglang       | **164.7s (2.7m)** | `54221dd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        288.3 |    160.0 | **137.8** |
| TPOT median (ms)          |        149.6 | **56.8** |      70.7 |
| E2E median (ms)           |        372.3 |    212.6 | **203.6** |
| Throughput median (tok/s) |          4.0 |  **6.8** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.1 |     198.4 | **198.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        325.4 | **221.2** |     332.4 |
| Throughput median (tok/s) |          3.1 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        528.8 |     172.8 | **161.4** |
| TPOT median (ms)          |        194.1 |  **51.9** |      96.5 |
| E2E median (ms)           |        631.1 | **220.8** |     261.0 |
| Throughput median (tok/s) |          2.1 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        338.4 | **58.4** |   75.9 |
| TPOT median (ms)          |        133.1 | **27.4** |   59.2 |
| E2E median (ms)           |        439.5 | **79.5** |  156.8 |
| Throughput median (tok/s) |          3.1 | **15.5** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      67.4 | **65.3** |
| TPOT median (ms)          |            - |  **15.0** |     22.0 |
| E2E median (ms)           |            - | **602.9** |    794.3 |
| Throughput median (tok/s) |            - |  **59.9** |     42.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        360.7 |     131.4 | **127.7** |
| TPOT median (ms)          |        119.2 |  **30.2** |      49.7 |
| E2E median (ms)           |        442.1 | **267.4** |     349.6 |
| Throughput median (tok/s) |          3.1 |  **18.6** |      13.3 |
| Correctness               |          98% |       99% |       99% |
