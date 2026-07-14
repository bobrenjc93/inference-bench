# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:57 AM PT, Jul 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.6s (0.8m)** | `96adc9d` |
| vllm         |    391.2s (6.5m) | `1ff9429` |
| sglang       |    201.1s (3.4m) | `271e5ef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.0 | **69.7** |   81.2 |
| TPOT median (ms)          |     **31.7** |     36.8 |   64.1 |
| E2E median (ms)           |        164.9 | **95.8** |  136.6 |
| Throughput median (tok/s) |          7.0 | **14.1** |    9.8 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **51.6** | 70.6 |  121.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **68.7** | 90.4 |  200.6 |
| Throughput median (tok/s) |     **14.5** | 11.1 |    5.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        188.1 | **74.1** |   86.7 |
| TPOT median (ms)          |         35.4 | **35.4** |   70.1 |
| E2E median (ms)           |        216.5 | **97.9** |  144.9 |
| Throughput median (tok/s) |          5.2 | **13.7** |    9.1 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.1 | **34.8** |   51.8 |
| TPOT median (ms)          |         34.7 | **22.7** |  400.5 |
| E2E median (ms)           |         74.3 | **52.6** |  449.1 |
| Throughput median (tok/s) |         19.5 | **25.1** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.1 |  **46.0** |   52.4 |
| TPOT median (ms)          |         19.1 |  **15.3** |   24.7 |
| E2E median (ms)           |        866.1 | **579.0** |  970.6 |
| Throughput median (tok/s) |         41.1 |  **60.9** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.0 |  **59.0** |   78.7 |
| TPOT median (ms)          |         24.2 |  **22.0** |  111.9 |
| E2E median (ms)           |        278.1 | **183.1** |  380.3 |
| Throughput median (tok/s) |         17.5 |  **25.0** |   13.2 |
| Correctness               |          99% |       98% |    99% |
