# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 AM PT, Jun 20 2026

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
| torchinferno |     401.9s (6.7m) | `35a935e` |
| vllm         |     476.7s (7.9m) | `dced290` |
| sglang       | **296.6s (4.9m)** | `a38eba0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        195.4 | **139.4** |  140.1 |
| TPOT median (ms)          |     **43.7** |      47.3 |   71.5 |
| E2E median (ms)           |        239.4 | **185.3** |  209.6 |
| Throughput median (tok/s) |          5.5 |   **7.8** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        275.7 | **169.5** |  214.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        385.7 | **201.8** |  367.4 |
| Throughput median (tok/s) |          2.6 |   **5.0** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        501.9 | **153.5** |  160.0 |
| TPOT median (ms)          |         57.6 |  **54.8** |  103.1 |
| E2E median (ms)           |        549.1 | **198.5** |  256.8 |
| Throughput median (tok/s) |          2.5 |   **6.9** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        232.6 | **58.6** |   85.8 |
| TPOT median (ms)          |         32.9 | **29.4** |   40.4 |
| E2E median (ms)           |        272.9 | **80.7** |  139.3 |
| Throughput median (tok/s) |          5.4 | **14.8** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        337.3 |      77.2 | **66.4** |
| TPOT median (ms)          |         21.4 |  **14.9** |     22.4 |
| E2E median (ms)           |       1114.1 | **615.3** |    855.3 |
| Throughput median (tok/s) |         32.9 |  **58.7** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        308.6 | **119.7** |  133.4 |
| TPOT median (ms)          |         31.1 |  **29.3** |   47.5 |
| E2E median (ms)           |        512.2 | **256.3** |  365.7 |
| Throughput median (tok/s) |          9.8 |  **18.6** |   13.1 |
| Correctness               |          99% |       99% |    99% |
