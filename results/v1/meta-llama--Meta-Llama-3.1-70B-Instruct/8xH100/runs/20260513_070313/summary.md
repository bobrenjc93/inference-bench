# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:07 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     345.7s (5.8m) | `9d5290c` |
| vllm         |    987.2s (16.5m) | `503697c` |
| sglang       | **167.4s (2.8m)** | `f2a9009` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        399.5 |    156.5 | **137.5** |
| TPOT median (ms)          |        478.6 | **56.2** |      76.2 |
| E2E median (ms)           |        793.6 |    211.6 | **205.1** |
| Throughput median (tok/s) |          1.7 |  **7.0** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        718.7 | **209.0** |      - |
| TPOT median (ms)          |          0.0 |       0.0 |      - |
| E2E median (ms)           |        749.6 | **229.8** |      - |
| Throughput median (tok/s) |          1.3 |   **4.4** |      - |
| Correctness               |         100% |      100% |      - |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        632.1 | **176.3** |      - |
| TPOT median (ms)          |        271.5 |  **53.2** |      - |
| E2E median (ms)           |        808.9 | **224.6** |      - |
| Throughput median (tok/s) |          1.6 |   **6.2** |      - |
| Correctness               |          98% |       98% |      - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        494.4 | **57.9** |      - |
| TPOT median (ms)          |        465.1 | **26.6** |      - |
| E2E median (ms)           |        873.6 | **78.6** |      - |
| Throughput median (tok/s) |          1.5 | **15.8** |      - |
| Correctness               |          97% |      97% |      - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        608.4 |  **69.0** |      - |
| TPOT median (ms)          |         31.1 |  **15.0** |      - |
| E2E median (ms)           |       1978.7 | **603.4** |      - |
| Throughput median (tok/s) |         18.4 |  **59.1** |      - |
| Correctness               |         100% |      100% |      - |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        570.6 | **133.8** |     137.5 |
| TPOT median (ms)          |        249.3 |  **30.2** |      76.2 |
| E2E median (ms)           |       1040.9 |     269.6 | **205.1** |
| Throughput median (tok/s) |          4.9 |  **18.5** |       5.9 |
| Correctness               |          98% |       99% |       98% |
