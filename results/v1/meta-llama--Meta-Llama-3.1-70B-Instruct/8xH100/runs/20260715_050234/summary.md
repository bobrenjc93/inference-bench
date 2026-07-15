# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 14 2026

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
| torchinferno | **46.1s (0.8m)** | `96adc9d` |
| vllm         |    452.0s (7.5m) | `6472131` |
| sglang       |    223.2s (3.7m) | `0832d85` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        144.7 |      83.2 | **79.8** |
| TPOT median (ms)          |     **31.6** |      37.1 |     65.0 |
| E2E median (ms)           |        170.1 | **113.6** |    135.8 |
| Throughput median (tok/s) |          6.8 |  **11.6** |      9.9 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.1** | 68.7 |  126.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **73.3** | 84.7 |  209.6 |
| Throughput median (tok/s) |     **13.6** | 11.8 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.0 |  **75.5** |   83.5 |
| TPOT median (ms)          |     **34.3** |      35.2 |   81.9 |
| E2E median (ms)           |        220.8 | **101.2** |  145.9 |
| Throughput median (tok/s) |          5.1 |  **13.1** |    9.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.7 | **34.9** |   52.2 |
| TPOT median (ms)          |         34.9 | **22.9** |  408.2 |
| E2E median (ms)           |         74.7 | **52.6** |  497.5 |
| Throughput median (tok/s) |         19.7 | **24.9** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        182.8 |  **46.0** |   51.8 |
| TPOT median (ms)          |         19.3 |  **15.3** |   25.4 |
| E2E median (ms)           |        887.6 | **573.2** |  947.4 |
| Throughput median (tok/s) |         41.0 |  **61.6** |   38.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.5 |  **61.7** |   78.8 |
| TPOT median (ms)          |         24.0 |  **22.1** |  116.1 |
| E2E median (ms)           |        285.3 | **185.0** |  387.2 |
| Throughput median (tok/s) |         17.3 |  **24.6** |   13.0 |
| Correctness               |          99% |       99% |    99% |
