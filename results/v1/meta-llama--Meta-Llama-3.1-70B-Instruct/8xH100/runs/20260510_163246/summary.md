# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:01 AM PT, May 10 2026

## Scorecard

| Benchmark        |      vllm | sglang | torchinferno |
| :--------------- | --------: | -----: | -----------: |
| few_shot         |   **3/5** |    2/5 |          0/5 |
| self_consistency |   **4/5** |    1/5 |          0/5 |
| multi_turn       |   **3/5** |    2/5 |          0/5 |
| tree_of_thought  |   **4/5** |    1/5 |          0/5 |
| long_output      |   **4/5** |    1/5 |          0/5 |
| **Total**        | **18/25** |   7/25 |         0/25 |

Each cell = metric wins out of 5 (TTFT, TPOT, E2E, throughput, correctness). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| vllm         |  1295.7s (21.6m) | `215e2f7` |
| sglang       |    183.9s (3.1m) | `335dbd6` |
| torchinferno | **44.3s (0.7m)** | `22b9c30` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 10k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     144.9 | **134.4** |            - |
| TPOT median (ms)          |  **52.4** |      76.4 |            - |
| E2E median (ms)           | **191.6** |     207.3 |            - |
| Throughput median (tok/s) |   **7.7** |       5.8 |            - |
| Correctness               |       98% |   **98%** |            - |

### self_consistency
> 10k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     196.2 | **195.9** |            - |
| TPOT median (ms)          |   **0.0** |       0.0 |            - |
| E2E median (ms)           | **271.0** |     346.2 |            - |
| Throughput median (tok/s) |   **3.7** |       2.9 |            - |
| Correctness               |  **100%** |      100% |            - |

### multi_turn
> 1250 concurrent 8-turn conversations (10k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     182.8 | **157.0** |            - |
| TPOT median (ms)          |  **69.8** |     104.8 |            - |
| E2E median (ms)           | **245.3** |     259.0 |            - |
| Throughput median (tok/s) |   **5.8** |       5.1 |            - |
| Correctness               |       98% |   **98%** |            - |

### tree_of_thought
> 323 tree searches (4-wide × 3-deep, ~10k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    |     vllm |  sglang | torchinferno |
| :------------------------ | -------: | ------: | -----------: |
| TTFT median (ms)          | **57.6** |    74.9 |            - |
| TPOT median (ms)          | **26.6** |    60.6 |            - |
| E2E median (ms)           | **78.1** |   141.2 |            - |
| Throughput median (tok/s) | **16.0** |    10.0 |            - |
| Correctness               |      97% | **97%** |            - |

### long_output
> 1 × <huge number> × 10k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    |      vllm |   sglang | torchinferno |
| :------------------------ | --------: | -------: | -----------: |
| TTFT median (ms)          |      68.7 | **64.2** |            - |
| TPOT median (ms)          |  **14.6** |     22.4 |            - |
| E2E median (ms)           | **630.3** |    892.6 |            - |
| Throughput median (tok/s) |  **60.8** |     42.3 |            - |
| Correctness               |  **100%** |     100% |            - |

## Cross-Benchmark Averages

| Metric                    |      vllm |    sglang | torchinferno |
| :------------------------ | --------: | --------: | -----------: |
| TTFT median (ms)          |     130.0 | **125.3** |            - |
| TPOT median (ms)          |  **32.7** |      52.8 |            - |
| E2E median (ms)           | **283.3** |     369.3 |            - |
| Throughput median (tok/s) |  **18.8** |      13.2 |            - |
| Correctness               |       99% |   **99%** |            - |
