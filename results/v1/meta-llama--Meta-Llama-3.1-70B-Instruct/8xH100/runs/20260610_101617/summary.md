# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 AM PT, Jun 10 2026

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
| torchinferno |     411.2s (6.9m) | `a870596` |
| vllm         |   1328.9s (22.1m) | `8a5cf1c` |
| sglang       | **215.8s (3.6m)** | `b0d888a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        300.2 |     161.7 | **147.9** |
| TPOT median (ms)          |         88.5 |  **56.9** |      77.3 |
| E2E median (ms)           |        377.1 | **217.8** |     218.3 |
| Throughput median (tok/s) |          3.3 |   **6.8** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        384.6 | **205.7** |  219.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        531.6 | **229.2** |  363.7 |
| Throughput median (tok/s) |          1.9 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        726.6 |     178.9 | **162.4** |
| TPOT median (ms)          |     **69.3** |      69.6 |      99.8 |
| E2E median (ms)           |        800.0 | **236.2** |     260.2 |
| Throughput median (tok/s) |          1.7 |   **6.0** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        416.8 | **64.4** |   80.8 |
| TPOT median (ms)          |         62.8 | **29.7** |   57.9 |
| E2E median (ms)           |        453.7 | **87.4** |  149.2 |
| Throughput median (tok/s) |          3.5 | **14.3** |    9.5 |
| Correctness               |          97% |      97% |    98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.2 |  **73.9** |   79.5 |
| TPOT median (ms)          |         26.4 |  **15.1** |   23.8 |
| E2E median (ms)           |       1206.2 | **632.2** |  884.9 |
| Throughput median (tok/s) |         30.2 |  **58.4** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        404.3 | **136.9** |  138.0 |
| TPOT median (ms)          |         49.4 |  **34.3** |   51.7 |
| E2E median (ms)           |        673.7 | **280.6** |  375.3 |
| Throughput median (tok/s) |          8.1 |  **18.0** |   12.4 |
| Correctness               |          99% |       99% |    99% |
