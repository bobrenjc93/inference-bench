# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 AM PT, May 12 2026

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

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **85.6s (1.4m)** | `ff6cea4` |
| vllm         |  1202.1s (20.0m) | `1ff9d33` |
| sglang       |    173.6s (2.9m) | `693f497` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        544.2 |    163.6 | **146.5** |
| TPOT median (ms)          |        473.5 | **62.6** |      76.5 |
| E2E median (ms)           |        855.8 |    219.9 | **215.7** |
| Throughput median (tok/s) |          1.6 |  **6.9** |       5.5 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        410.5 | **156.0** |  211.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        460.6 | **273.2** |  352.3 |
| Throughput median (tok/s) |          2.2 |   **3.7** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1525.4 |     179.5 | **164.0** |
| TPOT median (ms)          |        582.9 |  **60.1** |     106.5 |
| E2E median (ms)           |       2136.7 | **237.9** |     271.3 |
| Throughput median (tok/s) |          0.7 |   **5.9** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        444.8 | **60.8** |   79.7 |
| TPOT median (ms)          |        468.3 | **27.6** |   64.5 |
| E2E median (ms)           |        834.6 | **81.4** |  156.8 |
| Throughput median (tok/s) |          1.7 | **15.1** |    9.2 |
| Correctness               |          96% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1061.2 |      89.7 | **76.8** |
| TPOT median (ms)          |         27.3 |  **15.0** |     21.4 |
| E2E median (ms)           |       2079.6 | **635.4** |    814.1 |
| Throughput median (tok/s) |         16.5 |  **56.9** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        797.2 | **129.9** |  135.7 |
| TPOT median (ms)          |        310.4 |  **33.0** |   53.8 |
| E2E median (ms)           |       1273.4 | **289.6** |  362.0 |
| Throughput median (tok/s) |          4.6 |  **17.7** |   13.0 |
| Correctness               |          98% |       99% |    99% |
