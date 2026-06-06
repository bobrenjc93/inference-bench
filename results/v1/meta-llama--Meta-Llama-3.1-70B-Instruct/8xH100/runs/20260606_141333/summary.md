# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          1/4 |   **2/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         2/20 | **14/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     361.0s (6.0m) | `75bbe35` |
| vllm         |   1358.1s (22.6m) | `67d3792` |
| sglang       | **202.5s (3.4m)** | `bd7fea0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        299.3 |   171.6 | **143.6** |
| TPOT median (ms)          |     **53.4** |    60.3 |      75.4 |
| E2E median (ms)           |        354.8 |   222.8 | **213.9** |
| Throughput median (tok/s) |          3.4 | **6.7** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        258.6 | **202.4** |  207.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        361.4 | **225.7** |  354.8 |
| Throughput median (tok/s) |          2.8 |   **4.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        704.1 |     185.6 | **156.4** |
| TPOT median (ms)          |     **63.4** |      64.3 |     102.1 |
| E2E median (ms)           |        779.6 | **244.5** |     259.9 |
| Throughput median (tok/s) |          1.8 |   **5.7** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        346.9 | **60.9** |   78.6 |
| TPOT median (ms)          |         29.7 | **28.5** |   59.8 |
| E2E median (ms)           |        389.1 | **82.2** |  146.0 |
| Throughput median (tok/s) |          3.4 | **14.7** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        537.9 |  **75.3** |   75.6 |
| TPOT median (ms)          |         32.0 |  **15.1** |   23.6 |
| E2E median (ms)           |       1590.2 | **635.8** |  909.5 |
| Throughput median (tok/s) |         21.2 |  **58.4** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        429.4 |     139.2 | **132.3** |
| TPOT median (ms)          |         35.7 |  **33.6** |      52.2 |
| E2E median (ms)           |        695.0 | **282.2** |     376.8 |
| Throughput median (tok/s) |          6.5 |  **18.0** |      12.5 |
| Correctness               |          98% |       99% |       98% |
