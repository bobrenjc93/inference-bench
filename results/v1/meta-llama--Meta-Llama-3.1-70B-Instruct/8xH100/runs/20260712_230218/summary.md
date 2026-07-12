# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 12 2026

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
| torchinferno | **34.0s (0.6m)** | `96adc9d` |
| vllm         |    283.8s (4.7m) | `4c81772` |
| sglang       |    153.1s (2.6m) | `c616d5a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        143.0 |      78.2 | **76.7** |
| TPOT median (ms)          |     **30.8** |      42.0 |     65.0 |
| E2E median (ms)           |        166.8 | **110.2** |    131.4 |
| Throughput median (tok/s) |          6.9 |  **11.8** |     10.3 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **62.1** | 69.9 |  121.0 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **81.6** | 87.4 |  195.6 |
| Throughput median (tok/s) |     **12.3** | 11.4 |    5.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.3 | **72.3** |   83.7 |
| TPOT median (ms)          |     **34.4** |     37.6 |   72.7 |
| E2E median (ms)           |        223.8 | **99.5** |  142.1 |
| Throughput median (tok/s) |          5.0 | **13.8** |    9.3 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.9 | **35.5** |   52.0 |
| TPOT median (ms)          |         34.9 | **23.8** |  466.9 |
| E2E median (ms)           |         74.8 | **54.7** |  458.7 |
| Throughput median (tok/s) |         19.1 | **24.4** |    3.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        192.9 |  **46.8** |   53.4 |
| TPOT median (ms)          |         19.0 |  **15.4** |   23.8 |
| E2E median (ms)           |        864.6 | **575.5** |  882.0 |
| Throughput median (tok/s) |         41.8 |  **61.2** |   40.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        129.5 |  **60.6** |   77.4 |
| TPOT median (ms)          |         23.8 |  **23.7** |  125.7 |
| E2E median (ms)           |        282.3 | **185.5** |  362.0 |
| Throughput median (tok/s) |         17.0 |  **24.5** |   13.6 |
| Correctness               |          99% |       98% |    99% |
