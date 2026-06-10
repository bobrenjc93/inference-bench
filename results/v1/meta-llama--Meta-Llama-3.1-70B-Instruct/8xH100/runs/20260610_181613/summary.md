# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 AM PT, Jun 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     387.9s (6.5m) | `a870596` |
| vllm         |   1372.8s (22.9m) | `d1bcb4b` |
| sglang       | **199.9s (3.3m)** | `21647f1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        283.9 |     155.7 | **152.9** |
| TPOT median (ms)          |         95.2 |  **59.2** |      76.4 |
| E2E median (ms)           |        371.4 | **212.8** |     221.8 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        449.1 | **193.6** |  203.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        575.9 | **255.8** |  337.3 |
| Throughput median (tok/s) |          1.7 |   **3.9** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        708.9 |     187.2 | **167.7** |
| TPOT median (ms)          |     **67.8** |      68.3 |     101.0 |
| E2E median (ms)           |        782.1 | **243.2** |     270.3 |
| Throughput median (tok/s) |          1.7 |   **5.7** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        406.6 | **59.2** |   83.5 |
| TPOT median (ms)          |         63.0 | **28.3** |   51.2 |
| E2E median (ms)           |        456.5 | **81.3** |  147.8 |
| Throughput median (tok/s) |          3.0 | **15.3** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.6 |  **66.3** |   83.1 |
| TPOT median (ms)          |         26.6 |  **14.8** |   23.4 |
| E2E median (ms)           |       1247.5 | **599.4** |  878.0 |
| Throughput median (tok/s) |         30.9 |  **60.3** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        407.4 | **132.4** |  138.1 |
| TPOT median (ms)          |         50.5 |  **34.1** |   50.4 |
| E2E median (ms)           |        686.7 | **278.5** |  371.0 |
| Throughput median (tok/s) |          8.1 |  **18.5** |   12.5 |
| Correctness               |          98% |       98% |    99% |
