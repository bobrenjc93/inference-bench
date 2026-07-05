# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **12/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **40.2s (0.7m)** | `390fed4` |
| vllm         |    217.5s (3.6m) | `fa4321d` |
| sglang       |    221.0s (3.7m) | `addffd7` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        166.2 |     146.5 | **143.8** |
| TPOT median (ms)          |     **47.7** |      52.7 |      72.8 |
| E2E median (ms)           |        218.7 | **190.7** |     219.4 |
| Throughput median (tok/s) |          5.7 |   **7.5** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **159.0** | 201.3 |  220.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **170.8** | 230.8 |  375.6 |
| Throughput median (tok/s) |      **5.9** |   4.3 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        365.6 |     177.9 | **167.5** |
| TPOT median (ms)          |         63.5 |  **53.0** |     102.8 |
| E2E median (ms)           |        417.3 | **227.4** |     268.1 |
| Throughput median (tok/s) |          3.4 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        129.6 | **64.0** |   76.0 |
| TPOT median (ms)          |         42.2 | **30.4** |   54.9 |
| E2E median (ms)           |        158.1 | **87.8** |  144.1 |
| Throughput median (tok/s) |          8.4 | **13.6** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        220.9 |      83.0 | **74.0** |
| TPOT median (ms)          |         20.8 |  **14.9** |     22.2 |
| E2E median (ms)           |       1000.7 | **616.9** |    833.2 |
| Throughput median (tok/s) |         37.1 |  **57.4** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        208.3 | **134.5** |  136.3 |
| TPOT median (ms)          |         34.9 |  **30.2** |   50.5 |
| E2E median (ms)           |        393.1 | **270.7** |  368.1 |
| Throughput median (tok/s) |         12.1 |  **17.8** |   12.8 |
| Correctness               |          99% |       98% |    99% |
