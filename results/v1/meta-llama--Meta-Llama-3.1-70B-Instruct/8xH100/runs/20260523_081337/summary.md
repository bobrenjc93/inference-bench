# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 AM PT, May 23 2026

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
| torchinferno |     381.9s (6.4m) | `9f91b40` |
| vllm         |   1340.4s (22.3m) | `82536ac` |
| sglang       | **196.3s (3.3m)** | `19b60a4` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        290.3 |     147.3 | **143.2** |
| TPOT median (ms)          |        150.0 |  **51.4** |      74.5 |
| E2E median (ms)           |        399.0 | **198.4** |     211.1 |
| Throughput median (tok/s) |          3.5 |   **7.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        265.3 | **187.7** |  199.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        320.9 | **219.8** |  332.0 |
| Throughput median (tok/s) |          3.1 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        696.5 |     178.0 | **157.1** |
| TPOT median (ms)          |        138.3 |  **54.4** |      93.3 |
| E2E median (ms)           |        803.1 | **229.9** |     251.8 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        323.2 | **57.8** |   77.4 |
| TPOT median (ms)          |        127.7 | **27.1** |   52.6 |
| E2E median (ms)           |        425.4 | **79.0** |  143.0 |
| Throughput median (tok/s) |          3.4 | **15.4** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        931.9 |      70.1 | **66.2** |
| TPOT median (ms)          |         17.7 |  **15.1** |     22.4 |
| E2E median (ms)           |       1621.7 | **622.3** |    814.4 |
| Throughput median (tok/s) |         19.1 |  **58.5** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        501.5 | **128.2** |  128.7 |
| TPOT median (ms)          |         86.7 |  **29.6** |   48.6 |
| E2E median (ms)           |        714.0 | **269.9** |  350.5 |
| Throughput median (tok/s) |          6.1 |  **18.3** |   13.1 |
| Correctness               |          98% |       98% |    98% |
