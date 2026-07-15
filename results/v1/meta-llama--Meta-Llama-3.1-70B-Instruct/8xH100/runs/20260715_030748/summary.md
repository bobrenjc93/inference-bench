# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:07 PM PT, Jul 14 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **46.4s (0.8m)** | `96adc9d` |
| vllm         |    354.4s (5.9m) | `6472131` |
| sglang       |    197.7s (3.3m) | `c00131e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.9 |  **73.4** |   77.7 |
| TPOT median (ms)          |     **31.2** |      38.4 |   63.2 |
| E2E median (ms)           |        164.9 | **102.3** |  131.9 |
| Throughput median (tok/s) |          7.0 |  **12.6** |   10.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **53.3** | 68.7 |  129.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **71.0** | 87.7 |  216.8 |
| Throughput median (tok/s) |     **14.1** | 11.4 |    4.6 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        195.9 |  **79.3** |   84.5 |
| TPOT median (ms)          |     **34.3** |      35.9 |   79.7 |
| E2E median (ms)           |        223.7 | **106.7** |  152.4 |
| Throughput median (tok/s) |          5.0 |  **12.5** |    8.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.6 | **35.9** |   52.5 |
| TPOT median (ms)          |         34.9 | **23.5** |  397.3 |
| E2E median (ms)           |         73.9 | **53.9** |  447.0 |
| Throughput median (tok/s) |         19.8 | **23.7** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.5 |  **46.0** |   52.1 |
| TPOT median (ms)          |         19.7 |  **15.3** |   24.5 |
| E2E median (ms)           |        873.9 | **569.2** |  954.8 |
| Throughput median (tok/s) |         40.5 |  **61.7** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.2 |  **60.6** |   79.3 |
| TPOT median (ms)          |         24.0 |  **22.6** |  113.0 |
| E2E median (ms)           |        281.5 | **184.0** |  380.6 |
| Throughput median (tok/s) |         17.3 |  **24.4** |   13.3 |
| Correctness               |          99% |       98% |    99% |
