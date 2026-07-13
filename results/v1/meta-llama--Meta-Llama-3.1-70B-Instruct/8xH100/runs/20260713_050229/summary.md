# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jul 12 2026

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
| torchinferno | **45.2s (0.8m)** | `96adc9d` |
| vllm         |    364.5s (6.1m) | `36484e4` |
| sglang       |    165.8s (2.8m) | `cbcbef6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.3 |  **75.6** |   79.3 |
| TPOT median (ms)          |     **31.9** |      39.9 |   65.6 |
| E2E median (ms)           |        165.5 | **107.9** |  133.6 |
| Throughput median (tok/s) |          7.0 |  **12.2** |   10.0 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **54.9** | 75.9 |  129.2 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **72.3** | 96.9 |  206.4 |
| Throughput median (tok/s) |     **13.8** | 10.3 |    4.8 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        186.8 |  **78.8** |   86.2 |
| TPOT median (ms)          |         35.8 |  **34.2** |   72.6 |
| E2E median (ms)           |        215.8 | **106.6** |  148.2 |
| Throughput median (tok/s) |          5.2 |  **12.4** |    9.2 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.4 | **35.7** |   52.0 |
| TPOT median (ms)          |         34.9 | **23.4** |  447.2 |
| E2E median (ms)           |         75.3 | **53.6** |  473.2 |
| Throughput median (tok/s) |         19.5 | **23.8** |    3.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        181.3 |  **47.3** |   52.3 |
| TPOT median (ms)          |         19.5 |  **15.8** |   24.6 |
| E2E median (ms)           |        864.0 | **587.9** |  965.5 |
| Throughput median (tok/s) |         40.3 |  **59.1** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        123.5 |  **62.7** |   79.8 |
| TPOT median (ms)          |         24.4 |  **22.6** |  122.0 |
| E2E median (ms)           |        278.6 | **190.6** |  385.4 |
| Throughput median (tok/s) |         17.2 |  **23.6** |   13.3 |
| Correctness               |          99% |       99% |    99% |
