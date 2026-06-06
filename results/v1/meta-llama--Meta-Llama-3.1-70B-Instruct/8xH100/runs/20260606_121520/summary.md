# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     462.5s (7.7m) | `75bbe35` |
| vllm         |   1366.7s (22.8m) | `00d1fb7` |
| sglang       | **196.0s (3.3m)** | `9f28512` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        344.4 |     149.3 | **143.9** |
| TPOT median (ms)          |     **54.8** |      58.0 |      75.9 |
| E2E median (ms)           |        389.9 | **203.9** |     215.7 |
| Throughput median (tok/s) |          3.3 |   **7.5** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.1 | **187.4** |  196.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        403.1 | **210.8** |  329.6 |
| Throughput median (tok/s) |          2.5 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        763.5 |     172.2 | **163.1** |
| TPOT median (ms)          |     **55.6** |      68.8 |     104.3 |
| E2E median (ms)           |        854.2 | **230.6** |     268.8 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        385.8 | **58.4** |   78.2 |
| TPOT median (ms)          |         32.1 | **28.9** |   48.9 |
| E2E median (ms)           |        419.3 | **79.7** |  135.6 |
| Throughput median (tok/s) |          3.5 | **15.2** |    9.8 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        529.0 |      76.5 | **74.7** |
| TPOT median (ms)          |         31.7 |  **15.1** |     24.2 |
| E2E median (ms)           |       1592.2 | **621.2** |    912.0 |
| Throughput median (tok/s) |         21.4 |  **57.6** |     38.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        463.0 | **128.8** |  131.3 |
| TPOT median (ms)          |         34.9 |  **34.2** |   50.7 |
| E2E median (ms)           |        731.8 | **269.2** |  372.3 |
| Throughput median (tok/s) |          6.4 |  **18.2** |   12.4 |
| Correctness               |          98% |       99% |    99% |
