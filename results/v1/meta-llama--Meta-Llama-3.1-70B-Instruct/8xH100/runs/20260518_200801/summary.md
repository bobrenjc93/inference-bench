# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:09 PM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **15/20** |   4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     263.4s (4.4m) | `c837893` |
| vllm         |   1079.1s (18.0m) | `8fc1c28` |
| sglang       | **167.0s (2.8m)** | `1f185c6` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        249.9 |    159.1 | **141.3** |
| TPOT median (ms)          |        148.3 | **56.0** |      72.3 |
| E2E median (ms)           |        355.9 |    215.4 | **208.2** |
| Throughput median (tok/s) |          4.2 |  **6.6** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        268.8 | **168.7** |  202.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        297.3 | **190.6** |  338.2 |
| Throughput median (tok/s) |          3.4 |   **5.2** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        530.6 |     175.9 | **160.2** |
| TPOT median (ms)          |        111.7 |  **59.4** |      99.8 |
| E2E median (ms)           |        611.2 | **227.0** |     260.8 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        338.7 | **58.3** |   72.6 |
| TPOT median (ms)          |        130.1 | **26.7** |   57.3 |
| E2E median (ms)           |        436.4 | **79.4** |  138.3 |
| Throughput median (tok/s) |          2.8 | **15.4** |   10.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        732.9 |      71.0 | **64.7** |
| TPOT median (ms)          |         16.5 |  **15.0** |     22.4 |
| E2E median (ms)           |       1290.0 | **609.7** |    834.6 |
| Throughput median (tok/s) |         26.5 |  **58.9** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        424.2 | **126.6** |  128.3 |
| TPOT median (ms)          |         81.3 |  **31.4** |   50.4 |
| E2E median (ms)           |        598.2 | **264.4** |  356.0 |
| Throughput median (tok/s) |          7.8 |  **18.5** |   13.3 |
| Correctness               |          99% |       99% |    99% |
