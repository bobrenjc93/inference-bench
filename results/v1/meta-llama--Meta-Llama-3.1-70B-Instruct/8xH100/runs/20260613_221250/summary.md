# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jun 13 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     351.2s (5.9m) | `a102128` |
| vllm         |   1343.0s (22.4m) | `71b961d` |
| sglang       | **204.2s (3.4m)** | `10d3337` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        320.0 |     154.8 | **148.8** |
| TPOT median (ms)          |        101.3 |  **56.0** |      79.6 |
| E2E median (ms)           |        406.5 | **201.0** |     220.8 |
| Throughput median (tok/s) |          3.1 |   **7.3** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.5 | **188.9** |  206.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        441.3 | **256.7** |  337.1 |
| Throughput median (tok/s) |          2.3 |   **3.9** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        720.7 |     179.2 | **167.2** |
| TPOT median (ms)          |     **63.9** |      68.4 |      94.3 |
| E2E median (ms)           |        805.3 | **235.8** |     267.5 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        235.1 | **60.2** |   85.2 |
| TPOT median (ms)          |         47.1 | **28.1** |   41.8 |
| E2E median (ms)           |        281.5 | **81.4** |  138.7 |
| Throughput median (tok/s) |          4.5 | **15.1** |   10.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        339.1 |      72.4 | **64.8** |
| TPOT median (ms)          |         21.8 |  **14.9** |     23.0 |
| E2E median (ms)           |       1108.6 | **604.5** |    858.7 |
| Throughput median (tok/s) |         32.0 |  **58.9** |     41.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        387.5 | **131.1** |  134.4 |
| TPOT median (ms)          |         46.8 |  **33.5** |   47.7 |
| E2E median (ms)           |        608.6 | **275.9** |  364.6 |
| Throughput median (tok/s) |          8.7 |  **18.3** |   13.0 |
| Correctness               |          98% |       99% |    99% |
