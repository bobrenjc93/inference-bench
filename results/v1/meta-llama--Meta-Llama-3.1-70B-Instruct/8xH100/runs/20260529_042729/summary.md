# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:17 PM PT, May 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          1/4 |   **2/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **3/4** |     1/4 |
| **Total**        |         2/20 | **13/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     368.4s (6.1m) | `5d7f755` |
| vllm         |   1311.1s (21.9m) | `d63108f` |
| sglang       | **226.8s (3.8m)** | `fba083c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        235.7 |   164.7 | **150.4** |
| TPOT median (ms)          |     **59.0** |    61.1 |      75.3 |
| E2E median (ms)           |        296.5 |   219.5 | **218.7** |
| Throughput median (tok/s) |          4.4 | **6.7** |       5.4 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        285.9 | **184.3** |  217.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        332.6 | **209.8** |  346.5 |
| Throughput median (tok/s) |          3.0 |   **4.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        732.0 |     164.9 | **159.2** |
| TPOT median (ms)          |     **56.0** |      57.4 |     101.0 |
| E2E median (ms)           |        784.5 | **217.8** |     254.2 |
| Throughput median (tok/s) |          1.9 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        159.5 | **58.2** |   85.6 |
| TPOT median (ms)          |         28.1 | **27.9** |   47.7 |
| E2E median (ms)           |        180.6 | **78.3** |  141.9 |
| Throughput median (tok/s) |          6.6 | **15.5** |    9.6 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        553.6 |      76.8 | **76.0** |
| TPOT median (ms)          |         15.3 |  **15.0** |     23.6 |
| E2E median (ms)           |       1191.6 | **604.4** |    889.3 |
| Throughput median (tok/s) |         26.1 |  **58.6** |     39.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        393.3 | **129.8** |  137.7 |
| TPOT median (ms)          |     **31.7** |      32.3 |   49.5 |
| E2E median (ms)           |        557.2 | **265.9** |  370.1 |
| Throughput median (tok/s) |          8.4 |  **18.3** |   12.6 |
| Correctness               |          99% |       99% |    98% |
