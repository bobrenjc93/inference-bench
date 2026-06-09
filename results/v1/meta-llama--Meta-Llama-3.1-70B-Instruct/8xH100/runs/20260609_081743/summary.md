# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jun 9 2026

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
| torchinferno |     463.5s (7.7m) | `e211b4b` |
| vllm         |   1317.3s (22.0m) | `e6fc848` |
| sglang       | **211.1s (3.5m)** | `cd6efcb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        310.7 |     155.3 | **152.0** |
| TPOT median (ms)          |         83.8 |  **54.5** |      82.5 |
| E2E median (ms)           |        388.8 | **207.3** |     223.9 |
| Throughput median (tok/s) |          3.4 |   **7.3** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        394.4 | **203.5** |  230.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        559.2 | **230.1** |  377.9 |
| Throughput median (tok/s) |          1.8 |   **4.3** |    2.6 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        733.6 |     172.6 | **157.8** |
| TPOT median (ms)          |         68.4 |  **56.4** |     104.5 |
| E2E median (ms)           |        806.2 | **220.1** |     263.9 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        417.2 | **62.6** |   88.5 |
| TPOT median (ms)          |         60.4 | **28.4** |   49.1 |
| E2E median (ms)           |        467.9 | **84.1** |  145.8 |
| Throughput median (tok/s) |          2.9 | **14.3** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        486.0 |      79.3 | **78.8** |
| TPOT median (ms)          |         21.3 |  **14.8** |     23.0 |
| E2E median (ms)           |       1255.1 | **612.3** |    870.4 |
| Throughput median (tok/s) |         28.4 |  **58.5** |     40.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        468.4 | **134.7** |  141.5 |
| TPOT median (ms)          |         46.8 |  **30.8** |   51.8 |
| E2E median (ms)           |        695.4 | **270.8** |  376.4 |
| Throughput median (tok/s) |          7.6 |  **18.1** |   12.5 |
| Correctness               |          99% |       99% |    98% |
