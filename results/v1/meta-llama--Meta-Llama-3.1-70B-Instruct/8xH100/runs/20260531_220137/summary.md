# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:01 PM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **3/4** |     0/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **15/20** |    3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     273.9s (4.6m) | `90c8b9e` |
| vllm         |   1245.6s (20.8m) | `8b8546d` |
| sglang       | **186.1s (3.1m)** | `c062201` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        223.6 |   163.9 | **142.2** |
| TPOT median (ms)          |     **47.4** |    62.3 |      81.1 |
| E2E median (ms)           |        266.7 |   222.9 | **215.9** |
| Throughput median (tok/s) |          4.9 | **6.5** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        356.2 | **196.9** |  211.2 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        446.9 | **218.7** |  348.9 |
| Throughput median (tok/s) |          2.2 |   **4.6** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        902.5 |     170.2 | **161.3** |
| TPOT median (ms)          |         92.9 |  **53.7** |      95.7 |
| E2E median (ms)           |       1062.6 | **213.2** |     259.7 |
| Throughput median (tok/s) |          1.1 |   **6.4** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        314.3 | **58.5** |   80.6 |
| TPOT median (ms)          |         29.3 | **27.4** |   57.4 |
| E2E median (ms)           |        353.1 | **78.4** |  146.5 |
| Throughput median (tok/s) |          3.9 | **15.6** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        174.1 |  **69.8** |   74.5 |
| TPOT median (ms)          |         18.4 |  **15.0** |   24.0 |
| E2E median (ms)           |        862.2 | **603.8** |  893.4 |
| Throughput median (tok/s) |         33.5 |  **59.1** |   39.2 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        394.1 | **131.9** |  134.0 |
| TPOT median (ms)          |         37.6 |  **31.7** |   51.6 |
| E2E median (ms)           |        598.3 | **267.4** |  372.9 |
| Throughput median (tok/s) |          9.1 |  **18.4** |   12.4 |
| Correctness               |          99% |       99% |    99% |
