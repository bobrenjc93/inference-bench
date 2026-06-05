# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, Jun 5 2026

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
| torchinferno |     349.3s (5.8m) | `89edcfc` |
| vllm         |   1346.7s (22.4m) | `efc347f` |
| sglang       | **198.7s (3.3m)** | `d8487ba` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        331.0 |     163.2 | **146.3** |
| TPOT median (ms)          |     **51.5** |      56.1 |      73.6 |
| E2E median (ms)           |        387.2 | **216.3** |     218.6 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.0 | **176.8** |  214.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        399.2 | **198.1** |  359.5 |
| Throughput median (tok/s) |          2.5 |   **5.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        698.7 |     174.9 | **165.7** |
| TPOT median (ms)          |         70.0 |  **68.7** |     100.2 |
| E2E median (ms)           |        760.2 | **232.7** |     266.6 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        370.4 | **61.5** |   79.7 |
| TPOT median (ms)          |         33.6 | **30.0** |   59.7 |
| E2E median (ms)           |        412.0 | **85.1** |  151.9 |
| Throughput median (tok/s) |          3.5 | **14.5** |    9.4 |
| Correctness               |          97% |      97% |    98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        562.5 |  **73.5** |   78.5 |
| TPOT median (ms)          |         31.0 |  **15.0** |   23.6 |
| E2E median (ms)           |       1671.7 | **617.4** |  908.0 |
| Throughput median (tok/s) |         21.7 |  **58.7** |   39.4 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        450.9 | **130.0** |  137.0 |
| TPOT median (ms)          |         37.2 |  **34.0** |   51.4 |
| E2E median (ms)           |        726.1 | **269.9** |  380.9 |
| Throughput median (tok/s) |          6.5 |  **18.3** |   12.5 |
| Correctness               |          98% |       99% |    99% |
