# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **14/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **37.3s (0.6m)** | `96adc9d` |
| vllm         |    220.8s (3.7m) | `b3cfca9` |
| sglang       |    163.2s (2.7m) | `9fec359` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        142.8 |      79.3 | **78.8** |
| TPOT median (ms)          |     **32.8** |      38.2 |     66.8 |
| E2E median (ms)           |        168.7 | **110.7** |    134.0 |
| Throughput median (tok/s) |          7.0 |  **12.0** |      9.9 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **50.9** | 73.7 |  121.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **67.9** | 90.1 |  203.1 |
| Throughput median (tok/s) |     **14.7** | 11.1 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.0 |  **73.5** |   83.1 |
| TPOT median (ms)          |         35.7 |  **35.5** |   74.3 |
| E2E median (ms)           |        223.7 | **100.4** |  142.4 |
| Throughput median (tok/s) |          5.0 |  **12.8** |    9.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.3 | **38.4** |   53.3 |
| TPOT median (ms)          |         34.7 | **28.6** |  400.7 |
| E2E median (ms)           |         76.6 | **58.5** |  454.1 |
| Throughput median (tok/s) |         19.8 | **21.6** |    3.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.0 |  **47.1** |   52.9 |
| TPOT median (ms)          |         19.6 |  **15.6** |   24.6 |
| E2E median (ms)           |        876.4 | **577.7** |  954.0 |
| Throughput median (tok/s) |         40.0 |  **60.2** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.8 |  **62.4** |   78.0 |
| TPOT median (ms)          |         24.6 |  **23.6** |  113.3 |
| E2E median (ms)           |        282.7 | **187.5** |  377.5 |
| Throughput median (tok/s) |         17.3 |  **23.5** |   13.2 |
| Correctness               |          98% |       99% |    99% |
