# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:03 PM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     389.5s (6.5m) | `9f91b40` |
| vllm         |   1288.7s (21.5m) | `33d7cbe` |
| sglang       | **203.6s (3.4m)** | `af8f669` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        273.8 |    157.6 | **140.0** |
| TPOT median (ms)          |        154.1 | **54.8** |      75.9 |
| E2E median (ms)           |        371.5 |    212.2 | **209.7** |
| Throughput median (tok/s) |          4.1 |  **7.1** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        267.2 | **198.7** |  202.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        291.3 | **226.5** |  341.4 |
| Throughput median (tok/s) |          3.4 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        857.3 |     173.2 | **157.0** |
| TPOT median (ms)          |        125.1 |  **64.0** |      98.2 |
| E2E median (ms)           |        946.1 | **226.2** |     259.9 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        335.4 | **58.9** |   75.8 |
| TPOT median (ms)          |        133.6 | **27.1** |   68.6 |
| E2E median (ms)           |        435.7 | **79.9** |  159.3 |
| Throughput median (tok/s) |          3.2 | **15.5** |    9.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        704.1 |  **67.4** |   68.8 |
| TPOT median (ms)          |     **14.8** |      15.0 |   22.2 |
| E2E median (ms)           |       1345.8 | **616.0** |  819.0 |
| Throughput median (tok/s) |         25.0 |  **58.7** |   42.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        487.5 |     131.2 | **128.8** |
| TPOT median (ms)          |         85.5 |  **32.2** |      53.0 |
| E2E median (ms)           |        678.1 | **272.2** |     357.9 |
| Throughput median (tok/s) |          7.4 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       99% |
