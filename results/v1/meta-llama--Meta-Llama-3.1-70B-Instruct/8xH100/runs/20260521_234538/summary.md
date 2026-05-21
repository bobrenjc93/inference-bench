# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 4:02 PM PT, May 21 2026

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
| torchinferno | **89.8s (1.5m)** | `9f91b40` |
| vllm         |  1269.4s (21.2m) | `39d5fa9` |
| sglang       |    177.8s (3.0m) | `7cf193f` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        284.3 |     163.6 | **145.3** |
| TPOT median (ms)          |        160.9 |  **60.4** |      80.9 |
| E2E median (ms)           |        384.9 | **217.6** |     223.1 |
| Throughput median (tok/s) |          3.8 |   **6.8** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        283.5 | **207.7** |  215.8 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        309.2 | **238.3** |  359.0 |
| Throughput median (tok/s) |          3.2 |   **4.2** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |       1005.6 |     185.6 | **169.0** |
| TPOT median (ms)          |        133.1 |  **59.0** |     103.2 |
| E2E median (ms)           |       1126.4 | **237.0** |     283.1 |
| Throughput median (tok/s) |          1.1 |   **5.7** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        358.0 | **60.2** |   79.8 |
| TPOT median (ms)          |        137.4 | **27.0** |   77.6 |
| E2E median (ms)           |        469.0 | **80.0** |  161.2 |
| Throughput median (tok/s) |          3.0 | **15.5** |    8.9 |
| Correctness               |          97% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm |   sglang |
| :------------------------ | -----------: | --------: | -------: |
| TTFT median (ms)          |       1048.3 |      79.2 | **74.5** |
| TPOT median (ms)          |         16.1 |  **15.0** |     22.6 |
| E2E median (ms)           |       1623.7 | **630.4** |    913.2 |
| Throughput median (tok/s) |         20.8 |  **57.5** |     41.4 |
| Correctness               |         100% |      100% |     100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        595.9 |     139.3 | **136.9** |
| TPOT median (ms)          |         89.5 |  **32.3** |      56.9 |
| E2E median (ms)           |        782.7 | **280.7** |     387.9 |
| Throughput median (tok/s) |          6.4 |  **17.9** |      12.7 |
| Correctness               |          99% |       99% |       98% |
