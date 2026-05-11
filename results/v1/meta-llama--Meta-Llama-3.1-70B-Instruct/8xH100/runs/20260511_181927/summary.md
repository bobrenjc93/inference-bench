# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:01 AM PT, May 11 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **5/5** |    0/5 |          0/5 |
| multi_turn       |   **4/5** |    1/5 |          0/5 |
| tree_of_thought  |   **5/5** |    0/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **21/25** |   4/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1325.0s (22.1m) | `7863fff` |
| sglang       |    180.2s (3.0m) | `4b6f776` |
| torchinferno | **42.8s (0.7m)** | `aff7755` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |     vllm |    sglang | torchinferno |
| :------------------------ | -------: | --------: | -----------: |
| TTFT median (ms)          |    158.6 | **134.8** |        297.9 |
| TPOT median (ms)          | **56.0** |      77.9 |        167.0 |
| E2E median (ms)           |    215.1 | **206.5** |        509.1 |
| Throughput median (tok/s) |  **7.1** |       5.9 |          2.7 |
| Correctness               |  **98%** |       98% |          98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm | sglang | torchinferno |
| :------------------------ | --------: | -----: | -----------: |
| TTFT median (ms)          | **178.5** |  207.6 |        348.7 |
| TPOT median (ms)          |   **0.0** |    0.0 |          0.0 |
| E2E median (ms)           | **221.1** |  354.5 |        448.0 |
| Throughput median (tok/s) |   **4.5** |    2.8 |          2.2 |
| Correctness               |  **100%** |   100% |         100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     180.5 | **155.7** |            - |
| TPOT median (ms)          |  **60.0** |     107.3 |            - |
| E2E median (ms)           | **236.3** |     256.5 |            - |
| Throughput median (tok/s) |   **6.0** |       5.1 |            - |
| Correctness               |   **98%** |       98% |            - |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm | sglang | torchinferno |
| :------------------------ | -------: | -----: | -----------: |
| TTFT median (ms)          | **57.5** |   77.2 |            - |
| TPOT median (ms)          | **26.9** |   71.0 |            - |
| E2E median (ms)           | **77.8** |  162.0 |            - |
| Throughput median (tok/s) | **15.7** |    8.9 |            - |
| Correctness               |  **97%** |    97% |            - |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      72.2 | **68.2** |            - |
| TPOT median (ms)          |  **15.0** |     22.6 |            - |
| E2E median (ms)           | **611.8** |    860.0 |            - |
| Throughput median (tok/s) |  **58.6** |     41.7 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     129.5 | **128.7** |        323.3 |
| TPOT median (ms)          |  **31.6** |      55.8 |         83.5 |
| E2E median (ms)           | **272.4** |     367.9 |        478.5 |
| Throughput median (tok/s) |  **18.4** |      12.9 |          2.4 |
| Correctness               |       99% |       99% |      **99%** |
