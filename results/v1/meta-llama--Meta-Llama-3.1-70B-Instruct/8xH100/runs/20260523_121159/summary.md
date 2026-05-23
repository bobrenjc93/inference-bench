# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:03 AM PT, May 23 2026

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
| torchinferno |     294.4s (4.9m) | `9f91b40` |
| vllm         |   1282.9s (21.4m) | `3f3e862` |
| sglang       | **197.2s (3.3m)** | `a5a64a3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        270.3 |    158.7 | **135.8** |
| TPOT median (ms)          |        155.2 | **54.0** |      69.2 |
| E2E median (ms)           |        366.7 |    210.9 | **203.0** |
| Throughput median (tok/s) |          4.1 |  **7.1** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        267.6 | **189.6** |  198.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        289.6 | **211.3** |  328.3 |
| Throughput median (tok/s) |          3.5 |   **4.7** |    3.0 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        709.4 |     177.2 | **157.8** |
| TPOT median (ms)          |        122.0 |  **55.3** |     104.9 |
| E2E median (ms)           |        800.7 | **224.0** |     258.7 |
| Throughput median (tok/s) |          1.6 |   **6.1** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        337.4 | **57.4** |   78.0 |
| TPOT median (ms)          |        134.2 | **26.5** |   64.8 |
| E2E median (ms)           |        441.9 | **77.3** |  156.3 |
| Throughput median (tok/s) |          3.0 | **15.8** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        779.5 |  **65.2** |   66.8 |
| TPOT median (ms)          |         15.3 |  **15.0** |   22.4 |
| E2E median (ms)           |       1362.0 | **607.5** |  824.8 |
| Throughput median (tok/s) |         26.6 |  **59.7** |   42.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        472.8 |     129.6 | **127.3** |
| TPOT median (ms)          |         85.3 |  **30.2** |      52.3 |
| E2E median (ms)           |        652.2 | **266.2** |     354.2 |
| Throughput median (tok/s) |          7.7 |  **18.7** |      13.1 |
| Correctness               |          99% |       98% |       99% |
