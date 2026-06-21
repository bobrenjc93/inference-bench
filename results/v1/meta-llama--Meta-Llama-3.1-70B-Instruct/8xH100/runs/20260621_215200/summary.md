# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, Jun 21 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **3/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **16/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     318.6s (5.3m) | `9452794` |
| vllm         |     383.3s (6.4m) | `89bd2c1` |
| sglang       | **247.2s (4.1m)** | `a4d0ff3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        185.9 |     150.0 | **145.2** |
| TPOT median (ms)          |     **45.5** |      52.9 |      76.6 |
| E2E median (ms)           |        229.1 | **199.0** |     214.3 |
| Throughput median (tok/s) |          5.6 |   **7.4** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        286.8 | **186.6** |  218.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        399.3 | **211.7** |  375.3 |
| Throughput median (tok/s) |          2.5 |   **4.7** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        511.3 | **161.1** |  162.9 |
| TPOT median (ms)          |     **38.1** |      50.4 |  103.8 |
| E2E median (ms)           |        558.1 | **206.7** |  256.4 |
| Throughput median (tok/s) |          2.2 |   **6.6** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        190.3 | **60.3** |   85.5 |
| TPOT median (ms)          |         31.9 | **28.5** |   48.0 |
| E2E median (ms)           |        225.9 | **82.6** |  146.1 |
| Throughput median (tok/s) |          5.8 | **14.6** |    9.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        366.7 |  **71.3** |   73.8 |
| TPOT median (ms)          |         22.5 |  **14.9** |   22.3 |
| E2E median (ms)           |       1191.0 | **611.0** |  842.7 |
| Throughput median (tok/s) |         30.0 |  **59.4** |   41.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        308.2 | **125.9** |  137.2 |
| TPOT median (ms)          |     **27.6** |      29.3 |   50.1 |
| E2E median (ms)           |        520.7 | **262.2** |  367.0 |
| Throughput median (tok/s) |          9.2 |  **18.5** |   12.9 |
| Correctness               |          98% |       99% |    98% |
