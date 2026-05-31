# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:01 PM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     274.8s (4.6m) | `ce1612d` |
| vllm         |   1225.4s (20.4m) | `6bdabba` |
| sglang       | **192.8s (3.2m)** | `c062201` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        216.8 |     163.3 | **147.3** |
| TPOT median (ms)          |     **43.8** |      53.3 |      74.5 |
| E2E median (ms)           |        259.7 | **214.1** |     216.7 |
| Throughput median (tok/s) |          5.5 |   **7.0** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        357.5 | **203.0** |  204.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        449.8 | **231.2** |  335.0 |
| Throughput median (tok/s) |          2.2 |   **4.3** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        909.8 |     179.3 | **167.3** |
| TPOT median (ms)          |        134.8 |  **65.8** |     103.0 |
| E2E median (ms)           |       1234.1 | **232.5** |     263.5 |
| Throughput median (tok/s) |          1.1 |   **6.0** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        415.5 | **60.5** |   81.4 |
| TPOT median (ms)          |         27.6 | **27.0** |   48.4 |
| E2E median (ms)           |        440.3 | **81.4** |  139.6 |
| Throughput median (tok/s) |          3.5 | **15.3** |    9.3 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        320.3 |  **78.7** |   81.9 |
| TPOT median (ms)          |         23.3 |  **14.9** |   23.1 |
| E2E median (ms)           |       1329.0 | **632.5** |  881.2 |
| Throughput median (tok/s) |         27.0 |  **57.3** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        444.0 |     137.0 | **136.5** |
| TPOT median (ms)          |         45.9 |  **32.2** |      49.8 |
| E2E median (ms)           |        742.6 | **278.3** |     367.2 |
| Throughput median (tok/s) |          7.9 |  **18.0** |      12.5 |
| Correctness               |          98% |       98% |       99% |
