# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 20 2026

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
| torchinferno |     529.4s (8.8m) | `3ffe0eb` |
| vllm         |     227.2s (3.8m) | `c01618f` |
| sglang       | **219.2s (3.7m)** | `3d82dac` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **51.1** |     81.7 |   89.7 |
| TPOT median (ms)          |         47.7 | **37.2** |   74.7 |
| E2E median (ms)           |     **85.5** |    112.4 |  156.6 |
| Throughput median (tok/s) |     **14.4** |     12.6 |    8.3 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **33.6** | 68.4 |  155.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **49.8** | 84.6 |  234.8 |
| Throughput median (tok/s) |     **20.1** | 11.8 |    4.3 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.8** |     89.5 |   92.6 |
| TPOT median (ms)          |         38.2 | **35.0** |   77.6 |
| E2E median (ms)           |     **78.0** |    114.2 |  156.6 |
| Throughput median (tok/s) |     **16.7** |     11.7 |    8.5 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.5** | 36.8 |   61.1 |
| TPOT median (ms)          |     **16.5** | 26.6 |  369.0 |
| E2E median (ms)           |     **36.7** | 54.9 |  455.5 |
| Throughput median (tok/s) |     **38.4** | 23.2 |    3.0 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **45.0** |  47.6 |   59.5 |
| TPOT median (ms)          |     **14.0** |  15.6 |   27.8 |
| E2E median (ms)           |    **550.2** | 590.5 | 1050.3 |
| Throughput median (tok/s) |     **66.0** |  59.8 |   34.7 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **39.4** |     64.8 |   91.6 |
| TPOT median (ms)          |         23.3 | **22.9** |  109.8 |
| E2E median (ms)           |    **160.1** |    191.3 |  410.8 |
| Throughput median (tok/s) |     **31.1** |     23.8 |   11.8 |
| Correctness               |          98% |      98% |    99% |
