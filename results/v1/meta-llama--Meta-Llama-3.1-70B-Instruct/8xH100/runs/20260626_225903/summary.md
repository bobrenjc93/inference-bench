# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:59 PM PT, Jun 26 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/4** |    0/4 |          1/4 |
| self_consistency |   **2/4** |    0/4 |          1/4 |
| multi_turn       |   **3/4** |    0/4 |          1/4 |
| tree_of_thought  |   **4/4** |    0/4 |          0/4 |
| long_output      |   **4/4** |    0/4 |          0/4 |
| **Total**        | **16/20** |   0/20 |         3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `9222148` |
| sglang       |     0.0s (0.0m) | `bc15017` |
| torchinferno |     0.0s (0.0m) | `b7a4735` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **151.9** |  162.6 |        167.6 |
| TPOT median (ms)          |      56.9 |   77.8 |     **53.1** |
| E2E median (ms)           | **203.0** |  237.3 |        217.0 |
| Throughput median (tok/s) |   **7.0** |    5.0 |          5.3 |
| Correctness               |       98% |    98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |     175.8 |  234.1 |    **150.8** |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **263.4** |  394.4 |        353.7 |
| Throughput median (tok/s) |   **3.8** |    2.5 |          2.8 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **130.3** |  170.1 |        593.2 |
| TPOT median (ms)          |      83.3 |  119.8 |     **66.1** |
| E2E median (ms)           | **222.2** |  286.2 |        647.3 |
| Throughput median (tok/s) |   **5.9** |    4.5 |          2.1 |
| Correctness               |       98% |    98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **72.7** |   77.4 |        296.7 |
| TPOT median (ms)          | **35.3** |   66.8 |         55.4 |
| E2E median (ms)           | **99.0** |  158.5 |        332.1 |
| Throughput median (tok/s) | **12.4** |    8.7 |          4.1 |
| Correctness               |      97% |    97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **77.5** |   90.4 |        329.2 |
| TPOT median (ms)          |  **18.8** |   27.0 |         27.9 |
| E2E median (ms)           | **740.7** | 1039.1 |       1537.0 |
| Throughput median (tok/s) |  **47.8** |   34.1 |         25.2 |
| Correctness               |      100% |   100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **121.6** |  146.9 |        307.5 |
| TPOT median (ms)          |  **38.9** |   58.3 |         40.5 |
| E2E median (ms)           | **305.6** |  423.1 |        617.4 |
| Throughput median (tok/s) |  **15.4** |   11.0 |          7.9 |
| Correctness               |       99% |    98% |          99% |
