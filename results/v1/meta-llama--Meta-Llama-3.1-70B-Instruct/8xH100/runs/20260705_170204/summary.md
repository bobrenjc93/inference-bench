# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **36.1s (0.6m)** | `823d043` |
| vllm         |    227.7s (3.8m) | `cc1d020` |
| sglang       |    216.1s (3.6m) | `48ba79c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        147.6 | **126.4** |  129.1 |
| TPOT median (ms)          |         42.3 |  **40.9** |   83.8 |
| E2E median (ms)           |        186.4 | **161.8** |  210.3 |
| Throughput median (tok/s) |          6.5 |   **8.8** |    6.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **100.0** | 124.2 |  217.8 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **107.5** | 144.4 |  363.8 |
| Throughput median (tok/s) |      **9.3** |   6.9 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        227.3 | **149.3** |  163.0 |
| TPOT median (ms)          |         57.8 |  **43.1** |  103.4 |
| E2E median (ms)           |        280.3 | **194.2** |  274.5 |
| Throughput median (tok/s) |          4.7 |   **7.1** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         80.0 | **32.4** |   49.8 |
| TPOT median (ms)          |         64.7 | **21.7** |  422.4 |
| E2E median (ms)           |        115.1 | **47.8** |  465.8 |
| Throughput median (tok/s) |         12.0 | **25.9** |    3.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        283.3 |      80.6 | **66.9** |
| TPOT median (ms)          |         20.0 |  **14.6** |     22.7 |
| E2E median (ms)           |        988.5 | **597.9** |    915.7 |
| Throughput median (tok/s) |         35.7 |  **59.1** |     40.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        167.6 | **102.6** |  125.3 |
| TPOT median (ms)          |         37.0 |  **24.1** |  126.4 |
| E2E median (ms)           |        335.6 | **229.2** |  446.0 |
| Throughput median (tok/s) |         13.6 |  **21.6** |   11.5 |
| Correctness               |          99% |       99% |    99% |
