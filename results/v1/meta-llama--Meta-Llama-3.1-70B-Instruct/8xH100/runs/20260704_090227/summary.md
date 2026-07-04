# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         5/20 | **12/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.7s (0.6m)** | `390fed4` |
| vllm         |    297.5s (5.0m) | `e7c9df9` |
| sglang       |    174.6s (2.9m) | `b941e33` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        158.6 | **134.2** |  143.0 |
| TPOT median (ms)          |     **46.2** |      48.3 |   74.2 |
| E2E median (ms)           |        204.2 | **170.8** |  217.3 |
| Throughput median (tok/s) |          5.9 |   **8.1** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **174.4** | 198.3 |  225.4 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **182.1** | 223.1 |  378.6 |
| Throughput median (tok/s) |      **5.5** |   4.5 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        348.0 |     173.5 | **167.6** |
| TPOT median (ms)          |     **60.9** |      61.4 |     106.6 |
| E2E median (ms)           |        401.4 | **224.6** |     274.2 |
| Throughput median (tok/s) |          3.5 |   **6.0** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        128.4 | **61.9** |   74.6 |
| TPOT median (ms)          |         69.0 | **30.7** |   66.0 |
| E2E median (ms)           |        161.1 | **85.5** |  143.1 |
| Throughput median (tok/s) |          8.2 | **14.2** |    9.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        244.8 |      81.4 | **75.2** |
| TPOT median (ms)          |         21.0 |  **14.8** |     22.5 |
| E2E median (ms)           |        987.0 | **621.6** |    821.3 |
| Throughput median (tok/s) |         36.5 |  **57.5** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        210.8 | **129.9** |  137.2 |
| TPOT median (ms)          |         39.4 |  **31.1** |   53.9 |
| E2E median (ms)           |        387.2 | **265.1** |  366.9 |
| Throughput median (tok/s) |         11.9 |  **18.0** |   12.9 |
| Correctness               |          99% |       98% |    99% |
