# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 AM PT, May 23 2026

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
| torchinferno |     336.1s (5.6m) | `9f91b40` |
| vllm         |   1287.8s (21.5m) | `2a7d5b7` |
| sglang       | **208.9s (3.5m)** | `a5a64a3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        299.9 |    158.1 | **137.8** |
| TPOT median (ms)          |        154.7 | **58.6** |      77.7 |
| E2E median (ms)           |        408.6 |    215.1 | **208.0** |
| Throughput median (tok/s) |          3.6 |  **7.2** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        286.7 | **199.7** |  207.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        310.8 | **224.9** |  342.7 |
| Throughput median (tok/s) |          3.2 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        800.1 |     173.5 | **154.1** |
| TPOT median (ms)          |        102.0 |  **58.3** |     108.0 |
| E2E median (ms)           |        887.0 | **223.3** |     253.4 |
| Throughput median (tok/s) |          1.5 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        398.4 | **58.4** |   76.1 |
| TPOT median (ms)          |        130.5 | **26.9** |   65.1 |
| E2E median (ms)           |        497.6 | **79.7** |  151.8 |
| Throughput median (tok/s) |          2.6 | **15.5** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        821.7 |      69.2 | **63.8** |
| TPOT median (ms)          |         16.0 |  **15.1** |     22.4 |
| E2E median (ms)           |       1539.3 | **600.2** |    828.6 |
| Throughput median (tok/s) |         23.2 |  **59.1** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        521.4 |     131.8 | **127.8** |
| TPOT median (ms)          |         80.6 |  **31.8** |      54.6 |
| E2E median (ms)           |        728.7 | **268.7** |     356.9 |
| Throughput median (tok/s) |          6.8 |  **18.5** |      13.1 |
| Correctness               |          98% |       99% |       98% |
