# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:07 AM PT, Jun 11 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         1/20 | **16/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     381.3s (6.4m) | `065275c` |
| vllm         |   1337.5s (22.3m) | `c3662b3` |
| sglang       | **229.1s (3.8m)** | `8077fb1` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        313.2 |     158.0 | **151.9** |
| TPOT median (ms)          |         91.6 |  **52.3** |      73.3 |
| E2E median (ms)           |        390.7 | **207.4** |     220.3 |
| Throughput median (tok/s) |          3.1 |   **7.1** |       5.3 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        370.6 | **209.9** |  223.3 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        530.9 | **240.6** |  357.3 |
| Throughput median (tok/s) |          1.9 |   **4.2** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        749.3 |     184.6 | **169.5** |
| TPOT median (ms)          |     **65.8** |      66.1 |     102.1 |
| E2E median (ms)           |        796.7 | **241.6** |     264.7 |
| Throughput median (tok/s) |          1.7 |   **5.9** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        385.0 | **60.5** |   85.0 |
| TPOT median (ms)          |         60.5 | **29.3** |   45.4 |
| E2E median (ms)           |        437.7 | **82.3** |  143.4 |
| Throughput median (tok/s) |          3.4 | **14.7** |    9.6 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        193.5 |  **72.4** |   79.4 |
| TPOT median (ms)          |         26.8 |  **15.1** |   23.4 |
| E2E median (ms)           |       1256.2 | **624.2** |  886.5 |
| Throughput median (tok/s) |         30.0 |  **58.4** |   39.5 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        402.3 | **137.1** |  141.8 |
| TPOT median (ms)          |         48.9 |  **32.6** |   48.8 |
| E2E median (ms)           |        682.4 | **279.2** |  374.5 |
| Throughput median (tok/s) |          8.0 |  **18.1** |   12.4 |
| Correctness               |          99% |       98% |    99% |
