# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 PM PT, Jul 20 2026

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
| torchinferno |     302.0s (5.0m) | `3ffe0eb` |
| vllm         | **203.8s (3.4m)** | `58b2012` |
| sglang       |     260.9s (4.3m) | `8905cbd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **51.2** |     72.0 |   91.6 |
| TPOT median (ms)          |         47.9 | **37.5** |   70.1 |
| E2E median (ms)           |     **89.9** |     97.5 |  153.9 |
| Throughput median (tok/s) |     **14.3** |     13.7 |    8.1 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **31.9** | 70.5 |  154.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **48.0** | 90.4 |  226.5 |
| Throughput median (tok/s) |     **20.8** | 11.1 |    4.4 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.2** |     74.8 |   92.4 |
| TPOT median (ms)          |         37.5 | **36.2** |   76.4 |
| E2E median (ms)           |     **75.5** |    100.9 |  158.4 |
| Throughput median (tok/s) |     **17.3** |     13.2 |    8.5 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **23.8** | 37.6 |   60.2 |
| TPOT median (ms)          |     **16.3** | 27.3 |  371.8 |
| E2E median (ms)           |     **36.3** | 57.1 |  467.2 |
| Throughput median (tok/s) |     **39.5** | 22.5 |    3.0 |
| Correctness               |          96% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **45.5** |  46.9 |   58.3 |
| TPOT median (ms)          |     **14.0** |  15.4 |   29.2 |
| E2E median (ms)           |    **561.5** | 580.3 | 1108.7 |
| Throughput median (tok/s) |     **65.6** |  60.3 |   33.2 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **38.9** |  60.4 |   91.4 |
| TPOT median (ms)          |     **23.1** |  23.3 |  109.5 |
| E2E median (ms)           |    **162.2** | 185.2 |  422.9 |
| Throughput median (tok/s) |     **31.5** |  24.2 |   11.5 |
| Correctness               |          98% |   99% |    99% |
