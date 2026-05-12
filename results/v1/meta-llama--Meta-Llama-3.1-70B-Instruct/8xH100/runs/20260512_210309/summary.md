# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 1:07 PM PT, May 12 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     284.0s (4.7m) | `708195d` |
| vllm         |    974.1s (16.2m) | `0ce6613` |
| sglang       | **169.9s (2.8m)** | `486b547` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        360.5 |    163.0 | **140.8** |
| TPOT median (ms)          |        462.7 | **55.7** |      71.6 |
| E2E median (ms)           |        764.2 |    209.5 | **208.4** |
| Throughput median (tok/s) |          1.7 |  **6.8** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        349.5 | **204.8** |  209.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        391.8 | **271.6** |  350.1 |
| Throughput median (tok/s) |          2.6 |   **3.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        624.5 |     170.1 | **154.8** |
| TPOT median (ms)          |        196.8 |  **51.0** |     104.2 |
| E2E median (ms)           |        793.0 | **214.5** |     253.8 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        376.3 | **57.6** |   74.9 |
| TPOT median (ms)          |        421.9 | **27.2** |   64.4 |
| E2E median (ms)           |        745.1 | **77.8** |  148.5 |
| Throughput median (tok/s) |          2.0 | **15.7** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        546.3 |      66.4 | **64.0** |
| TPOT median (ms)          |         30.6 |  **15.0** |     22.3 |
| E2E median (ms)           |       1809.6 | **596.7** |    831.0 |
| Throughput median (tok/s) |         22.0 |  **59.8** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        451.4 |     132.4 | **128.8** |
| TPOT median (ms)          |        222.4 |  **29.8** |      52.5 |
| E2E median (ms)           |        900.7 | **274.0** |     358.4 |
| Throughput median (tok/s) |          6.0 |  **18.4** |      13.2 |
| Correctness               |          98% |       99% |       99% |
