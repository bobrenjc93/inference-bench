# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 12 2026

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
| torchinferno | **51.3s (0.9m)** | `96adc9d` |
| vllm         |    279.3s (4.7m) | `ee5a89f` |
| sglang       |    168.7s (2.8m) | `4cec9ef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.0 |  **77.5** |   79.7 |
| TPOT median (ms)          |     **31.1** |      38.7 |   64.5 |
| E2E median (ms)           |        167.0 | **109.0** |  133.5 |
| Throughput median (tok/s) |          6.9 |  **12.1** |   10.1 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.9** | 77.9 |  127.0 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **71.5** | 96.2 |  208.5 |
| Throughput median (tok/s) |     **14.0** | 10.4 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.0 |  **78.6** |   84.5 |
| TPOT median (ms)          |     **34.1** |      37.8 |   75.8 |
| E2E median (ms)           |        219.9 | **106.2** |  142.7 |
| Throughput median (tok/s) |          5.1 |  **12.5** |    8.7 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         52.9 | **35.0** |   52.4 |
| TPOT median (ms)          |         34.9 | **23.1** |  370.5 |
| E2E median (ms)           |         75.4 | **53.0** |  421.8 |
| Throughput median (tok/s) |         19.6 | **24.2** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        190.2 |  **47.7** |   52.1 |
| TPOT median (ms)          |         19.8 |  **15.6** |   25.0 |
| E2E median (ms)           |        877.4 | **584.9** |  928.0 |
| Throughput median (tok/s) |         40.8 |  **60.1** |   38.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.8 |  **63.4** |   79.1 |
| TPOT median (ms)          |         24.0 |  **23.0** |  107.2 |
| E2E median (ms)           |        282.2 | **189.9** |  366.9 |
| Throughput median (tok/s) |         17.3 |  **23.9** |   13.1 |
| Correctness               |          99% |       99% |    99% |
