# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         5/20 | **13/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **41.7s (0.7m)** | `c71ec5f` |
| vllm         |    374.5s (6.2m) | `83762b7` |
| sglang       |    168.7s (2.8m) | `80856ab` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        144.0 |      90.2 | **79.8** |
| TPOT median (ms)          |     **30.5** |      43.1 |     64.4 |
| E2E median (ms)           |        167.7 | **124.7** |    133.0 |
| Throughput median (tok/s) |          6.8 |  **10.6** |     10.1 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **62.5** | 76.6 |  128.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **82.3** | 95.3 |  210.1 |
| Throughput median (tok/s) |     **12.2** | 10.5 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.1 |  **80.7** |   81.1 |
| TPOT median (ms)          |     **34.4** |      37.3 |   73.6 |
| E2E median (ms)           |        219.1 | **109.6** |  137.5 |
| Throughput median (tok/s) |          5.1 |  **12.6** |    9.6 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.5 | **37.4** |   52.1 |
| TPOT median (ms)          |         34.7 | **26.9** |  417.2 |
| E2E median (ms)           |         73.5 | **56.0** |  413.1 |
| Throughput median (tok/s) |         19.8 | **23.0** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        191.5 |  **48.3** |   52.1 |
| TPOT median (ms)          |         19.0 |  **15.6** |   24.1 |
| E2E median (ms)           |        842.7 | **588.0** |  918.4 |
| Throughput median (tok/s) |         40.8 |  **59.8** |   40.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        128.3 |  **66.6** |   78.8 |
| TPOT median (ms)          |     **23.7** |      24.6 |  115.9 |
| E2E median (ms)           |        277.1 | **194.7** |  362.4 |
| Throughput median (tok/s) |         16.9 |  **23.3** |   13.6 |
| Correctness               |          99% |       99% |    99% |
