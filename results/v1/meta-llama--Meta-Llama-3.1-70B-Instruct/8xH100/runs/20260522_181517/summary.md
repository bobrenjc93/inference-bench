# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:03 AM PT, May 22 2026

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
| torchinferno |     392.6s (6.5m) | `9f91b40` |
| vllm         |   1307.9s (21.8m) | `8437157` |
| sglang       | **214.6s (3.6m)** | `0857772` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        313.2 |    158.5 | **139.0** |
| TPOT median (ms)          |        152.2 | **54.5** |      69.8 |
| E2E median (ms)           |        425.2 |    207.5 | **207.4** |
| Throughput median (tok/s) |          3.4 |  **7.2** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        298.2 |     203.5 | **197.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        328.5 | **230.3** |     333.7 |
| Throughput median (tok/s) |          3.0 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        782.4 |     177.1 | **158.4** |
| TPOT median (ms)          |        185.0 |  **61.3** |     102.1 |
| E2E median (ms)           |        889.8 | **227.7** |     254.8 |
| Throughput median (tok/s) |          1.4 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.5 | **58.2** |   77.8 |
| TPOT median (ms)          |        130.6 | **27.1** |   56.7 |
| E2E median (ms)           |        439.5 | **79.5** |  147.2 |
| Throughput median (tok/s) |          3.0 | **15.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        902.6 |      75.8 | **67.7** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.7 |
| E2E median (ms)           |       1624.5 | **616.0** |    842.4 |
| Throughput median (tok/s) |         20.9 |  **57.8** |     41.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        526.8 |     134.6 | **128.2** |
| TPOT median (ms)          |         96.8 |  **31.6** |      50.3 |
| E2E median (ms)           |        741.5 | **272.2** |     357.1 |
| Throughput median (tok/s) |          6.3 |  **18.2** |      13.0 |
| Correctness               |          99% |       99% |       99% |
