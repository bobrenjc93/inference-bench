# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, May 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **2/4** |     1/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         1/20 | **13/20** |    5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     355.0s (5.9m) | `f4c65f7` |
| vllm         |   1286.3s (21.4m) | `64e1218` |
| sglang       | **211.1s (3.5m)** | `d616b8e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        261.9 |   177.6 | **147.3** |
| TPOT median (ms)          |     **58.6** |    59.6 |      79.1 |
| E2E median (ms)           |        319.1 |   234.5 | **218.2** |
| Throughput median (tok/s) |          4.2 | **6.0** |       5.4 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        300.3 |     222.5 | **194.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        338.4 | **269.2** |     334.2 |
| Throughput median (tok/s) |          3.0 |   **3.7** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        743.4 |     179.0 | **170.3** |
| TPOT median (ms)          |         57.0 |  **48.8** |     101.2 |
| E2E median (ms)           |        793.8 | **220.9** |     279.1 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        174.7 | **60.0** |   83.5 |
| TPOT median (ms)          |         28.8 | **27.0** |   49.5 |
| E2E median (ms)           |        199.5 | **80.8** |  151.1 |
| Throughput median (tok/s) |          6.3 | **15.2** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        811.2 |      81.5 | **77.0** |
| TPOT median (ms)          |         15.2 |  **15.0** |     23.4 |
| E2E median (ms)           |       1280.4 | **617.5** |    887.6 |
| Throughput median (tok/s) |         23.7 |  **57.5** |     39.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        458.3 |     144.1 | **134.4** |
| TPOT median (ms)          |         31.9 |  **30.1** |      50.6 |
| E2E median (ms)           |        586.2 | **284.6** |     374.1 |
| Throughput median (tok/s) |          7.8 |  **17.7** |      12.5 |
| Correctness               |          98% |       99% |       99% |
