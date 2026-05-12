# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:01 PM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          1/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **95.4s (1.6m)** | `07a120b` |
| vllm         |  1192.1s (19.9m) | `39dff5f` |
| sglang       |    164.8s (2.7m) | `5495026` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        471.8 |     167.1 | **148.4** |
| TPOT median (ms)          |        488.5 |  **58.5** |      75.3 |
| E2E median (ms)           |        848.7 | **219.0** |     221.5 |
| Throughput median (tok/s) |          1.6 |   **6.8** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        445.8 | **192.2** |  221.0 |
| TPOT median (ms)          |      **0.0** |       0.0 |    0.0 |
| E2E median (ms)           |        625.0 | **221.8** |  371.9 |
| Throughput median (tok/s) |          1.6 |   **4.5** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1413.7 |     185.4 | **173.2** |
| TPOT median (ms)          |        666.4 |  **53.7** |     103.3 |
| E2E median (ms)           |       2081.7 | **240.9** |     279.4 |
| Throughput median (tok/s) |          0.7 |   **5.7** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        518.1 | **61.5** |   74.3 |
| TPOT median (ms)          |        448.5 | **27.6** |   72.6 |
| E2E median (ms)           |        859.7 | **82.9** |  160.9 |
| Throughput median (tok/s) |          1.7 | **15.6** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1061.5 |      76.5 | **70.8** |
| TPOT median (ms)          |         33.4 |  **15.0** |     22.7 |
| E2E median (ms)           |       2315.3 | **618.8** |    842.2 |
| Throughput median (tok/s) |         16.0 |  **58.1** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        782.2 | **136.5** |  137.6 |
| TPOT median (ms)          |        327.4 |  **31.0** |   54.8 |
| E2E median (ms)           |       1346.1 | **276.7** |  375.2 |
| Throughput median (tok/s) |          4.3 |  **18.1** |   12.7 |
| Correctness               |          99% |       98% |    98% |
