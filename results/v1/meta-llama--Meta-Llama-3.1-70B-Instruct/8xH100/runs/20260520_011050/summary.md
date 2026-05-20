# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 5:02 PM PT, May 19 2026

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
| torchinferno |     401.6s (6.7m) | `9f91b40` |
| vllm         |   1143.1s (19.1m) | `be16785` |
| sglang       | **188.7s (3.1m)** | `7f154ba` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        254.8 |    167.2 | **142.6** |
| TPOT median (ms)          |        149.6 | **55.2** |      73.7 |
| E2E median (ms)           |        353.8 |    226.7 | **210.8** |
| Throughput median (tok/s) |          4.2 |  **6.2** |       5.7 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        266.7 |     198.0 | **197.8** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        290.8 | **223.2** |     339.2 |
| Throughput median (tok/s) |          3.4 |   **4.5** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        523.7 |     171.3 | **162.4** |
| TPOT median (ms)          |        108.8 |  **56.4** |      99.4 |
| E2E median (ms)           |        611.5 | **215.6** |     262.3 |
| Throughput median (tok/s) |          2.3 |   **6.2** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.9 | **58.3** |   77.8 |
| TPOT median (ms)          |        131.8 | **27.3** |   53.9 |
| E2E median (ms)           |        435.2 | **78.5** |  144.6 |
| Throughput median (tok/s) |          3.2 | **15.6** |    9.8 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        826.8 |      70.3 | **67.1** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.0 |
| E2E median (ms)           |       1447.3 | **602.2** |    823.6 |
| Throughput median (tok/s) |         23.7 |  **58.8** |     42.5 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        442.0 |     133.0 | **129.5** |
| TPOT median (ms)          |         81.3 |  **30.8** |      49.8 |
| E2E median (ms)           |        627.7 | **269.3** |     356.1 |
| Throughput median (tok/s) |          7.4 |  **18.2** |      13.2 |
| Correctness               |          99% |       99% |       99% |
