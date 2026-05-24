# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, May 23 2026

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
| torchinferno |     390.6s (6.5m) | `9f91b40` |
| vllm         |   1278.0s (21.3m) | `33d7cbe` |
| sglang       | **184.2s (3.1m)** | `af8f669` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        332.3 |     153.5 | **142.3** |
| TPOT median (ms)          |        149.8 |  **52.4** |      73.7 |
| E2E median (ms)           |        443.6 | **201.4** |     212.8 |
| Throughput median (tok/s) |          3.3 |   **7.4** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        298.8 | **188.6** |  199.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        324.6 | **209.5** |  336.6 |
| Throughput median (tok/s) |          3.1 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        698.7 |     171.5 | **160.5** |
| TPOT median (ms)          |        111.0 |  **55.1** |     110.4 |
| E2E median (ms)           |        819.1 | **222.6** |     259.6 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        327.5 | **58.3** |   75.5 |
| TPOT median (ms)          |        130.9 | **26.6** |   62.4 |
| E2E median (ms)           |        426.9 | **78.8** |  154.7 |
| Throughput median (tok/s) |          3.1 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      69.1 | **65.9** |
| TPOT median (ms)          |            - |  **15.0** |     22.4 |
| E2E median (ms)           |            - | **615.1** |    829.0 |
| Throughput median (tok/s) |            - |  **59.6** |     42.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        414.3 | **128.2** |  128.8 |
| TPOT median (ms)          |         97.9 |  **29.8** |   53.8 |
| E2E median (ms)           |        503.5 | **265.5** |  358.5 |
| Throughput median (tok/s) |          2.8 |  **18.7** |   13.1 |
| Correctness               |          98% |       99% |    99% |
