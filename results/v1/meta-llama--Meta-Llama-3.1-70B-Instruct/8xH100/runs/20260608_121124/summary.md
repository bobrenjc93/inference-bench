# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, Jun 8 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     341.3s (5.7m) | `0c65c8b` |
| vllm         |   1278.3s (21.3m) | `980796c` |
| sglang       | **198.2s (3.3m)** | `6394a8b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        515.4 |     160.0 | **154.4** |
| TPOT median (ms)          |         92.4 |  **56.8** |      76.2 |
| E2E median (ms)           |        599.7 | **212.0** |     229.5 |
| Throughput median (tok/s) |          2.4 |   **6.8** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        397.6 | **205.8** |  212.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        538.0 | **230.4** |  346.0 |
| Throughput median (tok/s) |          1.9 |   **4.3** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        654.7 |     176.4 | **170.2** |
| TPOT median (ms)          |         65.9 |  **63.3** |     104.3 |
| E2E median (ms)           |        719.3 | **229.7** |     269.4 |
| Throughput median (tok/s) |          1.7 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        500.6 | **63.1** |   85.7 |
| TPOT median (ms)          |         60.8 | **28.4** |   46.0 |
| E2E median (ms)           |        528.6 | **84.8** |  148.2 |
| Throughput median (tok/s) |          2.8 | **14.1** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        498.6 |      79.8 | **77.0** |
| TPOT median (ms)          |         22.9 |  **14.7** |     23.5 |
| E2E median (ms)           |       1299.0 | **641.1** |    874.0 |
| Throughput median (tok/s) |         26.9 |  **58.1** |     39.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        513.4 | **137.0** |  140.0 |
| TPOT median (ms)          |         48.4 |  **32.6** |   50.0 |
| E2E median (ms)           |        736.9 | **279.6** |  373.4 |
| Throughput median (tok/s) |          7.1 |  **17.9** |   12.4 |
| Correctness               |          98% |       99% |    99% |
