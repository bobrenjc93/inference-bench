# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     380.2s (6.3m) | `a102128` |
| vllm         |   1344.9s (22.4m) | `71b961d` |
| sglang       | **205.9s (3.4m)** | `3f4a338` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        278.4 |    167.8 | **153.3** |
| TPOT median (ms)          |         96.8 | **64.3** |      71.3 |
| E2E median (ms)           |        378.5 |    225.9 | **224.3** |
| Throughput median (tok/s) |          3.4 |  **6.7** |       5.3 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        300.9 | **203.6** |  222.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        426.1 | **225.1** |  362.0 |
| Throughput median (tok/s) |          2.3 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        675.9 |     183.4 | **161.8** |
| TPOT median (ms)          |         70.4 |  **68.9** |     105.5 |
| E2E median (ms)           |        745.1 | **242.5** |     269.0 |
| Throughput median (tok/s) |          1.6 |   **5.8** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        244.6 | **61.4** |   84.3 |
| TPOT median (ms)          |         35.9 | **28.4** |   50.4 |
| E2E median (ms)           |        278.0 | **83.3** |  149.6 |
| Throughput median (tok/s) |          4.5 | **14.7** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        331.6 |      72.5 | **71.9** |
| TPOT median (ms)          |         22.0 |  **14.9** |     21.9 |
| E2E median (ms)           |       1151.2 | **613.8** |    816.7 |
| Throughput median (tok/s) |         31.9 |  **59.2** |     42.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        366.3 | **137.8** |  138.7 |
| TPOT median (ms)          |         45.0 |  **35.3** |   49.8 |
| E2E median (ms)           |        595.8 | **278.1** |  364.3 |
| Throughput median (tok/s) |          8.8 |  **18.2** |   13.1 |
| Correctness               |          99% |       99% |    99% |
