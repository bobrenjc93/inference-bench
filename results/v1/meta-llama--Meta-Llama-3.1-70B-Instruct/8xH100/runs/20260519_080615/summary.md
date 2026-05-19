# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:02 AM PT, May 19 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          1/4 |   **2/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **14/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     363.8s (6.1m) | `9f91b40` |
| vllm         |   1084.2s (18.1m) | `257af77` |
| sglang       | **169.6s (2.8m)** | `fbfddfd` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        292.7 |    159.8 | **137.6** |
| TPOT median (ms)          |        151.7 | **60.8** |      74.3 |
| E2E median (ms)           |        401.2 |    213.8 | **206.6** |
| Throughput median (tok/s) |          3.4 |  **6.6** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |    **199.5** |     209.7 |  200.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        333.1 | **233.2** |  330.1 |
| Throughput median (tok/s) |          3.0 |   **4.3** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        507.2 |     165.1 | **157.5** |
| TPOT median (ms)          |         98.1 |  **53.3** |     100.5 |
| E2E median (ms)           |        622.3 | **208.6** |     256.3 |
| Throughput median (tok/s) |          2.1 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        313.6 | **58.1** |   77.1 |
| TPOT median (ms)          |        126.3 | **26.6** |   63.9 |
| E2E median (ms)           |        404.2 | **78.4** |  155.2 |
| Throughput median (tok/s) |          4.1 | **15.6** |    9.3 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        743.5 |      72.3 | **66.6** |
| TPOT median (ms)          |         16.3 |  **15.0** |     22.7 |
| E2E median (ms)           |       1441.5 | **609.7** |    855.3 |
| Throughput median (tok/s) |         21.8 |  **59.0** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        411.3 |     133.0 | **127.9** |
| TPOT median (ms)          |         78.5 |  **31.1** |      52.3 |
| E2E median (ms)           |        640.5 | **268.7** |     360.7 |
| Throughput median (tok/s) |          6.9 |  **18.4** |      13.0 |
| Correctness               |          99% |       98% |       99% |
