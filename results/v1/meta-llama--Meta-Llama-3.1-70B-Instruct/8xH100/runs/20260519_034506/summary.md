# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 8:02 PM PT, May 18 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |             Time |    Commit |
| :----------- | ---------------: | --------: |
| torchinferno | **91.1s (1.5m)** | `e5272ff` |
| vllm         |  1248.0s (20.8m) | `287471b` |
| sglang       |    178.4s (3.0m) | `d8e66e5` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        279.8 |     156.0 | **144.4** |
| TPOT median (ms)          |        159.8 |  **56.6** |      83.8 |
| E2E median (ms)           |        378.4 | **210.6** |     222.2 |
| Throughput median (tok/s) |          3.9 |   **6.9** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        208.8 | **200.0** |  219.7 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        308.6 | **227.9** |  364.3 |
| Throughput median (tok/s) |          3.2 |   **4.4** |    2.7 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1038.3 |     184.6 | **169.9** |
| TPOT median (ms)          |        135.5 |  **56.7** |     117.3 |
| E2E median (ms)           |       1207.6 | **234.3** |     281.3 |
| Throughput median (tok/s) |          1.3 |   **5.9** |       4.7 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        387.2 | **60.8** |   78.5 |
| TPOT median (ms)          |        136.7 | **27.4** |   63.5 |
| E2E median (ms)           |        497.5 | **82.0** |  150.0 |
| Throughput median (tok/s) |          2.6 | **15.2** |    9.4 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1023.0 |     100.4 | **71.9** |
| TPOT median (ms)          |         17.2 |  **14.9** |     22.2 |
| E2E median (ms)           |       1647.4 | **669.3** |    887.6 |
| Throughput median (tok/s) |         19.5 |  **56.1** |     41.9 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        587.4 |     140.4 | **136.9** |
| TPOT median (ms)          |         89.8 |  **31.1** |      57.4 |
| E2E median (ms)           |        807.9 | **284.8** |     381.1 |
| Throughput median (tok/s) |          6.1 |  **17.7** |      12.8 |
| Correctness               |          98% |       99% |       99% |
