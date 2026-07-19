# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 19 2026

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
| torchinferno | **40.2s (0.7m)** | `96adc9d` |
| vllm         |    344.1s (5.7m) | `ace9fda` |
| sglang       |    172.7s (2.9m) | `d4801be` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        139.3 |  **88.6** |   99.3 |
| TPOT median (ms)          |     **31.6** |      39.6 |   71.7 |
| E2E median (ms)           |        163.8 | **123.0** |  162.7 |
| Throughput median (tok/s) |          7.0 |  **11.7** |    7.9 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **74.1** | 75.4 |  166.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **90.0** | 92.9 |  242.4 |
| Throughput median (tok/s) |     **11.1** | 10.8 |    4.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.0 |  **86.5** |  102.6 |
| TPOT median (ms)          |     **35.4** |      35.8 |   78.8 |
| E2E median (ms)           |        221.3 | **124.3** |  168.0 |
| Throughput median (tok/s) |          5.1 |  **11.4** |    7.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         54.1 | **39.9** |   62.6 |
| TPOT median (ms)          |         35.2 | **32.0** |  420.3 |
| E2E median (ms)           |         76.4 | **62.1** |  471.5 |
| Throughput median (tok/s) |         19.3 | **20.8** |    3.0 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.3 |  **47.3** |   58.7 |
| TPOT median (ms)          |         19.4 |  **15.5** |   28.2 |
| E2E median (ms)           |        880.0 | **580.3** | 1073.1 |
| Throughput median (tok/s) |         40.7 |  **60.1** |   34.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        129.6 |  **67.5** |   98.0 |
| TPOT median (ms)          |     **24.3** |      24.6 |  119.8 |
| E2E median (ms)           |        286.3 | **196.5** |  423.5 |
| Throughput median (tok/s) |         16.7 |  **22.9** |   11.4 |
| Correctness               |          99% |       98% |    99% |
