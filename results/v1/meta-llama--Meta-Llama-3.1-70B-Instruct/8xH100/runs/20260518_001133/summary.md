# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:09 PM PT, May 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     287.2s (4.8m) | `3f0f3bc` |
| vllm         |   1107.5s (18.5m) | `966903e` |
| sglang       | **160.6s (2.7m)** | `c67b287` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        294.8 |     161.9 | **147.6** |
| TPOT median (ms)          |        154.7 |  **54.6** |      75.4 |
| E2E median (ms)           |        388.6 | **214.4** |     217.9 |
| Throughput median (tok/s) |          3.7 |   **7.1** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        297.4 |     204.1 | **192.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        337.6 | **231.5** |     330.1 |
| Throughput median (tok/s) |          3.0 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        547.1 |     171.6 | **164.2** |
| TPOT median (ms)          |        137.1 |  **57.8** |      99.2 |
| E2E median (ms)           |        632.4 | **219.8** |     257.7 |
| Throughput median (tok/s) |          2.1 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        321.6 | **58.6** |   76.2 |
| TPOT median (ms)          |        132.1 | **27.4** |   54.1 |
| E2E median (ms)           |        423.0 | **78.9** |  148.2 |
| Throughput median (tok/s) |          3.5 | **15.5** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        763.5 |      71.5 | **68.8** |
| TPOT median (ms)          |         17.2 |  **15.2** |     22.2 |
| E2E median (ms)           |       1425.3 | **606.3** |    825.0 |
| Throughput median (tok/s) |         23.0 |  **58.3** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        444.9 |     133.5 | **129.8** |
| TPOT median (ms)          |         88.2 |  **31.0** |      50.2 |
| E2E median (ms)           |        641.4 | **270.2** |     355.8 |
| Throughput median (tok/s) |          7.0 |  **18.3** |      13.2 |
| Correctness               |          99% |       99% |       99% |
