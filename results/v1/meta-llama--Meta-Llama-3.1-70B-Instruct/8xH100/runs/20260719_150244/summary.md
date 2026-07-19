# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **49.9s (0.8m)** | `96adc9d` |
| vllm         |    365.1s (6.1m) | `e6d1310` |
| sglang       |    199.2s (3.3m) | `d4801be` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        144.4 |      88.1 | **84.4** |
| TPOT median (ms)          |     **31.0** |      37.6 |     69.7 |
| E2E median (ms)           |        168.3 | **121.6** |    143.6 |
| Throughput median (tok/s) |          6.8 |  **11.7** |      9.3 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.1** | 78.6 |  169.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.4** | 97.5 |  251.2 |
| Throughput median (tok/s) |     **13.3** | 10.3 |    4.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.8 |  **83.6** |   99.1 |
| TPOT median (ms)          |     **35.6** |      37.9 |   84.2 |
| E2E median (ms)           |        220.0 | **111.3** |  177.4 |
| Throughput median (tok/s) |          5.2 |  **11.4** |    7.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.2 | **35.8** |   61.2 |
| TPOT median (ms)          |         34.8 | **24.2** |  393.4 |
| E2E median (ms)           |         73.4 | **53.8** |  469.2 |
| Throughput median (tok/s) |         19.7 | **24.1** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        181.5 |  **46.1** |   56.7 |
| TPOT median (ms)          |         19.4 |  **15.1** |   27.3 |
| E2E median (ms)           |        859.6 | **574.0** | 1059.2 |
| Throughput median (tok/s) |         41.0 |  **61.8** |   35.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.6 |  **66.4** |   94.2 |
| TPOT median (ms)          |         24.2 |  **23.0** |  114.9 |
| E2E median (ms)           |        279.3 | **191.6** |  420.1 |
| Throughput median (tok/s) |         17.2 |  **23.9** |   11.9 |
| Correctness               |          99% |       99% |    99% |
