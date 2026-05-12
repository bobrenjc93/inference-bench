# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 11:06 PM PT, May 11 2026

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
| torchinferno |     390.0s (6.5m) | `b468ebb` |
| vllm         |    994.7s (16.6m) | `4e498b5` |
| sglang       | **159.7s (2.7m)** | `7582237` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |     vllm |    sglang |
| :------------------------ | -----------: | -------: | --------: |
| TTFT median (ms)          |        494.2 |    161.3 | **139.4** |
| TPOT median (ms)          |        363.9 | **54.9** |      76.1 |
| E2E median (ms)           |        804.1 |    211.8 | **210.7** |
| Throughput median (tok/s) |          1.7 |  **6.8** |       5.8 |
| Correctness               |          98% |      98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        400.3 | **184.3** |  213.9 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        491.4 | **205.2** |  357.7 |
| Throughput median (tok/s) |          2.0 |   **4.9** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        682.1 |     178.1 | **160.5** |
| TPOT median (ms)          |        573.1 |  **61.0** |     103.6 |
| E2E median (ms)           |       1327.7 | **239.4** |     258.3 |
| Throughput median (tok/s) |          1.1 |   **6.2** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        555.5 | **58.0** |   76.7 |
| TPOT median (ms)          |        419.3 | **27.8** |   55.5 |
| E2E median (ms)           |        845.3 | **79.0** |  147.1 |
| Throughput median (tok/s) |          1.6 | **15.9** |    9.6 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        715.7 |      72.1 | **68.6** |
| TPOT median (ms)          |         28.8 |  **14.8** |     21.9 |
| E2E median (ms)           |       1986.8 | **622.0** |    823.9 |
| Throughput median (tok/s) |         16.3 |  **58.1** |     42.8 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        569.6 | **130.8** |  131.8 |
| TPOT median (ms)          |        277.0 |  **31.7** |   51.4 |
| E2E median (ms)           |       1091.0 | **271.5** |  359.5 |
| Throughput median (tok/s) |          4.6 |  **18.4** |   13.2 |
| Correctness               |          98% |       98% |    99% |
