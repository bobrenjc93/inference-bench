# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:50 PM PT, Jun 26 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **2/4** |    1/4 |          1/4 |
| self_consistency |   **3/4** |    0/4 |          0/4 |
| multi_turn       |   **3/4** |    1/4 |          0/4 |
| tree_of_thought  |   **4/4** |    0/4 |          0/4 |
| long_output      |   **3/4** |    1/4 |          0/4 |
| **Total**        | **15/20** |   3/20 |         1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| vllm         | **0.0s (0.0m)** | `9222148` |
| sglang       |     0.0s (0.0m) | `bc15017` |
| torchinferno |     0.0s (0.0m) | `36eae02` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     153.9 | **145.9** |        167.5 |
| TPOT median (ms)          |      59.2 |      80.9 |     **54.3** |
| E2E median (ms)           | **207.6** |     224.3 |        217.7 |
| Throughput median (tok/s) |   **7.1** |       5.2 |          5.4 |
| Correctness               |       98% |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **194.7** |  254.8 |        328.4 |
| TPOT median (ms)          |       0.0 |    0.0 |          0.0 |
| E2E median (ms)           | **282.7** |  414.6 |        354.8 |
| Throughput median (tok/s) |   **3.5** |    2.4 |          2.8 |
| Correctness               |      100% |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     184.2 | **175.7** |        432.3 |
| TPOT median (ms)          |  **69.4** |     121.9 |         69.9 |
| E2E median (ms)           | **240.0** |     286.9 |        504.6 |
| Throughput median (tok/s) |   **5.8** |       4.4 |          2.3 |
| Correctness               |       98% |       98% |          98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          |  **72.6** |   81.3 |        352.6 |
| TPOT median (ms)          |  **35.7** |   71.9 |         56.1 |
| E2E median (ms)           | **100.0** |  167.7 |        408.2 |
| Throughput median (tok/s) |  **12.3** |    8.4 |          3.7 |
| Correctness               |       97% |    97% |          96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      87.9 | **86.5** |        350.1 |
| TPOT median (ms)          |  **18.8** |     27.0 |         27.3 |
| E2E median (ms)           | **790.6** |   1031.2 |       1418.1 |
| Throughput median (tok/s) |  **47.0** |     34.0 |         25.9 |
| Correctness               |      100% |     100% |         100% |

## Cross-Benchmark Averages

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **138.6** |  148.8 |        326.2 |
| TPOT median (ms)          |  **36.6** |   60.3 |         41.5 |
| E2E median (ms)           | **324.1** |  424.9 |        580.6 |
| Throughput median (tok/s) |  **15.2** |   10.9 |          8.0 |
| Correctness               |       99% |    99% |          98% |
