# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:32 PM PT, Jun 23 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         2/20 | **14/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |            Time |    Commit |
| :----------- | --------------: | --------: |
| torchinferno | **8.0s (0.1m)** | `f0c333d` |
| vllm         |   159.2s (2.7m) | `d4448b5` |
| sglang       |   126.8s (2.1m) | `84a7a84` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        168.6 |   158.0 | **142.0** |
| TPOT median (ms)          |     **54.5** |    57.0 |      75.0 |
| E2E median (ms)           |    **214.1** |   214.5 |     216.7 |
| Throughput median (tok/s) |          5.6 | **6.6** |       5.8 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        229.6 | **182.9** |  282.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        377.1 | **326.0** |  440.9 |
| Throughput median (tok/s) |          2.7 |   **3.1** |    2.3 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        440.6 |     182.4 | **163.9** |
| TPOT median (ms)          |         70.3 |  **69.6** |     119.0 |
| E2E median (ms)           |        512.4 | **242.0** |     302.9 |
| Throughput median (tok/s) |          2.2 |   **5.6** |       4.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        291.0 |  **74.2** |   75.7 |
| TPOT median (ms)          |         56.0 |  **34.9** |   63.9 |
| E2E median (ms)           |        333.0 | **101.8** |  152.0 |
| Throughput median (tok/s) |          4.1 |  **11.5** |    8.9 |
| Correctness               |          96% |       97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        334.4 |      82.2 | **81.1** |
| TPOT median (ms)          |         32.2 |  **18.8** |     26.9 |
| E2E median (ms)           |       1543.2 | **771.6** |    996.9 |
| Throughput median (tok/s) |         23.5 |  **47.2** |     34.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.8 | **135.9** |  149.0 |
| TPOT median (ms)          |         42.6 |  **36.1** |   57.0 |
| E2E median (ms)           |        595.9 | **331.2** |  421.8 |
| Throughput median (tok/s) |          7.6 |  **14.8** |   11.2 |
| Correctness               |          98% |       99% |    99% |
