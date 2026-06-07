# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 PM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     339.1s (5.7m) | `c60e0bd` |
| vllm         |   1279.7s (21.3m) | `bc5745a` |
| sglang       | **197.8s (3.3m)** | `5160f79` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        317.1 |     159.7 | **157.7** |
| TPOT median (ms)          |     **49.1** |      54.2 |      70.1 |
| E2E median (ms)           |        367.4 | **200.2** |     227.6 |
| Throughput median (tok/s) |          4.1 |   **7.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        247.7 | **193.6** |  210.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        346.7 | **257.7** |  351.6 |
| Throughput median (tok/s) |          2.9 |   **3.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        659.7 |     174.5 | **167.7** |
| TPOT median (ms)          |         59.9 |  **52.5** |      99.4 |
| E2E median (ms)           |        729.8 | **221.5** |     264.2 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        420.1 | **60.9** |   80.3 |
| TPOT median (ms)          |         30.8 | **28.2** |   46.4 |
| E2E median (ms)           |        451.2 | **83.2** |  141.8 |
| Throughput median (tok/s) |          3.0 | **14.6** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        558.8 |  **66.1** |   79.7 |
| TPOT median (ms)          |         31.8 |  **15.1** |   23.5 |
| E2E median (ms)           |       1688.3 | **597.1** |  914.5 |
| Throughput median (tok/s) |         20.7 |  **58.9** |   39.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        440.7 | **131.0** |  139.1 |
| TPOT median (ms)          |         34.3 |  **30.0** |   47.9 |
| E2E median (ms)           |        716.7 | **271.9** |  380.0 |
| Throughput median (tok/s) |          6.5 |  **18.1** |   12.4 |
| Correctness               |          98% |       98% |    98% |
