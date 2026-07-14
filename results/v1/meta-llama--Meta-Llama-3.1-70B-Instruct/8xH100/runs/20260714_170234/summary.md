# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jul 14 2026

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
| torchinferno | **44.7s (0.7m)** | `96adc9d` |
| vllm         |    408.7s (6.8m) | `cdaa40d` |
| sglang       |    155.2s (2.6m) | `cb47a68` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        143.1 | **69.3** |   79.1 |
| TPOT median (ms)          |     **31.2** |     38.7 |   65.8 |
| E2E median (ms)           |        167.2 | **97.2** |  133.2 |
| Throughput median (tok/s) |          6.8 | **13.5** |   10.1 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **56.9** | 74.6 |  116.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **75.4** | 90.7 |  197.5 |
| Throughput median (tok/s) |     **13.3** | 11.0 |    5.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        194.0 |  **79.3** |   82.0 |
| TPOT median (ms)          |     **34.3** |      45.7 |   70.6 |
| E2E median (ms)           |        222.3 | **112.1** |  140.1 |
| Throughput median (tok/s) |          5.1 |  **11.8** |    9.4 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         53.1 | **37.1** |   51.7 |
| TPOT median (ms)          |         35.1 | **27.5** |  406.9 |
| E2E median (ms)           |         75.5 | **56.2** |  491.7 |
| Throughput median (tok/s) |         19.0 | **23.2** |    2.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        185.1 |  **47.2** |   52.0 |
| TPOT median (ms)          |         19.2 |  **15.6** |   24.1 |
| E2E median (ms)           |        864.7 | **581.1** |  929.5 |
| Throughput median (tok/s) |         40.9 |  **60.3** |   40.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        126.5 |  **61.5** |   76.2 |
| TPOT median (ms)          |     **24.0** |      25.5 |  113.5 |
| E2E median (ms)           |        281.0 | **187.4** |  378.4 |
| Throughput median (tok/s) |         17.0 |  **24.0** |   13.5 |
| Correctness               |          99% |       98% |    99% |
