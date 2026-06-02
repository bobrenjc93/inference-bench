# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:01 AM PT, Jun 2 2026

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
| torchinferno |     370.1s (6.2m) | `1cbe525` |
| vllm         |   1360.3s (22.7m) | `f69ede4` |
| sglang       | **227.0s (3.8m)** | `ce7da73` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |    vllm |    sglang |
| :------------------------ | -----------: | ------: | --------: |
| TTFT median (ms)          |        232.2 |   163.5 | **141.3** |
| TPOT median (ms)          |     **45.0** |    56.2 |      74.2 |
| E2E median (ms)           |        271.2 |   214.9 | **212.0** |
| Throughput median (tok/s) |          5.2 | **6.7** |       5.8 |
| Correctness               |          98% |     98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       1023.3 | **197.3** |  205.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |       1121.7 | **257.1** |  346.5 |
| Throughput median (tok/s) |          0.9 |   **3.9** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       2308.4 |     180.4 | **163.6** |
| TPOT median (ms)          |        397.8 |  **60.8** |      98.6 |
| E2E median (ms)           |       2782.1 | **238.5** |     266.6 |
| Throughput median (tok/s) |          0.5 |   **5.9** |       5.1 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        771.7 | **58.8** |   79.5 |
| TPOT median (ms)          |         28.1 | **27.2** |   47.7 |
| E2E median (ms)           |        799.3 | **79.2** |  139.6 |
| Throughput median (tok/s) |          1.8 | **15.6** |   10.0 |
| Correctness               |          97% |      96% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |       2816.6 |  **70.1** |   74.3 |
| TPOT median (ms)          |         95.0 |  **15.0** |   23.7 |
| E2E median (ms)           |       5582.9 | **610.4** |  876.1 |
| Throughput median (tok/s) |          5.5 |  **58.8** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1430.5 |     134.0 | **132.8** |
| TPOT median (ms)          |        113.2 |  **31.8** |      48.8 |
| E2E median (ms)           |       2111.4 | **280.0** |     368.2 |
| Throughput median (tok/s) |          2.8 |  **18.2** |      12.6 |
| Correctness               |          99% |       98% |       99% |
