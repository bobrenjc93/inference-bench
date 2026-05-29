# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, May 28 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          1/4 |   **3/4** |    0/4 |
| long_output      |          1/4 |   **2/4** |    1/4 |
| **Total**        |         3/20 | **11/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     410.3s (6.8m) | `3cbe719` |
| vllm         |   1344.2s (22.4m) | `22a5864` |
| sglang       | **212.9s (3.5m)** | `73c99e3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        300.9 |    168.6 | **153.6** |
| TPOT median (ms)          |         68.8 | **64.6** |      77.2 |
| E2E median (ms)           |        381.5 |    231.6 | **224.1** |
| Throughput median (tok/s) |          3.6 |  **6.3** |       5.3 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        284.6 |     203.1 | **197.7** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        317.9 | **238.2** |     341.1 |
| Throughput median (tok/s) |          3.1 |   **4.2** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        727.7 |     170.5 | **164.1** |
| TPOT median (ms)          |     **57.7** |      63.1 |     110.3 |
| E2E median (ms)           |        782.4 | **224.4** |     278.7 |
| Throughput median (tok/s) |          1.8 |   **6.2** |       4.8 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        192.7 | **60.0** |   79.4 |
| TPOT median (ms)          |     **27.9** |     28.0 |   45.1 |
| E2E median (ms)           |        216.0 | **82.2** |  132.8 |
| Throughput median (tok/s) |          6.1 | **15.2** |   10.1 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        551.8 |      74.4 | **74.3** |
| TPOT median (ms)          |     **14.4** |      14.9 |     23.4 |
| E2E median (ms)           |       1296.8 | **626.2** |    859.8 |
| Throughput median (tok/s) |         28.5 |  **58.3** |     40.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        411.5 |     135.3 | **133.8** |
| TPOT median (ms)          |     **33.8** |      34.1 |      51.2 |
| E2E median (ms)           |        598.9 | **280.5** |     367.3 |
| Throughput median (tok/s) |          8.6 |  **18.0** |      12.6 |
| Correctness               |          98% |       99% |       98% |
