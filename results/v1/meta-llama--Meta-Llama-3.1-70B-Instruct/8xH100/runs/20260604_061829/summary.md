# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 3 2026

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
| torchinferno |     430.8s (7.2m) | `ae21327` |
| vllm         |   1398.4s (23.3m) | `b4b4aaa` |
| sglang       | **225.4s (3.8m)** | `e419170` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        329.5 |     161.3 | **150.8** |
| TPOT median (ms)          |     **51.6** |      52.3 |      72.7 |
| E2E median (ms)           |        389.0 | **218.2** |     223.4 |
| Throughput median (tok/s) |          3.3 |   **6.8** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.9 | **200.7** |  231.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        380.1 | **272.3** |  375.0 |
| Throughput median (tok/s) |          2.6 |   **3.7** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        821.4 |     174.7 | **165.8** |
| TPOT median (ms)          |        124.6 |  **55.2** |     110.9 |
| E2E median (ms)           |        948.7 | **224.4** |     265.6 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        354.0 | **62.6** |   88.3 |
| TPOT median (ms)          |         33.5 | **28.1** |   61.3 |
| E2E median (ms)           |        391.6 | **84.2** |  151.3 |
| Throughput median (tok/s) |          3.4 | **14.3** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        477.7 |  **76.6** |   79.7 |
| TPOT median (ms)          |         28.1 |  **14.8** |   23.9 |
| E2E median (ms)           |       1477.9 | **612.3** |  890.1 |
| Throughput median (tok/s) |         24.0 |  **58.6** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        452.3 | **135.2** |  143.3 |
| TPOT median (ms)          |         47.6 |  **30.1** |   53.8 |
| E2E median (ms)           |        717.5 | **282.3** |  381.1 |
| Throughput median (tok/s) |          6.9 |  **17.9** |   12.3 |
| Correctness               |          99% |       98% |    99% |
