# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 PM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno | **102.3s (1.7m)** | `9f91b40` |
| vllm         |   1403.4s (23.4m) | `d0a100c` |
| sglang       |     175.9s (2.9m) | `93fa577` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        286.4 |    168.1 | **147.0** |
| TPOT median (ms)          |        163.4 | **63.5** |      77.5 |
| E2E median (ms)           |        388.5 |    226.1 | **220.2** |
| Throughput median (tok/s) |          3.9 |  **6.5** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.6 | **174.5** |  223.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        327.7 | **197.2** |  376.2 |
| Throughput median (tok/s) |          3.1 |   **5.1** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1111.1 |     179.2 | **167.9** |
| TPOT median (ms)          |        102.6 |  **61.8** |     105.9 |
| E2E median (ms)           |       1182.8 | **232.9** |     274.5 |
| Throughput median (tok/s) |          1.0 |   **5.9** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        372.9 | **61.7** |   82.7 |
| TPOT median (ms)          |        139.7 | **28.5** |   61.3 |
| E2E median (ms)           |        480.9 | **83.1** |  149.9 |
| Throughput median (tok/s) |          2.9 | **14.7** |    9.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1117.6 |      84.9 | **74.7** |
| TPOT median (ms)          |         17.4 |  **15.0** |     22.5 |
| E2E median (ms)           |       1714.5 | **646.4** |    886.7 |
| Throughput median (tok/s) |         20.7 |  **57.2** |     41.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        635.7 | **133.7** |  139.2 |
| TPOT median (ms)          |         84.6 |  **33.7** |   53.4 |
| E2E median (ms)           |        818.9 | **277.1** |  381.5 |
| Throughput median (tok/s) |          6.3 |  **17.9** |   12.6 |
| Correctness               |          98% |       99% |    99% |
