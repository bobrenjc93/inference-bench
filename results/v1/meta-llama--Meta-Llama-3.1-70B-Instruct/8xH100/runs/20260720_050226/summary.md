# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **14/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **49.4s (0.8m)** | `96adc9d` |
| vllm         |    349.6s (5.8m) | `dcfebf9` |
| sglang       |    185.8s (3.1m) | `1843384` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.1 |  **84.5** |   87.3 |
| TPOT median (ms)          |     **31.6** |      41.3 |   77.8 |
| E2E median (ms)           |        163.7 | **123.9** |  152.6 |
| Throughput median (tok/s) |          7.1 |  **11.3** |    8.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **64.6** | 75.1 |  161.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **81.6** | 93.5 |  235.4 |
| Throughput median (tok/s) |     **12.3** | 10.7 |    4.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.4 | **72.5** |   98.5 |
| TPOT median (ms)          |     **35.1** |     35.3 |   75.2 |
| E2E median (ms)           |        223.5 | **97.4** |  163.2 |
| Throughput median (tok/s) |          5.1 | **13.3** |    8.2 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.4 | **35.3** |   60.3 |
| TPOT median (ms)          |         34.5 | **22.8** |  465.4 |
| E2E median (ms)           |         74.4 | **53.0** |  504.5 |
| Throughput median (tok/s) |         19.6 | **25.1** |    2.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.6 |  **46.4** |   55.5 |
| TPOT median (ms)          |         19.2 |  **15.3** |   27.8 |
| E2E median (ms)           |        870.3 | **575.5** | 1064.3 |
| Throughput median (tok/s) |         40.5 |  **61.4** |   35.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.0 |  **62.8** |   92.5 |
| TPOT median (ms)          |         24.1 |  **22.9** |  129.3 |
| E2E median (ms)           |        282.7 | **188.7** |  424.0 |
| Throughput median (tok/s) |         16.9 |  **24.3** |   11.7 |
| Correctness               |          99% |       99% |    99% |
