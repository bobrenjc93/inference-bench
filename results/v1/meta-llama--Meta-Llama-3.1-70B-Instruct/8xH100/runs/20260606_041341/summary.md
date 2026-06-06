# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 PM PT, Jun 5 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     349.9s (5.8m) | `75bbe35` |
| vllm         |   1318.7s (22.0m) | `ec0a31d` |
| sglang       | **194.8s (3.2m)** | `aa55657` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        401.9 |     155.3 | **150.4** |
| TPOT median (ms)          |         55.7 |  **51.4** |      76.6 |
| E2E median (ms)           |        450.5 | **206.3** |     224.4 |
| Throughput median (tok/s) |          3.2 |   **7.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        276.0 | **190.9** |  202.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        379.5 | **214.6** |  332.4 |
| Throughput median (tok/s) |          2.6 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        733.3 |     173.9 | **163.5** |
| TPOT median (ms)          |     **62.0** |      69.0 |      97.7 |
| E2E median (ms)           |        795.9 | **234.1** |     260.2 |
| Throughput median (tok/s) |          1.6 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        399.2 | **58.1** |   85.7 |
| TPOT median (ms)          |         32.3 | **28.3** |   44.7 |
| E2E median (ms)           |        443.8 | **78.9** |  145.1 |
| Throughput median (tok/s) |          3.3 | **15.3** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        508.4 |  **67.4** |   74.8 |
| TPOT median (ms)          |         29.9 |  **15.1** |   23.7 |
| E2E median (ms)           |       1633.4 | **609.7** |  896.5 |
| Throughput median (tok/s) |         22.8 |  **58.9** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        463.8 | **129.1** |  135.4 |
| TPOT median (ms)          |         36.0 |  **32.8** |   48.5 |
| E2E median (ms)           |        740.6 | **268.7** |  371.7 |
| Throughput median (tok/s) |          6.7 |  **18.4** |   12.5 |
| Correctness               |          99% |       98% |    99% |
