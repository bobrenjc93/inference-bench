# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:03 AM PT, May 21 2026

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
| torchinferno |     401.5s (6.7m) | `9f91b40` |
| vllm         |   1249.6s (20.8m) | `b730c46` |
| sglang       | **220.4s (3.7m)** | `ac83d8a` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        314.1 |     153.9 | **142.7** |
| TPOT median (ms)          |        153.4 |  **54.1** |      73.7 |
| E2E median (ms)           |        434.0 | **208.3** |     213.6 |
| Throughput median (tok/s) |          3.2 |   **6.8** |       5.5 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        290.1 | **192.9** |  197.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        327.0 | **216.9** |  332.7 |
| Throughput median (tok/s) |          3.1 |   **4.6** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        833.3 |     171.4 | **157.5** |
| TPOT median (ms)          |        119.0 |  **55.1** |     103.7 |
| E2E median (ms)           |        926.9 | **219.8** |     256.0 |
| Throughput median (tok/s) |          1.4 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        344.0 | **57.7** |   78.4 |
| TPOT median (ms)          |        134.6 | **26.7** |   61.8 |
| E2E median (ms)           |        445.0 | **78.7** |  158.8 |
| Throughput median (tok/s) |          2.7 | **15.7** |    9.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        985.7 |      72.4 | **66.2** |
| TPOT median (ms)          |         19.0 |  **15.0** |     22.5 |
| E2E median (ms)           |       1769.9 | **608.5** |    834.3 |
| Throughput median (tok/s) |         20.0 |  **58.2** |     41.7 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        553.4 |     129.7 | **128.4** |
| TPOT median (ms)          |         85.2 |  **30.2** |      52.4 |
| E2E median (ms)           |        780.6 | **266.5** |     359.1 |
| Throughput median (tok/s) |          6.1 |  **18.3** |      12.9 |
| Correctness               |          98% |       98% |       99% |
