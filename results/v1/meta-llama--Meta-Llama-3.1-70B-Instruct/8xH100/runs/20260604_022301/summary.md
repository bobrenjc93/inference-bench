# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:07 PM PT, Jun 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     427.9s (7.1m) | `56b5b44` |
| vllm         |   1420.9s (23.7m) | `ceb0111` |
| sglang       | **199.8s (3.3m)** | `1a57145` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        309.1 | **149.1** |  153.8 |
| TPOT median (ms)          |         56.1 |  **48.4** |   68.1 |
| E2E median (ms)           |        360.5 | **193.8** |  219.2 |
| Throughput median (tok/s) |          3.5 |   **7.5** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        255.0 | **188.1** |  208.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        358.8 | **212.1** |  337.7 |
| Throughput median (tok/s) |          2.8 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        765.0 |     174.4 | **168.5** |
| TPOT median (ms)          |        103.8 |  **62.2** |      95.2 |
| E2E median (ms)           |        952.0 | **230.6** |     268.8 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        347.9 | **58.9** |   85.9 |
| TPOT median (ms)          |         31.5 | **28.1** |   37.8 |
| E2E median (ms)           |        376.9 | **79.9** |  134.2 |
| Throughput median (tok/s) |          3.3 | **14.8** |    9.8 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        477.1 |  **73.4** |   79.6 |
| TPOT median (ms)          |         28.6 |  **14.9** |   23.4 |
| E2E median (ms)           |       1477.6 | **610.0** |  875.7 |
| Throughput median (tok/s) |         24.2 |  **59.2** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        430.8 | **128.8** |  139.2 |
| TPOT median (ms)          |         44.0 |  **30.7** |   44.9 |
| E2E median (ms)           |        705.2 | **265.3** |  367.1 |
| Throughput median (tok/s) |          7.1 |  **18.5** |   12.5 |
| Correctness               |          98% |       99% |    98% |
