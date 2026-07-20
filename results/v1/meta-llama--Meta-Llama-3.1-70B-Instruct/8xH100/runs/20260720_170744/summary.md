# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, Jul 20 2026

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
| torchinferno |     335.9s (5.6m) | `3ffe0eb` |
| vllm         | **235.5s (3.9m)** | `b23bd73` |
| sglang       |     266.4s (4.4m) | `5ab3d90` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **50.9** |     73.0 |   94.3 |
| TPOT median (ms)          |         48.2 | **37.6** |   70.3 |
| E2E median (ms)           |     **89.3** |     99.2 |  158.8 |
| Throughput median (tok/s) |     **14.3** |     13.5 |    8.2 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **33.0** | 73.7 |  151.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **49.9** | 92.0 |  229.1 |
| Throughput median (tok/s) |     **20.1** | 10.9 |    4.4 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.5** |     95.7 |   89.7 |
| TPOT median (ms)          |         37.5 | **36.3** |   79.2 |
| E2E median (ms)           |     **76.5** |    123.8 |  150.3 |
| Throughput median (tok/s) |     **17.1** |     11.0 |    8.9 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.0** | 38.8 |   62.4 |
| TPOT median (ms)          |     **16.3** | 29.5 |  424.1 |
| E2E median (ms)           |     **36.1** | 58.7 |  488.0 |
| Throughput median (tok/s) |     **38.9** | 21.7 |    2.9 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **46.3** |  48.4 |   60.8 |
| TPOT median (ms)          |     **14.0** |  15.6 |   28.6 |
| E2E median (ms)           |    **570.2** | 584.8 | 1034.6 |
| Throughput median (tok/s) |     **65.9** |  59.8 |   33.8 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **39.4** |  65.9 |   91.7 |
| TPOT median (ms)          |     **23.2** |  23.8 |  120.4 |
| E2E median (ms)           |    **164.4** | 191.7 |  412.1 |
| Throughput median (tok/s) |     **31.2** |  23.3 |   11.7 |
| Correctness               |          99% |   99% |    99% |
