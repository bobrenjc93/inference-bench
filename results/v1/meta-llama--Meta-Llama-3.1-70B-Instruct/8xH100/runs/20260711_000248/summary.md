# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:02 PM PT, Jul 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         4/20 | **15/20** |   0/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **36.6s (0.6m)** | `b3dab3b` |
| vllm         |    246.9s (4.1m) | `ed908cf` |
| sglang       |    207.9s (3.5m) | `7de33ce` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        141.2 |  **77.0** |   77.5 |
| TPOT median (ms)          |     **31.3** |      37.0 |   66.1 |
| E2E median (ms)           |        165.4 | **105.3** |  129.2 |
| Throughput median (tok/s) |          6.9 |  **12.5** |   10.4 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **24.1** | 75.6 |  120.8 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **24.6** | 92.6 |  197.0 |
| Throughput median (tok/s) |     **40.6** | 10.8 |    5.1 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **75.9** |   77.8 |
| TPOT median (ms)          |            - |  **34.2** |   74.6 |
| E2E median (ms)           |            - | **103.1** |  134.1 |
| Throughput median (tok/s) |            - |  **12.8** |    9.8 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **33.4** |   48.9 |
| TPOT median (ms)          |            - | **22.1** |  364.5 |
| E2E median (ms)           |            - | **50.5** |  456.2 |
| Throughput median (tok/s) |            - | **25.8** |    3.2 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[Errno 111] Connection refused`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **45.8** |   48.2 |
| TPOT median (ms)          |            - |  **15.0** |   24.5 |
| E2E median (ms)           |            - | **567.4** |  901.1 |
| Throughput median (tok/s) |            - |  **62.2** |   39.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[Errno 111] Connection refused`

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         82.6 | **61.5** |   74.6 |
| TPOT median (ms)          |     **15.6** |     21.7 |  105.9 |
| E2E median (ms)           |     **95.0** |    183.8 |  363.5 |
| Throughput median (tok/s) |         23.7 | **24.8** |   13.6 |
| Correctness               |          99% |      99% |    98% |
