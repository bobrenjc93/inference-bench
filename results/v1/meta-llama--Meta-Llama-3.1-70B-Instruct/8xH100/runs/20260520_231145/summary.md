# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 PM PT, May 20 2026

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
| torchinferno |     337.3s (5.6m) | `9f91b40` |
| vllm         |   1219.0s (20.3m) | `6dc0a71` |
| sglang       | **224.7s (3.7m)** | `9f2bc24` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        302.4 |    175.2 | **136.5** |
| TPOT median (ms)          |        153.5 | **64.3** |      75.3 |
| E2E median (ms)           |        407.5 |    233.9 | **205.7** |
| Throughput median (tok/s) |          3.8 |  **6.4** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        293.4 | **184.9** |  209.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        323.8 | **204.4** |  342.5 |
| Throughput median (tok/s) |          3.1 |   **4.9** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        893.4 |     169.9 | **154.7** |
| TPOT median (ms)          |        155.4 |  **57.0** |     106.9 |
| E2E median (ms)           |       1013.6 | **222.1** |     250.4 |
| Throughput median (tok/s) |          1.2 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        359.7 | **57.5** |   75.5 |
| TPOT median (ms)          |        130.5 | **26.5** |   64.1 |
| E2E median (ms)           |        471.3 | **78.0** |  150.7 |
| Throughput median (tok/s) |          2.8 | **15.6** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1025.4 |      73.4 | **66.3** |
| TPOT median (ms)          |         16.4 |  **15.1** |     21.8 |
| E2E median (ms)           |       1648.1 | **617.3** |    823.5 |
| Throughput median (tok/s) |         19.6 |  **58.0** |     43.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        574.9 |     132.2 | **128.4** |
| TPOT median (ms)          |         91.1 |  **32.6** |      53.6 |
| E2E median (ms)           |        772.8 | **271.2** |     354.5 |
| Throughput median (tok/s) |          6.1 |  **18.2** |      13.4 |
| Correctness               |          98% |       99% |       99% |
