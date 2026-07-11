# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **14/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **35.4s (0.6m)** | `d78c1ae` |
| vllm         |    200.4s (3.3m) | `29fd688` |
| sglang       |    199.4s (3.3m) | `fc2ef35` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        140.1 | **73.6** |   76.7 |
| TPOT median (ms)          |     **32.2** |     36.0 |   65.7 |
| E2E median (ms)           |        166.1 | **98.8** |  133.4 |
| Throughput median (tok/s) |          6.9 | **13.9** |   10.3 |
| Correctness               |          98% |      98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.8** | 82.0 |  124.6 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **25.8** | 99.6 |  205.0 |
| Throughput median (tok/s) |     **38.7** | 10.0 |    4.9 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      88.4 | **81.0** |
| TPOT median (ms)          |            - |  **33.2** |     73.7 |
| E2E median (ms)           |            - | **112.5** |    141.6 |
| Throughput median (tok/s) |            - |  **12.1** |      9.5 |
| Correctness               |            - |       98% |      98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.9** |   47.7 |
| TPOT median (ms)          |            - | **21.7** |  372.8 |
| E2E median (ms)           |            - | **49.2** |  412.1 |
| Throughput median (tok/s) |            - | **25.8** |    3.5 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[Errno 111] Connection refused`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **46.4** |   49.1 |
| TPOT median (ms)          |            - |  **15.1** |   24.0 |
| E2E median (ms)           |            - | **569.5** |  888.6 |
| Throughput median (tok/s) |            - |  **61.8** |   40.4 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[Errno 111] Connection refused`

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         82.4 | **64.7** |   75.8 |
| TPOT median (ms)          |     **16.1** |     21.2 |  107.2 |
| E2E median (ms)           |     **96.0** |    185.9 |  356.1 |
| Throughput median (tok/s) |         22.8 | **24.7** |   13.7 |
| Correctness               |          99% |      99% |    99% |
