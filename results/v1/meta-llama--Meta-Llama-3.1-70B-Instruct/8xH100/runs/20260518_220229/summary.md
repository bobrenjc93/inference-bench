# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:02 PM PT, May 18 2026

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
| torchinferno |     233.0s (3.9m) | `c837893` |
| vllm         |   1051.4s (17.5m) | `0191354` |
| sglang       | **171.6s (2.9m)** | `6f89204` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        275.1 |    157.4 | **135.1** |
| TPOT median (ms)          |        152.3 | **55.1** |      79.5 |
| E2E median (ms)           |        374.0 |    216.1 | **205.3** |
| Throughput median (tok/s) |          4.1 |  **6.8** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        269.9 | **193.1** |  209.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        300.3 | **249.2** |  357.7 |
| Throughput median (tok/s) |          3.3 |   **4.0** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        521.3 |     165.1 | **158.7** |
| TPOT median (ms)          |        100.4 |  **60.1** |     102.3 |
| E2E median (ms)           |        630.4 | **216.8** |     263.0 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        332.2 | **58.0** |   75.5 |
| TPOT median (ms)          |        130.8 | **26.7** |   46.9 |
| E2E median (ms)           |        425.3 | **78.0** |  127.1 |
| Throughput median (tok/s) |          3.7 | **15.8** |   10.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        720.8 |      71.9 | **68.9** |
| TPOT median (ms)          |         16.3 |  **14.9** |     22.4 |
| E2E median (ms)           |       1458.5 | **611.6** |    823.7 |
| Throughput median (tok/s) |         28.3 |  **58.6** |     42.1 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        423.9 | **129.1** |  129.6 |
| TPOT median (ms)          |         80.0 |  **31.4** |   50.2 |
| E2E median (ms)           |        637.7 | **274.3** |  355.3 |
| Throughput median (tok/s) |          8.3 |  **18.3** |   13.2 |
| Correctness               |          98% |       99% |    98% |
