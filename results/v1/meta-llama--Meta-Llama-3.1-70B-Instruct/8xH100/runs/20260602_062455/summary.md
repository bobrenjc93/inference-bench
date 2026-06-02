# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:12 PM PT, Jun 1 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          1/4 |   **3/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         2/20 | **14/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     314.7s (5.2m) | `1cbe525` |
| vllm         |   1331.9s (22.2m) | `f91fb2f` |
| sglang       | **214.1s (3.6m)** | `3b26644` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        242.1 |   166.3 | **140.0** |
| TPOT median (ms)          |     **46.4** |    59.3 |      77.4 |
| E2E median (ms)           |        280.5 |   224.3 | **213.2** |
| Throughput median (tok/s) |          5.2 | **6.5** |       5.7 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1043.5 | **183.6** |  196.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |       1144.1 | **205.3** |  330.5 |
| Throughput median (tok/s) |          0.9 |   **4.9** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2641.2 |     168.7 | **166.9** |
| TPOT median (ms)          |        391.7 |  **56.2** |      99.6 |
| E2E median (ms)           |       2934.3 | **217.1** |     268.4 |
| Throughput median (tok/s) |          0.4 |   **6.3** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        747.9 | **57.6** |   80.6 |
| TPOT median (ms)          |     **27.3** |     28.7 |   48.3 |
| E2E median (ms)           |        771.6 | **77.9** |  140.1 |
| Throughput median (tok/s) |          1.5 | **15.5** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       2897.5 |  **68.5** |   74.6 |
| TPOT median (ms)          |         93.6 |  **15.0** |   22.9 |
| E2E median (ms)           |       5775.5 | **599.3** |  860.4 |
| Throughput median (tok/s) |          5.5 |  **59.1** |   40.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1514.4 | **128.9** |  131.6 |
| TPOT median (ms)          |        111.8 |  **31.8** |   49.6 |
| E2E median (ms)           |       2181.2 | **264.8** |  362.5 |
| Throughput median (tok/s) |          2.7 |  **18.5** |   12.9 |
| Correctness               |          99% |       99% |    99% |
