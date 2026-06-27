# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:03 PM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **3/4** |    0/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **17/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     313.9s (5.2m) | `019ce7b` |
| vllm         |     436.0s (7.3m) | `35e3850` |
| sglang       | **263.4s (4.4m)** | `592f6c8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        253.7 | **143.9** |  147.3 |
| TPOT median (ms)          |     **47.5** |      50.3 |   79.1 |
| E2E median (ms)           |        299.6 | **188.3** |  219.3 |
| Throughput median (tok/s) |          4.4 |   **7.6** |    5.5 |
| Correctness               |          98% |       98% |    98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        273.3 | **199.9** |  219.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        293.2 | **225.7** |  370.3 |
| Throughput median (tok/s) |          3.4 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        492.2 | **161.2** |  169.4 |
| TPOT median (ms)          |         59.7 |  **57.7** |  105.2 |
| E2E median (ms)           |        544.7 | **202.9** |  267.6 |
| Throughput median (tok/s) |          2.4 |   **6.7** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        268.8 | **61.1** |   87.6 |
| TPOT median (ms)          |         42.9 | **31.4** |   44.0 |
| E2E median (ms)           |        309.5 | **85.0** |  138.6 |
| Throughput median (tok/s) |          4.4 | **14.2** |    9.5 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        325.9 |      76.1 | **72.8** |
| TPOT median (ms)          |         21.3 |  **15.0** |     22.5 |
| E2E median (ms)           |       1130.4 | **632.7** |    864.5 |
| Throughput median (tok/s) |         32.3 |  **57.9** |     41.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        322.8 | **128.4** |  139.4 |
| TPOT median (ms)          |         34.3 |  **30.9** |   50.2 |
| E2E median (ms)           |        515.5 | **266.9** |  372.1 |
| Throughput median (tok/s) |          9.4 |  **18.1** |   12.9 |
| Correctness               |          98% |       99% |    99% |
