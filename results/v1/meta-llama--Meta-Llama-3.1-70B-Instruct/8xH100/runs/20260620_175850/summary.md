# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **16/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     372.9s (6.2m) | `19a1183` |
| vllm         |     456.1s (7.6m) | `d272418` |
| sglang       | **240.5s (4.0m)** | `ff1fc1f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        205.8 | **135.7** |  139.0 |
| TPOT median (ms)          |     **34.6** |      48.4 |   72.9 |
| E2E median (ms)           |        228.6 | **176.3** |  209.9 |
| Throughput median (tok/s) |          5.3 |   **7.7** |    5.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        280.6 | **198.2** |  220.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        402.0 | **246.8** |  358.6 |
| Throughput median (tok/s) |          2.5 |   **4.1** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        494.2 | **160.7** |  163.8 |
| TPOT median (ms)          |     **36.9** |      51.4 |  104.1 |
| E2E median (ms)           |        529.9 | **204.9** |  259.5 |
| Throughput median (tok/s) |          2.2 |   **6.7** |    5.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        192.0 | **60.3** |   83.4 |
| TPOT median (ms)          |         31.0 | **28.5** |   40.7 |
| E2E median (ms)           |        228.9 | **82.8** |  130.4 |
| Throughput median (tok/s) |          5.7 | **14.5** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        348.5 |      64.5 | **64.0** |
| TPOT median (ms)          |         22.0 |  **14.9** |     22.6 |
| E2E median (ms)           |       1152.4 | **598.6** |    835.5 |
| Throughput median (tok/s) |         31.0 |  **60.5** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        304.2 | **123.9** |  134.2 |
| TPOT median (ms)          |     **24.9** |      28.6 |   48.1 |
| E2E median (ms)           |        508.4 | **261.9** |  358.8 |
| Throughput median (tok/s) |          9.3 |  **18.7** |   13.1 |
| Correctness               |          98% |       99% |    99% |
