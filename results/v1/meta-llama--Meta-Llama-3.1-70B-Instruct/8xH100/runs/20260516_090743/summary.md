# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:08 AM PT, May 16 2026

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
| torchinferno |     299.8s (5.0m) | `db749af` |
| vllm         |   1107.7s (18.5m) | `657b42b` |
| sglang       | **170.7s (2.8m)** | `7f37ffa` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        280.1 |     155.2 | **141.0** |
| TPOT median (ms)          |        146.5 |  **59.2** |      71.6 |
| E2E median (ms)           |        366.5 | **209.8** |     210.0 |
| Throughput median (tok/s) |          4.0 |   **7.1** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        289.9 | **195.0** |  207.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        313.7 | **217.2** |  343.1 |
| Throughput median (tok/s) |          3.2 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        524.9 |     182.8 | **157.9** |
| TPOT median (ms)          |        114.4 |  **57.2** |      94.9 |
| E2E median (ms)           |        621.5 | **236.1** |     248.6 |
| Throughput median (tok/s) |          2.1 |   **6.0** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        319.0 | **57.7** |   75.3 |
| TPOT median (ms)          |        128.4 | **26.6** |   52.7 |
| E2E median (ms)           |        422.3 | **78.2** |  143.8 |
| Throughput median (tok/s) |          3.3 | **15.7** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        736.6 |  **65.4** |   77.6 |
| TPOT median (ms)          |         16.7 |  **15.0** |   19.8 |
| E2E median (ms)           |       1483.7 | **602.3** |  769.2 |
| Throughput median (tok/s) |         21.3 |  **59.4** |   46.6 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        430.1 | **131.2** |  131.8 |
| TPOT median (ms)          |         81.2 |  **31.6** |   47.8 |
| E2E median (ms)           |        641.5 | **268.7** |  342.9 |
| Throughput median (tok/s) |          6.8 |  **18.5** |   14.2 |
| Correctness               |          99% |       99% |    98% |
