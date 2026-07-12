# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, Jul 12 2026

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
| torchinferno | **41.3s (0.7m)** | `59e0e13` |
| vllm         |    337.9s (5.6m) | `83762b7` |
| sglang       |    191.9s (3.2m) | `f1c247e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.1 | **69.3** |   77.6 |
| TPOT median (ms)          |     **31.8** |     38.3 |   64.0 |
| E2E median (ms)           |        165.5 | **96.4** |  132.3 |
| Throughput median (tok/s) |          7.0 | **13.4** |   10.3 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **67.7** | 70.4 |  119.3 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **86.4** | 89.6 |  206.3 |
| Throughput median (tok/s) |     **11.6** | 11.2 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.4 |  **76.0** |   82.0 |
| TPOT median (ms)          |         34.9 |  **34.6** |   75.3 |
| E2E median (ms)           |        216.4 | **104.3** |  140.7 |
| Throughput median (tok/s) |          5.2 |  **12.6** |    9.5 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.9 | **36.0** |   52.2 |
| TPOT median (ms)          |         34.5 | **23.3** |  417.2 |
| E2E median (ms)           |         74.5 | **54.5** |  470.0 |
| Throughput median (tok/s) |         19.8 | **24.5** |    3.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        188.3 |  **45.5** |   51.6 |
| TPOT median (ms)          |         19.2 |  **15.1** |   25.0 |
| E2E median (ms)           |        877.0 | **567.3** |  977.1 |
| Throughput median (tok/s) |         41.4 |  **61.9** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        127.7 |  **59.4** |   76.6 |
| TPOT median (ms)          |         24.1 |  **22.3** |  116.3 |
| E2E median (ms)           |        284.0 | **182.5** |  385.3 |
| Throughput median (tok/s) |         17.0 |  **24.7** |   13.3 |
| Correctness               |          98% |       99% |    99% |
