# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:02 PM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **88.5s (1.5m)** | `26df1b4` |
| vllm         |  1260.4s (21.0m) | `ff712f6` |
| sglang       |    187.3s (3.1m) | `46e0f50` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        314.2 |    167.6 | **141.6** |
| TPOT median (ms)          |        159.9 | **57.0** |      80.7 |
| E2E median (ms)           |        408.0 |    223.4 | **218.5** |
| Throughput median (tok/s) |          3.6 |  **6.6** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        235.5 | **214.1** |  215.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        335.6 | **245.5** |  363.3 |
| Throughput median (tok/s) |          3.0 |   **4.1** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        854.7 |     187.3 | **168.7** |
| TPOT median (ms)          |        136.4 |  **57.9** |     105.8 |
| E2E median (ms)           |        955.7 | **238.8** |     274.9 |
| Throughput median (tok/s) |          1.3 |   **5.8** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        375.2 | **61.9** |   79.4 |
| TPOT median (ms)          |        137.4 | **27.7** |   73.0 |
| E2E median (ms)           |        465.3 | **84.6** |  161.2 |
| Throughput median (tok/s) |          3.2 | **14.5** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1149.6 |  **74.0** |   75.8 |
| TPOT median (ms)          |         16.4 |  **15.1** |   22.0 |
| E2E median (ms)           |       1910.4 | **617.2** |  841.2 |
| Throughput median (tok/s) |         18.0 |  **57.9** |   42.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        585.8 |     141.0 | **136.3** |
| TPOT median (ms)          |         90.0 |  **31.5** |      56.3 |
| E2E median (ms)           |        815.0 | **281.9** |     371.8 |
| Throughput median (tok/s) |          5.8 |  **17.8** |      12.8 |
| Correctness               |          98% |       98% |       99% |
