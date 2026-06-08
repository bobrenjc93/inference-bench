# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 7 2026

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
| torchinferno |     400.8s (6.7m) | `551513c` |
| vllm         |   1349.5s (22.5m) | `eebce65` |
| sglang       | **224.6s (3.7m)** | `1aa5040` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        275.4 |     156.9 | **150.0** |
| TPOT median (ms)          |         97.7 |  **56.8** |      77.8 |
| E2E median (ms)           |        381.1 | **205.0** |     225.7 |
| Throughput median (tok/s) |          3.1 |   **7.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        364.6 | **200.1** |  209.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        494.6 | **246.7** |  351.7 |
| Throughput median (tok/s) |          2.0 |   **4.1** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        647.2 |     185.5 | **168.2** |
| TPOT median (ms)          |         66.8 |  **64.7** |     100.6 |
| E2E median (ms)           |        710.3 | **238.8** |     265.2 |
| Throughput median (tok/s) |          1.7 |   **5.9** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        429.7 | **61.7** |   85.5 |
| TPOT median (ms)          |         64.9 | **27.7** |   46.7 |
| E2E median (ms)           |        490.5 | **83.5** |  149.1 |
| Throughput median (tok/s) |          2.6 | **14.4** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        494.0 |  **71.6** |   82.5 |
| TPOT median (ms)          |         21.7 |  **14.8** |   23.5 |
| E2E median (ms)           |       1324.7 | **601.9** |  879.0 |
| Throughput median (tok/s) |         26.3 |  **59.4** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        442.2 | **135.1** |  139.2 |
| TPOT median (ms)          |         50.2 |  **32.8** |   49.7 |
| E2E median (ms)           |        680.2 | **275.2** |  374.1 |
| Throughput median (tok/s) |          7.1 |  **18.2** |   12.4 |
| Correctness               |          98% |       99% |    98% |
