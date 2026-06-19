# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jun 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **19/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     353.7s (5.9m) | `cd7d8e9` |
| vllm         |     408.3s (6.8m) | `4a083cc` |
| sglang       | **254.6s (4.2m)** | `d271de6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        314.1 | **138.5** |  148.9 |
| TPOT median (ms)          |         54.4 |  **48.1** |   74.4 |
| E2E median (ms)           |        368.2 | **178.1** |  213.2 |
| Throughput median (tok/s) |          3.3 |   **8.1** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        310.8 | **195.4** |  220.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        422.6 | **279.2** |  359.4 |
| Throughput median (tok/s) |          2.4 |   **3.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        701.7 | **159.1** |  161.6 |
| TPOT median (ms)          |         63.4 |  **52.4** |  105.7 |
| E2E median (ms)           |        760.6 | **206.6** |  260.1 |
| Throughput median (tok/s) |          1.9 |   **6.9** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        193.8 | **57.0** |   81.6 |
| TPOT median (ms)          |         33.3 | **29.0** |   37.2 |
| E2E median (ms)           |        233.3 | **79.5** |  124.6 |
| Throughput median (tok/s) |          5.6 | **15.0** |   10.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        331.4 |  **66.0** |   73.9 |
| TPOT median (ms)          |         21.3 |  **15.0** |   22.6 |
| E2E median (ms)           |       1080.3 | **594.8** |  834.3 |
| Throughput median (tok/s) |         32.3 |  **59.4** |   41.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        370.4 | **123.2** |  137.2 |
| TPOT median (ms)          |         34.5 |  **28.9** |   48.0 |
| E2E median (ms)           |        573.0 | **267.7** |  358.3 |
| Throughput median (tok/s) |          9.1 |  **18.6** |   13.0 |
| Correctness               |          98% |       98% |    99% |
