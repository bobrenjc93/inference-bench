# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **14/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **42.2s (0.7m)** | `390fed4` |
| vllm         |    233.9s (3.9m) | `26eb872` |
| sglang       |    159.9s (2.7m) | `03962d4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        177.9 | **131.3** |  143.7 |
| TPOT median (ms)          |         47.9 |  **43.4** |   73.2 |
| E2E median (ms)           |        231.5 | **165.3** |  218.2 |
| Throughput median (tok/s) |          5.7 |   **8.5** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **181.5** | 216.0 |  218.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **196.4** | 241.5 |  379.9 |
| Throughput median (tok/s) |      **5.1** |   4.1 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        341.2 |     169.4 | **165.5** |
| TPOT median (ms)          |         62.6 |  **40.4** |     104.5 |
| E2E median (ms)           |        399.5 | **208.1** |     279.7 |
| Throughput median (tok/s) |          3.5 |   **6.5** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        132.2 | **64.7** |   73.9 |
| TPOT median (ms)          |         49.6 | **30.4** |   65.1 |
| E2E median (ms)           |        163.0 | **88.4** |  144.5 |
| Throughput median (tok/s) |          8.0 | **13.7** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        258.7 |      85.2 | **72.2** |
| TPOT median (ms)          |         20.0 |  **14.9** |     22.3 |
| E2E median (ms)           |        957.9 | **645.2** |    845.0 |
| Throughput median (tok/s) |         37.2 |  **57.4** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        218.3 | **133.3** |  134.7 |
| TPOT median (ms)          |         36.0 |  **25.8** |   53.0 |
| E2E median (ms)           |        389.7 | **269.7** |  373.4 |
| Throughput median (tok/s) |         11.9 |  **18.1** |   12.8 |
| Correctness               |          99% |       99% |    99% |
