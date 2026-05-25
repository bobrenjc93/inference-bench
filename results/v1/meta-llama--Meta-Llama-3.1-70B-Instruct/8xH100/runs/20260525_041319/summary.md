# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:04 PM PT, May 24 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     333.8s (5.6m) | `9f91b40` |
| vllm         |   1266.0s (21.1m) | `b06813e` |
| sglang       | **199.2s (3.3m)** | `e86fdf3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        295.1 |     163.5 | **146.6** |
| TPOT median (ms)          |        154.9 |  **60.7** |      77.9 |
| E2E median (ms)           |        396.6 | **216.0** |     219.0 |
| Throughput median (tok/s) |          3.7 |   **6.8** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        295.1 |     217.0 | **196.4** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        331.5 | **237.5** |     336.4 |
| Throughput median (tok/s) |          3.0 |   **4.2** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        736.7 |     169.3 | **163.9** |
| TPOT median (ms)          |        131.3 |  **59.5** |     105.3 |
| E2E median (ms)           |        864.3 | **217.4** |     260.2 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        325.3 | **57.6** |   76.8 |
| TPOT median (ms)          |        133.3 | **27.2** |   65.1 |
| E2E median (ms)           |        426.1 | **77.5** |  155.9 |
| Throughput median (tok/s) |          3.0 | **15.9** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        982.0 |      83.3 | **66.7** |
| TPOT median (ms)          |         16.4 |  **15.0** |     22.2 |
| E2E median (ms)           |       1620.9 | **648.4** |    828.7 |
| Throughput median (tok/s) |         21.3 |  **57.1** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        526.8 |     138.1 | **130.1** |
| TPOT median (ms)          |         87.2 |  **32.5** |      54.1 |
| E2E median (ms)           |        727.9 | **279.4** |     360.0 |
| Throughput median (tok/s) |          6.5 |  **18.1** |      13.1 |
| Correctness               |          98% |       99% |       99% |
