# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 AM PT, May 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          1/4 |   **3/4** |    0/4 |
| **Total**        |         2/20 | **13/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     315.8s (5.3m) | `6ead340` |
| vllm         |   1294.9s (21.6m) | `e8b5199` |
| sglang       | **232.5s (3.9m)** | `ec075d8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        259.5 |    173.7 | **144.9** |
| TPOT median (ms)          |         67.8 | **61.4** |      71.3 |
| E2E median (ms)           |        319.4 |    237.4 | **212.9** |
| Throughput median (tok/s) |          4.1 |  **6.3** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.1 |     197.2 | **194.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        313.3 | **223.2** |     333.7 |
| Throughput median (tok/s) |          3.2 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        709.1 |     174.6 | **169.2** |
| TPOT median (ms)          |         55.5 |  **54.6** |     105.9 |
| E2E median (ms)           |        755.9 | **229.0** |     272.2 |
| Throughput median (tok/s) |          2.0 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        173.3 | **58.4** |   83.1 |
| TPOT median (ms)          |     **27.5** |     27.7 |   45.2 |
| E2E median (ms)           |        195.5 | **79.4** |  140.3 |
| Throughput median (tok/s) |          6.5 | **15.4** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        467.9 |  **68.8** |   75.4 |
| TPOT median (ms)          |     **14.7** |      15.1 |   23.9 |
| E2E median (ms)           |       1191.9 | **617.5** |  909.0 |
| Throughput median (tok/s) |         30.6 |  **58.8** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        377.8 |     134.5 | **133.3** |
| TPOT median (ms)          |         33.1 |  **31.8** |      49.2 |
| E2E median (ms)           |        555.2 | **277.3** |     373.6 |
| Throughput median (tok/s) |          9.3 |  **18.2** |      12.6 |
| Correctness               |          99% |       99% |       98% |
