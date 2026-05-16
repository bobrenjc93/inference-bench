# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 AM PT, May 16 2026

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
| torchinferno |     247.6s (4.1m) | `db749af` |
| vllm         |   1036.9s (17.3m) | `657b42b` |
| sglang       | **164.0s (2.7m)** | `af26b71` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.9 |     155.3 | **140.4** |
| TPOT median (ms)          |        150.2 |  **49.1** |      72.8 |
| E2E median (ms)           |        377.2 | **199.3** |     206.0 |
| Throughput median (tok/s) |          3.9 |   **7.4** |       5.9 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.9 | **187.1** |  193.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        315.0 | **209.2** |  323.9 |
| Throughput median (tok/s) |          3.2 |   **4.8** |    3.1 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        507.4 |     171.9 | **154.9** |
| TPOT median (ms)          |        105.8 |  **60.3** |     102.5 |
| E2E median (ms)           |        618.1 | **222.7** |     252.8 |
| Throughput median (tok/s) |          2.2 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.8 | **57.9** |   78.8 |
| TPOT median (ms)          |        131.3 | **26.6** |   55.0 |
| E2E median (ms)           |        453.2 | **78.6** |  142.7 |
| Throughput median (tok/s) |          2.8 | **15.9** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      76.8 | **66.0** |
| TPOT median (ms)          |            - |  **14.9** |     22.5 |
| E2E median (ms)           |            - | **631.8** |    838.9 |
| Throughput median (tok/s) |            - |  **58.4** |     41.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        360.0 |     129.8 | **126.7** |
| TPOT median (ms)          |         96.8 |  **30.2** |      50.5 |
| E2E median (ms)           |        440.9 | **268.3** |     352.9 |
| Throughput median (tok/s) |          3.0 |  **18.6** |      13.2 |
| Correctness               |          98% |       99% |       99% |
