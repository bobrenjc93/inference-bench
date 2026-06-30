# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    717.6s (12.0m) | `a45ef4a` |
| vllm         |    682.7s (11.4m) | `b8cb75b` |
| sglang       | **340.0s (5.7m)** | `bc8b3ab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        171.6 |   167.9 | **152.7** |
| TPOT median (ms)          |     **49.7** |    57.4 |      68.6 |
| E2E median (ms)           |    **214.4** |   221.9 |     223.4 |
| Throughput median (tok/s) |          5.4 | **6.6** |       5.3 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        223.7 | **203.8** |  213.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        241.3 | **229.2** |  368.1 |
| Throughput median (tok/s) |          4.1 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        310.7 |     168.0 | **167.1** |
| TPOT median (ms)          |         60.3 |  **57.1** |      98.4 |
| E2E median (ms)           |        365.4 | **219.6** |     263.5 |
| Throughput median (tok/s) |          3.9 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.2 | **65.0** |   84.8 |
| TPOT median (ms)          |         58.8 | **32.0** |   39.4 |
| E2E median (ms)           |        244.6 | **89.5** |  141.2 |
| Throughput median (tok/s) |          5.7 | **13.6** |    9.5 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        324.2 |      83.1 | **81.2** |
| TPOT median (ms)          |         23.7 |  **14.9** |     22.0 |
| E2E median (ms)           |       1157.6 | **640.2** |    868.6 |
| Throughput median (tok/s) |         31.2 |  **57.7** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        245.1 | **137.6** |  139.9 |
| TPOT median (ms)          |         38.5 |  **32.3** |   45.7 |
| E2E median (ms)           |        444.7 | **280.1** |  372.9 |
| Throughput median (tok/s) |         10.1 |  **17.7** |   12.8 |
| Correctness               |          99% |       99% |    98% |
