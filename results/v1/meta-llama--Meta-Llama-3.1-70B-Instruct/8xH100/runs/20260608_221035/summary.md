# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 PM PT, Jun 8 2026

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
| torchinferno |     297.8s (5.0m) | `a80b89c` |
| vllm         |   1331.4s (22.2m) | `6afa250` |
| sglang       | **207.2s (3.5m)** | `b5c64b9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        263.3 |     155.7 | **151.0** |
| TPOT median (ms)          |        101.9 |  **52.2** |      78.0 |
| E2E median (ms)           |        354.5 | **203.8** |     223.1 |
| Throughput median (tok/s) |          3.3 |   **7.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        374.0 | **192.1** |  208.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        518.6 | **213.1** |  343.6 |
| Throughput median (tok/s) |          1.9 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        737.9 |     182.4 | **179.5** |
| TPOT median (ms)          |     **63.5** |      64.9 |      92.0 |
| E2E median (ms)           |        789.9 | **238.7** |     278.2 |
| Throughput median (tok/s) |          1.7 |   **5.8** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        463.7 | **59.1** |   83.4 |
| TPOT median (ms)          |         64.9 | **29.8** |   41.6 |
| E2E median (ms)           |        522.2 | **81.1** |  135.2 |
| Throughput median (tok/s) |          2.7 | **15.1** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        481.3 |  **70.7** |   78.6 |
| TPOT median (ms)          |         21.1 |  **15.0** |   23.1 |
| E2E median (ms)           |       1210.8 | **621.4** |  867.0 |
| Throughput median (tok/s) |         28.7 |  **57.9** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        464.1 | **132.0** |  140.3 |
| TPOT median (ms)          |         50.3 |  **32.4** |   46.9 |
| E2E median (ms)           |        679.2 | **271.6** |  369.4 |
| Throughput median (tok/s) |          7.7 |  **18.1** |   12.6 |
| Correctness               |          99% |       99% |    99% |
