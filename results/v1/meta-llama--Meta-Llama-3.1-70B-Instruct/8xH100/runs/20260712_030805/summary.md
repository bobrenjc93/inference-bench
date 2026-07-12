# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:08 PM PT, Jul 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **43.0s (0.7m)** | `9808f42` |
| vllm         |    331.8s (5.5m) | `9a48eef` |
| sglang       |    166.5s (2.8m) | `592c043` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        143.6 | **72.3** |   80.3 |
| TPOT median (ms)          |     **31.0** |     38.5 |   64.5 |
| E2E median (ms)           |        167.6 | **99.6** |  136.0 |
| Throughput median (tok/s) |          6.8 | **12.6** |    9.9 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.4** | 70.8 |  124.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **74.8** | 87.9 |  201.8 |
| Throughput median (tok/s) |     **13.4** | 11.4 |    5.0 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        192.7 |      84.1 | **82.7** |
| TPOT median (ms)          |     **34.1** |      34.7 |     75.2 |
| E2E median (ms)           |        220.2 | **110.2** |    143.4 |
| Throughput median (tok/s) |          5.1 |  **12.0** |      9.2 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         54.0 | **37.6** |   52.4 |
| TPOT median (ms)          |         34.8 | **27.9** |  395.6 |
| E2E median (ms)           |         75.7 | **57.9** |  437.4 |
| Throughput median (tok/s) |         19.5 | **22.6** |    3.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        189.0 |  **47.2** |   51.8 |
| TPOT median (ms)          |         19.1 |  **15.5** |   25.4 |
| E2E median (ms)           |        834.2 | **575.6** |  989.6 |
| Throughput median (tok/s) |         42.2 |  **60.5** |   38.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.3 |  **62.4** |   78.4 |
| TPOT median (ms)          |         23.8 |  **23.3** |  112.1 |
| E2E median (ms)           |        274.5 | **186.2** |  381.6 |
| Throughput median (tok/s) |         17.4 |  **23.8** |   13.1 |
| Correctness               |          99% |       99% |    99% |
