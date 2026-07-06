# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         3/20 | **15/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **51.8s (0.9m)** | `b488218` |
| vllm         |    544.8s (9.1m) | `f70caef` |
| sglang       |    249.9s (4.2m) | `1b481de` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        143.0 | **120.2** |  132.6 |
| TPOT median (ms)          |         44.7 |  **39.8** |   80.0 |
| E2E median (ms)           |        182.4 | **153.1** |  211.7 |
| Throughput median (tok/s) |          6.4 |   **9.0** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |     **93.9** | 127.3 |  213.2 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **100.6** | 150.9 |  355.7 |
| Throughput median (tok/s) |      **9.9** |   6.6 |    2.8 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.5 | **151.6** |  162.2 |
| TPOT median (ms)          |         62.3 |  **46.4** |  109.1 |
| E2E median (ms)           |        330.7 | **197.5** |  274.4 |
| Throughput median (tok/s) |          4.3 |   **6.9** |    4.8 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         81.2 | **32.6** |   47.4 |
| TPOT median (ms)          |         64.0 | **21.7** |  371.7 |
| E2E median (ms)           |        117.0 | **48.1** |  395.8 |
| Throughput median (tok/s) |         12.4 | **25.7** |    3.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        251.5 |      76.4 | **68.6** |
| TPOT median (ms)          |         20.8 |  **14.7** |     22.2 |
| E2E median (ms)           |       1068.1 | **599.0** |    918.8 |
| Throughput median (tok/s) |         35.5 |  **59.9** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        169.6 | **101.6** |  124.8 |
| TPOT median (ms)          |         38.3 |  **24.5** |  116.6 |
| E2E median (ms)           |        359.8 | **229.7** |  431.3 |
| Throughput median (tok/s) |         13.7 |  **21.6** |   11.7 |
| Correctness               |          98% |       99% |    99% |
