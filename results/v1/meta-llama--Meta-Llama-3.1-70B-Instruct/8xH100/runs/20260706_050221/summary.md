# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **37.4s (0.6m)** | `fa12aa1` |
| vllm         |    185.3s (3.1m) | `6971582` |
| sglang       |    179.8s (3.0m) | `6f22790` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        165.3 | **125.7** |  137.5 |
| TPOT median (ms)          |         45.1 |  **41.2** |   77.8 |
| E2E median (ms)           |        203.4 | **156.7** |  212.5 |
| Throughput median (tok/s) |          6.2 |   **8.8** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **98.9** | 126.0 |  216.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **105.8** | 151.4 |  365.9 |
| Throughput median (tok/s) |      **9.4** |   6.6 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        228.8 | **155.1** |  160.5 |
| TPOT median (ms)          |         58.5 |  **50.6** |  106.8 |
| E2E median (ms)           |        280.7 | **199.9** |  269.0 |
| Throughput median (tok/s) |          4.6 |   **6.8** |    4.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         80.2 | **33.0** |   48.5 |
| TPOT median (ms)          |         64.6 | **21.7** |  359.9 |
| E2E median (ms)           |        114.1 | **48.7** |  393.8 |
| Throughput median (tok/s) |         12.5 | **25.6** |    3.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        267.8 |      78.2 | **68.8** |
| TPOT median (ms)          |         20.6 |  **14.7** |     22.4 |
| E2E median (ms)           |        990.0 | **600.2** |    906.0 |
| Throughput median (tok/s) |         35.9 |  **59.4** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        168.2 | **103.6** |  126.3 |
| TPOT median (ms)          |         37.7 |  **25.6** |  113.4 |
| E2E median (ms)           |        338.8 | **231.4** |  429.5 |
| Throughput median (tok/s) |         13.7 |  **21.4** |   11.7 |
| Correctness               |          99% |       99% |    99% |
