# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 PM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     326.6s (5.4m) | `7d2331a` |
| vllm         |   1307.1s (21.8m) | `2a983c7` |
| sglang       | **194.5s (3.2m)** | `4c8a022` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        533.8 |     157.4 | **148.6** |
| TPOT median (ms)          |     **54.8** |      57.8 |      72.1 |
| E2E median (ms)           |        596.5 | **211.7** |     219.1 |
| Throughput median (tok/s) |          2.6 |   **7.0** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        275.8 | **184.3** |  194.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        379.1 | **221.4** |  338.8 |
| Throughput median (tok/s) |          2.6 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        779.3 |     170.3 | **167.3** |
| TPOT median (ms)          |     **63.3** |      67.9 |     102.3 |
| E2E median (ms)           |        843.1 | **227.6** |     266.6 |
| Throughput median (tok/s) |          1.6 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.3 | **58.7** |   80.1 |
| TPOT median (ms)          |         32.1 | **28.4** |   42.8 |
| E2E median (ms)           |        408.4 | **80.4** |  136.7 |
| Throughput median (tok/s) |          3.4 | **14.9** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        609.3 |  **68.1** |   77.7 |
| TPOT median (ms)          |         32.3 |  **15.2** |   23.2 |
| E2E median (ms)           |       1655.0 | **614.2** |  862.0 |
| Throughput median (tok/s) |         20.3 |  **58.7** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        515.1 | **127.8** |  133.6 |
| TPOT median (ms)          |         36.5 |  **33.8** |   48.1 |
| E2E median (ms)           |        776.4 | **271.1** |  364.6 |
| Throughput median (tok/s) |          6.1 |  **18.3** |   12.8 |
| Correctness               |          99% |       99% |    99% |
