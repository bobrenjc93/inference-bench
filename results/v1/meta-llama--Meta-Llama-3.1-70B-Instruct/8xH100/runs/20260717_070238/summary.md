# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 17 2026

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
| torchinferno | **41.2s (0.7m)** | `96adc9d` |
| vllm         |    388.1s (6.5m) | `26c909e` |
| sglang       |    174.5s (2.9m) | `e835512` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.2 |  **78.7** |   84.4 |
| TPOT median (ms)          |     **31.3** |      37.5 |   65.3 |
| E2E median (ms)           |        165.1 | **106.5** |  141.5 |
| Throughput median (tok/s) |          6.9 |  **12.6** |    9.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **52.4** | 78.1 |  131.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **68.5** | 94.9 |  213.6 |
| Throughput median (tok/s) |     **14.6** | 10.5 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        189.7 |      88.5 | **83.8** |
| TPOT median (ms)          |     **34.1** |      38.5 |     77.8 |
| E2E median (ms)           |        218.3 | **118.7** |    148.5 |
| Throughput median (tok/s) |          5.2 |  **11.8** |      8.9 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.5 | **38.0** |   53.1 |
| TPOT median (ms)          |         35.5 | **27.5** |  369.8 |
| E2E median (ms)           |         76.3 | **57.6** |  410.9 |
| Throughput median (tok/s) |         18.7 | **22.5** |    3.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.6 |  **48.9** |   53.4 |
| TPOT median (ms)          |         19.0 |  **16.0** |   23.9 |
| E2E median (ms)           |        840.7 | **587.0** |  906.3 |
| Throughput median (tok/s) |         41.0 |  **58.4** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.3 |  **66.4** |   81.2 |
| TPOT median (ms)          |         24.0 |  **23.9** |  107.4 |
| E2E median (ms)           |        273.8 | **192.9** |  364.2 |
| Throughput median (tok/s) |         17.3 |  **23.2** |   13.3 |
| Correctness               |          99% |       99% |    99% |
