# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 29 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    604.7s (10.1m) | `07b0d6f` |
| vllm         |    642.0s (10.7m) | `a4e3cb4` |
| sglang       | **267.9s (4.5m)** | `a2b5ce2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        160.8 | **138.2** |  157.5 |
| TPOT median (ms)          |         47.2 |  **45.3** |   71.5 |
| E2E median (ms)           |        201.9 | **174.9** |  223.9 |
| Throughput median (tok/s) |          5.7 |   **8.2** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        251.7 | **199.0** |  219.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        269.1 | **224.6** |  368.5 |
| Throughput median (tok/s) |          3.7 |   **4.5** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        312.3 | **165.8** |  172.4 |
| TPOT median (ms)          |         58.1 |  **53.8** |  106.7 |
| E2E median (ms)           |        365.6 | **210.5** |  276.9 |
| Throughput median (tok/s) |          3.9 |   **6.4** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        191.8 | **62.1** |   86.1 |
| TPOT median (ms)          |         57.0 | **31.3** |   39.9 |
| E2E median (ms)           |        235.2 | **85.5** |  139.2 |
| Throughput median (tok/s) |          6.1 | **14.2** |    9.8 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        314.9 |      76.8 | **70.4** |
| TPOT median (ms)          |         23.2 |  **14.8** |     22.3 |
| E2E median (ms)           |       1121.3 | **619.6** |    833.4 |
| Throughput median (tok/s) |         32.2 |  **58.6** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        246.3 | **128.4** |  141.1 |
| TPOT median (ms)          |         37.1 |  **29.0** |   48.1 |
| E2E median (ms)           |        438.6 | **263.0** |  368.4 |
| Throughput median (tok/s) |         10.3 |  **18.4** |   12.9 |
| Correctness               |          98% |       99% |    99% |
