# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 11 2026

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
| torchinferno | **39.4s (0.7m)** | `49107ad` |
| vllm         |    278.6s (4.6m) | `54503ec` |
| sglang       |    146.6s (2.4m) | `d8ef766` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.2 |  **80.0** |   82.3 |
| TPOT median (ms)          |     **32.0** |      39.0 |   64.9 |
| E2E median (ms)           |        166.0 | **109.4** |  136.7 |
| Throughput median (tok/s) |          7.0 |  **12.1** |    9.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **64.3** |  84.8 |  122.1 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |     **84.8** | 103.0 |  208.0 |
| Throughput median (tok/s) |     **11.8** |   9.7 |    4.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.1 |  **75.6** |   81.3 |
| TPOT median (ms)          |         36.0 |  **34.2** |   69.0 |
| E2E median (ms)           |        221.6 | **102.5** |  139.1 |
| Throughput median (tok/s) |          5.1 |  **13.0** |    9.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.5 | **34.0** |   52.6 |
| TPOT median (ms)          |         35.2 | **22.7** |  340.4 |
| E2E median (ms)           |         74.9 | **51.4** |  390.4 |
| Throughput median (tok/s) |         19.5 | **25.0** |    3.7 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.3 |  **46.1** |   52.0 |
| TPOT median (ms)          |         19.0 |  **15.2** |   24.8 |
| E2E median (ms)           |        843.1 | **572.4** |  933.2 |
| Throughput median (tok/s) |         41.2 |  **61.6** |   39.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.1 |  **64.1** |   78.1 |
| TPOT median (ms)          |         24.4 |  **22.2** |   99.8 |
| E2E median (ms)           |        278.1 | **187.7** |  361.5 |
| Throughput median (tok/s) |         16.9 |  **24.3** |   13.4 |
| Correctness               |          98% |       99% |    98% |
