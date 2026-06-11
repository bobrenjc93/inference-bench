# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 10 2026

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
| torchinferno |     391.3s (6.5m) | `065275c` |
| vllm         |   1360.4s (22.7m) | `85a0ffa` |
| sglang       | **201.1s (3.4m)** | `5e02715` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        321.9 | **156.6** |  158.1 |
| TPOT median (ms)          |         89.2 |  **55.2** |   74.2 |
| E2E median (ms)           |        394.1 | **205.5** |  228.1 |
| Throughput median (tok/s) |          3.3 |   **7.1** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        397.9 | **192.6** |  225.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        532.9 | **218.0** |  375.7 |
| Throughput median (tok/s) |          1.9 |   **4.6** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        650.2 |     177.2 | **160.4** |
| TPOT median (ms)          |         65.6 |  **58.7** |     102.3 |
| E2E median (ms)           |        725.6 | **230.5** |     262.0 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        373.3 | **59.3** |   76.1 |
| TPOT median (ms)          |         60.8 | **28.0** |   46.8 |
| E2E median (ms)           |        436.2 | **81.4** |  129.8 |
| Throughput median (tok/s) |          3.5 | **14.8** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        192.8 |      83.4 | **81.5** |
| TPOT median (ms)          |         27.0 |  **15.1** |     23.1 |
| E2E median (ms)           |       1275.9 | **638.6** |    869.3 |
| Throughput median (tok/s) |         30.5 |  **57.4** |     39.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        387.2 | **133.8** |  140.4 |
| TPOT median (ms)          |         48.5 |  **31.4** |   49.3 |
| E2E median (ms)           |        672.9 | **274.8** |  373.0 |
| Throughput median (tok/s) |          8.2 |  **18.0** |   12.7 |
| Correctness               |          99% |       99% |    99% |
