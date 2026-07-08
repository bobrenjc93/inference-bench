# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:08 PM PT, Jul 8 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **45.4s (0.8m)** | `c65061f` |
| vllm         |    176.8s (2.9m) | `a5d19cb` |
| sglang       |    197.0s (3.3m) | `45019b5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        159.2 | **132.8** |  137.4 |
| TPOT median (ms)          |     **45.0** |      45.7 |   76.8 |
| E2E median (ms)           |        202.9 | **169.7** |  214.9 |
| Throughput median (tok/s) |          6.3 |   **8.1** |    5.7 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        173.9 | **135.9** |  215.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        183.4 | **160.8** |  365.9 |
| Throughput median (tok/s) |          5.5 |   **6.2** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **158.1** |  165.4 |
| TPOT median (ms)          |            - |  **46.8** |  111.6 |
| E2E median (ms)           |            - | **203.4** |  281.4 |
| Throughput median (tok/s) |            - |   **6.9** |    4.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **34.0** |   49.8 |
| TPOT median (ms)          |            - | **22.3** |  385.8 |
| E2E median (ms)           |            - | **50.3** |  433.8 |
| Throughput median (tok/s) |            - | **25.1** |    3.3 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      91.9 | **68.8** |
| TPOT median (ms)          |            - |  **14.9** |     22.4 |
| E2E median (ms)           |            - | **619.1** |    882.7 |
| Throughput median (tok/s) |            - |  **56.9** |     41.1 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        166.6 | **110.5** |  127.4 |
| TPOT median (ms)          |     **22.5** |      25.9 |  119.3 |
| E2E median (ms)           |    **193.2** |     240.7 |  435.7 |
| Throughput median (tok/s) |          5.9 |  **20.7** |   11.5 |
| Correctness               |          99% |       98% |    99% |
