# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:09 PM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     343.1s (5.7m) | `5bb4303` |
| vllm         |   1322.9s (22.0m) | `3bb4697` |
| sglang       | **200.5s (3.3m)** | `52f221c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        303.2 |     166.9 | **144.9** |
| TPOT median (ms)          |     **50.6** |      56.2 |      77.3 |
| E2E median (ms)           |        349.8 | **217.1** |     218.0 |
| Throughput median (tok/s) |          3.6 |   **6.7** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        238.1 | **189.9** |  219.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        345.5 | **211.3** |  362.8 |
| Throughput median (tok/s) |          2.9 |   **4.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        730.7 |     174.0 | **166.5** |
| TPOT median (ms)          |     **59.8** |      67.2 |     107.4 |
| E2E median (ms)           |        781.6 | **236.8** |     266.5 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        424.2 | **62.8** |   78.7 |
| TPOT median (ms)          |         32.9 | **29.3** |   68.2 |
| E2E median (ms)           |        461.7 | **85.8** |  158.7 |
| Throughput median (tok/s) |          2.9 | **14.3** |    9.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        551.9 |  **70.0** |   77.5 |
| TPOT median (ms)          |         32.5 |  **15.0** |   23.7 |
| E2E median (ms)           |       1770.8 | **613.9** |  884.3 |
| Throughput median (tok/s) |         20.5 |  **58.0** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        449.7 | **132.7** |  137.3 |
| TPOT median (ms)          |         35.2 |  **33.5** |   55.3 |
| E2E median (ms)           |        741.9 | **273.0** |  378.1 |
| Throughput median (tok/s) |          6.3 |  **18.0** |   12.3 |
| Correctness               |          99% |       98% |    99% |
