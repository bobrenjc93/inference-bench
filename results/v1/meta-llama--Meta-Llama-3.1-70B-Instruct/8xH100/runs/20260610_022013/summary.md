# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:09 PM PT, Jun 9 2026

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
| torchinferno |     387.0s (6.5m) | `a870596` |
| vllm         |   1314.1s (21.9m) | `6deb05e` |
| sglang       | **195.8s (3.3m)** | `854d232` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        310.7 |     164.0 | **146.6** |
| TPOT median (ms)          |         79.4 |  **56.7** |      78.1 |
| E2E median (ms)           |        391.5 | **214.0** |     218.2 |
| Throughput median (tok/s) |          3.5 |   **7.1** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        406.2 | **177.3** |  207.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        543.0 | **197.0** |  340.9 |
| Throughput median (tok/s) |          1.8 |   **5.1** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        724.2 |     167.5 | **163.6** |
| TPOT median (ms)          |         70.3 |  **55.4** |     102.1 |
| E2E median (ms)           |        791.9 | **217.5** |     258.6 |
| Throughput median (tok/s) |          1.6 |   **6.5** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        373.5 | **59.1** |   82.0 |
| TPOT median (ms)          |         65.1 | **28.8** |   46.8 |
| E2E median (ms)           |        422.4 | **81.8** |  141.7 |
| Throughput median (tok/s) |          3.5 | **14.7** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.1 |  **69.2** |   76.8 |
| TPOT median (ms)          |         26.5 |  **15.1** |   23.1 |
| E2E median (ms)           |       1262.6 | **609.7** |  865.9 |
| Throughput median (tok/s) |         30.6 |  **58.2** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        400.6 | **127.4** |  135.2 |
| TPOT median (ms)          |         48.3 |  **31.2** |   50.0 |
| E2E median (ms)           |        682.3 | **264.0** |  365.1 |
| Throughput median (tok/s) |          8.2 |  **18.3** |   12.8 |
| Correctness               |          99% |       98% |    98% |
