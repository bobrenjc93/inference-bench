# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, Jun 29 2026

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
| torchinferno |    776.5s (12.9m) | `6854049` |
| vllm         |     582.9s (9.7m) | `5b4cb69` |
| sglang       | **365.0s (6.1m)** | `3add35e` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        163.4 | **146.3** |  149.8 |
| TPOT median (ms)          |     **46.0** |      52.8 |   68.3 |
| E2E median (ms)           |        203.1 | **196.0** |  219.6 |
| Throughput median (tok/s) |          5.8 |   **7.4** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        255.0 | **192.1** |  219.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        276.2 | **218.3** |  358.2 |
| Throughput median (tok/s) |          3.6 |   **4.6** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        296.6 | **168.1** |  173.6 |
| TPOT median (ms)          |         57.4 |  **52.4** |   98.1 |
| E2E median (ms)           |        352.1 | **213.7** |  267.8 |
| Throughput median (tok/s) |          4.0 |   **6.4** |    4.9 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        219.4 | **63.9** |   88.1 |
| TPOT median (ms)          |         57.0 | **31.7** |   46.4 |
| E2E median (ms)           |        259.6 | **86.9** |  139.6 |
| Throughput median (tok/s) |          5.7 | **13.8** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        308.3 |      80.7 | **72.5** |
| TPOT median (ms)          |         22.9 |  **15.0** |     22.6 |
| E2E median (ms)           |       1115.2 | **618.6** |    841.4 |
| Throughput median (tok/s) |         32.3 |  **58.0** |     41.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        248.5 | **130.2** |  140.7 |
| TPOT median (ms)          |         36.7 |  **30.4** |   47.1 |
| E2E median (ms)           |        441.3 | **266.7** |  365.3 |
| Throughput median (tok/s) |         10.3 |  **18.0** |   12.7 |
| Correctness               |          99% |       99% |    99% |
