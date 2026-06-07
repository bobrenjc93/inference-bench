# Benchmark Summary

- **Model:** meta-llama/Meta-Llama-3.1-70B-Instruct
- **TP:** 8
- **Hardware:** 8xH100
- **Timestamp:** 10:02 PM PT, Jun 6 2026

## Scorecard

| Benchmark        | torchinferno |      vllm | sglang |
| :--------------- | -----------: | --------: | -----: |
| few_shot         |          1/4 |   **2/4** |    1/4 |
| self_consistency |          0/4 |   **3/4** |    0/4 |
| multi_turn       |          1/4 |   **2/4** |    1/4 |
| tree_of_thought  |          0/4 |   **4/4** |    0/4 |
| long_output      |          0/4 |   **4/4** |    0/4 |
| **Total**        |         2/20 | **15/20** |   2/20 |

Each cell = metric wins out of 4 (TTFT, TPOT, E2E, throughput). **Bold** = best in row.

## Build Times

| Provider     |              Time |    Commit |
| :----------- | ----------------: | --------: |
| torchinferno |     418.5s (7.0m) | `917c432` |
| vllm         |   1357.2s (22.6m) | `32f34d3` |
| sglang       | **210.6s (3.5m)** | `0ce3db3` |

## Per-Benchmark Results

### few_shot
> 5-shot math × 1k requests (64 concurrent) — tests prefill speed under load ([source](../../../../../../inference_bench/benchmarks/few_shot.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        340.9 |     160.7 | **147.7** |
| TPOT median (ms)          |     **52.9** |      58.3 |      76.3 |
| E2E median (ms)           |        380.1 | **210.8** |     218.9 |
| Throughput median (tok/s) |          3.3 |   **7.1** |       5.4 |
| Correctness               |          98% |       98% |       98% |

### self_consistency
> 1k concurrent identical math prompts at temp=0.7 — tests batch throughput and prefix caching ([source](../../../../../../inference_bench/benchmarks/self_consistency.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        274.0 | **205.2** |  207.1 |
| TPOT median (ms)          |          0.0 |       0.0 |    0.0 |
| E2E median (ms)           |        374.7 | **228.7** |  339.6 |
| Throughput median (tok/s) |          2.7 |   **4.4** |    2.9 |
| Correctness               |         100% |      100% |   100% |

### multi_turn
> 125 concurrent 8-turn conversations (1k requests) — tests KV cache management under load ([source](../../../../../../inference_bench/benchmarks/multi_turn.py))

| Metric                    | torchinferno |      vllm |    sglang |
| :------------------------ | -----------: | --------: | --------: |
| TTFT median (ms)          |        728.6 |     176.1 | **165.3** |
| TPOT median (ms)          |     **64.7** |      67.6 |      96.8 |
| E2E median (ms)           |        782.6 | **231.8** |     270.9 |
| Throughput median (tok/s) |          1.7 |   **6.1** |       4.9 |
| Correctness               |          98% |       98% |       98% |

### tree_of_thought
> 32 tree searches (4-wide × 3-deep, ~1k requests) — tests bursty scheduling under load ([source](../../../../../../inference_bench/benchmarks/tree_of_thought.py))

| Metric                    | torchinferno |     vllm | sglang |
| :------------------------ | -----------: | -------: | -----: |
| TTFT median (ms)          |        441.9 | **63.6** |   83.2 |
| TPOT median (ms)          |         31.7 | **29.5** |   54.9 |
| E2E median (ms)           |        499.3 | **86.0** |  151.5 |
| Throughput median (tok/s) |          2.9 | **14.1** |    9.2 |
| Correctness               |          96% |      97% |    96% |

### long_output
> 1 × <huge number> × 1k requests (64 concurrent) — tests decode throughput under load ([source](../../../../../../inference_bench/benchmarks/long_output.py))

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        587.1 |  **73.1** |   78.9 |
| TPOT median (ms)          |         31.9 |  **15.1** |   23.3 |
| E2E median (ms)           |       1761.8 | **632.5** |  888.5 |
| Throughput median (tok/s) |         20.3 |  **57.6** |   40.0 |
| Correctness               |         100% |      100% |   100% |

## Cross-Benchmark Averages

| Metric                    | torchinferno |      vllm | sglang |
| :------------------------ | -----------: | --------: | -----: |
| TTFT median (ms)          |        474.5 | **135.7** |  136.5 |
| TPOT median (ms)          |         36.3 |  **34.1** |   50.3 |
| E2E median (ms)           |        759.7 | **277.9** |  373.9 |
| Throughput median (tok/s) |          6.2 |  **17.9** |   12.5 |
| Correctness               |          98% |       99% |    98% |
