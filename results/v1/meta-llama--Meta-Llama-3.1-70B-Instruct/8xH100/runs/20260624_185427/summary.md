# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:54 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **3.9s (0.1m)** | `76107de` |
| vllm         |    86.2s (1.4m) | `1cd3e0e` |
| sglang       |     9.0s (0.1m) | `4a4f063` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        152.1 | **137.2** |  144.2 |
| TPOT median (ms)          |         51.3 |  **49.6** |   84.9 |
| E2E median (ms)           |        195.9 | **182.0** |  226.8 |
| Throughput median (tok/s) |          6.2 |   **7.4** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        349.9 |     259.3 | **246.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        378.4 | **296.6** |     423.5 |
| Throughput median (tok/s) |          2.6 |   **3.4** |       2.4 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        432.0 | **139.0** |  178.4 |
| TPOT median (ms)          |     **64.7** |      84.6 |  104.8 |
| E2E median (ms)           |        498.3 | **217.6** |  289.9 |
| Throughput median (tok/s) |          2.3 |   **5.8** |    4.5 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        240.0 |  **73.3** |   76.5 |
| TPOT median (ms)          |         51.3 |  **35.8** |   69.7 |
| E2E median (ms)           |        288.3 | **100.1** |  159.9 |
| Throughput median (tok/s) |          4.3 |  **12.1** |    8.9 |
| Correctness               |          96% |       97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        382.4 |  **73.8** |   85.3 |
| TPOT median (ms)          |         26.9 |  **18.7** |   26.2 |
| E2E median (ms)           |       1561.1 | **752.4** | 1016.8 |
| Throughput median (tok/s) |         25.6 |  **47.7** |   34.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        311.3 | **136.5** |  146.1 |
| TPOT median (ms)          |         38.8 |  **37.7** |   57.1 |
| E2E median (ms)           |        584.4 | **309.7** |  423.4 |
| Throughput median (tok/s) |          8.2 |  **15.3** |   11.1 |
| Correctness               |          98% |       98% |    99% |
