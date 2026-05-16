# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, May 16 2026

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
| torchinferno |     244.2s (4.1m) | `db749af` |
| vllm         |   1019.1s (17.0m) | `d1586e1` |
| sglang       | **165.0s (2.8m)** | `0be5390` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        287.7 |    171.5 | **139.8** |
| TPOT median (ms)          |        151.3 | **64.1** |      74.0 |
| E2E median (ms)           |        376.9 |    231.9 | **208.4** |
| Throughput median (tok/s) |          3.8 |  **6.3** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        276.5 |     208.5 | **200.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        316.8 | **233.7** |     337.9 |
| Throughput median (tok/s) |          3.2 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        534.3 |     167.9 | **152.8** |
| TPOT median (ms)          |        133.3 |  **60.0** |     110.1 |
| E2E median (ms)           |        626.5 | **216.0** |     252.8 |
| Throughput median (tok/s) |          2.2 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        323.5 | **58.6** |   77.5 |
| TPOT median (ms)          |        130.7 | **27.2** |   67.8 |
| E2E median (ms)           |        422.8 | **79.9** |  156.3 |
| Throughput median (tok/s) |          3.5 | **15.4** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      68.4 | **65.0** |
| TPOT median (ms)          |            - |  **15.0** |     22.2 |
| E2E median (ms)           |            - | **617.0** |    816.0 |
| Throughput median (tok/s) |            - |  **58.7** |     42.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `illegal chunk header: bytearray(b'HTTP/1.1 500 Internal Server Error\r\n')`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        355.5 |     135.0 | **127.1** |
| TPOT median (ms)          |        103.8 |  **33.2** |      54.8 |
| E2E median (ms)           |        435.8 | **275.7** |     354.3 |
| Throughput median (tok/s) |          3.2 |  **18.2** |      13.2 |
| Correctness               |          98% |       99% |       99% |
