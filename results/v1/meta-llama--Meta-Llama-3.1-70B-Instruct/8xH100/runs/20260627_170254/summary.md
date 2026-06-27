# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 AM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     380.5s (6.3m) | `019ce7b` |
| vllm         |     475.1s (7.9m) | `51a9956` |
| sglang       | **227.1s (3.8m)** | `592f6c8` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        244.7 |     146.0 | **140.6** |
| TPOT median (ms)          |     **44.5** |      46.9 |      78.7 |
| E2E median (ms)           |        283.4 | **186.7** |     212.0 |
| Throughput median (tok/s) |          5.1 |   **7.6** |       5.7 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        250.5 | **207.3** |  214.5 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        267.9 | **264.5** |  350.5 |
| Throughput median (tok/s) |          3.7 |   **3.8** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        375.7 |     166.2 | **163.3** |
| TPOT median (ms)          |         56.1 |  **55.3** |     107.3 |
| E2E median (ms)           |        436.5 | **213.5** |     266.2 |
| Throughput median (tok/s) |          2.6 |   **6.4** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        286.1 | **60.7** |   81.9 |
| TPOT median (ms)          |         43.7 | **30.5** |   56.8 |
| E2E median (ms)           |        337.4 | **84.3** |  147.4 |
| Throughput median (tok/s) |          3.8 | **14.3** |    9.5 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        304.6 |  **70.7** |   70.8 |
| TPOT median (ms)          |         21.5 |  **14.9** |   22.2 |
| E2E median (ms)           |       1067.3 | **602.3** |  817.7 |
| Throughput median (tok/s) |         33.3 |  **59.7** |   41.7 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        292.3 | **130.2** |  134.2 |
| TPOT median (ms)          |         33.2 |  **29.5** |   53.0 |
| E2E median (ms)           |        478.5 | **270.3** |  358.8 |
| Throughput median (tok/s) |          9.7 |  **18.4** |   13.0 |
| Correctness               |          99% |       98% |    99% |
