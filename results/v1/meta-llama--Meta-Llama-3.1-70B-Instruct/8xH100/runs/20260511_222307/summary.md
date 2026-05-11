# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:05 PM PT, May 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/5 |   **4/5** |    1/5 |
| self_consistency |          2/5 |   **3/5** |    0/5 |
| multi_turn       |          0/5 |   **3/5** |    2/5 |
| tree_of_thought  |          0/5 |   **5/5** |    0/5 |
| long_output      |          0/5 |   **4/5** |    1/5 |
| **Total**        |         2/25 | **19/25** |   4/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     321.0s (5.3m) | `661636c` |
| vllm         |    943.8s (15.7m) | `d7af6b3` |
| sglang       | **158.7s (2.6m)** | `ce1736f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        303.4 |     154.9 | **142.9** |
| TPOT median (ms)          |        191.9 |  **51.6** |      72.6 |
| E2E median (ms)           |        446.9 | **202.8** |     209.5 |
| Throughput median (tok/s) |          3.4 |   **6.9** |       5.8 |
| Correctness               |          98% |   **98%** |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        386.4 | **188.4** |  212.0 |
| TPOT median (ms)          |      **0.0** |       0.0 |    0.0 |
| E2E median (ms)           |        479.6 | **208.3** |  357.0 |
| Throughput median (tok/s) |          2.1 |   **4.8** |    2.8 |
| Correctness               |     **100%** |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1079.8 |     171.8 | **158.9** |
| TPOT median (ms)          |        403.8 |  **50.7** |      95.0 |
| E2E median (ms)           |       1544.8 | **222.0** |     255.3 |
| Throughput median (tok/s) |          0.8 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |   **98%** |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        376.0 | **58.9** |   72.4 |
| TPOT median (ms)          |        155.3 | **26.7** |   63.6 |
| E2E median (ms)           |        493.7 | **79.7** |  148.1 |
| Throughput median (tok/s) |          2.7 | **15.4** |    9.7 |
| Correctness               |          97% |  **97%** |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      69.7 | **67.9** |
| TPOT median (ms)          |            - |  **15.1** |     22.1 |
| E2E median (ms)           |            - | **604.2** |    825.4 |
| Throughput median (tok/s) |            - |  **58.6** |     42.8 |
| Correctness               |            - |  **100%** |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        536.4 | **128.7** |  130.8 |
| TPOT median (ms)          |        187.7 |  **28.8** |   50.7 |
| E2E median (ms)           |        741.3 | **263.4** |  359.1 |
| Throughput median (tok/s) |          2.2 |  **18.4** |   13.3 |
| Correctness               |          98% |   **99%** |    99% |
