# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 PM PT, Jul 20 2026

## Scorecard

| Benchmark        | torchinferno | vllm | sglang |
| :--------------- | -----------: | ---: | -----: |
| few_shot         |      **3/4** |  1/4 |    0/4 |
| self_consistency |      **3/4** |  0/4 |    0/4 |
| multi_turn       |      **3/4** |  1/4 |    0/4 |
| tree_of_thought  |      **4/4** |  0/4 |    0/4 |
| long_output      |      **3/4** |  1/4 |    0/4 |
| **Total**        |    **16/20** | 3/20 |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     354.1s (5.9m) | `3ffe0eb` |
| vllm         | **209.8s (3.5m)** | `4ec199b` |
| sglang       |     239.7s (4.0m) | `91b210f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **50.9** |     74.2 |   93.0 |
| TPOT median (ms)          |         47.2 | **36.3** |   69.0 |
| E2E median (ms)           |     **89.3** |    102.8 |  154.0 |
| Throughput median (tok/s) |     **14.3** |     12.7 |    8.6 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **32.4** | 80.2 |  147.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **48.7** | 98.7 |  226.0 |
| Throughput median (tok/s) |     **20.5** | 10.1 |    4.4 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |     **42.5** |     72.9 |   97.5 |
| TPOT median (ms)          |         37.6 | **37.3** |   75.6 |
| E2E median (ms)           |     **76.2** |    100.9 |  163.9 |
| Throughput median (tok/s) |     **17.3** |     13.3 |    8.1 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **23.6** | 37.4 |   59.5 |
| TPOT median (ms)          |     **16.3** | 27.6 |  411.4 |
| E2E median (ms)           |     **36.3** | 55.8 |  425.6 |
| Throughput median (tok/s) |     **40.0** | 22.7 |    3.2 |
| Correctness               |          96% |  97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         47.2 | **47.1** |   55.7 |
| TPOT median (ms)          |     **14.1** |     15.4 |   26.4 |
| E2E median (ms)           |    **544.1** |    578.5 | 1036.3 |
| Throughput median (tok/s) |     **65.0** |     60.5 |   36.4 |
| Correctness               |         100% |     100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **39.3** |  62.4 |   90.6 |
| TPOT median (ms)          |     **23.1** |  23.3 |  116.5 |
| E2E median (ms)           |    **158.9** | 187.3 |  401.2 |
| Throughput median (tok/s) |     **31.4** |  23.9 |   12.2 |
| Correctness               |          98% |   99% |    99% |
