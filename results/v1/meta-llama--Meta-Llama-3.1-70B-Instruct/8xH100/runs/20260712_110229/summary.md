# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 12 2026

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
| torchinferno | **39.9s (0.7m)** | `e286ddf` |
| vllm         |    339.9s (5.7m) | `370b678` |
| sglang       |    151.3s (2.5m) | `80856ab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.1 |  **73.9** |   76.4 |
| TPOT median (ms)          |     **31.6** |      39.7 |   65.0 |
| E2E median (ms)           |        164.3 | **102.5** |  130.1 |
| Throughput median (tok/s) |          7.1 |  **12.2** |   10.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **61.8** | 68.1 |  117.3 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **80.2** | 85.2 |  203.5 |
| Throughput median (tok/s) |     **12.5** | 11.7 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.4 |  **77.7** |   81.8 |
| TPOT median (ms)          |     **35.5** |      36.0 |   72.1 |
| E2E median (ms)           |        222.5 | **104.0** |  141.3 |
| Throughput median (tok/s) |          5.1 |  **12.8** |    9.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.4 | **35.1** |   51.8 |
| TPOT median (ms)          |         34.7 | **23.1** |  377.6 |
| E2E median (ms)           |         73.2 | **53.4** |  442.7 |
| Throughput median (tok/s) |         19.6 | **24.3** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.8 |  **47.0** |   51.6 |
| TPOT median (ms)          |         19.4 |  **15.4** |   23.9 |
| E2E median (ms)           |        871.2 | **581.7** |  915.8 |
| Throughput median (tok/s) |         40.2 |  **59.8** |   40.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.3 |  **60.4** |   75.8 |
| TPOT median (ms)          |         24.2 |  **22.9** |  107.7 |
| E2E median (ms)           |        282.3 | **185.4** |  366.7 |
| Throughput median (tok/s) |         16.9 |  **24.2** |   13.7 |
| Correctness               |          99% |       99% |    98% |
