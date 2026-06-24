# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     401.1s (6.7m) | `0afa3a4` |
| vllm         |     550.2s (9.2m) | `52fbe12` |
| sglang       | **264.2s (4.4m)** | `7430c56` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        156.4 |     143.2 | **142.4** |
| TPOT median (ms)          |         57.0 |  **53.5** |      74.3 |
| E2E median (ms)           |        207.6 | **197.4** |     210.0 |
| Throughput median (tok/s) |          5.6 |   **7.5** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.0 | **193.2** |  216.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        404.9 | **229.5** |  358.5 |
| Throughput median (tok/s) |          2.5 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        425.4 |     162.9 | **161.0** |
| TPOT median (ms)          |         67.1 |  **54.1** |      97.1 |
| E2E median (ms)           |        504.6 | **206.3** |     255.2 |
| Throughput median (tok/s) |          2.5 |   **6.6** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        295.3 | **58.6** |   80.8 |
| TPOT median (ms)          |         42.5 | **29.8** |   42.3 |
| E2E median (ms)           |        335.0 | **80.4** |  135.7 |
| Throughput median (tok/s) |          3.7 | **15.1** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        307.7 |  **69.2** |   75.3 |
| TPOT median (ms)          |         28.8 |  **15.0** |   22.4 |
| E2E median (ms)           |       1429.9 | **601.0** |  850.9 |
| Throughput median (tok/s) |         26.5 |  **59.4** |   41.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.6 | **125.4** |  135.1 |
| TPOT median (ms)          |         39.1 |  **30.5** |   47.2 |
| E2E median (ms)           |        576.4 | **262.9** |  362.1 |
| Throughput median (tok/s) |          8.2 |  **18.6** |   13.1 |
| Correctness               |          99% |       98% |    99% |
