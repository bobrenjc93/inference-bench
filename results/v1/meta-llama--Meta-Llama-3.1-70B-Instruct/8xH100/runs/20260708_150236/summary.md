# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 AM PT, Jul 8 2026

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
| torchinferno | **42.8s (0.7m)** | `a647250` |
| vllm         |    200.2s (3.3m) | `f05603f` |
| sglang       |    184.4s (3.1m) | `04e4fad` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        147.8 | **118.7** |  134.3 |
| TPOT median (ms)          |     **42.5** |      42.8 |   77.7 |
| E2E median (ms)           |        186.1 | **152.8** |  210.2 |
| Throughput median (tok/s) |          6.5 |   **9.2** |    5.8 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        173.4 | **123.4** |  221.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        183.9 | **144.9** |  371.1 |
| Throughput median (tok/s) |          5.4 |   **6.9** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **143.1** |  165.4 |
| TPOT median (ms)          |            - |  **45.5** |  122.3 |
| E2E median (ms)           |            - | **187.1** |  283.4 |
| Throughput median (tok/s) |            - |   **7.3** |    4.5 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.5** |   47.8 |
| TPOT median (ms)          |            - | **21.7** |  394.0 |
| E2E median (ms)           |            - | **48.3** |  406.4 |
| Throughput median (tok/s) |            - | **25.6** |    3.6 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      77.0 | **73.5** |
| TPOT median (ms)          |            - |  **14.8** |     22.3 |
| E2E median (ms)           |            - | **604.2** |    953.6 |
| Throughput median (tok/s) |            - |  **58.3** |     41.2 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        160.6 | **98.9** |  128.5 |
| TPOT median (ms)          |     **21.2** |     24.9 |  123.3 |
| E2E median (ms)           |    **185.0** |    227.5 |  444.9 |
| Throughput median (tok/s) |          6.0 | **21.4** |   11.5 |
| Correctness               |          99% |      99% |    98% |
