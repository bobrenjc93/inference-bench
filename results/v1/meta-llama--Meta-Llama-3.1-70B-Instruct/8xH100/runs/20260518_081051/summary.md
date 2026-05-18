# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 12:09 AM PT, May 18 2026

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
| torchinferno |     306.0s (5.1m) | `3f0f3bc` |
| vllm         |   1114.2s (18.6m) | `7d5b033` |
| sglang       | **169.7s (2.8m)** | `54eb290` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        276.3 |    161.4 | **135.0** |
| TPOT median (ms)          |        151.0 | **58.3** |      74.4 |
| E2E median (ms)           |        373.1 |    215.5 | **203.7** |
| Throughput median (tok/s) |          4.1 |  **6.8** |       6.0 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        261.6 | **192.3** |  202.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        289.7 | **236.5** |  342.2 |
| Throughput median (tok/s) |          3.5 |   **4.2** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        538.3 |     174.8 | **153.4** |
| TPOT median (ms)          |        124.2 |  **55.6** |     105.2 |
| E2E median (ms)           |        630.8 | **220.0** |     255.0 |
| Throughput median (tok/s) |          2.1 |   **6.1** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        335.6 | **58.2** |   77.7 |
| TPOT median (ms)          |        131.1 | **27.3** |   69.4 |
| E2E median (ms)           |        436.0 | **78.9** |  164.2 |
| Throughput median (tok/s) |          3.1 | **15.4** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        797.0 |      69.8 | **63.5** |
| TPOT median (ms)          |         17.4 |  **15.1** |     22.4 |
| E2E median (ms)           |       1370.9 | **608.9** |    820.0 |
| Throughput median (tok/s) |         24.5 |  **58.9** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        441.8 |     131.3 | **126.5** |
| TPOT median (ms)          |         84.8 |  **31.3** |      54.3 |
| E2E median (ms)           |        620.1 | **272.0** |     357.0 |
| Throughput median (tok/s) |          7.4 |  **18.3** |      13.1 |
| Correctness               |          98% |       98% |       99% |
