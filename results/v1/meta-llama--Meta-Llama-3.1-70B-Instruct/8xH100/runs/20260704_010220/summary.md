# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:02 PM PT, Jul 3 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |      **2/4** |       1/4 |    1/4 |
| self_consistency |      **3/4** |       0/4 |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         5/20 | **11/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **39.5s (0.7m)** | `390fed4` |
| vllm         |    280.0s (4.7m) | `ab3b6d9` |
| sglang       |    149.4s (2.5m) | `b28bc10` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        158.7 |   172.9 | **140.2** |
| TPOT median (ms)          |     **45.8** |    75.4 |      79.3 |
| E2E median (ms)           |    **200.9** |   232.3 |     217.6 |
| Throughput median (tok/s) |          5.8 | **6.2** |       5.6 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |  vllm | sglang |
| :------------------------ | -----------: | ----: | -----: |
| TTFT median (ms)          |    **178.3** | 233.0 |  224.0 |
| TPOT median (ms)          |          0.0 |   0.0 |    0.0 |
| E2E median (ms)           |    **189.0** | 264.2 |  371.5 |
| Throughput median (tok/s) |      **5.3** |   3.8 |    2.7 |
| Correctness               |         100% |  100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        324.2 |     182.1 | **161.9** |
| TPOT median (ms)          |         59.8 |  **55.2** |     103.7 |
| E2E median (ms)           |        381.4 | **235.8** |     271.8 |
| Throughput median (tok/s) |          3.9 |   **5.8** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        138.5 | **65.8** |   73.8 |
| TPOT median (ms)          |         40.6 | **30.1** |   61.6 |
| E2E median (ms)           |        164.2 | **90.3** |  141.5 |
| Throughput median (tok/s) |          8.4 | **13.5** |   10.1 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        237.1 |      77.0 | **73.8** |
| TPOT median (ms)          |         21.0 |  **15.3** |     22.3 |
| E2E median (ms)           |        958.9 | **612.6** |    877.2 |
| Throughput median (tok/s) |         35.9 |  **57.5** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        207.4 |     146.2 | **134.7** |
| TPOT median (ms)          |     **33.4** |      35.2 |      53.4 |
| E2E median (ms)           |        378.9 | **287.0** |     375.9 |
| Throughput median (tok/s) |         11.9 |  **17.3** |      12.9 |
| Correctness               |          98% |       98% |       99% |
