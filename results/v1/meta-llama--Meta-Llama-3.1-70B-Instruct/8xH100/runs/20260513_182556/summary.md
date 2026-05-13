# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:22 AM PT, May 13 2026

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
| torchinferno |     379.7s (6.3m) | `8684859` |
| vllm         |   1099.5s (18.3m) | `0f69128` |
| sglang       | **166.2s (2.8m)** | `22012ba` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        295.3 |    164.4 | **137.9** |
| TPOT median (ms)          |        276.4 | **56.3** |      73.9 |
| E2E median (ms)           |        555.2 |    216.2 | **205.7** |
| Throughput median (tok/s) |          2.7 |  **6.7** |       5.9 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        472.9 | **174.1** |  202.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        544.7 | **198.0** |  344.5 |
| Throughput median (tok/s) |          1.8 |   **5.1** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        671.3 |     167.2 | **156.7** |
| TPOT median (ms)          |        241.9 |  **53.7** |      98.4 |
| E2E median (ms)           |        873.5 | **216.7** |     256.2 |
| Throughput median (tok/s) |          1.5 |   **6.4** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        378.7 | **59.1** |   74.9 |
| TPOT median (ms)          |        265.3 | **26.7** |   58.7 |
| E2E median (ms)           |        596.7 | **79.9** |  143.0 |
| Throughput median (tok/s) |          2.4 | **15.3** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        712.2 |      68.7 | **67.2** |
| TPOT median (ms)          |         28.1 |  **14.9** |     22.3 |
| E2E median (ms)           |       2019.3 | **606.5** |    851.5 |
| Throughput median (tok/s) |         16.8 |  **58.8** |     42.2 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        506.1 | **126.7** |  127.7 |
| TPOT median (ms)          |        162.4 |  **30.3** |   50.6 |
| E2E median (ms)           |        917.9 | **263.5** |  360.2 |
| Throughput median (tok/s) |          5.1 |  **18.4** |   13.3 |
| Correctness               |          99% |       99% |    98% |
