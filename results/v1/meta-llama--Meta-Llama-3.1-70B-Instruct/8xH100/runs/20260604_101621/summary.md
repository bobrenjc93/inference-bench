# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **15/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     369.3s (6.2m) | `a9e2f5a` |
| vllm         |   1371.2s (22.9m) | `d0975a4` |
| sglang       | **205.5s (3.4m)** | `a5c7e9d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        430.2 |   168.4 | **145.4** |
| TPOT median (ms)          |     **55.3** |    65.3 |      72.4 |
| E2E median (ms)           |        483.8 |   227.6 | **210.6** |
| Throughput median (tok/s) |          3.2 | **6.6** |       5.7 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.9 | **183.6** |  204.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        411.1 | **206.5** |  334.9 |
| Throughput median (tok/s) |          2.4 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        865.3 |     174.7 | **166.6** |
| TPOT median (ms)          |        119.3 |  **74.7** |     100.1 |
| E2E median (ms)           |        960.9 | **233.7** |     263.6 |
| Throughput median (tok/s) |          1.3 |   **5.9** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        336.1 | **61.2** |   81.5 |
| TPOT median (ms)          |         33.3 | **29.5** |   44.8 |
| E2E median (ms)           |        364.5 | **84.1** |  141.6 |
| Throughput median (tok/s) |          3.5 | **14.3** |    9.7 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        478.5 |  **75.2** |   76.3 |
| TPOT median (ms)          |         28.0 |  **14.8** |   23.5 |
| E2E median (ms)           |       1479.9 | **614.7** |  882.6 |
| Throughput median (tok/s) |         24.1 |  **58.7** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        480.2 | **132.6** |  134.8 |
| TPOT median (ms)          |         47.2 |  **36.9** |   48.1 |
| E2E median (ms)           |        740.0 | **273.3** |  366.7 |
| Throughput median (tok/s) |          6.9 |  **18.1** |   12.6 |
| Correctness               |          98% |       98% |    99% |
