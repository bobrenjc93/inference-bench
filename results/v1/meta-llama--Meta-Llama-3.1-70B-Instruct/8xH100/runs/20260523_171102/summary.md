# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:03 AM PT, May 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     350.7s (5.8m) | `9f91b40` |
| vllm         |   1314.8s (21.9m) | `a0be71e` |
| sglang       | **214.0s (3.6m)** | `a5a64a3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        312.7 |     154.2 | **142.0** |
| TPOT median (ms)          |        149.1 |  **54.6** |      76.0 |
| E2E median (ms)           |        432.6 | **207.2** |     213.8 |
| Throughput median (tok/s) |          3.5 |   **7.2** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.2 |     200.2 | **199.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        310.0 | **221.3** |     333.3 |
| Throughput median (tok/s) |          3.2 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        743.4 |     177.3 | **160.9** |
| TPOT median (ms)          |        119.1 |  **64.2** |     100.8 |
| E2E median (ms)           |        890.5 | **231.6** |     254.1 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        326.4 | **58.7** |   77.0 |
| TPOT median (ms)          |        131.5 | **27.2** |   58.7 |
| E2E median (ms)           |        427.4 | **79.4** |  146.1 |
| Throughput median (tok/s) |          3.1 | **15.4** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        969.7 |  **69.1** |   70.9 |
| TPOT median (ms)          |         17.3 |  **15.0** |   22.1 |
| E2E median (ms)           |       1685.4 | **611.7** |  828.9 |
| Throughput median (tok/s) |         20.1 |  **58.6** |   42.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        527.9 |     131.9 | **130.1** |
| TPOT median (ms)          |         83.4 |  **32.2** |      51.5 |
| E2E median (ms)           |        749.2 | **270.3** |     355.2 |
| Throughput median (tok/s) |          6.3 |  **18.4** |      13.1 |
| Correctness               |          99% |       99% |       99% |
