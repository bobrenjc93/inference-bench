# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    703.1s (11.7m) | `bd7e38b` |
| vllm         |    608.8s (10.1m) | `07d33e5` |
| sglang       | **276.8s (4.6m)** | `5169df7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        168.7 | **135.2** |  148.1 |
| TPOT median (ms)          |         48.0 |  **43.5** |   71.4 |
| E2E median (ms)           |        211.9 | **170.1** |  217.6 |
| Throughput median (tok/s) |          5.5 |   **8.0** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        260.4 |     227.6 | **224.4** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        281.8 | **256.8** |     367.9 |
| Throughput median (tok/s) |          3.5 |   **3.9** |       2.7 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        289.4 |     163.8 | **159.9** |
| TPOT median (ms)          |         54.4 |  **47.9** |     103.5 |
| E2E median (ms)           |        341.9 | **207.9** |     256.8 |
| Throughput median (tok/s) |          4.1 |   **6.5** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        196.8 | **61.5** |   82.1 |
| TPOT median (ms)          |         57.8 | **31.7** |   47.7 |
| E2E median (ms)           |        242.6 | **85.3** |  133.0 |
| Throughput median (tok/s) |          5.7 | **14.0** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        309.6 |      71.3 | **69.3** |
| TPOT median (ms)          |         23.6 |  **14.9** |     22.5 |
| E2E median (ms)           |       1153.9 | **602.1** |    843.4 |
| Throughput median (tok/s) |         31.6 |  **58.8** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        245.0 | **131.9** |  136.7 |
| TPOT median (ms)          |         36.8 |  **27.6** |   49.0 |
| E2E median (ms)           |        446.4 | **264.5** |  363.7 |
| Throughput median (tok/s) |         10.1 |  **18.2** |   13.0 |
| Correctness               |          99% |       99% |    99% |
