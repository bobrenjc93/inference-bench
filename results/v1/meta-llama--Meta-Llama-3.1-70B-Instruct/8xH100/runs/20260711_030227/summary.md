# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, Jul 10 2026

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
| torchinferno | **42.2s (0.7m)** | `54cb558` |
| vllm         |    199.8s (3.3m) | `04d553f` |
| sglang       |    204.7s (3.4m) | `9068836` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        141.5 |      80.6 | **80.0** |
| TPOT median (ms)          |     **32.6** |      36.5 |     65.6 |
| E2E median (ms)           |        165.8 | **113.2** |    135.4 |
| Throughput median (tok/s) |          6.9 |  **12.4** |      9.7 |
| Correctness               |          98% |       98% |      98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno | vllm | sglang |
| :------------------------ | -----------: | ---: | -----: |
| TTFT median (ms)          |     **23.9** | 71.9 |  122.1 |
| TPOT median (ms)          |          0.0 |  0.0 |    0.0 |
| E2E median (ms)           |     **24.5** | 89.4 |  210.8 |
| Throughput median (tok/s) |     **40.9** | 11.2 |    4.7 |
| Correctness               |         100% | 100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **71.2** |   83.1 |
| TPOT median (ms)          |            - | **34.2** |   77.5 |
| E2E median (ms)           |            - | **94.6** |  142.9 |
| Throughput median (tok/s) |            - | **14.3** |    9.4 |
| Correctness               |            - |      98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **34.0** |   51.9 |
| TPOT median (ms)          |            - | **22.4** |  342.7 |
| E2E median (ms)           |            - | **51.4** |  401.4 |
| Throughput median (tok/s) |            - | **25.4** |    3.4 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `[Errno 111] Connection refused`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - |  **44.6** |   51.4 |
| TPOT median (ms)          |            - |  **15.0** |   24.4 |
| E2E median (ms)           |            - | **563.0** |  918.7 |
| Throughput median (tok/s) |            - |  **62.5** |   39.6 |
| Correctness               |            - |      100% |   100% |

> **torchinferno error:** `[Errno 111] Connection refused`

## Cross-Benchmark Averages

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |         82.7 | **60.5** |   77.7 |
| TPOT median (ms)          |     **16.3** |     21.6 |  102.0 |
| E2E median (ms)           |     **95.1** |    182.3 |  361.8 |
| Throughput median (tok/s) |         23.9 | **25.1** |   13.4 |
| Correctness               |          99% |      98% |    99% |
