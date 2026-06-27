# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 2:03 PM PT, Jun 27 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **3/4** |    1/4 |
| **Total**        |         1/20 | **15/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     347.5s (5.8m) | `ccb13de` |
| vllm         |     471.5s (7.9m) | `b6caeb5` |
| sglang       | **282.3s (4.7m)** | `073de15` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        180.6 |     146.7 | **141.5** |
| TPOT median (ms)          |     **44.8** |      52.4 |      80.1 |
| E2E median (ms)           |        220.2 | **196.0** |     213.4 |
| Throughput median (tok/s) |          5.8 |   **7.3** |       5.8 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        250.2 | **198.2** |  207.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        285.3 | **252.0** |  345.8 |
| Throughput median (tok/s) |          3.5 |   **4.0** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        453.9 |     168.7 | **160.2** |
| TPOT median (ms)          |         57.7 |  **56.2** |      99.6 |
| E2E median (ms)           |        508.6 | **218.1** |     252.5 |
| Throughput median (tok/s) |          2.6 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        256.6 | **67.0** |   84.0 |
| TPOT median (ms)          |         42.8 | **33.2** |   37.3 |
| E2E median (ms)           |        297.5 | **93.2** |  130.5 |
| Throughput median (tok/s) |          4.6 | **13.1** |   10.0 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |        303.2 |      74.8 | **74.4** |
| TPOT median (ms)          |         22.0 |  **14.9** |     22.2 |
| E2E median (ms)           |       1114.1 | **614.4** |    824.5 |
| Throughput median (tok/s) |         32.4 |  **58.6** |     42.0 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        288.9 | **131.1** |  133.5 |
| TPOT median (ms)          |         33.4 |  **31.3** |   47.8 |
| E2E median (ms)           |        485.2 | **274.7** |  353.3 |
| Throughput median (tok/s) |          9.8 |  **17.8** |   13.2 |
| Correctness               |          99% |       99% |    99% |
