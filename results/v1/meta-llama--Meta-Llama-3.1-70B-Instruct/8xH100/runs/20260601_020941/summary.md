# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 PM PT, May 31 2026

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
| torchinferno |     309.3s (5.2m) | `8d4e46c` |
| vllm         |   1287.6s (21.5m) | `8b8546d` |
| sglang       | **202.6s (3.4m)** | `1ee1898` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        249.8 |     155.7 | **147.3** |
| TPOT median (ms)          |     **45.5** |      59.6 |      76.9 |
| E2E median (ms)           |        304.0 | **211.2** |     217.5 |
| Throughput median (tok/s) |          4.1 |   **7.3** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        551.6 | **198.0** |  201.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        645.2 | **221.9** |  340.7 |
| Throughput median (tok/s) |          1.5 |   **4.5** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        802.5 |     173.9 | **162.5** |
| TPOT median (ms)          |        112.3 |  **57.6** |     107.8 |
| E2E median (ms)           |        926.0 | **227.8** |     261.8 |
| Throughput median (tok/s) |          1.4 |   **6.0** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        402.5 | **56.5** |   81.5 |
| TPOT median (ms)          |         28.3 | **27.4** |   47.0 |
| E2E median (ms)           |        442.5 | **76.3** |  132.5 |
| Throughput median (tok/s) |          2.9 | **15.9** |   10.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        182.6 |  **70.4** |   75.2 |
| TPOT median (ms)          |         22.2 |  **15.0** |   23.2 |
| E2E median (ms)           |       1081.0 | **609.3** |  878.2 |
| Throughput median (tok/s) |         32.2 |  **59.1** |   40.1 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        437.8 | **130.9** |  133.7 |
| TPOT median (ms)          |         41.7 |  **31.9** |   51.0 |
| E2E median (ms)           |        679.7 | **269.3** |  366.1 |
| Throughput median (tok/s) |          8.4 |  **18.6** |   12.8 |
| Correctness               |          98% |       99% |    99% |
