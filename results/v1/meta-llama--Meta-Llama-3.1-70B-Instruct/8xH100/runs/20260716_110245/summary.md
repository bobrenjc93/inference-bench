# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 16 2026

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
| torchinferno | **38.9s (0.6m)** | `96adc9d` |
| vllm         |    353.4s (5.9m) | `530852f` |
| sglang       |    206.7s (3.4m) | `b296e1a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        139.8 |  **75.5** |   79.2 |
| TPOT median (ms)          |     **32.2** |      37.8 |   68.1 |
| E2E median (ms)           |        165.1 | **106.5** |  133.7 |
| Throughput median (tok/s) |          7.1 |  **12.5** |   10.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.9** | 70.5 |  131.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **71.7** | 87.4 |  207.0 |
| Throughput median (tok/s) |     **13.9** | 11.4 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        188.2 |      98.0 | **84.1** |
| TPOT median (ms)          |     **35.4** |      45.7 |     87.1 |
| E2E median (ms)           |        217.8 | **137.0** |    146.9 |
| Throughput median (tok/s) |          5.2 |  **10.2** |      9.0 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.7 | **38.2** |   52.6 |
| TPOT median (ms)          |         35.1 | **28.4** |  381.3 |
| E2E median (ms)           |         75.1 | **58.6** |  458.1 |
| Throughput median (tok/s) |         19.5 | **22.4** |    3.1 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.8 |  **47.9** |   52.0 |
| TPOT median (ms)          |         19.0 |  **15.8** |   25.2 |
| E2E median (ms)           |        870.1 | **590.9** |  969.2 |
| Throughput median (tok/s) |         40.6 |  **59.4** |   38.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.7 |  **66.0** |   79.9 |
| TPOT median (ms)          |     **24.4** |      25.5 |  112.3 |
| E2E median (ms)           |        280.0 | **196.1** |  383.0 |
| Throughput median (tok/s) |         17.3 |  **23.2** |   13.1 |
| Correctness               |          99% |       99% |    98% |
