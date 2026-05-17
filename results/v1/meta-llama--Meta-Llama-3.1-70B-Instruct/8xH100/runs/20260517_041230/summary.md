# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:09 PM PT, May 16 2026

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
| torchinferno |     355.1s (5.9m) | `db749af` |
| vllm         |   1134.4s (18.9m) | `504a26c` |
| sglang       | **166.4s (2.8m)** | `229cade` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        285.2 |     150.8 | **133.4** |
| TPOT median (ms)          |        151.4 |  **52.2** |      71.8 |
| E2E median (ms)           |        371.2 | **197.5** |     201.4 |
| Throughput median (tok/s) |          3.9 |   **7.4** |       6.2 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        294.5 | **195.5** |  200.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        327.2 | **213.2** |  332.2 |
| Throughput median (tok/s) |          3.1 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        536.5 |     171.0 | **155.9** |
| TPOT median (ms)          |        185.5 |  **58.0** |      98.9 |
| E2E median (ms)           |        649.4 | **217.8** |     250.6 |
| Throughput median (tok/s) |          2.1 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        339.3 | **58.7** |   75.6 |
| TPOT median (ms)          |        130.9 | **27.0** |   56.5 |
| E2E median (ms)           |        436.3 | **79.0** |  149.2 |
| Throughput median (tok/s) |          3.1 | **15.5** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        756.6 |      68.2 | **64.3** |
| TPOT median (ms)          |         15.9 |  **15.0** |     21.7 |
| E2E median (ms)           |       1394.4 | **617.7** |    806.0 |
| Throughput median (tok/s) |         22.6 |  **59.1** |     43.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        442.4 |     128.8 | **126.0** |
| TPOT median (ms)          |         96.7 |  **30.4** |      49.8 |
| E2E median (ms)           |        635.7 | **265.0** |     347.9 |
| Throughput median (tok/s) |          6.9 |  **18.6** |      13.5 |
| Correctness               |          99% |       99% |       98% |
