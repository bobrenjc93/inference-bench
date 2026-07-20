# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 20 2026

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
| torchinferno | **51.8s (0.9m)** | `96adc9d` |
| vllm         |    294.0s (4.9m) | `37bf988` |
| sglang       |    224.7s (3.7m) | `2f14d6c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        139.6 | **73.3** |   87.0 |
| TPOT median (ms)          |     **31.9** |     36.5 |   70.7 |
| E2E median (ms)           |        163.9 | **99.5** |  147.1 |
| Throughput median (tok/s) |          7.1 | **12.7** |    9.3 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.4** | 77.9 |  174.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.7** | 97.4 |  246.5 |
| Throughput median (tok/s) |     **13.2** | 10.3 |    4.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.4 |  **74.3** |   93.8 |
| TPOT median (ms)          |     **35.3** |      42.6 |   79.0 |
| E2E median (ms)           |        222.3 | **103.9** |  157.0 |
| Throughput median (tok/s) |          5.1 |  **11.8** |    8.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.2 | **36.2** |   68.3 |
| TPOT median (ms)          |         34.7 | **23.7** |  373.7 |
| E2E median (ms)           |         73.9 | **54.8** |  486.0 |
| Throughput median (tok/s) |         19.8 | **23.8** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.3 |  **46.1** |   57.3 |
| TPOT median (ms)          |         18.8 |  **15.5** |   27.5 |
| E2E median (ms)           |        827.0 | **578.5** | 1055.9 |
| Throughput median (tok/s) |         41.6 |  **60.4** |   35.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.4 |  **61.5** |   96.2 |
| TPOT median (ms)          |         24.2 |  **23.7** |  110.2 |
| E2E median (ms)           |        272.6 | **186.8** |  418.5 |
| Throughput median (tok/s) |         17.4 |  **23.8** |   12.0 |
| Correctness               |          99% |       99% |    99% |
