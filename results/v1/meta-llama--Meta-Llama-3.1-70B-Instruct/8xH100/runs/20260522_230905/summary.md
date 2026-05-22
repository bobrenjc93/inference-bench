# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 3:03 PM PT, May 22 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **2/4** |    1/4 |
| multi_turn       |          0/4 |   **3/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **16/20** |   3/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     256.7s (4.3m) | `9f91b40` |
| vllm         |   1288.7s (21.5m) | `8de5cab` |
| sglang       | **176.7s (2.9m)** | `cadfa2d` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        292.9 |     153.1 | **141.7** |
| TPOT median (ms)          |        149.3 |  **59.9** |      71.4 |
| E2E median (ms)           |        396.2 | **207.2** |     211.2 |
| Throughput median (tok/s) |          3.8 |   **6.9** |       5.6 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        287.0 |     198.0 | **195.6** |
| TPOT median (ms)          |          0.0 |       0.0 |       0.0 |
| E2E median (ms)           |        320.5 | **231.8** |     331.0 |
| Throughput median (tok/s) |          3.1 |   **4.3** |       3.0 |
| Correctness               |         100% |      100% |      100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        688.8 |     169.5 | **155.6** |
| TPOT median (ms)          |        117.1 |  **65.3** |      99.5 |
| E2E median (ms)           |        792.0 | **218.2** |     252.4 |
| Throughput median (tok/s) |          1.7 |   **6.3** |       5.2 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        378.7 | **57.9** |   78.3 |
| TPOT median (ms)          |        131.8 | **26.2** |   58.7 |
| E2E median (ms)           |        481.4 | **78.8** |  154.1 |
| Throughput median (tok/s) |          2.9 | **15.8** |    9.3 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        806.8 |  **65.2** |   66.6 |
| TPOT median (ms)          |         17.0 |  **14.9** |   22.2 |
| E2E median (ms)           |       1583.3 | **594.8** |  831.9 |
| Throughput median (tok/s) |         22.0 |  **60.2** |   42.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        490.8 |     128.8 | **127.6** |
| TPOT median (ms)          |         83.0 |  **33.3** |      50.4 |
| E2E median (ms)           |        714.6 | **266.2** |     356.1 |
| Throughput median (tok/s) |          6.7 |  **18.7** |      13.1 |
| Correctness               |          98% |       98% |       98% |
