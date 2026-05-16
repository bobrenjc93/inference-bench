# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:08 AM PT, May 16 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     322.8s (5.4m) | `db749af` |
| vllm         |   1083.8s (18.1m) | `4db300e` |
| sglang       | **167.9s (2.8m)** | `596b45b` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        287.2 |    152.7 | **133.6** |
| TPOT median (ms)          |        148.8 | **54.1** |      75.1 |
| E2E median (ms)           |        373.8 |    204.0 | **202.1** |
| Throughput median (tok/s) |          3.9 |  **7.3** |       6.1 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        271.2 | **193.2** |  199.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        297.1 | **214.5** |  332.2 |
| Throughput median (tok/s) |          3.4 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        537.1 |     173.7 | **153.1** |
| TPOT median (ms)          |        112.6 |  **57.8** |     107.6 |
| E2E median (ms)           |        632.7 | **220.0** |     250.3 |
| Throughput median (tok/s) |          2.0 |   **6.3** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        304.9 | **58.6** |   72.1 |
| TPOT median (ms)          |        129.4 | **27.0** |   64.7 |
| E2E median (ms)           |        403.5 | **79.6** |  154.6 |
| Throughput median (tok/s) |          3.8 | **15.4** |    9.5 |
| Correctness               |          96% |      96% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        704.4 |  **68.5** |   68.7 |
| TPOT median (ms)          |         16.6 |  **15.0** |   21.9 |
| E2E median (ms)           |       1389.7 | **617.1** |  847.7 |
| Throughput median (tok/s) |         26.8 |  **59.0** |   42.9 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        420.9 |     129.3 | **125.3** |
| TPOT median (ms)          |         81.5 |  **30.8** |      53.9 |
| E2E median (ms)           |        619.4 | **267.1** |     357.4 |
| Throughput median (tok/s) |          8.0 |  **18.5** |      13.3 |
| Correctness               |          98% |       98% |       98% |
