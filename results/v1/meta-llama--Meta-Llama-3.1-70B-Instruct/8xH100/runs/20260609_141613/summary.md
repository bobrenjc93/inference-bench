# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 6:01 AM PT, Jun 9 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          0/4 |   **3/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          0/4 |   **4/4** |    0/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         0/20 | **18/20** |   1/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     390.4s (6.5m) | `bb2b2bf` |
| vllm         |   1336.9s (22.3m) | `ee4d7df` |
| sglang       | **191.5s (3.2m)** | `1368717` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        253.7 |     159.2 | **157.4** |
| TPOT median (ms)          |         93.3 |  **54.4** |      76.7 |
| E2E median (ms)           |        336.8 | **211.9** |     231.8 |
| Throughput median (tok/s) |          3.5 |   **7.1** |       5.0 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        372.1 | **203.2** |  211.4 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        520.4 | **236.2** |  356.2 |
| Throughput median (tok/s) |          1.9 |   **4.2** |    2.8 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        731.4 | **162.8** |  171.1 |
| TPOT median (ms)          |         72.1 |  **52.7** |  105.6 |
| E2E median (ms)           |        795.6 | **209.1** |  265.8 |
| Throughput median (tok/s) |          1.6 |   **6.5** |    5.1 |
| Correctness               |          98% |       98% |    98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        400.2 | **59.8** |   85.1 |
| TPOT median (ms)          |         62.5 | **28.5** |   54.1 |
| E2E median (ms)           |        458.9 | **81.9** |  153.5 |
| Throughput median (tok/s) |          3.3 | **14.8** |    9.2 |
| Correctness               |          97% |      97% |    97% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        496.4 |  **71.1** |   75.2 |
| TPOT median (ms)          |         22.8 |  **15.1** |   23.9 |
| E2E median (ms)           |       1250.3 | **625.2** |  869.7 |
| Throughput median (tok/s) |         28.4 |  **58.1** |   39.3 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        450.8 | **131.2** |  140.0 |
| TPOT median (ms)          |         50.1 |  **30.1** |   52.0 |
| E2E median (ms)           |        672.4 | **272.9** |  375.4 |
| Throughput median (tok/s) |          7.8 |  **18.1** |   12.3 |
| Correctness               |          99% |       99% |    99% |
