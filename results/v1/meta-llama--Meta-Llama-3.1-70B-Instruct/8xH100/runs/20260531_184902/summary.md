# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:49 AM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     253.7s (4.2m) | `9106c2f` |
| vllm         |   1233.3s (20.6m) | `6bdabba` |
| sglang       | **181.7s (3.0m)** | `c062201` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        245.0 | **154.1** |  155.3 |
| TPOT median (ms)          |     **45.9** |      56.3 |   80.8 |
| E2E median (ms)           |        281.9 | **206.3** |  229.0 |
| Throughput median (tok/s) |          4.7 |   **7.0** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        359.8 |     210.6 | **209.7** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        453.9 | **232.9** |     351.1 |
| Throughput median (tok/s) |          2.2 |   **4.3** |       2.8 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        844.7 |     176.3 | **165.3** |
| TPOT median (ms)          |         78.8 |  **53.8** |     110.9 |
| E2E median (ms)           |       1179.7 | **231.4** |     268.6 |
| Throughput median (tok/s) |          1.3 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        398.5 | **61.0** |   80.5 |
| TPOT median (ms)          |         30.6 | **28.0** |   43.6 |
| E2E median (ms)           |        440.0 | **82.2** |  134.6 |
| Throughput median (tok/s) |          3.0 | **14.9** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        421.3 |  **71.0** |   75.5 |
| TPOT median (ms)          |         28.5 |  **15.0** |   23.9 |
| E2E median (ms)           |       1451.8 | **623.5** |  890.6 |
| Throughput median (tok/s) |         21.4 |  **58.4** |   39.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        453.9 | **134.6** |  137.3 |
| TPOT median (ms)          |         36.8 |  **30.6** |   51.8 |
| E2E median (ms)           |        761.4 | **275.3** |  374.8 |
| Throughput median (tok/s) |          6.5 |  **18.2** |   12.5 |
| Correctness               |          99% |       99% |    99% |
