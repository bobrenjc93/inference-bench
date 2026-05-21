# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 PM PT, May 21 2026

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
| torchinferno |     374.9s (6.2m) | `9f91b40` |
| vllm         |   1192.3s (19.9m) | `0f66623` |
| sglang       | **221.8s (3.7m)** | `c5251a9` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        318.7 |    156.9 | **139.8** |
| TPOT median (ms)          |        151.2 | **58.6** |      74.7 |
| E2E median (ms)           |        435.2 |    211.6 | **208.7** |
| Throughput median (tok/s) |          3.0 |  **7.1** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.5 | **195.8** |  199.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        312.0 | **223.9** |  338.1 |
| Throughput median (tok/s) |          3.2 |   **4.5** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        628.4 |     169.4 | **151.4** |
| TPOT median (ms)          |        115.2 |  **57.8** |     103.4 |
| E2E median (ms)           |        742.2 | **222.8** |     248.0 |
| Throughput median (tok/s) |          1.7 |   **6.4** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        326.4 | **57.3** |   74.2 |
| TPOT median (ms)          |        128.7 | **26.5** |   59.1 |
| E2E median (ms)           |        424.3 | **77.6** |  145.9 |
| Throughput median (tok/s) |          3.5 | **15.7** |    9.9 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        918.9 |      70.7 | **65.2** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.4 |
| E2E median (ms)           |       1598.5 | **625.4** |    842.3 |
| Throughput median (tok/s) |         21.0 |  **58.8** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        496.2 |     130.0 | **126.0** |
| TPOT median (ms)          |         82.3 |  **31.6** |      51.9 |
| E2E median (ms)           |        702.5 | **272.3** |     356.6 |
| Throughput median (tok/s) |          6.5 |  **18.5** |      13.3 |
| Correctness               |          98% |       99% |       99% |
