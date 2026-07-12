# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 12 2026

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
| torchinferno | **36.3s (0.6m)** | `96adc9d` |
| vllm         |    294.2s (4.9m) | `4c81772` |
| sglang       |    160.8s (2.7m) | `96a04cb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        146.9 |  **74.7** |   83.4 |
| TPOT median (ms)          |     **31.8** |      37.6 |   70.9 |
| E2E median (ms)           |        173.7 | **101.0** |  143.3 |
| Throughput median (tok/s) |          6.8 |  **13.1** |    9.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **60.6** | 75.5 |  127.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **79.4** | 93.3 |  219.3 |
| Throughput median (tok/s) |     **12.6** | 10.7 |    4.6 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.2 |  **79.2** |   86.8 |
| TPOT median (ms)          |         36.2 |  **34.0** |   70.7 |
| E2E median (ms)           |        222.2 | **106.8** |  147.6 |
| Throughput median (tok/s) |          5.0 |  **12.8** |    9.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.2 | **35.6** |   52.0 |
| TPOT median (ms)          |         34.3 | **23.5** |  417.1 |
| E2E median (ms)           |         72.9 | **54.1** |  511.3 |
| Throughput median (tok/s) |         20.1 | **24.1** |    2.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.9 |  **47.0** |   51.6 |
| TPOT median (ms)          |         19.4 |  **15.4** |   24.8 |
| E2E median (ms)           |        886.4 | **575.6** |  932.8 |
| Throughput median (tok/s) |         40.7 |  **60.7** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.2 |  **62.4** |   80.3 |
| TPOT median (ms)          |         24.3 |  **22.1** |  116.7 |
| E2E median (ms)           |        286.9 | **186.2** |  390.9 |
| Throughput median (tok/s) |         17.0 |  **24.3** |   12.9 |
| Correctness               |          99% |       98% |    99% |
