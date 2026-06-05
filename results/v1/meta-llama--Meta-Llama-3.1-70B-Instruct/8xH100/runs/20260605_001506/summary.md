# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 PM PT, Jun 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     380.6s (6.3m) | `795761d` |
| vllm         |   1316.7s (21.9m) | `b7c5baf` |
| sglang       | **196.2s (3.3m)** | `4737752` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        283.4 |     153.8 | **147.1** |
| TPOT median (ms)          |     **51.8** |      53.6 |      73.8 |
| E2E median (ms)           |        331.1 | **203.6** |     216.1 |
| Throughput median (tok/s) |          3.9 |   **7.2** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        247.8 | **203.6** |  207.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        352.5 | **247.5** |  351.8 |
| Throughput median (tok/s) |          2.8 |   **4.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        877.1 |     177.9 | **152.6** |
| TPOT median (ms)          |         91.7 |  **62.5** |     104.9 |
| E2E median (ms)           |        967.8 | **231.8** |     255.9 |
| Throughput median (tok/s) |          1.3 |   **6.0** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.2 | **61.2** |   78.9 |
| TPOT median (ms)          |         30.6 | **28.9** |   52.2 |
| E2E median (ms)           |        407.8 | **83.1** |  137.1 |
| Throughput median (tok/s) |          3.5 | **14.5** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        476.7 |      79.8 | **78.0** |
| TPOT median (ms)          |         28.7 |  **14.9** |     23.2 |
| E2E median (ms)           |       1531.3 | **613.4** |    878.3 |
| Throughput median (tok/s) |         24.1 |  **58.4** |     40.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        447.2 |     135.3 | **132.8** |
| TPOT median (ms)          |         40.6 |  **32.0** |      50.8 |
| E2E median (ms)           |        718.1 | **275.9** |     367.8 |
| Throughput median (tok/s) |          7.1 |  **18.0** |      12.8 |
| Correctness               |          99% |       99% |       99% |
