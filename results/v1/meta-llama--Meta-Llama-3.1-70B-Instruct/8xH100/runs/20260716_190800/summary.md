# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, Jul 16 2026

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
| torchinferno | **38.7s (0.6m)** | `96adc9d` |
| vllm         |    268.3s (4.5m) | `02bf9c7` |
| sglang       |    162.4s (2.7m) | `8c9833f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        144.2 |      87.0 | **79.4** |
| TPOT median (ms)          |     **31.6** |      41.8 |     66.5 |
| E2E median (ms)           |        168.4 | **128.6** |    134.2 |
| Throughput median (tok/s) |          6.8 |  **11.3** |     10.0 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.8** | 73.1 |  127.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **73.8** | 89.9 |  213.5 |
| Throughput median (tok/s) |     **13.6** | 11.1 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.0 |  **74.7** |   83.9 |
| TPOT median (ms)          |     **34.6** |      35.3 |   86.1 |
| E2E median (ms)           |        219.1 | **103.7** |  152.9 |
| Throughput median (tok/s) |          5.1 |  **13.3** |    8.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.2 | **36.7** |   51.8 |
| TPOT median (ms)          |         34.7 | **25.2** |  398.6 |
| E2E median (ms)           |         76.6 | **55.4** |  441.7 |
| Throughput median (tok/s) |         19.2 | **23.4** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.9 |  **47.1** |   53.3 |
| TPOT median (ms)          |         19.7 |  **15.5** |   25.0 |
| E2E median (ms)           |        896.9 | **575.1** |  928.7 |
| Throughput median (tok/s) |         40.3 |  **60.2** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.8 |  **63.7** |   79.2 |
| TPOT median (ms)          |         24.1 |  **23.6** |  115.2 |
| E2E median (ms)           |        286.9 | **190.5** |  374.2 |
| Throughput median (tok/s) |         17.0 |  **23.9** |   13.1 |
| Correctness               |          99% |       98% |    99% |
