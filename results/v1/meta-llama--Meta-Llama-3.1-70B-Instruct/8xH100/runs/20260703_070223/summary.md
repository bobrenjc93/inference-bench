# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **13/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.4s (0.7m)** | `a2463e4` |
| vllm         |    254.3s (4.2m) | `1f486d9` |
| sglang       |    165.2s (2.8m) | `67697fb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        151.4 |     156.6 | **141.0** |
| TPOT median (ms)          |         48.7 |  **45.0** |      77.5 |
| E2E median (ms)           |        192.1 | **191.6** |     218.0 |
| Throughput median (tok/s) |          6.4 |   **7.4** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **143.4** | 213.3 |  222.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **153.7** | 246.1 |  391.5 |
| Throughput median (tok/s) |      **6.5** |   4.1 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        317.6 |     175.7 | **167.4** |
| TPOT median (ms)          |         60.2 |  **43.2** |     105.1 |
| E2E median (ms)           |        371.5 | **220.5** |     270.4 |
| Throughput median (tok/s) |          3.9 |   **6.4** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        132.8 | **64.9** |   72.4 |
| TPOT median (ms)          |         44.6 | **30.5** |   72.3 |
| E2E median (ms)           |        161.0 | **89.4** |  153.3 |
| Throughput median (tok/s) |          8.1 | **13.5** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        259.2 |      74.0 | **72.6** |
| TPOT median (ms)          |         21.0 |  **15.2** |     22.1 |
| E2E median (ms)           |        965.7 | **619.5** |    816.0 |
| Throughput median (tok/s) |         35.7 |  **57.7** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        200.9 |     136.9 | **135.2** |
| TPOT median (ms)          |         34.9 |  **26.8** |      55.4 |
| E2E median (ms)           |        368.8 | **273.4** |     369.9 |
| Throughput median (tok/s) |         12.1 |  **17.8** |      12.9 |
| Correctness               |          99% |       99% |       99% |
