# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jun 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **17/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     432.3s (7.2m) | `065275c` |
| vllm         |   1449.1s (24.2m) | `fbc3a19` |
| sglang       | **238.1s (4.0m)** | `50815d5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        311.7 |     151.4 | **150.1** |
| TPOT median (ms)          |         84.0 |  **49.3** |      75.7 |
| E2E median (ms)           |        392.3 | **199.3** |     221.7 |
| Throughput median (tok/s) |          3.2 |   **7.2** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        376.5 | **189.0** |  203.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        560.2 | **233.8** |  329.6 |
| Throughput median (tok/s) |          1.8 |   **4.3** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        721.9 |     172.2 | **164.5** |
| TPOT median (ms)          |         72.9 |  **59.1** |     102.0 |
| E2E median (ms)           |        785.4 | **218.4** |     261.5 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        455.4 | **61.1** |   79.6 |
| TPOT median (ms)          |         62.3 | **28.5** |   45.0 |
| E2E median (ms)           |        513.0 | **81.7** |  136.6 |
| Throughput median (tok/s) |          3.0 | **14.5** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.0 |  **74.8** |   77.0 |
| TPOT median (ms)          |         27.3 |  **14.9** |   24.1 |
| E2E median (ms)           |       1278.3 | **618.7** |  895.4 |
| Throughput median (tok/s) |         30.4 |  **59.0** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        410.9 | **129.7** |  134.9 |
| TPOT median (ms)          |         49.3 |  **30.4** |   49.4 |
| E2E median (ms)           |        705.9 | **270.4** |  368.9 |
| Throughput median (tok/s) |          8.0 |  **18.2** |   12.5 |
| Correctness               |          98% |       99% |    99% |
