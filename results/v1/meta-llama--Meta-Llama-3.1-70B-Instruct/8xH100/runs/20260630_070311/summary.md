# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 AM PT, Jun 30 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    719.5s (12.0m) | `7cbb5fe` |
| vllm         |    626.4s (10.4m) | `8cc2423` |
| sglang       | **344.3s (5.7m)** | `4b4b4af` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        164.9 |     144.6 | **142.9** |
| TPOT median (ms)          |     **49.2** |      55.0 |      67.5 |
| E2E median (ms)           |        206.6 | **195.7** |     211.2 |
| Throughput median (tok/s) |          5.6 |   **7.5** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        240.5 | **181.3** |  204.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        258.5 | **225.4** |  358.2 |
| Throughput median (tok/s) |          3.9 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.2 | **157.3** |  161.2 |
| TPOT median (ms)          |         56.2 |  **51.1** |   92.4 |
| E2E median (ms)           |        339.1 | **200.6** |  252.6 |
| Throughput median (tok/s) |          4.4 |   **6.9** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        201.6 | **60.3** |   82.2 |
| TPOT median (ms)          |         58.0 | **32.2** |   40.8 |
| E2E median (ms)           |        244.9 | **84.9** |  131.4 |
| Throughput median (tok/s) |          5.7 | **14.4** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        281.0 |      73.0 | **72.1** |
| TPOT median (ms)          |         23.5 |  **15.0** |     22.2 |
| E2E median (ms)           |       1165.3 | **601.7** |    820.7 |
| Throughput median (tok/s) |         32.6 |  **59.3** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        235.3 | **123.3** |  132.5 |
| TPOT median (ms)          |         37.4 |  **30.7** |   44.6 |
| E2E median (ms)           |        442.9 | **261.7** |  354.8 |
| Throughput median (tok/s) |         10.4 |  **18.5** |   13.2 |
| Correctness               |          99% |       99% |    99% |
