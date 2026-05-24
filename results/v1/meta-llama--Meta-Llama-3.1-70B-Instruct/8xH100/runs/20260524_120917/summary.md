# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, May 24 2026

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
| torchinferno |     305.5s (5.1m) | `9f91b40` |
| vllm         |   1241.7s (20.7m) | `1806d1a` |
| sglang       | **210.1s (3.5m)** | `b6f71d5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        289.2 |     153.6 | **137.6** |
| TPOT median (ms)          |        153.6 |  **56.0** |      74.5 |
| E2E median (ms)           |        385.4 | **202.5** |     210.6 |
| Throughput median (tok/s) |          3.9 |   **7.2** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        270.9 |     203.5 | **198.9** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        300.0 | **235.6** |     336.6 |
| Throughput median (tok/s) |          3.3 |   **4.2** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        697.1 |     164.8 | **156.3** |
| TPOT median (ms)          |         96.0 |  **60.3** |     107.3 |
| E2E median (ms)           |        797.0 | **212.7** |     255.1 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        317.1 | **57.7** |   73.0 |
| TPOT median (ms)          |        133.0 | **26.2** |   67.6 |
| E2E median (ms)           |        415.8 | **77.7** |  160.2 |
| Throughput median (tok/s) |          3.7 | **15.4** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        883.2 |      65.3 | **64.6** |
| TPOT median (ms)          |         16.3 |  **15.0** |     22.7 |
| E2E median (ms)           |       1549.5 | **608.1** |    839.0 |
| Throughput median (tok/s) |         22.5 |  **59.9** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        491.5 |     129.0 | **126.1** |
| TPOT median (ms)          |         79.8 |  **31.5** |      54.4 |
| E2E median (ms)           |        689.6 | **267.3** |     360.3 |
| Throughput median (tok/s) |          7.0 |  **18.6** |      12.9 |
| Correctness               |          98% |       98% |       98% |
