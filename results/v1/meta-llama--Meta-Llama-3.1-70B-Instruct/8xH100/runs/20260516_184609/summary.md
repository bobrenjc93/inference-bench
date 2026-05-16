# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:01 AM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno | **144.8s (2.4m)** | `db749af` |
| vllm         |   1294.5s (21.6m) | `d1586e1` |
| sglang       |     174.3s (2.9m) | `57eb5bd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        311.9 |    171.5 | **149.2** |
| TPOT median (ms)          |        156.9 | **60.8** |      77.7 |
| E2E median (ms)           |        413.1 |    230.8 | **221.5** |
| Throughput median (tok/s) |          3.4 |  **6.4** |       5.3 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        306.2 | **150.5** |  222.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        332.4 | **225.1** |  359.9 |
| Throughput median (tok/s) |          3.0 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1151.6 |     191.4 | **167.1** |
| TPOT median (ms)          |        125.3 |  **72.7** |     110.2 |
| E2E median (ms)           |       1238.5 | **258.9** |     276.4 |
| Throughput median (tok/s) |          1.2 |   **5.4** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        413.1 | **60.9** |   82.7 |
| TPOT median (ms)          |        136.0 | **28.0** |   60.2 |
| E2E median (ms)           |        519.9 | **82.1** |  153.7 |
| Throughput median (tok/s) |          2.5 | **15.2** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1061.7 |      77.9 | **75.6** |
| TPOT median (ms)          |         15.7 |  **15.0** |     22.3 |
| E2E median (ms)           |       1675.6 | **626.4** |    843.3 |
| Throughput median (tok/s) |         19.9 |  **58.3** |     41.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        648.9 | **130.4** |  139.5 |
| TPOT median (ms)          |         86.8 |  **35.3** |   54.1 |
| E2E median (ms)           |        835.9 | **284.7** |  371.0 |
| Throughput median (tok/s) |          6.0 |  **18.0** |   12.6 |
| Correctness               |          99% |       99% |    99% |
