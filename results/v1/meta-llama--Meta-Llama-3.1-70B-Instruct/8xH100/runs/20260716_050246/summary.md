# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **42.5s (0.7m)** | `96adc9d` |
| vllm         |    313.1s (5.2m) | `59b964f` |
| sglang       |    193.5s (3.2m) | `dc60f65` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.1 |  **78.0** |   87.1 |
| TPOT median (ms)          |     **32.4** |      37.7 |   71.2 |
| E2E median (ms)           |        165.4 | **107.1** |  148.0 |
| Throughput median (tok/s) |          7.0 |  **12.2** |    9.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.3** | 66.5 |  125.9 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.3** | 85.8 |  203.0 |
| Throughput median (tok/s) |     **13.5** | 11.7 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.9 |  **86.2** |   87.3 |
| TPOT median (ms)          |     **35.4** |      37.2 |   77.0 |
| E2E median (ms)           |        218.6 | **114.6** |  153.0 |
| Throughput median (tok/s) |          5.2 |  **12.0** |    8.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.3 | **35.1** |   53.0 |
| TPOT median (ms)          |         34.7 | **23.1** |  415.9 |
| E2E median (ms)           |         74.4 | **53.8** |  461.0 |
| Throughput median (tok/s) |         19.5 | **24.5** |    3.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.7 |  **47.0** |   53.1 |
| TPOT median (ms)          |         19.4 |  **15.3** |   25.4 |
| E2E median (ms)           |        878.4 | **576.6** |  981.7 |
| Throughput median (tok/s) |         40.8 |  **60.7** |   38.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.7 |  **62.6** |   81.3 |
| TPOT median (ms)          |         24.4 |  **22.6** |  117.9 |
| E2E median (ms)           |        282.2 | **187.6** |  389.3 |
| Throughput median (tok/s) |         17.2 |  **24.2** |   12.8 |
| Correctness               |          99% |       99% |    99% |
