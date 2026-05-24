# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     405.4s (6.8m) | `9f91b40` |
| vllm         |   1143.8s (19.1m) | `0902d8e` |
| sglang       | **177.8s (3.0m)** | `4c2b32b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        325.9 |    162.7 | **139.4** |
| TPOT median (ms)          |        151.4 | **60.7** |      75.0 |
| E2E median (ms)           |        448.0 |    215.2 | **210.3** |
| Throughput median (tok/s) |          2.9 |  **6.8** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.5 | **192.2** |  202.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        319.1 | **212.9** |  335.3 |
| Throughput median (tok/s) |          3.1 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        841.3 |     170.7 | **158.0** |
| TPOT median (ms)          |        141.6 |  **62.7** |     107.9 |
| E2E median (ms)           |        946.7 | **226.7** |     263.6 |
| Throughput median (tok/s) |          1.4 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        345.3 | **57.6** |   77.4 |
| TPOT median (ms)          |        129.8 | **27.4** |   59.7 |
| E2E median (ms)           |        444.2 | **77.6** |  150.7 |
| Throughput median (tok/s) |          2.9 | **15.7** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      70.0 | **68.1** |
| TPOT median (ms)          |            - |  **15.1** |     22.1 |
| E2E median (ms)           |            - | **611.5** |    825.8 |
| Throughput median (tok/s) |            - |  **58.6** |     42.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        450.7 |     130.6 | **129.0** |
| TPOT median (ms)          |        105.7 |  **33.2** |      52.9 |
| E2E median (ms)           |        539.5 | **268.8** |     357.1 |
| Throughput median (tok/s) |          2.6 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       99% |
