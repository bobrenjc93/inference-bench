# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **55.8s (0.9m)** | `96adc9d` |
| vllm         |    459.2s (7.7m) | `3935829` |
| sglang       |    211.2s (3.5m) | `bc525dc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.8 |  **74.3** |   78.7 |
| TPOT median (ms)          |     **31.2** |      36.2 |   63.9 |
| E2E median (ms)           |        167.4 | **101.8** |  132.7 |
| Throughput median (tok/s) |          6.8 |  **13.0** |   10.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **58.1** | 73.0 |  123.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **77.7** | 90.3 |  207.8 |
| Throughput median (tok/s) |     **12.9** | 11.1 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        190.2 |      85.3 | **84.5** |
| TPOT median (ms)          |     **34.3** |      35.4 |     80.9 |
| E2E median (ms)           |        218.4 | **112.7** |    143.4 |
| Throughput median (tok/s) |          5.2 |  **11.9** |      9.4 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.5 | **37.2** |   53.2 |
| TPOT median (ms)          |         34.5 | **26.7** |  383.6 |
| E2E median (ms)           |         74.3 | **56.5** |  441.1 |
| Throughput median (tok/s) |         19.6 | **23.3** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        179.3 |  **47.6** |   53.0 |
| TPOT median (ms)          |         19.1 |  **15.6** |   24.4 |
| E2E median (ms)           |        896.2 | **579.4** |  935.6 |
| Throughput median (tok/s) |         41.2 |  **60.2** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.8 |  **63.5** |   78.6 |
| TPOT median (ms)          |         23.8 |  **22.8** |  110.6 |
| E2E median (ms)           |        286.8 | **188.1** |  372.1 |
| Throughput median (tok/s) |         17.2 |  **23.9** |   13.4 |
| Correctness               |          99% |       99% |    99% |
