# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 9:43 PM PT, May 18 2026

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

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     215.8s (3.6m) | `9f91b40` |
| vllm         |   1083.2s (18.1m) | `6e889b5` |
| sglang       | **167.1s (2.8m)** | `4c9f31b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        280.1 |    166.7 | **137.8** |
| TPOT median (ms)          |        153.2 | **61.3** |      73.4 |
| E2E median (ms)           |        368.5 |    221.3 | **207.4** |
| Throughput median (tok/s) |          4.1 |  **6.5** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.2 | **170.3** |  207.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        299.3 | **194.0** |  350.9 |
| Throughput median (tok/s) |          3.3 |   **5.2** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        525.0 |     172.9 | **157.9** |
| TPOT median (ms)          |        116.5 |  **61.0** |     106.8 |
| E2E median (ms)           |        616.6 | **222.7** |     260.3 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        346.0 | **57.9** |   73.2 |
| TPOT median (ms)          |        130.9 | **26.7** |   65.7 |
| E2E median (ms)           |        453.3 | **78.3** |  152.9 |
| Throughput median (tok/s) |          2.8 | **15.5** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        732.4 |  **67.1** |   68.8 |
| TPOT median (ms)          |         16.1 |  **15.0** |   22.1 |
| E2E median (ms)           |       1366.1 | **599.2** |  827.4 |
| Throughput median (tok/s) |         28.2 |  **59.5** |   42.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        431.6 | **127.0** |  129.1 |
| TPOT median (ms)          |         83.3 |  **32.8** |   53.6 |
| E2E median (ms)           |        620.7 | **263.1** |  359.8 |
| Throughput median (tok/s) |          8.1 |  **18.6** |   13.2 |
| Correctness               |          98% |       99% |    99% |
