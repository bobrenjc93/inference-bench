# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, Jun 15 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     397.3s (6.6m) | `ccca738` |
| vllm         |     510.3s (8.5m) | `b997071` |
| sglang       | **238.5s (4.0m)** | `eb349ef` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        336.8 |     164.3 | **154.7** |
| TPOT median (ms)          |     **57.1** |      66.4 |      75.3 |
| E2E median (ms)           |        402.2 | **221.1** |     224.3 |
| Throughput median (tok/s) |          3.5 |   **6.8** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        276.1 | **162.9** |  211.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        396.9 | **186.0** |  360.8 |
| Throughput median (tok/s) |          2.5 |   **5.4** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        765.3 |     174.6 | **162.9** |
| TPOT median (ms)          |     **61.4** |      66.6 |     101.8 |
| E2E median (ms)           |        832.8 | **239.8** |     260.4 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        215.6 | **61.0** |   82.0 |
| TPOT median (ms)          |         33.9 | **28.5** |   42.7 |
| E2E median (ms)           |        251.8 | **84.1** |  136.8 |
| Throughput median (tok/s) |          5.4 | **14.5** |   10.1 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        362.1 |      70.2 | **68.5** |
| TPOT median (ms)          |         22.0 |  **14.8** |     22.1 |
| E2E median (ms)           |       1174.6 | **626.1** |    822.9 |
| Throughput median (tok/s) |         29.7 |  **59.2** |     42.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        391.2 | **126.6** |  135.8 |
| TPOT median (ms)          |     **34.9** |      35.3 |   48.4 |
| E2E median (ms)           |        611.7 | **271.4** |  361.0 |
| Throughput median (tok/s) |          8.6 |  **18.4** |   13.2 |
| Correctness               |          98% |       98% |    99% |
