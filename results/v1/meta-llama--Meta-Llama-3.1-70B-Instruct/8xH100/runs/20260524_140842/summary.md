# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 AM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     316.2s (5.3m) | `9f91b40` |
| vllm         |   1248.2s (20.8m) | `1806d1a` |
| sglang       | **202.5s (3.4m)** | `b6f71d5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        312.8 |     147.0 | **144.6** |
| TPOT median (ms)          |        153.7 |  **52.7** |      72.8 |
| E2E median (ms)           |        429.6 | **191.7** |     212.5 |
| Throughput median (tok/s) |          3.2 |   **7.6** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        304.6 | **198.3** |  204.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        339.2 | **226.5** |  339.2 |
| Throughput median (tok/s) |          2.9 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        850.9 |     173.3 | **162.7** |
| TPOT median (ms)          |        128.3 |  **60.1** |     103.9 |
| E2E median (ms)           |        941.4 | **228.8** |     256.8 |
| Throughput median (tok/s) |          1.4 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.4 | **57.4** |   77.3 |
| TPOT median (ms)          |        130.3 | **26.7** |   63.2 |
| E2E median (ms)           |        473.5 | **77.6** |  157.2 |
| Throughput median (tok/s) |          2.9 | **15.9** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        902.7 |      76.2 | **66.8** |
| TPOT median (ms)          |         15.9 |  **14.9** |     22.3 |
| E2E median (ms)           |       1597.2 | **627.2** |    845.1 |
| Throughput median (tok/s) |         21.0 |  **58.2** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        549.7 | **130.5** |  131.2 |
| TPOT median (ms)          |         85.6 |  **30.9** |   52.4 |
| E2E median (ms)           |        756.2 | **270.4** |  362.2 |
| Throughput median (tok/s) |          6.3 |  **18.4** |   13.0 |
| Correctness               |          98% |       98% |    99% |
