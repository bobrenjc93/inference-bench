# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          1/4 |   **2/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     353.8s (5.9m) | `9f91b40` |
| vllm         |   1285.4s (21.4m) | `3f3e862` |
| sglang       | **215.8s (3.6m)** | `81cd338` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        269.3 |    166.8 | **144.3** |
| TPOT median (ms)          |        152.7 | **59.6** |      75.0 |
| E2E median (ms)           |        362.7 |    223.6 | **217.8** |
| Throughput median (tok/s) |          4.1 |  **6.3** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |    **178.5** |     188.1 |  209.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        302.0 | **250.3** |  350.9 |
| Throughput median (tok/s) |          3.3 |   **4.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        760.6 |     163.6 | **159.1** |
| TPOT median (ms)          |        116.3 |  **55.0** |     106.3 |
| E2E median (ms)           |        874.6 | **209.8** |     263.2 |
| Throughput median (tok/s) |          1.5 |   **6.5** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        366.3 | **57.5** |   78.1 |
| TPOT median (ms)          |        130.8 | **26.7** |   59.7 |
| E2E median (ms)           |        468.8 | **78.1** |  148.5 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.4 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        822.5 |  **66.2** |   68.6 |
| TPOT median (ms)          |         15.7 |  **15.1** |   23.1 |
| E2E median (ms)           |       1521.6 | **606.0** |  881.5 |
| Throughput median (tok/s) |         25.9 |  **59.4** |   40.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        479.5 | **128.4** |  132.0 |
| TPOT median (ms)          |         83.1 |  **31.3** |   52.8 |
| E2E median (ms)           |        705.9 | **273.6** |  372.4 |
| Throughput median (tok/s) |          7.6 |  **18.4** |   12.7 |
| Correctness               |          98% |       99% |    98% |
