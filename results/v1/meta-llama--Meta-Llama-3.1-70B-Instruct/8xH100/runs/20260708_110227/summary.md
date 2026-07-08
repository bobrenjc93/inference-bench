# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jul 8 2026

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
| torchinferno | **39.0s (0.7m)** | `5aec879` |
| vllm         |    210.4s (3.5m) | `2cae98d` |
| sglang       |    199.9s (3.3m) | `108a183` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        152.9 | **115.0** |  142.7 |
| TPOT median (ms)          |         45.0 |  **41.4** |   79.0 |
| E2E median (ms)           |        193.2 | **149.6** |  222.0 |
| Throughput median (tok/s) |          6.4 |   **9.3** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        165.2 | **130.3** |  205.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        178.4 | **155.6** |  365.1 |
| Throughput median (tok/s) |          5.6 |   **6.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **147.8** |  161.0 |
| TPOT median (ms)          |            - |  **50.5** |  111.0 |
| E2E median (ms)           |            - | **195.5** |  278.1 |
| Throughput median (tok/s) |            - |   **7.0** |    4.7 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.6** |   47.6 |
| TPOT median (ms)          |            - | **21.7** |  363.7 |
| E2E median (ms)           |            - | **48.3** |  427.1 |
| Throughput median (tok/s) |            - | **25.7** |    3.3 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      80.9 | **69.1** |
| TPOT median (ms)          |            - |  **14.8** |     22.4 |
| E2E median (ms)           |            - | **607.5** |    954.7 |
| Throughput median (tok/s) |            - |  **58.2** |     41.5 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        159.1 | **101.3** |  125.1 |
| TPOT median (ms)          |     **22.5** |      25.7 |  115.2 |
| E2E median (ms)           |    **185.8** |     231.3 |  449.4 |
| Throughput median (tok/s) |          6.0 |  **21.3** |   11.5 |
| Correctness               |          99% |       99% |    99% |
