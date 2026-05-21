# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:03 PM PT, May 20 2026

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
| torchinferno |     313.7s (5.2m) | `9f91b40` |
| vllm         |   1101.1s (18.4m) | `9640970` |
| sglang       | **176.7s (2.9m)** | `791a2f0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        271.1 |    159.6 | **136.1** |
| TPOT median (ms)          |        148.5 | **61.3** |      77.7 |
| E2E median (ms)           |        367.3 |    217.5 | **206.3** |
| Throughput median (tok/s) |          4.1 |  **7.2** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        275.5 | **187.9** |  204.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        299.7 | **211.0** |  336.4 |
| Throughput median (tok/s) |          3.3 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        803.1 |     171.5 | **157.0** |
| TPOT median (ms)          |        151.1 |  **42.3** |     106.2 |
| E2E median (ms)           |        901.8 | **210.8** |     259.2 |
| Throughput median (tok/s) |          1.5 |   **6.5** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        326.8 | **57.5** |   74.7 |
| TPOT median (ms)          |        127.9 | **26.7** |   65.5 |
| E2E median (ms)           |        414.0 | **78.2** |  154.4 |
| Throughput median (tok/s) |          3.5 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.2 | **67.1** |
| TPOT median (ms)          |            - |  **15.1** |     22.3 |
| E2E median (ms)           |            - | **623.3** |    846.7 |
| Throughput median (tok/s) |            - |  **58.6** |     42.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        419.1 |     130.6 | **127.9** |
| TPOT median (ms)          |        106.9 |  **29.1** |      54.3 |
| E2E median (ms)           |        495.7 | **268.2** |     360.6 |
| Throughput median (tok/s) |          3.1 |  **18.5** |      13.1 |
| Correctness               |          98% |       99% |       98% |
