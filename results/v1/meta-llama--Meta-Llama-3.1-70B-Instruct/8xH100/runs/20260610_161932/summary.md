# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:07 AM PT, Jun 10 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     385.6s (6.4m) | `a870596` |
| vllm         |   1384.9s (23.1m) | `de900fa` |
| sglang       | **207.9s (3.5m)** | `0c7faf0` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        303.1 |     159.7 | **145.5** |
| TPOT median (ms)          |         96.3 |  **57.1** |      76.5 |
| E2E median (ms)           |        385.0 | **214.2** |     215.4 |
| Throughput median (tok/s) |          3.2 |   **6.8** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        419.6 | **174.0** |  217.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        570.9 | **195.9** |  375.6 |
| Throughput median (tok/s) |          1.8 |   **5.1** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        705.6 |     172.5 | **163.1** |
| TPOT median (ms)          |     **66.4** |      68.9 |      98.0 |
| E2E median (ms)           |        778.7 | **233.9** |     260.3 |
| Throughput median (tok/s) |          1.7 |   **5.9** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        359.6 | **58.8** |   81.8 |
| TPOT median (ms)          |         59.1 | **28.4** |   49.3 |
| E2E median (ms)           |        417.9 | **79.6** |  144.7 |
| Throughput median (tok/s) |          3.6 | **15.1** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        187.6 |  **69.8** |   80.3 |
| TPOT median (ms)          |         26.7 |  **14.8** |   23.2 |
| E2E median (ms)           |       1223.3 | **595.2** |  876.9 |
| Throughput median (tok/s) |         30.8 |  **59.3** |   40.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        395.1 | **127.0** |  137.7 |
| TPOT median (ms)          |         49.7 |  **33.8** |   49.4 |
| E2E median (ms)           |        675.1 | **263.7** |  374.6 |
| Throughput median (tok/s) |          8.2 |  **18.5** |   12.7 |
| Correctness               |          98% |       98% |    99% |
