# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 11 2026

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
| torchinferno |     314.7s (5.2m) | `065275c` |
| vllm         |   1358.9s (22.6m) | `39dee11` |
| sglang       | **219.2s (3.7m)** | `ca17bd8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        307.1 |    164.8 | **149.9** |
| TPOT median (ms)          |        100.7 | **55.2** |      72.7 |
| E2E median (ms)           |        392.8 |    223.6 | **219.0** |
| Throughput median (tok/s) |          3.1 |  **6.8** |       5.4 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        315.1 | **189.5** |  205.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        421.6 | **230.5** |  361.3 |
| Throughput median (tok/s) |          2.4 |   **4.3** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        712.7 |     173.0 | **162.2** |
| TPOT median (ms)          |         69.2 |  **56.9** |      98.4 |
| E2E median (ms)           |        750.9 | **221.3** |     262.3 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        373.3 | **61.6** |   83.0 |
| TPOT median (ms)          |         40.8 | **29.5** |   51.3 |
| E2E median (ms)           |        442.7 | **84.3** |  143.6 |
| Throughput median (tok/s) |          3.5 | **14.3** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        199.0 |  **73.9** |   76.0 |
| TPOT median (ms)          |         26.1 |  **15.0** |   23.2 |
| E2E median (ms)           |       1239.1 | **624.6** |  882.9 |
| Throughput median (tok/s) |         31.4 |  **57.9** |   39.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        381.5 | **132.6** |  135.4 |
| TPOT median (ms)          |         47.4 |  **31.3** |   49.1 |
| E2E median (ms)           |        649.4 | **276.9** |  373.9 |
| Throughput median (tok/s) |          8.5 |  **17.9** |   12.6 |
| Correctness               |          99% |       98% |    99% |
