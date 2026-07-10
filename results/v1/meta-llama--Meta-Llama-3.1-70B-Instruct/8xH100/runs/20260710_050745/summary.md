# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 PM PT, Jul 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.7s (0.7m)** | `861b7c3` |
| vllm         |    238.2s (4.0m) | `95ed0fe` |
| sglang       |    226.5s (3.8m) | `b76dd0b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        145.4 | **68.9** |   73.3 |
| TPOT median (ms)          |     **32.5** |     35.5 |   64.7 |
| E2E median (ms)           |        171.4 | **95.2** |  128.4 |
| Throughput median (tok/s) |          6.6 | **14.4** |   10.6 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **55.1** | 70.5 |  115.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **55.6** | 85.2 |  192.3 |
| Throughput median (tok/s) |     **18.0** | 11.7 |    5.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        481.6 | **73.2** |   82.0 |
| TPOT median (ms)          |        122.3 | **34.5** |   68.9 |
| E2E median (ms)           |        585.3 | **97.8** |  142.5 |
| Throughput median (tok/s) |          2.1 | **13.4** |    9.4 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        131.5 | **33.9** |   48.2 |
| TPOT median (ms)          |         82.8 | **22.2** |  411.5 |
| E2E median (ms)           |        166.5 | **51.5** |  443.3 |
| Throughput median (tok/s) |          8.5 | **25.6** |    3.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        595.5 |  **44.6** |   48.8 |
| TPOT median (ms)          |         65.0 |  **15.0** |   24.7 |
| E2E median (ms)           |       2814.3 | **566.5** |  929.4 |
| Throughput median (tok/s) |         12.1 |  **62.1** |   39.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        281.8 |  **58.2** |   73.6 |
| TPOT median (ms)          |         60.5 |  **21.4** |  113.9 |
| E2E median (ms)           |        758.6 | **179.3** |  367.2 |
| Throughput median (tok/s) |          9.5 |  **25.5** |   13.6 |
| Correctness               |          98% |       99% |    98% |
