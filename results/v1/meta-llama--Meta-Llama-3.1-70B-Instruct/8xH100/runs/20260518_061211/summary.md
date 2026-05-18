# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:09 PM PT, May 17 2026

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
| torchinferno |     257.4s (4.3m) | `3f0f3bc` |
| vllm         |   1075.7s (17.9m) | `23c15ac` |
| sglang       | **166.4s (2.8m)** | `6ccc5b8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        298.0 |    160.8 | **136.0** |
| TPOT median (ms)          |        153.4 | **55.3** |      71.5 |
| E2E median (ms)           |        397.7 |    216.1 | **204.2** |
| Throughput median (tok/s) |          3.8 |  **7.1** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        295.4 | **201.1** |  208.0 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        319.4 | **227.3** |  348.8 |
| Throughput median (tok/s) |          3.1 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        540.0 |     176.1 | **163.9** |
| TPOT median (ms)          |        125.1 |  **55.0** |     102.0 |
| E2E median (ms)           |        640.0 | **227.9** |     266.8 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        377.1 | **57.8** |   74.2 |
| TPOT median (ms)          |        132.2 | **27.1** |   51.0 |
| E2E median (ms)           |        494.5 | **78.3** |  144.4 |
| Throughput median (tok/s) |          2.8 | **15.6** |    9.6 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        779.7 |      69.7 | **67.1** |
| TPOT median (ms)          |         16.6 |  **15.1** |     22.2 |
| E2E median (ms)           |       1415.4 | **607.7** |    802.9 |
| Throughput median (tok/s) |         24.0 |  **59.0** |     42.6 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        458.0 |     133.1 | **129.9** |
| TPOT median (ms)          |         85.5 |  **30.5** |      49.3 |
| E2E median (ms)           |        653.4 | **271.5** |     353.4 |
| Throughput median (tok/s) |          7.1 |  **18.4** |      13.2 |
| Correctness               |          98% |       99% |       98% |
