# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 PM PT, May 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     384.9s (6.4m) | `1587d5e` |
| vllm         |   1315.1s (21.9m) | `094124a` |
| sglang       | **211.4s (3.5m)** | `0abe6a8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        282.4 |    168.1 | **140.1** |
| TPOT median (ms)          |         66.2 | **56.5** |      71.0 |
| E2E median (ms)           |        346.4 |    225.6 | **207.0** |
| Throughput median (tok/s) |          3.5 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        279.4 | **187.7** |  198.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        319.1 | **210.3** |  336.8 |
| Throughput median (tok/s) |          3.1 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        887.2 |     179.0 | **161.0** |
| TPOT median (ms)          |     **56.6** |      67.7 |      99.6 |
| E2E median (ms)           |        937.2 | **242.3** |     265.3 |
| Throughput median (tok/s) |          1.3 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        202.6 | **58.8** |   82.0 |
| TPOT median (ms)          |         29.5 | **27.0** |   56.6 |
| E2E median (ms)           |        234.0 | **79.2** |  147.3 |
| Throughput median (tok/s) |          5.7 | **15.4** |    9.6 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        750.8 |  **74.0** |   76.3 |
| TPOT median (ms)          |         15.1 |  **15.0** |   23.6 |
| E2E median (ms)           |       1412.9 | **615.1** |  882.7 |
| Throughput median (tok/s) |         23.7 |  **58.6** |   39.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        480.5 |     133.5 | **131.6** |
| TPOT median (ms)          |         33.5 |  **33.2** |      50.2 |
| E2E median (ms)           |        649.9 | **274.5** |     367.8 |
| Throughput median (tok/s) |          7.5 |  **18.3** |      12.6 |
| Correctness               |          98% |       98% |       99% |
