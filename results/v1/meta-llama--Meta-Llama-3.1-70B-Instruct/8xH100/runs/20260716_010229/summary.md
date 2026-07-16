# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 15 2026

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
| torchinferno | **45.8s (0.8m)** | `96adc9d` |
| vllm         |    334.2s (5.6m) | `81e13a0` |
| sglang       |    171.2s (2.9m) | `d9003dd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        140.9 |  **76.9** |   79.1 |
| TPOT median (ms)          |     **31.8** |      38.5 |   66.4 |
| E2E median (ms)           |        165.6 | **112.3** |  133.6 |
| Throughput median (tok/s) |          7.0 |  **12.2** |   10.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **59.2** | 76.6 |  119.5 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **77.0** | 96.7 |  207.0 |
| Throughput median (tok/s) |     **13.0** | 10.3 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.5 |  **75.6** |   91.4 |
| TPOT median (ms)          |     **34.3** |      36.5 |   70.1 |
| E2E median (ms)           |        218.1 | **101.1** |  148.4 |
| Throughput median (tok/s) |          5.2 |  **13.0** |    9.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.4 | **35.5** |   54.1 |
| TPOT median (ms)          |         34.9 | **23.5** |  364.9 |
| E2E median (ms)           |         74.0 | **53.9** |  421.9 |
| Throughput median (tok/s) |         19.3 | **24.2** |    3.3 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        184.8 |  **47.3** |   53.4 |
| TPOT median (ms)          |         19.2 |  **15.3** |   24.8 |
| E2E median (ms)           |        885.5 | **573.0** |  952.2 |
| Throughput median (tok/s) |         41.2 |  **61.4** |   38.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        125.8 |  **62.4** |   79.5 |
| TPOT median (ms)          |         24.0 |  **22.8** |  105.2 |
| E2E median (ms)           |        284.0 | **187.4** |  372.6 |
| Throughput median (tok/s) |         17.1 |  **24.2** |   13.2 |
| Correctness               |          98% |       98% |    98% |
