# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 11 2026

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
| torchinferno | **47.8s (0.8m)** | `7e3d6f9` |
| vllm         |    354.9s (5.9m) | `8e98163` |
| sglang       |    163.3s (2.7m) | `592c043` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        147.8 | **69.2** |   81.9 |
| TPOT median (ms)          |     **31.2** |     37.4 |   65.0 |
| E2E median (ms)           |        172.0 | **93.4** |  137.6 |
| Throughput median (tok/s) |          6.6 | **13.9** |    9.7 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.8** | 68.5 |  118.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **76.1** | 88.0 |  188.9 |
| Throughput median (tok/s) |     **13.1** | 11.4 |    5.3 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        190.5 |     102.1 | **82.7** |
| TPOT median (ms)          |     **34.0** |      64.6 |     76.1 |
| E2E median (ms)           |        219.4 | **136.2** |    143.2 |
| Throughput median (tok/s) |          5.2 |   **9.9** |      9.6 |
| Correctness               |          98% |       98% |      98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.1 | **37.3** |   52.6 |
| TPOT median (ms)          |         34.6 | **27.7** |  379.3 |
| E2E median (ms)           |         73.9 | **56.0** |  428.8 |
| Throughput median (tok/s) |         19.5 | **22.9** |    3.4 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        175.0 |  **47.4** |   52.2 |
| TPOT median (ms)          |         19.1 |  **15.4** |   25.1 |
| E2E median (ms)           |        890.7 | **586.9** |  977.0 |
| Throughput median (tok/s) |         41.7 |  **60.3** |   38.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.6 |  **64.9** |   77.5 |
| TPOT median (ms)          |     **23.8** |      29.0 |  109.1 |
| E2E median (ms)           |        286.4 | **192.1** |  375.1 |
| Throughput median (tok/s) |         17.2 |  **23.7** |   13.3 |
| Correctness               |          99% |       99% |    98% |
