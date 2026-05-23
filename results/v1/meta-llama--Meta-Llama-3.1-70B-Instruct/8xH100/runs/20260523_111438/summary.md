# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 AM PT, May 23 2026

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
| torchinferno |     403.8s (6.7m) | `9f91b40` |
| vllm         |   1336.5s (22.3m) | `3f3e862` |
| sglang       | **204.1s (3.4m)** | `a5a64a3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        278.2 |     149.8 | **143.3** |
| TPOT median (ms)          |        149.5 |  **54.3** |      74.7 |
| E2E median (ms)           |        371.9 | **201.4** |     214.6 |
| Throughput median (tok/s) |          3.9 |   **7.3** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        255.2 | **191.7** |  203.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        303.9 | **216.3** |  345.0 |
| Throughput median (tok/s) |          3.3 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        762.7 |     171.2 | **161.9** |
| TPOT median (ms)          |        123.8 |  **58.8** |     103.8 |
| E2E median (ms)           |        867.8 | **221.7** |     270.4 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        347.4 | **57.5** |   74.3 |
| TPOT median (ms)          |        129.2 | **27.1** |   64.3 |
| E2E median (ms)           |        455.6 | **78.4** |  140.9 |
| Throughput median (tok/s) |          2.9 | **15.7** |    9.7 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        709.9 |      72.8 | **66.4** |
| TPOT median (ms)          |         15.1 |  **15.0** |     22.5 |
| E2E median (ms)           |       1469.5 | **614.9** |    842.7 |
| Throughput median (tok/s) |         22.7 |  **59.2** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        470.7 | **128.6** |  129.9 |
| TPOT median (ms)          |         83.5 |  **31.0** |   53.1 |
| E2E median (ms)           |        693.7 | **266.5** |  362.7 |
| Throughput median (tok/s) |          6.8 |  **18.6** |   13.0 |
| Correctness               |          98% |       98% |    99% |
