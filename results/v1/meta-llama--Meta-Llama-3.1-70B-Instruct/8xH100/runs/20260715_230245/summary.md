# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, Jul 15 2026

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
| torchinferno | **45.5s (0.8m)** | `96adc9d` |
| vllm         |    304.2s (5.1m) | `eb33ff3` |
| sglang       |    207.0s (3.5m) | `b0b2dfb` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        141.6 | **70.8** |   79.7 |
| TPOT median (ms)          |     **31.3** |     37.0 |   65.0 |
| E2E median (ms)           |        165.5 | **96.1** |  137.0 |
| Throughput median (tok/s) |          6.9 | **13.6** |   10.0 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **57.4** | 69.6 |  127.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **76.5** | 85.8 |  205.9 |
| Throughput median (tok/s) |     **13.1** | 11.7 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        195.3 | **75.4** |   85.4 |
| TPOT median (ms)          |         35.4 | **34.7** |   75.0 |
| E2E median (ms)           |        224.3 | **99.7** |  149.1 |
| Throughput median (tok/s) |          5.0 | **13.1** |    9.1 |
| Correctness               |          98% |      98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.1 | **37.7** |   53.2 |
| TPOT median (ms)          |         35.1 | **27.9** |  400.5 |
| E2E median (ms)           |         74.8 | **58.3** |  461.3 |
| Throughput median (tok/s) |         19.1 | **22.7** |    2.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        177.3 |  **47.2** |   53.0 |
| TPOT median (ms)          |         19.1 |  **15.3** |   24.7 |
| E2E median (ms)           |        889.7 | **578.6** |  959.4 |
| Throughput median (tok/s) |         41.7 |  **60.6** |   39.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        124.9 |  **60.1** |   79.7 |
| TPOT median (ms)          |         24.2 |  **23.0** |  113.1 |
| E2E median (ms)           |        286.2 | **183.7** |  382.5 |
| Throughput median (tok/s) |         17.2 |  **24.3** |   13.2 |
| Correctness               |          99% |       98% |    98% |
