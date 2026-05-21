# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:02 AM PT, May 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **86.9s (1.4m)** | `9f91b40` |
| vllm         |  1292.0s (21.5m) | `1c78f76` |
| sglang       |    181.9s (3.0m) | `b765fae` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        316.0 |     161.9 | **145.2** |
| TPOT median (ms)          |        163.7 |  **52.3** |      80.8 |
| E2E median (ms)           |        431.4 | **214.4** |     221.1 |
| Throughput median (tok/s) |          3.3 |   **7.0** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        293.0 | **175.8** |  224.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        338.5 | **201.1** |  369.3 |
| Throughput median (tok/s) |          3.0 |   **5.0** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        950.6 |     176.5 | **170.0** |
| TPOT median (ms)          |        130.3 |  **39.4** |     114.8 |
| E2E median (ms)           |       1040.5 | **226.3** |     276.1 |
| Throughput median (tok/s) |          1.2 |   **6.1** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        355.9 | **62.0** |   80.5 |
| TPOT median (ms)          |        139.3 | **27.9** |   59.0 |
| E2E median (ms)           |        461.5 | **84.3** |  144.2 |
| Throughput median (tok/s) |          3.3 | **14.9** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1092.6 |      79.0 | **75.5** |
| TPOT median (ms)          |         17.0 |  **15.2** |     21.8 |
| E2E median (ms)           |       1628.0 | **680.4** |    796.2 |
| Throughput median (tok/s) |         20.0 |  **56.9** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        601.6 | **131.1** |  139.1 |
| TPOT median (ms)          |         90.1 |  **27.0** |   55.3 |
| E2E median (ms)           |        780.0 | **281.3** |  361.4 |
| Throughput median (tok/s) |          6.2 |  **18.0** |   13.0 |
| Correctness               |          99% |       98% |    98% |
