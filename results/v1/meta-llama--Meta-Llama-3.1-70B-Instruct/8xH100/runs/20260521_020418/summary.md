# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:03 PM PT, May 20 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |       2/4 |    2/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **14/20** |   5/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     260.4s (4.3m) | `9f91b40` |
| vllm         |   1102.4s (18.4m) | `9640970` |
| sglang       | **183.6s (3.1m)** | `ddf3817` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        271.1 |    157.5 | **137.0** |
| TPOT median (ms)          |        155.2 | **56.1** |      81.2 |
| E2E median (ms)           |        368.1 |    214.5 | **207.9** |
| Throughput median (tok/s) |          4.1 |  **6.9** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        276.5 |     199.9 | **194.0** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        308.4 | **222.9** |     324.9 |
| Throughput median (tok/s) |          3.2 |   **4.5** |       3.1 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        703.6 |     166.4 | **155.8** |
| TPOT median (ms)          |        107.0 |  **50.5** |     102.3 |
| E2E median (ms)           |        806.8 | **209.0** |     259.3 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        333.1 | **57.3** |   72.9 |
| TPOT median (ms)          |        133.6 | **26.4** |   71.7 |
| E2E median (ms)           |        435.5 | **77.5** |  166.8 |
| Throughput median (tok/s) |          3.1 | **15.8** |    8.9 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        727.9 |      70.3 | **65.7** |
| TPOT median (ms)          |         15.3 |  **14.9** |     22.0 |
| E2E median (ms)           |       1388.1 | **612.4** |    824.2 |
| Throughput median (tok/s) |         25.6 |  **59.2** |     43.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        462.4 |     130.3 | **125.1** |
| TPOT median (ms)          |         82.2 |  **29.6** |      55.4 |
| E2E median (ms)           |        661.4 | **267.3** |     356.6 |
| Throughput median (tok/s) |          7.5 |  **18.6** |      13.2 |
| Correctness               |          99% |       99% |       99% |
