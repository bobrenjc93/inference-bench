# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 12 2026

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
| torchinferno | **37.8s (0.6m)** | `96adc9d` |
| vllm         |    283.0s (4.7m) | `4c81772` |
| sglang       |    153.0s (2.6m) | `96a04cb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        139.6 | **72.9** |   82.9 |
| TPOT median (ms)          |     **32.4** |     35.6 |   66.5 |
| E2E median (ms)           |        164.5 | **97.3** |  140.0 |
| Throughput median (tok/s) |          7.1 | **14.0** |    9.7 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **64.4** | 74.9 |  117.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **83.0** | 92.0 |  204.8 |
| Throughput median (tok/s) |     **12.1** | 10.9 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        189.6 | **69.2** |   82.8 |
| TPOT median (ms)          |         35.6 | **35.5** |   72.4 |
| E2E median (ms)           |        218.0 | **94.2** |  141.1 |
| Throughput median (tok/s) |          5.2 | **14.3** |    9.5 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.4 | **36.3** |   52.3 |
| TPOT median (ms)          |         34.8 | **23.6** |  438.7 |
| E2E median (ms)           |         72.5 | **54.7** |  495.1 |
| Throughput median (tok/s) |         19.7 | **23.8** |    2.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.2 |  **46.0** |   51.5 |
| TPOT median (ms)          |         19.1 |  **15.1** |   24.2 |
| E2E median (ms)           |        886.0 | **572.7** |  930.1 |
| Throughput median (tok/s) |         41.4 |  **61.5** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.8 |  **59.9** |   77.4 |
| TPOT median (ms)          |         24.4 |  **22.0** |  120.4 |
| E2E median (ms)           |        284.8 | **182.2** |  382.2 |
| Throughput median (tok/s) |         17.1 |  **24.9** |   13.4 |
| Correctness               |          99% |       99% |    99% |
