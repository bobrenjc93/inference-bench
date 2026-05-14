# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:07 AM PT, May 14 2026

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
| torchinferno |     350.0s (5.8m) | `1824bbb` |
| vllm         |   1095.1s (18.3m) | `addef32` |
| sglang       | **161.0s (2.7m)** | `2279b79` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        266.3 |    155.8 | **134.5** |
| TPOT median (ms)          |        168.6 | **56.9** |      76.7 |
| E2E median (ms)           |        397.1 |    211.5 | **203.3** |
| Throughput median (tok/s) |          3.7 |  **7.1** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        292.4 |     216.2 | **198.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        327.4 | **294.7** |     327.7 |
| Throughput median (tok/s) |          3.1 |   **3.4** |       3.1 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        656.2 |     167.7 | **154.1** |
| TPOT median (ms)          |        206.8 |  **53.2** |     105.3 |
| E2E median (ms)           |        800.2 | **214.1** |     250.6 |
| Throughput median (tok/s) |          1.7 |   **6.5** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        389.8 | **58.0** |   76.8 |
| TPOT median (ms)          |        246.5 | **27.4** |   57.4 |
| E2E median (ms)           |        583.9 | **78.0** |  143.7 |
| Throughput median (tok/s) |          2.3 | **15.6** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        611.2 |      73.2 | **66.2** |
| TPOT median (ms)          |         23.8 |  **14.9** |     22.2 |
| E2E median (ms)           |       1798.8 | **619.4** |    841.3 |
| Throughput median (tok/s) |         19.4 |  **58.3** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        443.2 |     134.2 | **126.1** |
| TPOT median (ms)          |        129.1 |  **30.5** |      52.3 |
| E2E median (ms)           |        781.5 | **283.5** |     353.3 |
| Throughput median (tok/s) |          6.0 |  **18.2** |      13.4 |
| Correctness               |          99% |       99% |       99% |
