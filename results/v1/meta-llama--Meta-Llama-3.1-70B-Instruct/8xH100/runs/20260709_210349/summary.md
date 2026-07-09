# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, Jul 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **4/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **38.6s (0.6m)** | `75387c9` |
| vllm         |    214.7s (3.6m) | `e12b91b` |
| sglang       |    239.7s (4.0m) | `40a5222` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        144.2 | **118.7** |  139.1 |
| TPOT median (ms)          |         43.0 |  **42.9** |   79.2 |
| E2E median (ms)           |        183.8 | **146.0** |  215.5 |
| Throughput median (tok/s) |          6.6 |   **9.2** |    5.6 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        160.9 | **129.0** |  222.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        171.5 | **156.6** |  375.3 |
| Throughput median (tok/s) |          5.8 |   **6.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **152.5** |  168.0 |
| TPOT median (ms)          |            - |  **49.3** |  114.1 |
| E2E median (ms)           |            - | **199.0** |  286.4 |
| Throughput median (tok/s) |            - |   **7.0** |    4.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **33.5** |   50.3 |
| TPOT median (ms)          |            - | **22.6** |  370.1 |
| E2E median (ms)           |            - | **50.4** |  466.9 |
| Throughput median (tok/s) |            - | **25.0** |    3.0 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      74.5 | **70.2** |
| TPOT median (ms)          |            - |  **14.8** |     22.4 |
| E2E median (ms)           |            - | **600.9** |    881.2 |
| Throughput median (tok/s) |            - |  **59.8** |     41.8 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        152.6 | **101.6** |  130.1 |
| TPOT median (ms)          |     **21.5** |      25.9 |  117.2 |
| E2E median (ms)           |    **177.6** |     230.6 |  445.1 |
| Throughput median (tok/s) |          6.2 |  **21.5** |   11.5 |
| Correctness               |          99% |       98% |    99% |
