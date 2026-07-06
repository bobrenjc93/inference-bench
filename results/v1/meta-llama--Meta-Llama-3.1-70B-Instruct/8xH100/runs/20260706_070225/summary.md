# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 6 2026

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
| torchinferno | **45.3s (0.8m)** | `0d6ab82` |
| vllm         |    226.7s (3.8m) | `cdab283` |
| sglang       |    183.5s (3.1m) | `5f98f62` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        158.8 | **121.9** |  134.6 |
| TPOT median (ms)          |         44.5 |  **42.5** |   86.5 |
| E2E median (ms)           |        206.5 | **158.0** |  222.4 |
| Throughput median (tok/s) |          6.1 |   **9.0** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **100.9** | 128.6 |  212.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **107.9** | 152.5 |  353.5 |
| Throughput median (tok/s) |      **9.3** |   6.6 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        234.3 | **145.5** |  161.8 |
| TPOT median (ms)          |         56.7 |  **44.6** |  110.5 |
| E2E median (ms)           |        291.9 | **190.0** |  270.3 |
| Throughput median (tok/s) |          4.4 |   **7.0** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         76.4 | **32.8** |   51.0 |
| TPOT median (ms)          |         63.4 | **21.7** |  386.6 |
| E2E median (ms)           |        107.2 | **48.4** |  434.1 |
| Throughput median (tok/s) |         12.6 | **25.6** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        307.5 |      74.8 | **72.3** |
| TPOT median (ms)          |         18.5 |  **14.8** |     22.4 |
| E2E median (ms)           |       1061.5 | **658.8** |    933.6 |
| Throughput median (tok/s) |         35.5 |  **59.1** |     40.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        175.6 | **100.7** |  126.3 |
| TPOT median (ms)          |         36.6 |  **24.7** |  121.2 |
| E2E median (ms)           |        355.0 | **241.5** |  442.8 |
| Throughput median (tok/s) |         13.6 |  **21.5** |   11.4 |
| Correctness               |          98% |       98% |    98% |
