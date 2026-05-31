# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 7:40 AM PT, May 31 2026

## Scorecard

| Benchmark        | torchinferno |      vllm |  sglang |
| :--------------- | -----------: | --------: | ------: |
| few_shot         |          1/4 |       1/4 | **2/4** |
| self_consistency |          0/4 |   **2/4** |     1/4 |
| multi_turn       |          0/4 |   **3/4** |     1/4 |
| tree_of_thought  |          0/4 |   **4/4** |     0/4 |
| long_output      |          0/4 |   **4/4** |     0/4 |
| **Total**        |         1/20 | **14/20** |    4/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     286.2s (4.8m) | `2f8bd57` |
| vllm         |   1255.4s (20.9m) | `6bdabba` |
| sglang       | **182.5s (3.0m)** | `c062201` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        191.1 |   164.1 | **143.7** |
| TPOT median (ms)          |     **43.8** |    55.7 |      75.0 |
| E2E median (ms)           |        225.0 |   220.0 | **212.8** |
| Throughput median (tok/s) |          5.5 | **6.9** |       5.7 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        360.6 |     214.9 | **195.2** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        455.2 | **234.8** |     339.8 |
| Throughput median (tok/s) |          2.2 |   **4.3** |       2.9 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1055.2 |     172.8 | **165.0** |
| TPOT median (ms)          |         97.7 |  **58.8** |      99.4 |
| E2E median (ms)           |       1304.8 | **228.6** |     261.1 |
| Throughput median (tok/s) |          1.1 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        413.8 | **58.5** |   79.0 |
| TPOT median (ms)          |         30.4 | **26.3** |   63.5 |
| E2E median (ms)           |        473.7 | **79.4** |  157.9 |
| Throughput median (tok/s) |          3.2 | **15.9** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        357.7 |  **71.6** |   84.6 |
| TPOT median (ms)          |         26.0 |  **15.0** |   23.1 |
| E2E median (ms)           |       1358.5 | **612.4** |  875.1 |
| Throughput median (tok/s) |         25.4 |  **58.5** |   39.8 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        475.7 |     136.4 | **133.5** |
| TPOT median (ms)          |         39.6 |  **31.2** |      52.2 |
| E2E median (ms)           |        763.4 | **275.0** |     369.3 |
| Throughput median (tok/s) |          7.5 |  **18.3** |      12.5 |
| Correctness               |          98% |       99% |       99% |
