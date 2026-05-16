# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:08 AM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     354.1s (5.9m) | `db749af` |
| vllm         |   1107.3s (18.5m) | `4db300e` |
| sglang       | **168.9s (2.8m)** | `0f50ed8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        288.8 |    160.4 | **135.8** |
| TPOT median (ms)          |        150.5 | **52.2** |      72.7 |
| E2E median (ms)           |        375.0 |    210.4 | **205.5** |
| Throughput median (tok/s) |          3.9 |  **7.0** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        266.7 |     201.9 | **199.5** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        294.6 | **226.4** |     336.3 |
| Throughput median (tok/s) |          3.4 |   **4.4** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        514.0 |     180.5 | **151.3** |
| TPOT median (ms)          |        108.9 |  **64.0** |     102.9 |
| E2E median (ms)           |        614.0 | **238.1** |     256.0 |
| Throughput median (tok/s) |          2.1 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        361.0 | **58.8** |   79.9 |
| TPOT median (ms)          |        130.5 | **26.8** |   51.1 |
| E2E median (ms)           |        457.0 | **78.8** |  149.3 |
| Throughput median (tok/s) |          3.3 | **15.7** |    9.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        703.4 |  **68.6** |   70.8 |
| TPOT median (ms)          |         15.3 |  **15.0** |   22.5 |
| E2E median (ms)           |       1327.6 | **607.3** |  843.2 |
| Throughput median (tok/s) |         24.4 |  **58.8** |   41.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        426.8 |     134.0 | **127.4** |
| TPOT median (ms)          |         81.0 |  **31.6** |      49.8 |
| E2E median (ms)           |        613.6 | **272.2** |     358.1 |
| Throughput median (tok/s) |          7.4 |  **18.4** |      13.0 |
| Correctness               |          98% |       98% |       99% |
