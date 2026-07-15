# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 15 2026

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
| torchinferno | **40.6s (0.7m)** | `96adc9d` |
| vllm         |    425.1s (7.1m) | `1d99f0f` |
| sglang       |    191.9s (3.2m) | `d36e96c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.5 | **72.8** |   82.0 |
| TPOT median (ms)          |     **32.2** |     37.6 |   66.2 |
| E2E median (ms)           |        165.5 | **99.0** |  137.2 |
| Throughput median (tok/s) |          6.9 | **13.2** |    9.6 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.5** | 71.2 |  119.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **79.0** | 88.4 |  199.6 |
| Throughput median (tok/s) |     **12.7** | 11.3 |    5.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.7 |  **77.3** |   84.6 |
| TPOT median (ms)          |     **35.6** |      35.6 |   74.0 |
| E2E median (ms)           |        217.0 | **106.0** |  145.9 |
| Throughput median (tok/s) |          5.2 |  **12.2** |    9.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.2 | **37.8** |   52.9 |
| TPOT median (ms)          |         34.9 | **27.5** |  394.4 |
| E2E median (ms)           |         73.9 | **56.6** |  465.4 |
| Throughput median (tok/s) |         19.6 | **22.8** |    3.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        182.8 |  **47.3** |   51.8 |
| TPOT median (ms)          |         19.3 |  **15.6** |   24.7 |
| E2E median (ms)           |        885.0 | **580.4** |  925.5 |
| Throughput median (tok/s) |         41.0 |  **60.6** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.2 |  **61.3** |   78.2 |
| TPOT median (ms)          |         24.4 |  **23.3** |  111.8 |
| E2E median (ms)           |        284.1 | **186.1** |  374.7 |
| Throughput median (tok/s) |         17.1 |  **24.0** |   13.2 |
| Correctness               |          98% |       99% |    99% |
