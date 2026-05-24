# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:03 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     317.0s (5.3m) | `9f91b40` |
| vllm         |   1138.8s (19.0m) | `d0a100c` |
| sglang       | **165.4s (2.8m)** | `44922de` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.4 |     162.6 | **140.4** |
| TPOT median (ms)          |        152.1 |  **56.3** |      76.6 |
| E2E median (ms)           |        379.8 | **212.0** |     213.4 |
| Throughput median (tok/s) |          4.0 |   **6.8** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        275.9 |     207.3 | **200.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        297.1 | **253.8** |     336.5 |
| Throughput median (tok/s) |          3.4 |   **3.9** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |            - |     165.4 | **161.0** |
| TPOT median (ms)          |            - |  **50.9** |     108.0 |
| E2E median (ms)           |            - | **205.9** |     263.4 |
| Throughput median (tok/s) |            - |   **6.6** |       5.1 |
| Correctness               |            - |       98% |       98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **57.6** |   79.4 |
| TPOT median (ms)          |            - | **27.1** |   58.9 |
| E2E median (ms)           |            - | **78.1** |  146.3 |
| Throughput median (tok/s) |            - | **15.7** |    9.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **66.6** |   67.8 |
| TPOT median (ms)          |            - |  **15.0** |   22.1 |
| E2E median (ms)           |            - | **607.8** |  802.4 |
| Throughput median (tok/s) |            - |  **59.7** |   42.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        281.7 |     131.9 | **129.8** |
| TPOT median (ms)          |         76.0 |  **29.9** |      53.1 |
| E2E median (ms)           |        338.4 | **271.5** |     352.4 |
| Throughput median (tok/s) |          3.7 |  **18.5** |      13.1 |
| Correctness               |          99% |       98% |       99% |
