# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jun 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **18/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     328.1s (5.5m) | `8225da4` |
| vllm         |     453.8s (7.6m) | `0fbf42a` |
| sglang       | **259.1s (4.3m)** | `871ed0d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        321.2 | **138.5** |  145.2 |
| TPOT median (ms)          |     **50.5** |      51.7 |   67.4 |
| E2E median (ms)           |        377.3 | **181.4** |  214.2 |
| Throughput median (tok/s) |          3.5 |   **8.0** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        306.3 | **178.0** |  230.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        415.5 | **203.9** |  370.3 |
| Throughput median (tok/s) |          2.4 |   **4.9** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        652.8 | **155.8** |  167.6 |
| TPOT median (ms)          |         65.7 |  **49.2** |  100.5 |
| E2E median (ms)           |        715.7 | **198.5** |  265.9 |
| Throughput median (tok/s) |          1.9 |   **6.9** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        182.9 | **59.6** |   87.9 |
| TPOT median (ms)          |         34.1 | **30.7** |   41.0 |
| E2E median (ms)           |        218.2 | **82.5** |  141.9 |
| Throughput median (tok/s) |          6.1 | **15.1** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        349.2 |  **65.6** |   67.0 |
| TPOT median (ms)          |         21.4 |  **14.8** |   22.5 |
| E2E median (ms)           |       1153.2 | **603.3** |  839.7 |
| Throughput median (tok/s) |         32.2 |  **60.3** |   41.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        362.5 | **119.5** |  139.5 |
| TPOT median (ms)          |         34.3 |  **29.3** |   46.3 |
| E2E median (ms)           |        576.0 | **253.9** |  366.4 |
| Throughput median (tok/s) |          9.2 |  **19.0** |   12.9 |
| Correctness               |          98% |       98% |    99% |
