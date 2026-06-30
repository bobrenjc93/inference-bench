# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 30 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     593.1s (9.9m) | `7cbb5fe` |
| vllm         |     587.1s (9.8m) | `364ee36` |
| sglang       | **346.8s (5.8m)** | `2f730e2` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        164.8 | **146.8** |  153.0 |
| TPOT median (ms)          |     **48.3** |      55.4 |   66.3 |
| E2E median (ms)           |        208.5 | **200.7** |  220.0 |
| Throughput median (tok/s) |          5.5 |   **7.1** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.9 | **190.2** |  214.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        287.8 | **256.2** |  359.5 |
| Throughput median (tok/s) |          3.5 |   **3.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        302.9 | **164.1** |  167.9 |
| TPOT median (ms)          |         55.8 |  **55.5** |  100.5 |
| E2E median (ms)           |        358.3 | **214.8** |  262.1 |
| Throughput median (tok/s) |          4.0 |   **6.5** |    5.0 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        193.6 | **61.7** |   87.4 |
| TPOT median (ms)          |         57.6 | **32.0** |   39.3 |
| E2E median (ms)           |        238.5 | **86.6** |  135.5 |
| Throughput median (tok/s) |          5.9 | **14.1** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        319.9 |      72.5 | **72.2** |
| TPOT median (ms)          |         24.2 |  **14.9** |     21.8 |
| E2E median (ms)           |       1195.4 | **614.5** |    830.4 |
| Throughput median (tok/s) |         31.9 |  **59.7** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        250.0 | **127.1** |  139.0 |
| TPOT median (ms)          |         37.2 |  **31.6** |   45.6 |
| E2E median (ms)           |        457.7 | **274.6** |  361.5 |
| Throughput median (tok/s) |         10.2 |  **18.3** |   13.1 |
| Correctness               |          99% |       99% |    99% |
