# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 AM PT, Jul 8 2026

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
| torchinferno | **47.2s (0.8m)** | `b243727` |
| vllm         |    174.8s (2.9m) | `68b4a1d` |
| sglang       |    224.7s (3.7m) | `b8ca06f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        149.8 | **123.7** |  143.6 |
| TPOT median (ms)          |         44.5 |  **41.5** |   80.6 |
| E2E median (ms)           |        187.9 | **156.4** |  222.6 |
| Throughput median (tok/s) |          6.4 |   **9.0** |    5.3 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        167.2 | **130.8** |  213.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        179.0 | **157.1** |  342.0 |
| Throughput median (tok/s) |          5.6 |   **6.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |            - | **154.1** |  170.2 |
| TPOT median (ms)          |            - |  **51.0** |  109.2 |
| E2E median (ms)           |            - | **202.2** |  285.2 |
| Throughput median (tok/s) |            - |   **6.8** |    4.6 |
| Correctness               |            - |       98% |    98% |

> **torchinferno error:** `timed out`

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |            - | **32.5** |   50.8 |
| TPOT median (ms)          |            - | **21.7** |  382.4 |
| E2E median (ms)           |            - | **48.2** |  452.6 |
| Throughput median (tok/s) |            - | **25.8** |    3.2 |
| Correctness               |            - |      97% |    97% |

> **torchinferno error:** `timed out`

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      75.4 | **71.1** |
| TPOT median (ms)          |            - |  **14.8** |     22.1 |
| E2E median (ms)           |            - | **663.7** |    904.3 |
| Throughput median (tok/s) |            - |  **58.5** |     41.6 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        158.5 | **103.3** |  129.8 |
| TPOT median (ms)          |     **22.3** |      25.8 |  118.9 |
| E2E median (ms)           |    **183.4** |     245.5 |  441.3 |
| Throughput median (tok/s) |          6.0 |  **21.3** |   11.5 |
| Correctness               |          99% |       99% |    99% |
