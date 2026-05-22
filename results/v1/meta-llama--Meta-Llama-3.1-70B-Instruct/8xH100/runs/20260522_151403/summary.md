# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:03 AM PT, May 22 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     374.4s (6.2m) | `9f91b40` |
| vllm         |   1314.2s (21.9m) | `f0feb15` |
| sglang       | **185.6s (3.1m)** | `f5ed268` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        301.7 |    160.5 | **138.2** |
| TPOT median (ms)          |        153.3 | **54.3** |      71.0 |
| E2E median (ms)           |        404.9 |    212.0 | **203.9** |
| Throughput median (tok/s) |          3.7 |  **7.0** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        289.3 |     197.8 | **196.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        314.9 | **222.8** |     324.8 |
| Throughput median (tok/s) |          3.2 |   **4.5** |       3.1 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        790.4 |     176.6 | **158.0** |
| TPOT median (ms)          |        106.9 |  **61.9** |     106.8 |
| E2E median (ms)           |        872.9 | **231.7** |     252.4 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        355.9 | **57.6** |   75.8 |
| TPOT median (ms)          |        130.0 | **26.3** |   47.2 |
| E2E median (ms)           |        462.3 | **78.0** |  129.0 |
| Throughput median (tok/s) |          2.8 | **15.7** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        984.4 |      67.6 | **66.7** |
| TPOT median (ms)          |         19.5 |  **15.1** |     22.3 |
| E2E median (ms)           |       1675.0 | **604.2** |    846.4 |
| Throughput median (tok/s) |         21.0 |  **59.6** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        544.4 |     132.0 | **127.0** |
| TPOT median (ms)          |         81.9 |  **31.5** |      49.5 |
| E2E median (ms)           |        746.0 | **269.8** |     351.3 |
| Throughput median (tok/s) |          6.4 |  **18.6** |      13.3 |
| Correctness               |          99% |       99% |       98% |
