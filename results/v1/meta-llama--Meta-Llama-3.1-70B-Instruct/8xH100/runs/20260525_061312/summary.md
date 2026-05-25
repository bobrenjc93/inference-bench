# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:04 PM PT, May 24 2026

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
| torchinferno |     322.0s (5.4m) | `9f91b40` |
| vllm         |   1311.2s (21.9m) | `6cbe448` |
| sglang       | **215.8s (3.6m)** | `2bd3ac0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        298.8 |    161.7 | **143.2** |
| TPOT median (ms)          |        155.9 | **64.3** |      75.0 |
| E2E median (ms)           |        416.5 |    218.0 | **214.6** |
| Throughput median (tok/s) |          3.4 |  **6.7** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        306.6 | **195.6** |  201.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        334.9 | **218.1** |  339.3 |
| Throughput median (tok/s) |          3.0 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        850.8 |     173.0 | **164.8** |
| TPOT median (ms)          |        181.5 |  **56.2** |      99.2 |
| E2E median (ms)           |        937.6 | **225.9** |     262.7 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        382.7 | **57.9** |   77.4 |
| TPOT median (ms)          |        133.6 | **27.2** |   62.2 |
| E2E median (ms)           |        486.6 | **78.7** |  150.6 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.5 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        849.3 |      71.8 | **68.3** |
| TPOT median (ms)          |         15.9 |  **15.0** |     22.1 |
| E2E median (ms)           |       1559.0 | **607.4** |    805.9 |
| Throughput median (tok/s) |         21.5 |  **58.9** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        537.6 |     132.0 | **130.9** |
| TPOT median (ms)          |         97.4 |  **32.5** |      51.7 |
| E2E median (ms)           |        746.9 | **269.6** |     354.6 |
| Throughput median (tok/s) |          6.4 |  **18.4** |      13.2 |
| Correctness               |          98% |       98% |       99% |
