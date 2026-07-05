# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **12/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **39.6s (0.7m)** | `390fed4` |
| vllm         |    271.5s (4.5m) | `34b560b` |
| sglang       |    231.7s (3.9m) | `754524d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        152.2 |     145.1 | **143.8** |
| TPOT median (ms)          |     **45.4** |      49.4 |      75.0 |
| E2E median (ms)           |        194.3 | **189.8** |     221.5 |
| Throughput median (tok/s) |          6.2 |   **7.5** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **143.3** | 149.1 |  219.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **152.5** | 222.0 |  372.3 |
| Throughput median (tok/s) |      **6.6** |   4.5 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        343.3 |     172.0 | **168.0** |
| TPOT median (ms)          |         59.8 |  **49.4** |     100.6 |
| E2E median (ms)           |        401.6 | **217.4** |     273.6 |
| Throughput median (tok/s) |          3.6 |   **6.2** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        118.7 | **64.4** |   74.6 |
| TPOT median (ms)          |         35.9 | **30.9** |   56.7 |
| E2E median (ms)           |        145.7 | **87.5** |  139.5 |
| Throughput median (tok/s) |          9.1 | **13.7** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        255.1 |      91.4 | **73.3** |
| TPOT median (ms)          |         20.4 |  **14.9** |     22.1 |
| E2E median (ms)           |        992.5 | **661.0** |    804.8 |
| Throughput median (tok/s) |         36.6 |  **56.7** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        202.5 | **124.4** |  135.8 |
| TPOT median (ms)          |         32.3 |  **28.9** |   50.9 |
| E2E median (ms)           |        377.3 | **275.6** |  362.4 |
| Throughput median (tok/s) |         12.4 |  **17.7** |   13.0 |
| Correctness               |          99% |       99% |    99% |
