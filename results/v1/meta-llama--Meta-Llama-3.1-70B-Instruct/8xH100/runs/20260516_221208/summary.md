# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:08 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     330.6s (5.5m) | `db749af` |
| vllm         |   1045.1s (17.4m) | `36e74c9` |
| sglang       | **168.0s (2.8m)** | `9869ef0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        282.8 |    161.0 | **148.5** |
| TPOT median (ms)          |        148.8 | **58.2** |      73.9 |
| E2E median (ms)           |        369.9 |    220.3 | **216.2** |
| Throughput median (tok/s) |          4.0 |  **6.2** |       5.6 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        273.7 |     202.2 | **198.1** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        299.4 | **224.0** |     335.2 |
| Throughput median (tok/s) |          3.3 |   **4.5** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        552.1 |     176.4 | **153.9** |
| TPOT median (ms)          |        132.3 |  **57.8** |     100.9 |
| E2E median (ms)           |        645.2 | **224.0** |     251.1 |
| Throughput median (tok/s) |          2.0 |   **6.1** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        340.4 | **57.6** |   75.7 |
| TPOT median (ms)          |        130.2 | **26.8** |   53.8 |
| E2E median (ms)           |        437.2 | **78.0** |  138.2 |
| Throughput median (tok/s) |          2.8 | **15.6** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      66.6 | **65.8** |
| TPOT median (ms)          |            - |  **14.9** |     22.6 |
| E2E median (ms)           |            - | **595.9** |    836.0 |
| Throughput median (tok/s) |            - |  **59.8** |     41.9 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        362.2 |     132.8 | **128.4** |
| TPOT median (ms)          |        102.8 |  **31.5** |      50.3 |
| E2E median (ms)           |        437.9 | **268.4** |     355.3 |
| Throughput median (tok/s) |          3.0 |  **18.4** |      13.1 |
| Correctness               |          98% |       99% |       98% |
