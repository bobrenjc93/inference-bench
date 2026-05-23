# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:03 PM PT, May 23 2026

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
| torchinferno |     395.5s (6.6m) | `9f91b40` |
| vllm         |   1342.9s (22.4m) | `819c610` |
| sglang       | **194.8s (3.2m)** | `982f67d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        273.9 |    163.5 | **141.2** |
| TPOT median (ms)          |        155.2 | **57.7** |      76.8 |
| E2E median (ms)           |        372.7 |    216.0 | **212.7** |
| Throughput median (tok/s) |          4.0 |  **6.9** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        280.1 | **204.6** |  218.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        309.2 | **270.9** |  353.2 |
| Throughput median (tok/s) |          3.2 |   **3.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        752.7 |     173.9 | **162.2** |
| TPOT median (ms)          |        193.1 |  **56.7** |     102.4 |
| E2E median (ms)           |        890.4 | **224.2** |     265.4 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        324.5 | **58.2** |   77.3 |
| TPOT median (ms)          |        134.1 | **26.3** |   47.3 |
| E2E median (ms)           |        422.5 | **78.9** |  136.2 |
| Throughput median (tok/s) |          3.4 | **15.7** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        781.2 |      72.8 | **69.6** |
| TPOT median (ms)          |         15.6 |  **15.0** |     22.0 |
| E2E median (ms)           |       1585.7 | **622.8** |    836.8 |
| Throughput median (tok/s) |         23.3 |  **58.1** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        482.5 |     134.6 | **133.8** |
| TPOT median (ms)          |         99.6 |  **31.2** |      49.7 |
| E2E median (ms)           |        716.1 | **282.6** |     360.8 |
| Throughput median (tok/s) |          7.1 |  **18.1** |      13.2 |
| Correctness               |          98% |       98% |       98% |
