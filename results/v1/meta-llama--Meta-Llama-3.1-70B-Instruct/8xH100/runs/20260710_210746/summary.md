# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:07 PM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **14/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **35.8s (0.6m)** | `ea1e71a` |
| vllm         |    224.9s (3.7m) | `26ff616` |
| sglang       |    200.6s (3.3m) | `4fcc994` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        143.0 |      81.2 | **75.7** |
| TPOT median (ms)          |     **31.7** |      37.6 |     65.5 |
| E2E median (ms)           |        168.3 | **111.9** |    128.0 |
| Throughput median (tok/s) |          6.7 |  **12.0** |     10.6 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **25.8** | 66.8 |  121.4 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **26.6** | 84.2 |  194.2 |
| Throughput median (tok/s) |     **37.5** | 11.9 |    5.2 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **76.8** |   77.6 |
| TPOT median (ms)          |            - |  **36.1** |   72.5 |
| E2E median (ms)           |            - | **104.7** |  134.2 |
| Throughput median (tok/s) |            - |  **13.0** |    9.9 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.8** |   48.3 |
| TPOT median (ms)          |            - | **21.8** |  430.4 |
| E2E median (ms)           |            - | **49.5** |  446.4 |
| Throughput median (tok/s) |            - | **25.7** |    3.1 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[Errno 111] Connection refused`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **45.1** |   49.7 |
| TPOT median (ms)          |            - |  **15.0** |   24.4 |
| E2E median (ms)           |            - | **567.4** |  923.0 |
| Throughput median (tok/s) |            - |  **62.2** |   39.5 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[Errno 111] Connection refused`

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         84.4 | **60.5** |   74.5 |
| TPOT median (ms)          |     **15.8** |     22.1 |  118.6 |
| E2E median (ms)           |     **97.5** |    183.5 |  365.1 |
| Throughput median (tok/s) |         22.1 | **25.0** |   13.7 |
| Correctness               |          99% |      99% |    99% |
