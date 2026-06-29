# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |    661.2s (11.0m) | `642b555` |
| vllm         |     564.1s (9.4m) | `4559c43` |
| sglang       | **277.1s (4.6m)** | `38d4ffc` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        165.6 | **136.9** |  149.0 |
| TPOT median (ms)          |     **47.2** |      49.0 |   70.6 |
| E2E median (ms)           |        208.0 | **177.4** |  219.1 |
| Throughput median (tok/s) |          5.7 |   **8.1** |    5.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        269.2 |     211.4 | **203.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        287.5 | **236.8** |     343.5 |
| Throughput median (tok/s) |          3.5 |   **4.2** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        321.4 |     167.1 | **163.4** |
| TPOT median (ms)          |         61.4 |  **51.4** |      96.1 |
| E2E median (ms)           |        381.7 | **207.1** |     261.4 |
| Throughput median (tok/s) |          3.5 |   **6.5** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        192.9 | **63.7** |   81.6 |
| TPOT median (ms)          |         57.2 | **32.0** |   39.5 |
| E2E median (ms)           |        239.5 | **87.6** |  133.5 |
| Throughput median (tok/s) |          5.9 | **13.9** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        316.8 |      77.8 | **70.5** |
| TPOT median (ms)          |         23.0 |  **14.8** |     22.4 |
| E2E median (ms)           |       1117.0 | **603.2** |    845.6 |
| Throughput median (tok/s) |         32.8 |  **58.5** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        253.2 | **131.4** |  133.6 |
| TPOT median (ms)          |         37.8 |  **29.5** |   45.7 |
| E2E median (ms)           |        446.8 | **262.4** |  360.6 |
| Throughput median (tok/s) |         10.3 |  **18.2** |   13.1 |
| Correctness               |          99% |       98% |    98% |
