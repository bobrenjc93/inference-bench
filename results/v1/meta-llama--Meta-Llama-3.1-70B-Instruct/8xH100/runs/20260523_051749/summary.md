# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:03 PM PT, May 22 2026

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
| torchinferno |     342.3s (5.7m) | `9f91b40` |
| vllm         |   1315.5s (21.9m) | `a5bbd81` |
| sglang       | **193.9s (3.2m)** | `c69844f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        293.3 |     156.9 | **138.3** |
| TPOT median (ms)          |        154.2 |  **59.7** |      77.4 |
| E2E median (ms)           |        395.6 | **208.9** |     212.3 |
| Throughput median (tok/s) |          3.8 |   **7.0** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.5 | **203.3** |  207.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        320.7 | **226.6** |  340.5 |
| Throughput median (tok/s) |          3.1 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        751.6 |     176.5 | **160.4** |
| TPOT median (ms)          |        114.1 |  **58.7** |     107.4 |
| E2E median (ms)           |        844.7 | **228.0** |     259.2 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.0 | **58.0** |   77.6 |
| TPOT median (ms)          |        130.5 | **26.8** |   59.4 |
| E2E median (ms)           |        468.6 | **77.7** |  145.1 |
| Throughput median (tok/s) |          2.8 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.9 | **67.7** |
| TPOT median (ms)          |            - |  **15.0** |     22.6 |
| E2E median (ms)           |            - | **605.5** |    835.0 |
| Throughput median (tok/s) |            - |  **59.4** |     42.0 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        428.1 |     132.7 | **130.3** |
| TPOT median (ms)          |         99.7 |  **32.0** |      53.4 |
| E2E median (ms)           |        507.4 | **269.3** |     358.4 |
| Throughput median (tok/s) |          2.8 |  **18.5** |      13.0 |
| Correctness               |          98% |       98% |       98% |
