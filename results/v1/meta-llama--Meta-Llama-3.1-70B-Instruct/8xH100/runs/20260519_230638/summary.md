# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:02 PM PT, May 19 2026

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
| torchinferno |     306.5s (5.1m) | `9f91b40` |
| vllm         |   1122.2s (18.7m) | `117afee` |
| sglang       | **192.8s (3.2m)** | `3ef832f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        291.3 |    165.4 | **137.7** |
| TPOT median (ms)          |        152.3 | **58.7** |      74.0 |
| E2E median (ms)           |        388.8 |    215.3 | **209.0** |
| Throughput median (tok/s) |          3.9 |  **6.7** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        267.1 | **184.2** |  198.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        297.1 | **206.2** |  332.5 |
| Throughput median (tok/s) |          3.4 |   **4.8** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        509.7 |     171.8 | **155.0** |
| TPOT median (ms)          |        168.0 |  **55.2** |     104.0 |
| E2E median (ms)           |        612.2 | **224.7** |     254.9 |
| Throughput median (tok/s) |          2.1 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        334.5 | **57.2** |   75.9 |
| TPOT median (ms)          |        128.5 | **27.0** |   58.6 |
| E2E median (ms)           |        435.5 | **77.8** |  146.4 |
| Throughput median (tok/s) |          3.0 | **15.8** |    9.7 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        696.5 |      67.7 | **64.9** |
| TPOT median (ms)          |         15.5 |  **15.0** |     22.2 |
| E2E median (ms)           |       1264.0 | **603.1** |    839.4 |
| Throughput median (tok/s) |         27.8 |  **59.5** |     42.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        419.8 |     129.3 | **126.5** |
| TPOT median (ms)          |         92.9 |  **31.2** |      51.8 |
| E2E median (ms)           |        599.5 | **265.4** |     356.4 |
| Throughput median (tok/s) |          8.0 |  **18.6** |      13.2 |
| Correctness               |          98% |       99% |       99% |
