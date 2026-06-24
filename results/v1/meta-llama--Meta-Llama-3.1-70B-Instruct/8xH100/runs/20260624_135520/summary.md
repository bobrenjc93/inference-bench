# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:23 AM PT, Jun 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **20.0s (0.3m)** | `f0c333d` |
| vllm         |    532.2s (8.9m) | `62890e2` |
| sglang       |    214.6s (3.6m) | `09b808a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        193.5 |     150.4 | **148.9** |
| TPOT median (ms)          |         56.8 |  **44.0** |      78.7 |
| E2E median (ms)           |        255.8 | **189.7** |     223.1 |
| Throughput median (tok/s) |          5.0 |   **7.4** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        279.9 | **184.3** |  229.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        300.0 | **217.3** |  376.4 |
| Throughput median (tok/s) |          3.3 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        404.8 | **175.4** |  179.8 |
| TPOT median (ms)          |         70.2 |  **55.3** |  101.5 |
| E2E median (ms)           |        478.0 | **227.9** |  284.4 |
| Throughput median (tok/s) |          2.4 |   **6.1** |    4.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        307.5 | **64.8** |   85.8 |
| TPOT median (ms)          |         43.3 | **30.4** |   60.8 |
| E2E median (ms)           |        354.6 | **87.8** |  148.1 |
| Throughput median (tok/s) |          3.7 | **13.6** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        284.3 |      89.2 | **87.3** |
| TPOT median (ms)          |         30.5 |  **15.0** |     22.5 |
| E2E median (ms)           |       1429.3 | **653.6** |    878.7 |
| Throughput median (tok/s) |         26.1 |  **55.7** |     40.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.0 | **132.8** |  146.3 |
| TPOT median (ms)          |         40.2 |  **28.9** |   52.7 |
| E2E median (ms)           |        563.5 | **275.3** |  382.2 |
| Throughput median (tok/s) |          8.1 |  **17.5** |   12.5 |
| Correctness               |          99% |       99% |    99% |
