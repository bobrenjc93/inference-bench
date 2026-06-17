# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 17 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     415.4s (6.9m) | `ccca738` |
| vllm         |     479.3s (8.0m) | `06e1e08` |
| sglang       | **252.2s (4.2m)** | `735a256` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        390.2 | **139.8** |  150.5 |
| TPOT median (ms)          |         56.7 |  **51.7** |   76.1 |
| E2E median (ms)           |        437.7 | **186.9** |  224.5 |
| Throughput median (tok/s) |          3.1 |   **7.9** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        289.4 | **176.8** |  216.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        410.6 | **201.0** |  357.9 |
| Throughput median (tok/s) |          2.4 |   **5.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        728.0 |     165.0 | **160.7** |
| TPOT median (ms)          |         65.1 |  **52.4** |     102.9 |
| E2E median (ms)           |        795.7 | **208.8** |     258.7 |
| Throughput median (tok/s) |          1.7 |   **6.5** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        202.6 | **60.3** |   80.6 |
| TPOT median (ms)          |         31.9 | **29.7** |   41.9 |
| E2E median (ms)           |        243.7 | **82.4** |  131.8 |
| Throughput median (tok/s) |          5.7 | **14.7** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        321.2 |      72.6 | **71.3** |
| TPOT median (ms)          |         21.6 |  **14.9** |     22.6 |
| E2E median (ms)           |       1079.4 | **617.9** |    829.8 |
| Throughput median (tok/s) |         32.8 |  **58.7** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        386.3 | **122.9** |  136.0 |
| TPOT median (ms)          |         35.1 |  **29.8** |   48.7 |
| E2E median (ms)           |        593.4 | **259.4** |  360.5 |
| Throughput median (tok/s) |          9.1 |  **18.6** |   13.0 |
| Correctness               |          98% |       99% |    99% |
