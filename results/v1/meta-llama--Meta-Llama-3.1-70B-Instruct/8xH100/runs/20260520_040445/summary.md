# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, May 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     284.0s (4.7m) | `9f91b40` |
| vllm         |   1114.5s (18.6m) | `cd0ff26` |
| sglang       | **182.6s (3.0m)** | `579fed2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        238.3 |    161.3 | **142.9** |
| TPOT median (ms)          |        152.7 | **51.7** |      76.3 |
| E2E median (ms)           |        361.2 |    214.7 | **213.9** |
| Throughput median (tok/s) |          4.2 |  **6.8** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        279.8 | **191.1** |  204.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        301.8 | **224.6** |  345.5 |
| Throughput median (tok/s) |          3.3 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        536.6 |     163.0 | **159.9** |
| TPOT median (ms)          |        175.5 |  **51.5** |     104.8 |
| E2E median (ms)           |        626.6 | **207.9** |     255.4 |
| Throughput median (tok/s) |          2.1 |   **6.6** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        348.6 | **57.8** |   77.8 |
| TPOT median (ms)          |        131.1 | **27.1** |   63.8 |
| E2E median (ms)           |        452.7 | **78.7** |  150.2 |
| Throughput median (tok/s) |          2.9 | **15.7** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        751.5 |      83.2 | **68.3** |
| TPOT median (ms)          |         16.6 |  **15.0** |     21.9 |
| E2E median (ms)           |       1450.5 | **626.3** |    815.6 |
| Throughput median (tok/s) |         24.0 |  **57.3** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        430.9 |     131.3 | **130.6** |
| TPOT median (ms)          |         95.2 |  **29.1** |      53.4 |
| E2E median (ms)           |        638.6 | **270.4** |     356.1 |
| Throughput median (tok/s) |          7.3 |  **18.2** |      13.1 |
| Correctness               |          99% |       99% |       99% |
