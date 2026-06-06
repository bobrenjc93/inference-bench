# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 PM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     361.1s (6.0m) | `e2056aa` |
| vllm         |   1265.0s (21.1m) | `062b05f` |
| sglang       | **196.7s (3.3m)** | `4989d66` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        260.3 |     155.3 | **149.1** |
| TPOT median (ms)          |         92.9 |  **56.6** |      76.9 |
| E2E median (ms)           |        354.1 | **209.8** |     221.5 |
| Throughput median (tok/s) |          3.6 |   **7.0** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        332.9 | **186.6** |  208.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        523.1 | **241.2** |  354.6 |
| Throughput median (tok/s) |          1.9 |   **4.1** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        818.1 | **155.3** |  164.4 |
| TPOT median (ms)          |        115.5 |  **61.8** |  106.7 |
| E2E median (ms)           |        995.7 | **205.0** |  263.3 |
| Throughput median (tok/s) |          1.4 |   **6.5** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        389.1 | **59.5** |   79.6 |
| TPOT median (ms)          |         67.0 | **29.0** |   43.3 |
| E2E median (ms)           |        453.0 | **82.2** |  136.0 |
| Throughput median (tok/s) |          3.2 | **14.6** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        518.5 |  **68.1** |   77.2 |
| TPOT median (ms)          |         23.4 |  **15.1** |   23.7 |
| E2E median (ms)           |       1296.2 | **617.0** |  874.3 |
| Throughput median (tok/s) |         26.7 |  **58.7** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        463.8 | **124.9** |  135.7 |
| TPOT median (ms)          |         59.8 |  **32.5** |   50.1 |
| E2E median (ms)           |        724.4 | **271.0** |  369.9 |
| Throughput median (tok/s) |          7.3 |  **18.2** |   12.6 |
| Correctness               |          98% |       98% |    98% |
