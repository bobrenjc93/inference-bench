# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          1/4 |   **2/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **14/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     376.9s (6.3m) | `db749af` |
| vllm         |   1071.0s (17.9m) | `504a26c` |
| sglang       | **168.0s (2.8m)** | `229cade` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        288.3 |    160.6 | **137.4** |
| TPOT median (ms)          |        150.4 | **52.6** |      74.8 |
| E2E median (ms)           |        374.1 |    215.4 | **205.0** |
| Throughput median (tok/s) |          4.0 |  **6.8** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |    **191.8** |     199.3 |  197.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        328.8 | **245.1** |  326.1 |
| Throughput median (tok/s) |          3.0 |   **4.1** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        553.0 |     168.8 | **156.0** |
| TPOT median (ms)          |        160.2 |  **60.4** |      99.4 |
| E2E median (ms)           |        645.2 | **221.5** |     256.8 |
| Throughput median (tok/s) |          2.0 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        366.9 | **58.3** |   75.5 |
| TPOT median (ms)          |        130.1 | **27.3** |   61.1 |
| E2E median (ms)           |        474.3 | **78.9** |  151.7 |
| Throughput median (tok/s) |          2.8 | **15.3** |    9.5 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      67.4 | **66.6** |
| TPOT median (ms)          |            - |  **15.0** |     22.6 |
| E2E median (ms)           |            - | **610.0** |    835.1 |
| Throughput median (tok/s) |            - |  **59.2** |     41.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        350.0 |     130.9 | **126.6** |
| TPOT median (ms)          |        110.2 |  **31.1** |      51.6 |
| E2E median (ms)           |        455.6 | **274.2** |     354.9 |
| Throughput median (tok/s) |          3.0 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       98% |
