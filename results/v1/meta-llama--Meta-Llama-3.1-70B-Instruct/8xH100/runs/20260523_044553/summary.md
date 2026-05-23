# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:03 PM PT, May 22 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     359.1s (6.0m) | `9f91b40` |
| vllm         |   1143.1s (19.1m) | `367cb81` |
| sglang       | **170.3s (2.8m)** | `c69844f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        300.5 |     156.5 | **141.4** |
| TPOT median (ms)          |        149.5 |  **54.4** |      70.3 |
| E2E median (ms)           |        410.4 | **203.7** |     210.6 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        254.4 | **191.9** |  197.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        322.0 | **213.0** |  337.0 |
| Throughput median (tok/s) |          3.1 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        770.1 |     165.4 | **159.3** |
| TPOT median (ms)          |        107.8 |  **56.8** |     106.6 |
| E2E median (ms)           |        854.6 | **213.3** |     267.3 |
| Throughput median (tok/s) |          1.5 |   **6.3** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        313.5 | **58.5** |   77.1 |
| TPOT median (ms)          |        131.2 | **26.8** |   62.2 |
| E2E median (ms)           |        416.1 | **78.9** |  149.7 |
| Throughput median (tok/s) |          3.3 | **15.3** |    9.5 |
| Correctness               |          97% |      97% |    98% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |            - |      71.6 | **69.0** |
| TPOT median (ms)          |            - |  **15.0** |     22.3 |
| E2E median (ms)           |            - | **621.1** |    834.5 |
| Throughput median (tok/s) |            - |  **58.5** |     42.4 |
| Correctness               |            - |      100% |     100% |

> **torchinferno error:** `timed out`

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        409.6 | **128.8** |  129.0 |
| TPOT median (ms)          |         97.1 |  **30.6** |   52.3 |
| E2E median (ms)           |        500.8 | **266.0** |  359.8 |
| Throughput median (tok/s) |          2.8 |  **18.4** |   13.1 |
| Correctness               |          98% |       99% |    99% |
