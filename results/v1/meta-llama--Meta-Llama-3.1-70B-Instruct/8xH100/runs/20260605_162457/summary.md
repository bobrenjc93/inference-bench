# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:07 AM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     444.6s (7.4m) | `89edcfc` |
| vllm         |   1413.2s (23.6m) | `6a89457` |
| sglang       | **212.5s (3.5m)** | `e4a7388` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        352.8 | **163.1** |  163.1 |
| TPOT median (ms)          |         56.4 |  **53.7** |   76.2 |
| E2E median (ms)           |        417.1 | **212.8** |  234.0 |
| Throughput median (tok/s) |          3.0 |   **6.9** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        295.7 | **203.3** |  211.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        412.1 | **222.7** |  352.6 |
| Throughput median (tok/s) |          2.4 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        746.8 |     179.0 | **166.7** |
| TPOT median (ms)          |     **62.1** |      69.6 |     111.4 |
| E2E median (ms)           |        804.1 | **243.2** |     259.4 |
| Throughput median (tok/s) |          1.4 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        367.3 | **59.5** |   81.9 |
| TPOT median (ms)          |         32.4 | **27.5** |   47.3 |
| E2E median (ms)           |        397.5 | **80.6** |  142.9 |
| Throughput median (tok/s) |          3.6 | **15.0** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        532.7 |  **71.7** |   75.7 |
| TPOT median (ms)          |         31.1 |  **14.7** |   23.8 |
| E2E median (ms)           |       1564.8 | **602.5** |  901.9 |
| Throughput median (tok/s) |         21.6 |  **59.7** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        459.0 | **135.3** |  139.7 |
| TPOT median (ms)          |         36.4 |  **33.1** |   51.7 |
| E2E median (ms)           |        719.1 | **272.4** |  378.2 |
| Throughput median (tok/s) |          6.4 |  **18.4** |   12.4 |
| Correctness               |          98% |       98% |    99% |
