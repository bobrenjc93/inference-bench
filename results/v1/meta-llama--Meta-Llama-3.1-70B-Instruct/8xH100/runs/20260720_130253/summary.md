# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 20 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **3/4** |  1/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **4/4** |  0/4 |    0/4 |
| **Total**        |    **17/20** | 2/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     416.9s (6.9m) | `3ffe0eb` |
| vllm         | **212.4s (3.5m)** | `8ce53a6` |
| sglang       |     238.8s (4.0m) | `370f454` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **51.6** |     90.0 |   98.1 |
| TPOT median (ms)          |         48.6 | **36.5** |   68.0 |
| E2E median (ms)           |     **89.7** |    119.8 |  163.1 |
| Throughput median (tok/s) |     **14.2** |     11.3 |    7.8 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **32.6** | 69.8 |  149.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **47.9** | 88.0 |  224.3 |
| Throughput median (tok/s) |     **20.9** | 11.4 |    4.5 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.4** |     71.2 |   94.1 |
| TPOT median (ms)          |         37.4 | **36.1** |   89.8 |
| E2E median (ms)           |     **75.4** |     97.0 |  165.9 |
| Throughput median (tok/s) |     **17.4** |     13.8 |    8.0 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **23.8** | 34.3 |   60.6 |
| TPOT median (ms)          |     **16.3** | 22.6 |  389.6 |
| E2E median (ms)           |     **36.1** | 52.2 |  459.3 |
| Throughput median (tok/s) |     **39.7** | 25.2 |    3.2 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **44.9** |  47.4 |   55.0 |
| TPOT median (ms)          |     **14.1** |  15.4 |   27.4 |
| E2E median (ms)           |    **537.9** | 573.9 | 1003.7 |
| Throughput median (tok/s) |     **65.2** |  61.1 |   35.4 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **39.1** |     62.5 |   91.5 |
| TPOT median (ms)          |         23.3 | **22.1** |  115.0 |
| E2E median (ms)           |    **157.4** |    186.2 |  403.3 |
| Throughput median (tok/s) |     **31.5** |     24.5 |   11.8 |
| Correctness               |          99% |      99% |    98% |
