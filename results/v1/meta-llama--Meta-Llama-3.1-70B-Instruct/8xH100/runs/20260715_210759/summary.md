# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 PM PT, Jul 15 2026

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
| torchinferno | **42.2s (0.7m)** | `96adc9d` |
| vllm         |    337.1s (5.6m) | `3034c8d` |
| sglang       |    207.8s (3.5m) | `6714844` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        143.2 |      85.4 | **78.2** |
| TPOT median (ms)          |     **30.8** |      38.8 |     64.5 |
| E2E median (ms)           |        166.2 | **119.3** |    133.8 |
| Throughput median (tok/s) |          6.8 |  **11.9** |     10.1 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.0** | 73.2 |  125.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.3** | 92.9 |  213.2 |
| Throughput median (tok/s) |     **13.3** | 10.8 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.6 |  **76.6** |   84.4 |
| TPOT median (ms)          |     **34.4** |      34.9 |   86.9 |
| E2E median (ms)           |        218.4 | **111.4** |  153.5 |
| Throughput median (tok/s) |          5.1 |  **12.5** |    8.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         51.8 | **37.3** |   53.5 |
| TPOT median (ms)          |         34.3 | **27.2** |  409.9 |
| E2E median (ms)           |         73.1 | **56.3** |  449.9 |
| Throughput median (tok/s) |         20.2 | **22.8** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.1 |  **46.6** |   51.7 |
| TPOT median (ms)          |         19.3 |  **15.5** |   25.4 |
| E2E median (ms)           |        858.0 | **584.9** |  971.7 |
| Throughput median (tok/s) |         41.1 |  **60.1** |   38.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.5 |  **63.8** |   78.7 |
| TPOT median (ms)          |         23.8 |  **23.3** |  117.3 |
| E2E median (ms)           |        278.2 | **193.0** |  384.4 |
| Throughput median (tok/s) |         17.3 |  **23.6** |   13.0 |
| Correctness               |          99% |       99% |    98% |
