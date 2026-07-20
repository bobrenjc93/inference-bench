# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 20 2026

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
| torchinferno |     466.0s (7.8m) | `3ffe0eb` |
| vllm         |     210.8s (3.5m) | `ae10e85` |
| sglang       | **207.9s (3.5m)** | `3d82dac` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **50.8** |     75.9 |   94.8 |
| TPOT median (ms)          |         47.5 | **36.6** |   69.8 |
| E2E median (ms)           |     **88.1** |    103.8 |  156.9 |
| Throughput median (tok/s) |     **14.5** |     12.9 |    8.3 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **32.2** | 71.2 |  163.7 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **48.8** | 88.6 |  239.9 |
| Throughput median (tok/s) |     **20.5** | 11.3 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.1** |     84.5 |   96.2 |
| TPOT median (ms)          |         37.6 | **33.9** |   84.9 |
| E2E median (ms)           |     **74.9** |    110.2 |  164.6 |
| Throughput median (tok/s) |     **17.6** |     12.5 |    8.2 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.2** | 34.7 |   64.6 |
| TPOT median (ms)          |     **16.4** | 22.6 |  413.2 |
| E2E median (ms)           |     **36.4** | 52.4 |  466.5 |
| Throughput median (tok/s) |     **39.6** | 24.9 |    3.0 |
| Correctness               |          97% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **46.1** |  46.5 |   57.1 |
| TPOT median (ms)          |     **14.0** |  15.5 |   27.6 |
| E2E median (ms)           |    **574.3** | 581.9 | 1040.4 |
| Throughput median (tok/s) |     **65.6** |  60.6 |   34.9 |
| Correctness               |         100% |  100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **39.1** |     62.6 |   95.3 |
| TPOT median (ms)          |         23.1 | **21.7** |  119.1 |
| E2E median (ms)           |    **164.5** |    187.4 |  413.7 |
| Throughput median (tok/s) |     **31.6** |     24.4 |   11.7 |
| Correctness               |          98% |      99% |    99% |
