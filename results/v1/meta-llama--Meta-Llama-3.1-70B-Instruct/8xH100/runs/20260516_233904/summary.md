# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:09 PM PT, May 16 2026

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
| torchinferno |     319.3s (5.3m) | `db749af` |
| vllm         |    961.2s (16.0m) | `0867497` |
| sglang       | **159.2s (2.7m)** | `9869ef0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        275.0 |    158.0 | **139.2** |
| TPOT median (ms)          |        146.7 | **56.7** |      73.0 |
| E2E median (ms)           |        364.7 |    210.6 | **207.9** |
| Throughput median (tok/s) |          4.0 |  **6.6** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        225.7 | **201.6** |  214.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        313.1 | **222.4** |  352.5 |
| Throughput median (tok/s) |          3.2 |   **4.5** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        583.6 |     173.5 | **161.9** |
| TPOT median (ms)          |        114.0 |  **55.8** |      98.9 |
| E2E median (ms)           |        678.3 | **226.6** |     259.6 |
| Throughput median (tok/s) |          2.0 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        334.5 | **58.3** |   73.8 |
| TPOT median (ms)          |        128.4 | **27.2** |   59.4 |
| E2E median (ms)           |        437.1 | **79.1** |  147.4 |
| Throughput median (tok/s) |          3.0 | **15.6** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **66.0** |   66.1 |
| TPOT median (ms)          |            - |  **15.0** |   22.6 |
| E2E median (ms)           |            - | **605.9** |  835.4 |
| Throughput median (tok/s) |            - |  **59.4** |   41.9 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        354.7 |     131.5 | **131.2** |
| TPOT median (ms)          |         97.3 |  **30.9** |      50.8 |
| E2E median (ms)           |        448.3 | **268.9** |     360.6 |
| Throughput median (tok/s) |          3.0 |  **18.5** |      13.1 |
| Correctness               |          98% |       99% |       99% |
