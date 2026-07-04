# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 PM PT, Jul 4 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         4/20 | **13/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **34.5s (0.6m)** | `390fed4` |
| vllm         |    302.2s (5.0m) | `d2afe39` |
| sglang       |    165.0s (2.7m) | `63c4996` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        158.2 | **145.1** |  146.7 |
| TPOT median (ms)          |     **46.8** |      47.8 |   75.8 |
| E2E median (ms)           |        201.8 | **188.3** |  221.9 |
| Throughput median (tok/s) |          5.8 |   **7.4** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **172.8** | 216.6 |  225.7 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **184.7** | 240.5 |  387.1 |
| Throughput median (tok/s) |      **5.4** |   4.2 |    2.6 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        364.9 |     174.8 | **161.1** |
| TPOT median (ms)          |         61.9 |  **46.4** |     113.1 |
| E2E median (ms)           |        418.2 | **222.4** |     269.0 |
| Throughput median (tok/s) |          3.3 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        134.3 | **62.9** |   74.1 |
| TPOT median (ms)          |         40.4 | **30.5** |   57.2 |
| E2E median (ms)           |        164.2 | **85.8** |  142.8 |
| Throughput median (tok/s) |          8.2 | **14.2** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        243.1 |      79.2 | **76.6** |
| TPOT median (ms)          |         21.5 |  **14.8** |     22.0 |
| E2E median (ms)           |        995.4 | **625.5** |    831.1 |
| Throughput median (tok/s) |         35.4 |  **58.0** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        214.6 | **135.7** |  136.8 |
| TPOT median (ms)          |         34.1 |  **27.9** |   53.6 |
| E2E median (ms)           |        392.9 | **272.5** |  370.4 |
| Throughput median (tok/s) |         11.6 |  **18.0** |   13.0 |
| Correctness               |          98% |       99% |    99% |
