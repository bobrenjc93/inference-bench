# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:10 PM PT, Jul 2 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **23.7s (0.4m)** | `02949d2` |
| vllm         |    194.0s (3.2m) | `e24d1b2` |
| sglang       |    161.8s (2.7m) | `17cce6a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        156.3 | **141.1** |  146.2 |
| TPOT median (ms)          |     **47.1** |      49.9 |   74.4 |
| E2E median (ms)           |        200.5 | **181.7** |  223.5 |
| Throughput median (tok/s) |          6.4 |   **7.8** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **138.7** | 183.2 |  220.5 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **148.8** | 207.1 |  375.3 |
| Throughput median (tok/s) |      **6.7** |   4.8 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        303.9 |     176.6 | **166.5** |
| TPOT median (ms)          |         61.2 |  **59.0** |     108.4 |
| E2E median (ms)           |        358.3 | **227.2** |     271.2 |
| Throughput median (tok/s) |          4.0 |   **6.1** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        136.4 | **61.5** |   72.5 |
| TPOT median (ms)          |         32.0 | **29.7** |   75.1 |
| E2E median (ms)           |        162.0 | **84.7** |  152.4 |
| Throughput median (tok/s) |          7.9 | **14.2** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        244.3 |      84.3 | **72.7** |
| TPOT median (ms)          |         21.5 |  **15.1** |     21.8 |
| E2E median (ms)           |        993.2 | **627.5** |    863.4 |
| Throughput median (tok/s) |         35.9 |  **56.2** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        195.9 | **129.3** |  135.7 |
| TPOT median (ms)          |         32.4 |  **30.7** |   55.9 |
| E2E median (ms)           |        372.6 | **265.6** |  377.2 |
| Throughput median (tok/s) |         12.2 |  **17.8** |   12.9 |
| Correctness               |          99% |       99% |    99% |
