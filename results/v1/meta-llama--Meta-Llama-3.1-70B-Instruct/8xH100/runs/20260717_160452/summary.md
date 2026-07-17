# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:04 AM PT, Jul 17 2026

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
| torchinferno | **51.7s (0.9m)** | `96adc9d` |
| vllm         |    266.9s (4.4m) | `877dae9` |
| sglang       |    162.0s (2.7m) | `53229e8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.3 |  **93.5** |   96.4 |
| TPOT median (ms)          |     **31.5** |      37.1 |   71.8 |
| E2E median (ms)           |        167.4 | **122.1** |  162.0 |
| Throughput median (tok/s) |          6.9 |  **11.7** |    7.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.6** | 79.4 |  123.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.0** | 97.2 |  210.2 |
| Throughput median (tok/s) |     **13.5** | 10.3 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.9 |  **90.0** |   95.5 |
| TPOT median (ms)          |         34.4 |  **33.3** |   77.6 |
| E2E median (ms)           |        218.6 | **113.8** |  160.8 |
| Throughput median (tok/s) |          5.2 |  **11.5** |    8.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.0 | **35.1** |   62.4 |
| TPOT median (ms)          |         34.9 | **23.0** |  387.3 |
| E2E median (ms)           |         75.3 | **53.1** |  459.0 |
| Throughput median (tok/s) |         19.6 | **24.5** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        177.2 |  **47.5** |   54.9 |
| TPOT median (ms)          |         19.1 |  **15.6** |   27.5 |
| E2E median (ms)           |        896.5 | **584.1** | 1045.5 |
| Throughput median (tok/s) |         41.8 |  **60.2** |   35.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.0 |  **69.1** |   86.5 |
| TPOT median (ms)          |         24.0 |  **21.8** |  112.9 |
| E2E median (ms)           |        286.3 | **194.1** |  407.5 |
| Throughput median (tok/s) |         17.4 |  **23.6** |   11.9 |
| Correctness               |          99% |       99% |    99% |
