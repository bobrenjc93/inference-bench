# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:09 AM PT, May 17 2026

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
| torchinferno |     253.2s (4.2m) | `13d21ac` |
| vllm         |   1110.5s (18.5m) | `599e75f` |
| sglang       | **165.7s (2.8m)** | `89e501c` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        252.0 |    159.1 | **133.4** |
| TPOT median (ms)          |        151.7 | **55.4** |      74.4 |
| E2E median (ms)           |        357.0 |    213.4 | **201.8** |
| Throughput median (tok/s) |          4.2 |  **6.9** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        274.0 |     207.5 | **200.7** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        290.0 | **230.6** |     333.6 |
| Throughput median (tok/s) |          3.4 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        536.8 |     171.3 | **156.7** |
| TPOT median (ms)          |        132.7 |  **57.2** |     107.0 |
| E2E median (ms)           |        640.9 | **223.1** |     256.7 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        311.6 | **57.3** |   77.6 |
| TPOT median (ms)          |        130.4 | **26.6** |   51.0 |
| E2E median (ms)           |        415.6 | **77.5** |  139.5 |
| Throughput median (tok/s) |          3.6 | **15.6** |   10.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      67.4 | **63.9** |
| TPOT median (ms)          |            - |  **15.0** |     22.4 |
| E2E median (ms)           |            - | **603.1** |    828.3 |
| Throughput median (tok/s) |            - |  **59.3** |     42.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        343.6 |     132.5 | **126.5** |
| TPOT median (ms)          |        103.7 |  **30.8** |      51.0 |
| E2E median (ms)           |        425.9 | **269.5** |     352.0 |
| Throughput median (tok/s) |          3.3 |  **18.5** |      13.4 |
| Correctness               |          98% |       99% |       99% |
