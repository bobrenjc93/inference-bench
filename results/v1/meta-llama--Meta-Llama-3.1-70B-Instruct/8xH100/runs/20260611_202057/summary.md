# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, Jun 11 2026

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
| torchinferno |     411.7s (6.9m) | `065275c` |
| vllm         |   1280.5s (21.3m) | `3b03a2c` |
| sglang       | **192.5s (3.2m)** | `10219bd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        314.4 |     159.0 | **154.0** |
| TPOT median (ms)          |         88.8 |  **57.0** |      75.4 |
| E2E median (ms)           |        397.1 | **212.2** |     226.6 |
| Throughput median (tok/s) |          3.1 |   **7.1** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        406.8 | **190.6** |  213.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        557.3 | **213.6** |  345.3 |
| Throughput median (tok/s) |          1.8 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        725.4 |     180.3 | **167.1** |
| TPOT median (ms)          |         67.4 |  **59.9** |     100.2 |
| E2E median (ms)           |        776.3 | **241.9** |     265.2 |
| Throughput median (tok/s) |          1.8 |   **5.9** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        422.9 | **61.3** |   84.8 |
| TPOT median (ms)          |         63.7 | **28.0** |   54.9 |
| E2E median (ms)           |        482.5 | **82.7** |  152.3 |
| Throughput median (tok/s) |          2.9 | **14.4** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.0 |  **70.8** |   82.9 |
| TPOT median (ms)          |         26.7 |  **15.2** |   23.5 |
| E2E median (ms)           |       1259.5 | **629.0** |  888.8 |
| Throughput median (tok/s) |         31.1 |  **58.4** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        412.1 | **132.4** |  140.5 |
| TPOT median (ms)          |         49.3 |  **32.0** |   50.8 |
| E2E median (ms)           |        694.5 | **275.9** |  375.6 |
| Throughput median (tok/s) |          8.1 |  **18.1** |   12.4 |
| Correctness               |          99% |       98% |    98% |
