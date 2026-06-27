# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:07 PM PT, Jun 26 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **2/4** |    1/4 |          1/4 |
| self_consistency |   **2/4** |    0/4 |          1/4 |
| multi_turn       |   **3/4** |    1/4 |          0/4 |
| tree_of_thought  |   **4/4** |    0/4 |          0/4 |
| long_output      |   **4/4** |    0/4 |          0/4 |
| **Total**        | **15/20** |   2/20 |         2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `9222148` |
| sglang       |     0.0s (0.0m) | `bc15017` |
| torchinferno |     0.0s (0.0m) | `89bb0d3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     155.9 | **150.1** |        162.9 |
| TPOT median (ms)          |      59.1 |      79.8 |     **54.6** |
| E2E median (ms)           | **200.5** |     229.3 |        211.5 |
| Throughput median (tok/s) |   **6.9** |       5.2 |          5.3 |
| Correctness               |       98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |     167.6 |  215.7 |    **164.3** |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **288.6** |  419.3 |        339.6 |
| Throughput median (tok/s) |   **3.5** |    2.4 |          2.9 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     178.3 | **171.6** |        502.5 |
| TPOT median (ms)          |  **60.0** |     104.5 |         66.2 |
| E2E median (ms)           | **231.2** |     284.9 |        552.6 |
| Throughput median (tok/s) |   **5.9** |       4.3 |          2.2 |
| Correctness               |       98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **72.6** |   77.0 |        318.1 |
| TPOT median (ms)          |  **35.3** |   68.1 |         57.3 |
| E2E median (ms)           | **100.1** |  150.7 |        362.4 |
| Throughput median (tok/s) |  **12.4** |    8.8 |          3.8 |
| Correctness               |       97% |    97% |          97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **88.7** |   91.1 |        306.9 |
| TPOT median (ms)          |  **18.9** |   26.2 |         27.4 |
| E2E median (ms)           | **790.5** |  989.1 |       1406.6 |
| Throughput median (tok/s) |  **46.8** |   34.5 |         28.2 |
| Correctness               |      100% |   100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **132.6** |  141.1 |        290.9 |
| TPOT median (ms)          |  **34.7** |   55.7 |         41.1 |
| E2E median (ms)           | **322.2** |  414.7 |        574.5 |
| Throughput median (tok/s) |  **15.1** |   11.0 |          8.5 |
| Correctness               |       99% |    99% |          98% |
