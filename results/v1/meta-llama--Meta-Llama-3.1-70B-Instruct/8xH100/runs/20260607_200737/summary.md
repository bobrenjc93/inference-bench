# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 PM PT, Jun 7 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     300.3s (5.0m) | `e19c01f` |
| vllm         |   1302.5s (21.7m) | `4dcd10e` |
| sglang       | **177.0s (2.9m)** | `02be2e7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        294.2 |    170.1 | **147.5** |
| TPOT median (ms)          |         93.4 | **54.4** |      75.0 |
| E2E median (ms)           |        378.5 |    223.0 | **216.4** |
| Throughput median (tok/s) |          3.2 |  **6.8** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        392.9 | **192.0** |  203.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        548.1 | **248.6** |  332.1 |
| Throughput median (tok/s) |          1.8 |   **4.0** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        731.6 |     175.2 | **160.9** |
| TPOT median (ms)          |         68.8 |  **63.9** |      97.2 |
| E2E median (ms)           |        795.0 | **236.3** |     255.3 |
| Throughput median (tok/s) |          1.5 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.5 | **58.2** |   81.9 |
| TPOT median (ms)          |         69.5 | **28.4** |   41.8 |
| E2E median (ms)           |        416.7 | **79.2** |  134.4 |
| Throughput median (tok/s) |          3.0 | **15.3** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        464.0 |  **64.7** |   78.5 |
| TPOT median (ms)          |         21.6 |  **15.1** |   23.4 |
| E2E median (ms)           |       1263.4 | **604.5** |  887.9 |
| Throughput median (tok/s) |         29.0 |  **59.6** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        446.8 | **132.0** |  134.5 |
| TPOT median (ms)          |         50.7 |  **32.4** |   47.5 |
| E2E median (ms)           |        680.3 | **278.3** |  365.2 |
| Throughput median (tok/s) |          7.7 |  **18.4** |   12.7 |
| Correctness               |          99% |       99% |    98% |
