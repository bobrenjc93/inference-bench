# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:07 AM PT, May 12 2026

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
| torchinferno |     356.1s (5.9m) | `708195d` |
| vllm         |   1001.3s (16.7m) | `4d591db` |
| sglang       | **160.4s (2.7m)** | `e86fb42` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        394.5 |    164.1 | **140.4** |
| TPOT median (ms)          |        419.7 | **59.6** |      74.0 |
| E2E median (ms)           |        736.1 |    221.7 | **209.2** |
| Throughput median (tok/s) |          1.7 |  **6.6** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        356.2 | **209.4** |  210.6 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        399.1 | **237.0** |  355.7 |
| Throughput median (tok/s) |          2.5 |   **4.2** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        660.3 |     167.1 | **155.1** |
| TPOT median (ms)          |        181.8 |  **55.5** |      96.7 |
| E2E median (ms)           |        827.7 | **215.5** |     251.5 |
| Throughput median (tok/s) |          1.6 |   **6.3** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        445.9 | **57.5** |   76.8 |
| TPOT median (ms)          |        438.3 | **27.0** |   58.6 |
| E2E median (ms)           |        806.6 | **77.8** |  148.1 |
| Throughput median (tok/s) |          1.9 | **15.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        543.6 |      73.0 | **65.1** |
| TPOT median (ms)          |         31.0 |  **15.0** |     22.2 |
| E2E median (ms)           |       1813.2 | **620.1** |    814.6 |
| Throughput median (tok/s) |         21.7 |  **58.4** |     42.3 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        480.1 |     134.2 | **129.6** |
| TPOT median (ms)          |        214.2 |  **31.4** |      50.3 |
| E2E median (ms)           |        916.5 | **274.4** |     355.8 |
| Throughput median (tok/s) |          5.9 |  **18.3** |      13.2 |
| Correctness               |          99% |       99% |       99% |
