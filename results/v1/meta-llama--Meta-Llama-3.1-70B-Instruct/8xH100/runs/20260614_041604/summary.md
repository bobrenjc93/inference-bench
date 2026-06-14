# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jun 13 2026

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
| torchinferno |     380.4s (6.3m) | `a102128` |
| vllm         |   1306.4s (21.8m) | `cf027b8` |
| sglang       | **211.2s (3.5m)** | `a3fd5c2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        313.7 |    169.0 | **144.8** |
| TPOT median (ms)          |         96.0 | **58.4** |      76.0 |
| E2E median (ms)           |        400.7 |    224.6 | **211.7** |
| Throughput median (tok/s) |          3.1 |  **6.7** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        317.4 | **199.5** |  207.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        433.6 | **225.3** |  343.8 |
| Throughput median (tok/s) |          2.3 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        705.3 |     175.9 | **165.2** |
| TPOT median (ms)          |         69.9 |  **66.5** |     102.3 |
| E2E median (ms)           |        779.1 | **232.6** |     264.9 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        293.9 | **59.2** |   83.8 |
| TPOT median (ms)          |         63.4 | **27.8** |   55.1 |
| E2E median (ms)           |        346.2 | **79.8** |  148.3 |
| Throughput median (tok/s) |          4.1 | **15.5** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        335.2 |      65.8 | **65.8** |
| TPOT median (ms)          |         21.8 |  **15.2** |     22.5 |
| E2E median (ms)           |       1134.8 | **612.9** |    847.9 |
| Throughput median (tok/s) |         32.1 |  **58.7** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        393.1 |     133.9 | **133.5** |
| TPOT median (ms)          |         50.2 |  **33.6** |      51.2 |
| E2E median (ms)           |        618.9 | **275.0** |     363.3 |
| Throughput median (tok/s) |          8.6 |  **18.3** |      13.0 |
| Correctness               |          99% |       99% |       98% |
