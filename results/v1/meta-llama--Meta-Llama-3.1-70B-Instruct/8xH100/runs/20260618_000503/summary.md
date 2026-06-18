# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, Jun 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     362.3s (6.0m) | `ccca738` |
| vllm         |     535.5s (8.9m) | `0d339cf` |
| sglang       | **267.7s (4.5m)** | `d773b49` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        463.8 | **137.6** |  152.2 |
| TPOT median (ms)          |         57.9 |  **40.5** |   78.0 |
| E2E median (ms)           |        506.8 | **170.4** |  222.8 |
| Throughput median (tok/s) |          2.5 |   **8.1** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        279.1 | **211.7** |  217.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        389.4 | **236.7** |  365.0 |
| Throughput median (tok/s) |          2.6 |   **4.2** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        669.7 | **163.2** |  164.0 |
| TPOT median (ms)          |         67.7 |  **47.5** |  103.3 |
| E2E median (ms)           |        736.0 | **201.2** |  269.2 |
| Throughput median (tok/s) |          1.8 |   **6.8** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        185.9 | **58.5** |   85.9 |
| TPOT median (ms)          |         32.6 | **28.1** |   42.4 |
| E2E median (ms)           |        223.7 | **79.1** |  149.5 |
| Throughput median (tok/s) |          6.0 | **15.4** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        359.6 |  **69.2** |   69.7 |
| TPOT median (ms)          |         21.6 |  **15.1** |   22.9 |
| E2E median (ms)           |       1117.0 | **617.9** |  911.6 |
| Throughput median (tok/s) |         31.9 |  **58.7** |   40.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        391.6 | **128.0** |  137.8 |
| TPOT median (ms)          |         36.0 |  **26.2** |   49.3 |
| E2E median (ms)           |        594.6 | **261.0** |  383.6 |
| Throughput median (tok/s) |          8.9 |  **18.6** |   12.7 |
| Correctness               |          98% |       98% |    99% |
