# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 AM PT, May 21 2026

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
| torchinferno |     301.6s (5.0m) | `9f91b40` |
| vllm         |   1160.9s (19.3m) | `5ecd8e9` |
| sglang       | **170.9s (2.8m)** | `fbebdd5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        281.5 |    165.9 | **139.4** |
| TPOT median (ms)          |        154.7 | **59.2** |      73.2 |
| E2E median (ms)           |        374.1 |    225.0 | **208.5** |
| Throughput median (tok/s) |          4.0 |  **6.3** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        278.2 | **186.9** |  208.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        304.9 | **211.9** |  344.2 |
| Throughput median (tok/s) |          3.3 |   **4.7** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        766.4 |     172.0 | **163.4** |
| TPOT median (ms)          |        128.9 |  **60.0** |      99.7 |
| E2E median (ms)           |        855.5 | **223.3** |     256.9 |
| Throughput median (tok/s) |          1.5 |   **6.2** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        351.0 | **57.6** |   74.9 |
| TPOT median (ms)          |        132.9 | **27.2** |   54.7 |
| E2E median (ms)           |        445.7 | **78.4** |  134.3 |
| Throughput median (tok/s) |          3.3 | **15.6** |   10.0 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        734.4 |      69.8 | **65.5** |
| TPOT median (ms)          |         15.2 |  **14.9** |     22.6 |
| E2E median (ms)           |       1321.7 | **602.4** |    837.2 |
| Throughput median (tok/s) |         26.9 |  **59.6** |     41.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        482.3 |     130.4 | **130.3** |
| TPOT median (ms)          |         86.3 |  **32.3** |      50.0 |
| E2E median (ms)           |        660.4 | **268.2** |     356.2 |
| Throughput median (tok/s) |          7.8 |  **18.5** |      13.1 |
| Correctness               |          98% |       98% |       99% |
